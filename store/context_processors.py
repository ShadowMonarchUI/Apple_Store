from .models import Cart

def cart_processor(request):
    cart_count = 0
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        if cart:
            cart_count = sum(item.quantity for item in cart.items.all())
    else:
        session_key = request.session.session_key
        if session_key:
            cart = Cart.objects.filter(session_key=session_key, user=None).first()
            if cart:
                cart_count = sum(item.quantity for item in cart.items.all())
    return {'cart_item_count': cart_count}
