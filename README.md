Project Overview

A simple Django application demonstrating Stripe payment integration with three fixed products.
After a successful payment, the paid order is displayed immediately on the same page.

This project was built as part of a technical assignment for VipraTech Labs Pvt. Ltd.

Assumptions Made

Only three fixed products are available.

Payment is handled in Stripe test mode.

User authentication is optional and not implemented.

Orders are displayed immediately after payment; no separate order history page exists.

SQLite is used for simplicity (can be switched to PostgreSQL/MySQL).

Stripe Flow Choice and Reasoning

Flow Used: Stripe Checkout Session (redirect-based)

Reasoning:

Secure and easy to implement for a fixed-product scenario.

Card details are handled entirely by Stripe, reducing PCI compliance complexity.

Stripe manages validation, success, and failure handling.

Ideal for assignments and demos where correctness and clarity matter more than complexity.

Double-Charge Prevention Strategy

Each order stores a unique stripe_session_id.

Before marking an order as PAID, the system verifies that the session ID has not already been processed.

This prevents duplicate charges if the success URL is refreshed.

In real production systems, Stripe Webhooks would be used for maximum reliability (not required for this assignment).

Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/Sourabh2517x/VIPRA_ASSIGNMENT.git
cd VIPRA_ASSIGNMENT

All Django commands must be run from the directory containing manage.py.

2️⃣ Create Virtual Environment & Install Dependencies
python -m venv venv


# Activate virtual environment
# Linux / Mac
source venv/bin/activate


# Windows
venv\Scripts\activate


pip install -r requirements.txt
3️⃣ Environment Variables

Create a .env file in the project root (same level as manage.py) using .env.example.

STRIPE_PUBLIC_KEY=pk_test_xxxxxxxxxxxxx
STRIPE_SECRET_KEY=sk_test_xxxxxxxxxxxxx

Environment variables are loaded using python-dotenv in settings.py.

4️⃣ Apply Migrations
python manage.py migrate
5️⃣ (Optional) Create Superuser
python manage.py createsuperuser
6️⃣ Run the Server
python manage.py runserver

Visit:
👉 http://127.0.0.1:8000

Notes on Code Quality

Clear separation between ProductModel and Order.

Payment logic kept minimal and readable.

No unnecessary abstractions — clarity over over-engineering.

Inline comments explain key logic.

Defensive checks added for invalid or duplicate Stripe sessions.

Structure follows standard Django best practices.

AI-Assist Documentation

See AI-assist.md for full details on tools used and how they assisted development.