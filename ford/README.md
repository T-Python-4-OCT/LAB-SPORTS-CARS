# Ford Showroom

A responsive Ford vehicle showroom built with Django for the LAB-SPORTS-CARS project. It features 20 vehicles covering every model year from 2010 through 2027, with Arabic and English interfaces.

## Features

- Responsive layouts for desktop, tablet, and mobile.
- Light and dark themes with saved preferences.
- Homepage with a Mustang video and a smaller mobile version.
- Vehicle search and filters for model, year, and price.
- Individual vehicle pages with separate overview, specifications, and features.
- Full-screen image galleries.
- Two-car comparison with a differences-only option.
- Test-drive booking with city, date, and time selection.
- Cash-purchase requests and an installment calculator.
- Local account registration and sign-in.
- Remember me sessions lasting two days.
- Account-based favorites and browser-based guest favorites.
- Recently viewed vehicles and saved comparison selections.
- An About Us page with Ford history and showroom information.
- Animations that respect reduced-motion preferences.

Prices, purchase requests, bookings, financing estimates, and newsletter signup demonstrate the website's functionality. Payments are not collected, and requests are not sent to Ford Motor Company.

## Technologies

- Python
- Django 5.2
- SQLite
- Django Templates
- HTML and CSS
- JavaScript
- Locally hosted Google Fonts and icons

## Requirements

- Python 3.12 or 3.13
- An internet connection for the initial dependency installation
- A modern web browser

## First-Time Setup on Windows

Download or clone the repository, then open PowerShell in this ford folder.

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py runserver
```

If your Python installation uses `python` instead of `py`, create the environment with `python -m venv .venv`.

Open [Ford Showroom](http://127.0.0.1:8000/home/).

The migration command creates the database and automatically adds all 20 vehicles. Register through the website to try accounts and favorites.

## First-Time Setup on macOS or Linux

Open a terminal in this ford folder.

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python manage.py migrate
.venv/bin/python manage.py runserver
```

Some Linux distributions require their `python3-venv` package to create virtual environments.

## Running the Project Again

From the `ford` folder on Windows.

```powershell
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py runserver
```

From the `ford` folder on macOS or Linux.

```sh
.venv/bin/python manage.py migrate
.venv/bin/python manage.py runserver
```

Press `Ctrl+C` in the terminal to stop the server.

If port 8000 is already in use, run `manage.py runserver 8001` with your environment's Python executable and open `http://127.0.0.1:8001/home/`.

## Main Pages

| Page | URL |
|---|---|
| Home | `/home/` |
| All Cars | `/cars/` |
| Vehicle Details Example | `/cars/mustang-gt/` |
| About Us | `/about/` |
| Sign In and Account | `/account/` |
| Registration | `/account/register/` |
| Django Admin | `/admin/` |

## Admin Access

Create an administrator from the `ford` folder.

```powershell
.\.venv\Scripts\python.exe manage.py createsuperuser
```

On macOS or Linux, use `.venv/bin/python manage.py createsuperuser`.

Visit `/admin/` to manage vehicles and review purchase requests and test-drive bookings.

## Checks and Tests

Run from the `ford` folder on Windows.

```powershell
.\.venv\Scripts\python.exe manage.py check
.\.venv\Scripts\python.exe manage.py test
```

On macOS or Linux, replace the Python path with `.venv/bin/python`.

Tests cover filtering, comparisons, bookings, purchase requests, accounts, favorites, session expiration, and theme persistence.

## Project Structure

```text
ford/
├── manage.py
├── requirements.txt
├── config/
│   ├── settings.py
│   └── urls.py
└── showroom/
    ├── models.py
    ├── forms.py
    ├── views.py
    ├── urls.py
    ├── tests.py
    ├── migrations/
    ├── templates/showroom/
    ├── static/showroom/
    └── locale/ar/
```

## Assets and Data

Vehicle images, desktop and mobile videos, fonts, icons, and the compiled Arabic translation are included in the repository.

Keep the `static`, `locale`, and `migrations` folders when copying the project. The virtual environment and SQLite database are created during setup.

External Ford and social-media links require an internet connection.

## Saved Preferences

| Preference | Duration |
|---|---|
| Language and theme | 180 days |
| Remember me | 2 days |
| Vehicle comparison | 2 days |
| Recently viewed vehicles | 7 days |
| Search filters | Browser tab session |

Signed-in favorites are stored in the database and linked to the user's account.

## Lab Requirements

The project implements template inheritance, static assets, Google Fonts and icons, dark mode, CSS transitions and animations, responsive layouts, and the required home, inventory, vehicle detail, and About Us pages.

The included settings support local development and academic evaluation. Public deployment requires production configuration.
