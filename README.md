Title: Django Stripe Test Project – VipraTech

Description:

A simple Django application demonstrating Stripe payment integration with three fixed products. Paid orders are displayed immediately after successful payment.

Assumptions Made:

Only three fixed products available.

Payment flow is in Stripe test mode.

User authentication is optional and not implemented (or if implemented, mention it).

Stripe Flow Choice and Reasoning:

Used Stripe Checkout Session because it simplifies payment handling and automatically handles payment status, currency, and secure redirect.

Double-Charge Prevention:

Orders are linked with stripe_session_id which is unique.

Once an order has a PAID status, further requests with the same session are ignored.

Setup Instructions:

# Clone the repo
git clone <repo_url>
cd my-django-stripe-project


# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


# Install dependencies
pip install -r requirements.txt


# Setup .env file from .env.example
# STRIPE_SECRET_KEY=<your_key>
# STRIPE_PUBLISHABLE_KEY=<your_key>


# Apply migrations
python manage.py migrate


# Run server
python manage.py runserver

Notes on Code Quality:

Proper models with clear relationships.

Views handle Stripe checkout securely.

Frontend uses basic Bootstrap for styling.

Comments added for clarity.

Actual Time Spent:

e.g., 3-4 hours