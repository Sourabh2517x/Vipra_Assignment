Project Overview

A simple Django application demonstrating Stripe payment integration with three fixed products. Paid orders are displayed immediately after successful payment.

Assumptions Made

Only three fixed products are available.

Payment flow is in Stripe test mode.

User authentication is optional and not implemented (or mentioned if implemented).

Orders are displayed immediately after payment without a separate order history page.

Stripe Flow Choice and Reasoning

Flow Used: Stripe Checkout Session (redirect-based)

Reasoning:

Simple and secure for a fixed-product scenario.

Handles card input and validation on Stripe’s hosted page → reduces PCI compliance complexity.

Automatic payment status tracking and success/failure redirects make it ideal for a quick demo project.

Double-Charge Prevention Strategy

Each order is assigned a unique stripe_session_id.

Before marking an order as PAID, the system checks if that stripe_session_id already exists in the database.

This prevents accidental double-processing of the same session.

Optional: Use Stripe webhooks in production for extra reliability (not required in test/demo mode).

Setup Instructions

Clone the repository

git clone <repo-url>
cd <project-folder>

Create virtual environment & install dependencies

python -m venv VE
source VE/bin/activate   # Linux/Mac
VE\Scripts\activate      # Windows
pip install -r requirements.txt

Set up database

Default is SQLite (already configured)

Optional: Switch to PostgreSQL or MySQL in settings.py

Add .env file

Copy .env.example to .env and fill in your Stripe keys:

STRIPE_PUBLIC_KEY=<your-stripe-public-key>
STRIPE_SECRET_KEY=<your-stripe-secret-key>

Apply migrations

python manage.py migrate

Create superuser (optional for admin panel)

python manage.py createsuperuser

Run the server

python manage.py runserver

Visit http://127.0.0.1:8000 to view products and make test payments.

Notes on Code Quality

Clear model separation (ProductModel, Order) with readable fields.

Payment logic encapsulated in a single view for simplicity.

Minimal hardcoding — product details can be expanded via Django admin.

Comments included for all key sections, making it easy to maintain.

Basic error handling for invalid sessions or duplicate payments.

AI-Assist Documentation (AI-assist.md)

Tools used: ChatGPT (GPT-5 mini)

Where applied:

Initial project structure planning

Stripe payment flow guidance

README, .env.example, and doc writing

Troubleshooting model/database issues

Code quality suggestions