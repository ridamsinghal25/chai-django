# 🫖 Chai Django Project

This is a Django web application for managing different varieties of chai (tea).  
It allows you to **add**, **update**, **delete**, and **list** chai varieties with details like name, type, description, price, and image.

---

## 🚀 Features

- 📝 Add new chai varieties
- ✏️ Update existing chai details
- 🗑️ Delete chai varieties
- 📃 List all chai varieties with their details
- 📦 Image upload support for each chai

---

## 🛠️ Tech Stack

- Python 3.x
- Django 4.x
- SQLite (default) or PostgreSQL (optional)
- Tailwind CSS (for styling)

---


## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
    ```

2. **Create a virtual environment**
   ```bash
    python -m venv .venv

    source .venv/bin/activate  # On Windows: .venv\Scripts\activate

   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations
   ```bash
   python manage.py migrate
   ```  

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   Open your web browser and navigate to http://localhost:8000.

---