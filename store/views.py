from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import Product, Cart, CartItem, Order, UserProfile
from .forms import UserRegistrationForm, UserProfileForm

# --- HOME VIEW ---
def home(request):
    products = Product.objects.all()
    
    query = request.GET.get('q')
    if query:
        products = products.filter(name__icontains=query) | products.filter(description__icontains=query)
        
    category = request.GET.get('category')
    if category:
        products = products.filter(category__name__iexact=category)
        
    return render(request, 'store/home.html', {'products': products})

# --- AUTHENTICATION VIEWS ---
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    # Add glass-input class and placeholder to standard auth form fields for cinematic UI
    for field in form.fields.values():
        field.widget.attrs['class'] = 'form-control glass-input'
        field.widget.attrs['placeholder'] = field.label
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

# --- CART VIEWS ---
def get_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        cart, created = Cart.objects.get_or_create(session_key=session_key, user=None)
    return cart

def view_cart(request):
    cart = get_cart(request)
    items = cart.items.all() if cart else []
    total = sum(item.product.price * item.quantity for item in items)
    return render(request, 'cart/cart.html', {'items': items, 'total': total})

def add_to_cart(request, product_id):
    cart = get_cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        
    return redirect('view_cart')

def remove_from_cart(request, item_id):
    cart = get_cart(request)
    item = get_object_or_404(CartItem, id=item_id, cart=cart)
    item.delete()
    return redirect('view_cart')

def update_cart_quantity(request, item_id, action):
    cart = get_cart(request)
    item = get_object_or_404(CartItem, id=item_id, cart=cart)
    
    if action == 'add':
        item.quantity += 1
        item.save()
    elif action == 'sub':
        if item.quantity > 1:
            item.quantity -= 1
            item.save()
        else:
            item.delete()
            
    return redirect('view_cart')

# --- CHECKOUT VIEW ---
def checkout(request):
    cart = get_cart(request)
    items = cart.items.all()
    
    if not items:
        return redirect('view_cart')
        
    total = sum(item.product.price * item.quantity for item in items)
    
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')
        shipping_address = request.POST.get('shipping_address')
        
        # Create Order
        order = Order.objects.create(
            user=request.user if request.user.is_authenticated else None,
            cart=cart,
            customer_name=customer_name,
            customer_email=customer_email,
            shipping_address=shipping_address,
            status='PENDING'
        )
        
        # Detach cart from session/user by clearing the keys on the OLD cart
        # so a new cart gets created next time
        if request.user.is_authenticated:
            cart.user = None
            cart.save()
        else:
            cart.delete()
            
        return render(request, 'cart/order_success.html', {'order': order})
        
    return render(request, 'cart/checkout.html', {'items': items, 'total': total})

# --- ACCOUNT VIEWS ---
@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'account/orders.html', {'orders': orders})

@login_required
def account_settings(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('account_settings')
    else:
        form = UserProfileForm(instance=profile)
        
    return render(request, 'account/account.html', {'form': form})

# --- HELP & CONTACT VIEWS ---
def help_page(request):
    return render(request, 'support/help.html')

def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        try:
            send_mail(
                subject=f"Contact Us Form: from {name}",
                message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['shrijithmd3genai@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            messages.error(request, f"An error occurred while sending the email. Ensure your email settings are correct. Error: {e}")
            
        return redirect('contact')
        
    return render(request, 'support/contact.html')
