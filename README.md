# Django Stripe Payment Demo

A simple Django application demonstrating **Stripe payment integration** with **three fixed products**. After a successful payment, the paid order is displayed immediately on the **My Orders**.

This project was built as part of a **technical assignment for VipraTech Labs Pvt. Ltd.**

---

## 📌 Project Overview

* Three fixed products displayed on a single page
* User selects quantities and clicks **Buy**
* Payment processed via **Stripe (test mode)**
* After successful payment, the **paid order appears instantly** on the My Orders page

---

## ✅ Assumptions Made

* Only **three fixed products** are available
* Payments run in **Stripe test mode**
* **User authentication is optional** and not implemented
* Orders are shown immediately after payment
* **SQLite** is used for simplicity later switched to postgress

---

## 💳 Stripe Flow Choice & Reasoning

**Flow Used:** Stripe Checkout Session (redirect-based)

**Why this approach?**

* Secure and quick to implement for fixed products
* Card details are handled entirely by Stripe (reduced PCI complexity)
* Stripe manages validation, success, and failure states
* Ideal for demos and assignments where clarity > complexity

---

## 🔒 Double-Charge Prevention Strategy

* Each order stores a unique `stripe_session_id`
* Before marking an order as **PAID**, the system checks whether the session ID was already processed
* Prevents duplicate charges if the success URL is refreshed

> ⚠️ In production systems, **Stripe Webhooks** should be used for maximum reliability (not required for this assignment)

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Sourabh2517x/VIPRA_ASSIGNMENT.git
cd VIPRA_ASSIGNMENT
```

> All Django commands must be run from the directory containing `manage.py`

---

### 2️⃣ Create Virtual Environment & Install Dependencies

```bash
python -m venv VE
```

**Activate the virtual environment**

* **Linux / Mac**

  ```bash
  source VE/bin/activate
  ```
* **Windows**

  ```bash
  VE\Scripts\activate
  ```

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Environment Variables

Create a `.env` file in the project root (same level as `manage.py`) using `.env.example`.

```env
STRIPE_PUBLIC_KEY=pk_test_xxxxxxxxxxxxx
STRIPE_SECRET_KEY=sk_test_xxxxxxxxxxxxx
```

Environment variables are loaded using **python-dotenv** in `settings.py`.

---

### 4️⃣ Apply Migrations

```bash
python manage.py migrate
```

---

### 5️⃣ (Optional) Create Superuser

```bash
python manage.py createsuperuser
```

---

### 6️⃣ Run the Server

```bash
python manage.py runserver
```

Visit 👉 **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## 🧠 Notes on Code Quality

* Clear separation between **Product** and **Order** models
* Minimal and readable payment logic
* No unnecessary abstractions — clarity over over-engineering
* Inline comments explain key logic
* Defensive checks for invalid or duplicate Stripe sessions
* Follows standard Django project structure and best practices

---

## 🤖 AI-Assist Documentation

See **AI-assist.md** for full details on tools used and how they assisted development.
