from django.core.management.base import BaseCommand
from store.models import Category, Product

class Command(BaseCommand):
    help = 'Seeds the database with a rich set of premium fake Apple products'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding premium Apple products...')
        
        products_data = [
            # iPhones
            {"category": "iPhone", "name": "iPhone 15 Pro Max", "desc": "Forged in titanium. Featuring the groundbreaking A17 Pro chip, a customizable Action button, and the most powerful iPhone camera system ever.", "price": 1199.00, "stock": 50, "img": "https://pngimg.com/uploads/iphone_14/iphone_14_PNG16.png"},
            {"category": "iPhone", "name": "iPhone 15 Pro", "desc": "The first iPhone to feature an aerospace-grade titanium design. A17 Pro chip. Advanced Pro camera system.", "price": 999.00, "stock": 45, "img": "https://pngimg.com/uploads/iphone_14/iphone_14_PNG16.png"},
            {"category": "iPhone", "name": "iPhone 15", "desc": "Dynamic Island stays on top of it all. New 48MP Main camera. Super-high-resolution photos.", "price": 799.00, "stock": 100, "img": "https://pngimg.com/uploads/iphone_14/iphone_14_PNG16.png"},
            
            # MacBooks
            {"category": "Mac", "name": "MacBook Pro 16-inch (M3 Max)", "desc": "Mind-blowing. Head-turning. The most advanced chip ever built for a personal computer. Up to 22 hours of battery life.", "price": 3499.00, "stock": 20, "img": "https://pngimg.com/uploads/macbook/macbook_PNG8.png"},
            {"category": "Mac", "name": "MacBook Pro 14-inch (M3 Pro)", "desc": "Supercharged by M3 Pro. Brilliant Liquid Retina XDR display. All the ports you need.", "price": 1999.00, "stock": 35, "img": "https://pngimg.com/uploads/macbook/macbook_PNG8.png"},
            {"category": "Mac", "name": "MacBook Air 15-inch (M3)", "desc": "Supersized Air. Strikingly thin and light. Supercharged by the M3 chip. Up to 18 hours battery life.", "price": 1299.00, "stock": 60, "img": "https://pngimg.com/uploads/macbook/macbook_PNG8.png"},
            
            # iPads
            {"category": "iPad", "name": "iPad Pro 12.9-inch (M2)", "desc": "Astonishing performance. Incredibly advanced displays. Superfast wireless connectivity. Next-level Apple Pencil capabilities.", "price": 1099.00, "stock": 40, "img": "https://pngimg.com/uploads/tablet/tablet_PNG8599.png"},
            {"category": "iPad", "name": "iPad Air (M1)", "desc": "Light. Bright. Full of might. Supercharged by the Apple M1 chip. 12MP Ultra Wide front camera with Center Stage.", "price": 599.00, "stock": 80, "img": "https://pngimg.com/uploads/tablet/tablet_PNG8599.png"},
            
            # Wearables & Audio
            {"category": "Watch", "name": "Apple Watch Ultra 2", "desc": "The most rugged and capable Apple Watch pushes the limits again. Featuring the all-new S9 SiP. A magical new way to use your watch without touching the screen.", "price": 799.00, "stock": 30, "img": "https://pngimg.com/uploads/watches/watches_PNG9859.png"},
            {"category": "Watch", "name": "Apple Watch Series 9", "desc": "Smarter. Brighter. Mightier. Our most powerful chip in Apple Watch ever.", "price": 399.00, "stock": 100, "img": "https://pngimg.com/uploads/watches/watches_PNG9859.png"},
            {"category": "AirPods", "name": "AirPods Pro (2nd generation)", "desc": "Rebuilt from the sound up. Up to 2x more Active Noise Cancellation. Adaptive Audio. Personalized Spatial Audio.", "price": 249.00, "stock": 150, "img": "https://pngimg.com/uploads/headphones/headphones_PNG101968.png"},
            {"category": "AirPods", "name": "AirPods Max", "desc": "A radically original composition. High-fidelity audio. Active Noise Cancellation with Transparency mode.", "price": 549.00, "stock": 25, "img": "https://pngimg.com/uploads/headphones/headphones_PNG101968.png"},
            
            # Vision
            {"category": "Vision", "name": "Apple Vision Pro", "desc": "Welcome to the era of spatial computing. Apple Vision Pro seamlessly blends digital content with your physical space.", "price": 3499.00, "stock": 10, "img": "https://pngimg.com/uploads/vr_glasses/vr_glasses_PNG31.png"},
        ]

        for item in products_data:
            cat_obj, _ = Category.objects.get_or_create(name=item['category'])
            Product.objects.update_or_create(
                name=item['name'],
                defaults={
                    'category': cat_obj,
                    'description': item['desc'],
                    'price': item['price'],
                    'stock': item['stock'],
                    'image_url': item['img']
                }
            )
            self.stdout.write(self.style.SUCCESS(f"Synced {item['name']}"))

        self.stdout.write(self.style.SUCCESS('Successfully seeded premium fake products!'))
