
# 🏎️ SportsCars

### An Interactive 3D Sports Car Showroom Built with Django

SportsCars is a responsive automotive showroom web application built with Django, Python, HTML, CSS, and JavaScript.

The platform allows users to explore sports cars and hypercars, interact with 3D vehicle models, compare specifications, save favorite vehicles, and submit inquiries.

It also features a dedicated administration dashboard for managing vehicles and customer inquiries.

> Built as an educational web development project.

---

## ✨ Features

### 🚗 Interactive Car Showroom
- Browse a collection of sports cars and hypercars.
- View car images, specifications, and descriptions.
- Explore detailed vehicle information.
- Display featured cars on the homepage.
- Experience responsive layouts across desktop and mobile.

### 🎮 Interactive 3D Models
- View vehicles using interactive 3D models.
- Rotate vehicles and explore them from different angles.
- Automatic rotation on supported views.
- Integration with Google's `<model-viewer>` component.

### 🔍 Advanced Search & Filtering
- Search by car name, manufacturer, or engine.
- Filter vehicles by manufacturer.
- Filter by horsepower.
- Filter by maximum price.
- Filter by model year.
- Sort by name, year, horsepower, or price.
- Browse paginated results.

### ⚖️ Car Comparison
- Select two or three vehicles.
- Compare their specifications side by side.
- Compare engines, horsepower, model years, and prices.
- Highlight selected performance differences.

### ❤️ Wishlist
- Save favorite vehicles.
- Remove vehicles from the wishlist.
- Display the number of saved cars.
- Store wishlist preferences locally in the browser using localStorage.

### 🌓 Light & Dark Mode
- Switch between light and dark themes.
- Save theme preferences using localStorage.
- Automatically switch between light and dark logo variants.

### ✉️ Vehicle Inquiries
- Submit inquiries for individual vehicles.
- Open inquiry forms in a modal window.
- Validate user input with Django ModelForms.
- Store inquiries in the database.
- Associate inquiries with specific vehicles.

### 🛡️ Administration Dashboard
- Secure administrator authentication.
- View vehicle and inquiry statistics.
- Monitor recent customer inquiries.
- Identify the most inquired-about vehicles.
- Manage vehicle information.
- Add and edit cars.
- Review inquiries and update their statuses.
- Restrict management actions through Django permissions.

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Backend | Python, Django |
| Frontend | HTML5, CSS3, JavaScript |
| Database | SQLite |
| 3D Rendering | Google Model Viewer |
| Authentication | Django Authentication |
| Administration | Django Admin + Custom Dashboard |
| Styling | Custom CSS, Google Fonts |
| Icons | Google Material Symbols |
| Version Control | Git & GitHub |

---

## 📸 Screenshots

Add screenshots of the application to showcase its interface.

Suggested screenshots:

- Homepage and 3D vehicle viewer
- Car collection and filters
- Vehicle details
- Side-by-side comparison
- Wishlist
- Inquiry modal
- Administration dashboard
- Car management interface

Screenshots can be stored in a `screenshots/` directory.

---

## 📁 Project Structure

```text
SportsCars/
│
├── manage.py
├── db.sqlite3
│
├── SportsCars/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── cars/
│   ├── migrations/
│   │
│   ├── static/
│   │   └── cars/
│   │       ├── css/
│   │       ├── js/
│   │       ├── images/
│   │       └── models/
│   │
│   ├── templates/
│   │   └── cars/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── all_cars.html
│   │       ├── car_detail.html
│   │       ├── about.html
│   │       ├── compare.html
│   │       ├── wishlist.html
│   │       ├── dashboard.html
│   │       ├── manage_cars.html
│   │       ├── car_form.html
│   │       └── manage_inquiries.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── car_management.py
│   ├── dashboard.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <REPOSITORY_URL>
cd SportsCars
```

Replace `<REPOSITORY_URL>` with the actual GitHub repository URL.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

### 4. Install Django

```bash
python -m pip install "Django>=6.1,<6.2"
```

The project was developed using Django 6.1.3.

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Create an administrator account

```bash
python manage.py createsuperuser
```

### 7. Start the development server

```bash
python manage.py runserver
```

Open your browser at:

http://127.0.0.1:8000/

**Note:** A fresh database does not automatically contain the original showroom collection. Add vehicles through the administrator interface and ensure the corresponding image and 3D model assets are available.

---

## 🔗 Main Routes

| Route | Description |
|-------|-------------|
| `/` | Homepage |
| `/cars/` | Car collection |
| `/cars/<id>/` | Vehicle details |
| `/compare/` | Car comparison |
| `/wishlist/` | Saved vehicles |
| `/about/` | About SportsCars |
| `/dashboard/` | Administration dashboard |
| `/dashboard/cars/` | Manage vehicles |
| `/dashboard/cars/add/` | Add a vehicle |
| `/dashboard/inquiries/` | Manage inquiries |
| `/admin/` | Django administration |

---

## 🗃️ Database Models

### Car

Stores information about each vehicle, including:

- Name and manufacturer
- Model year
- Engine
- Horsepower
- Price
- 3D model path
- Image path
- Description
- Featured status

### CarInquiry

Stores customer inquiries, including:

- Related car
- Customer name
- Email address
- Optional phone number
- Inquiry message
- Status
- Submission timestamp

Each inquiry is connected to a vehicle through a Django ForeignKey relationship.

---

## 🔐 Authentication & Permissions

SportsCars uses Django's built-in authentication and permission system.

Public visitors can browse vehicles, use the wishlist, compare cars, and submit inquiries.

Authorized staff can access management features according to their assigned permissions.

Administrator actions are protected on the server, rather than relying only on hidden interface elements.

---

## 🎨 User Interface

The interface uses a modern automotive design inspired by premium sports car showrooms.

Design highlights include:

- Red, black, and white visual identity
- Cinematic automotive backgrounds
- Interactive 3D vehicle displays
- Custom dropdown menus
- Responsive vehicle cards
- Modal inquiry forms
- Light and dark themes
- Dedicated management interfaces

---

## 🧪 Development Checks

Run Django's system checks:

```bash
python manage.py check
```

Check for pending migrations:

```bash
python manage.py makemigrations --check --dry-run
```

Run tests:

```bash
python manage.py test
```

These commands help validate the project during development.

---

## 📌 Project Scope

SportsCars is an educational showroom application.

It is not a real vehicle dealership or payment platform.

Vehicle specifications, prices, images, and 3D models are used for demonstration purposes.

Some vehicle model assets may be subject to their original creators' licenses and attribution requirements.

---

## 🚀 Future Improvements

Potential enhancements include:

- Direct image and 3D model uploads
- Vehicle image galleries
- Email notifications for inquiries
- Automated testing
- Production deployment
- Additional vehicle analytics

---

## 👨‍💻 Developer

**Abdulrahman Al-Qahtani**

Computer Science Graduate  
Python & Django Web Developer

---

## 📄 License

No software license has been specified for this project.

Third-party vehicle images and 3D models retain their respective licensing terms.
