# Apple Store Clone (Cinematic E-Commerce)

A highly polished, premium, glassmorphism-themed e-commerce platform built with Django. This project perfectly mimics the aesthetic of the Apple Store, featuring high-contrast dark modes, immersive animations, and robust shopping capabilities.

**🌟 Live Demo:** [https://apple-store-uuqr.onrender.com/](https://apple-store-uuqr.onrender.com/)

## 🚀 Features

- **Cinematic UI/UX:** Built with Bootstrap 5 and custom CSS to achieve deep black backgrounds, bento-box layouts, and frosted glassmorphism elements.
- **Dynamic Animations:** Uses GSAP and ScrollTrigger for stunning scroll-based reveals and floating element animations.
- **Amazon-Style Cart:** A powerful, 2-column shopping cart featuring sticky order summaries and inline `+`/`-` quantity controls.
- **Premium Admin Dashboard:** Completely overhauled Django Admin interface powered by `django-jazzmin`, featuring a sleek dark mode and advanced filtering.
- **Google Sign-In:** Fully integrated OAuth2 via `django-allauth` allowing users to log in with their Google accounts.
- **Customizable User Profiles:** Users can upload profile pictures that dynamically update in the site's navigation bar.
- **Order History:** Authenticated users have a dedicated "My Orders" dashboard tracking their purchase history.
- **Live Search & Category Filters:** Instantly search products by name/description or filter by Apple product categories (Mac, iPad, iPhone, etc.).
- **Functional Contact Form:** A beautifully styled Contact Us page that integrates with Django's email backend to send real emails to support.

## 🛠 Tech Stack

- **Backend:** Python 3, Django, MySQL
- **Frontend:** HTML5, CSS3 (Custom Glassmorphism), Bootstrap 5, GSAP
- **Authentication:** `django-allauth` (Google OAuth2)
- **Image Handling:** Pillow

## 📦 Project Structure

The project has been carefully restructured for maximum readability:
```text
internship_project/
├── AppleStoreProj/          # Core Django settings, URLs, WSGI
├── store/                   # Main application (Models, Views, Forms, URLs)
│   ├── management/          # Contains the custom DB sync script
├── static/                  # CSS, JS, and global images
└── templates/               # Modularized HTML templates
    ├── account/             # account.html, orders.html
    ├── cart/                # cart.html, checkout.html, order_success.html
    ├── store/               # home.html
    ├── support/             # help.html, contact.html
    └── base.html            # The main layout with Nav and Footer
```

## ⚙️ Setup Instructions

Follow these steps to get the project running locally.

### 1. Environment Setup
```bash
# Clone the repository and navigate into the directory
cd internship_project

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
.\venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install django mysqlclient django-allauth Pillow
```

### 2. Database Configuration (MySQL)
1. Ensure you have MySQL installed and running locally.
2. Open your MySQL client (or terminal) and create the database:
   ```sql
   CREATE DATABASE applestore;
   ```
3. Open `AppleStoreProj/settings.py` and ensure the `DATABASES` dictionary matches your local MySQL credentials:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'applestore',
           'USER': 'root', # Your MySQL username
           'PASSWORD': 'your_password', # Your MySQL password
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

### 3. Third-Party Credentials Configuration
To enable the advanced features, you must update `AppleStoreProj/settings.py`:

**Google Sign-In:**
Under `SOCIALACCOUNT_PROVIDERS`, replace `YOUR_GOOGLE_CLIENT_ID` and `YOUR_GOOGLE_CLIENT_SECRET` with valid credentials from the Google Cloud Console.

**Contact Us Email:**
Under the Email settings block, replace the `EMAIL_HOST_USER` with your sender email address (e.g., your Gmail) and `EMAIL_HOST_PASSWORD` with an App Password. Note: The target inbox is currently hardcoded in `store/views.py` (`contact_us` view) to `shrijithmd3genai@gmail.com`.

### 4. Migrations, Admin, & Seeding
Apply the database schemas, create an admin account to view the custom Jazzmin dashboard, and generate the premium fake Apple products:
```bash
# Apply database migrations
python manage.py makemigrations
python manage.py migrate

# Create a superuser for the Admin Dashboard (Username: admin, Password: admin)
python manage.py createsuperuser --noinput --username admin --email admin@example.com
# Note: In development, you may need to set the password via the Django shell if using --noinput.

# Seed the database with 13 premium Apple products
python manage.py sync_apple_products
```

### 5. Run the Server
```bash
python manage.py runserver
```
Navigate to `http://127.0.0.1:8000/` in your browser to experience the store!

## 🚀 Deployment (Render/Railway)
This project is pre-configured for deployment on platforms like Render or Railway. 
1. Connect your GitHub repository to Render/Railway.
2. The platform will automatically detect the `requirements.txt` and `Procfile`.
3. In your host's dashboard, set the following Environment Variables:
   - `SECRET_KEY`: (Generate a long, random string)
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: `your-app-url.onrender.com`
   - `DATABASE_URL`: (Your hosted PostgreSQL/MySQL connection string)
4. Deploy!
