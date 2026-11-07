# 🚘 MOTORQUE --- Premium Automotive Experience

A modern automotive showcase built with **Django**, presenting a curated
collection of premium vehicles through an immersive, responsive
interface.

MOTORQUE brings together a refined visual identity, vehicle-focused
storytelling, and an interactive browsing experience. The website
includes both light and dark themes across its pages.

------------------------------------------------------------------------

## 📸 Screenshots

The screenshots below show both **Light Mode** and **Dark Mode** for
each page.

### 🏠 Home

![MOTORQUE Home --- Light and Dark
Modes](Motorque/MotorqueApp/Screenshots/Home.png)

### 🚗 Cars Collection

![MOTORQUE Cars Collection --- Light and Dark
Modes](Motorque/MotorqueApp/Screenshots/Cars.png)

### ✨ Genesis G80

![Genesis G80 --- Light and Dark
Modes](Motorque/MotorqueApp/Screenshots/Genesis%20G80.png)

### 🏎️ Porsche 911 Carrera

![Porsche 911 Carrera --- Light and Dark
Modes](Motorque/MotorqueApp/Screenshots/Porsch%20911.png)

### 🛻 Cadillac Escalade

![Cadillac Escalade --- Light and Dark
Modes](Motorque/MotorqueApp/Screenshots/Escalade.png)

### 🏢 About Us

![MOTORQUE About Us --- Light and Dark
Modes](Motorque/MotorqueApp/Screenshots/About.png)

------------------------------------------------------------------------

## 🌟 Features

-   📱 **Responsive design** for desktop and mobile screens.
-   🌓 **Light and dark themes** available throughout the website.
-   🏠 **Home page** introducing the MOTORQUE experience and featured
    vehicles.
-   🚘 **Cars collection** page for browsing the available vehicles.
-   🏁 **Dedicated vehicle detail pages** with model-specific content
    and visual galleries.
-   🖼️ **Interactive visual elements**, including image galleries and
    vehicle presentation features.
-   🧩 **Reusable Django templates** with template inheritance.
-   ✨ **CSS transitions and animations** for a smoother browsing
    experience.
-   🎞️ **Static asset management** for stylesheets, images, and videos.

## 🚙 Vehicle Collection

  Vehicle               Category         Listed Price
  --------------------- -------------- --------------
  Porsche 911 Carrera   Sports Car        SAR 650,000
  Genesis G80           Luxury Sedan      SAR 230,000
  Cadillac Escalade     Luxury SUV        SAR 550,000

*Prices are illustrative listings used in this project.*

------------------------------------------------------------------------

## 🛠️ Tech Stack

-   🐍 **Backend:** Python, Django
-   🎨 **Frontend:** HTML, CSS, JavaScript
-   🔤 **Typography:** Google Fonts --- Phudu
-   🗄️ **Database:** SQLite (Django default configuration)
-   🖼️ **Assets:** Django static files, images, and video

------------------------------------------------------------------------

## 📁 Project Structure

``` text
LAB-SPORTS-CARS/
├── README.md
└── Motorque/
    ├── manage.py
    ├── Motorque/
    │   ├── settings.py
    │   ├── urls.py
    │   └── ...
    └── MotorqueApp/
        ├── views.py
        ├── urls.py
        ├── templates/
        │   └── MotorqueApp/
        │       └── base.html
        ├── static/
        │   └── MotorqueApp/
        │       └── css/
        │           └── style.css
        ├── images/
        ├── videos/
        └── Screenshots/
            ├── Home.png
            ├── Cars.png
            ├── Genesis G80.png
            ├── Porsch 911.png
            ├── Escalade.png
            └── About.png
```

------------------------------------------------------------------------

## 🚀 Run Locally

### 1️⃣ Clone the repository

``` bash
git clone https://github.com/iimustafa/LAB-SPORTS-CARS.git
cd LAB-SPORTS-CARS/Motorque
```

### 2️⃣ Create and activate a virtual environment

**macOS / Linux**

``` bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows**

``` bash
python -m venv .venv
.venv\Scripts\activate
```

### 3️⃣ Install Django

``` bash
pip install django
```

### 4️⃣ Apply database migrations

``` bash
python manage.py migrate
```

### 5️⃣ Start the development server

``` bash
python manage.py runserver
```

Open <http://127.0.0.1:8000/> in your browser.

------------------------------------------------------------------------

## 🧭 Website Pages

  Page                     URL
  ------------------------ ----------------------------
  🏠 Home                  `/`
  🚘 Cars Collection       `/cars/`
  ✨ Genesis G80           `/cars/genesis-g80/`
  🏎️ Porsche 911 Carrera   `/cars/porsche-911/`
  🛻 Cadillac Escalade     `/cars/cadillac-escalade/`
  🏢 About Us              `/about/`

------------------------------------------------------------------------

## ❤️ Project

**MOTORQUE** --- *More than cars. A statement.*

🔗 [View the repository on
GitHub](https://github.com/iimustafa/LAB-SPORTS-CARS)
