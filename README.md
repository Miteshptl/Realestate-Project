
# 🏡 LUXEHOMES – Real Estate Management System

**LUXEHOMES** is a full-featured real estate web application built using Python and Django. It allows users to browse, list, and manage real estate properties while providing an intuitive admin interface. With Razorpay integration, it supports seamless payment functionality for bookings or featured listings.

## 🌟 Features

- 🔐 User authentication (signup/login)
- 🏘️ Add, edit, and delete property listings
- 🔍 Advanced property search and filters
- 📷 Image uploads for listings
- 💳 Razorpay payment gateway integration
- 📱 Responsive design with Bootstrap
- 🛠️ Admin panel for property and user management

## 🧰 Tech Stack

| Layer       | Technology            |
|-------------|------------------------|
| Backend     | Python, Django         |
| Frontend    | HTML5, CSS3, Bootstrap |
| Payments    | Razorpay API           |
| Media Mgmt  | Pillow (image handling)|
| Packaging   | setuptools             |
| Database    | SQLite (default) or MySQL/PostgreSQL |

## 🚀 Installation

### 📦 Prerequisites

- Python 3.8+
- pip
- virtualenv (optional but recommended)
- MySQL/PostgreSQL (if not using SQLite)

### 🔧 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Miteshptl/Realestate-Project.git
   cd Realestate-Project
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**
   - For SQLite (default), no setup needed.
   - For MySQL/PostgreSQL, update `settings.py` accordingly.

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

## 💳 Payments via Razorpay

- You must [create a Razorpay account](https://razorpay.com/) and obtain your API key and secret.
- Add these to your Django settings or environment variables:
  ```env
  RAZORPAY_KEY_ID=your_key_id
  RAZORPAY_KEY_SECRET=your_key_secret
  ```

## 📁 Project Structure

```
Realestate-Project/
│
├── luxehomes/            # Main Django app
├── media/                # Uploaded property images
├── templates/            # HTML templates
├── static/               # CSS, JS, and assets
├── manage.py
└── requirements.txt
```

## 📄 Requirements

Here’s a quick look at the key dependencies (from `requirements.txt`):

```
Django>=4.2,<5.0
setuptools>=67.0
pillow>=10.0
razorpay>=1.3.0
django-crispy-forms
python-decouple
django-environ
gunicorn
whitenoise
```


## 🙌 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

## 📬 Contact

**Mitesh Patel**  
[LinkedIn](https://www.linkedin.com/in/miteshptl/) | [GitHub](https://github.com/Miteshptl)
