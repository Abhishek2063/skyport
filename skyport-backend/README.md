
# 🐍 Flask Backend with PostgreSQL

This project is a boilerplate backend built using **Flask (Python)** and **PostgreSQL** with a clean folder structure, best practices, and basic API setup.

---

## 🗂️ Project Structure

```

backend/
│
├── app/
│   ├── **init**.py            # Initializes Flask app & extensions
│   ├── config.py              # Configuration (dev, prod, test)
│   ├── models/                # SQLAlchemy models
│   ├── routes/                # Route definitions
│   ├── services/              # Business logic layer
│   ├── controllers/           # API logic
│   ├── utils/                 # Helper functions
│   └── validations/           # Request schema validations
│
├── migrations/                # Alembic migration files
├── .env                       # Environment variables
├── requirements.txt           # Python dependencies
├── run.py                     # Entry point to run the app
└── README.md                  # Project documentation

````

---

## ⚙️ Tech Stack

- **Python 3.x**
- **Flask**
- **SQLAlchemy**
- **PostgreSQL**
- **Marshmallow / Pydantic**
- **Flask-Migrate** (for DB migrations)
- **dotenv** (for env variables)

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Abhishek2063/skyport.git
cd your-repo-name/backend
````

### 2️⃣ Create virtual environment & activate it

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Create a `.env` file

```env
FLASK_ENV=development
FLASK_APP=run.py
SECRET_KEY=your_secret_key
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/your_db_name
```

### 5️⃣ Set up the PostgreSQL DB using pgAdmin

* Create a database named `your_db_name`
* Ensure port 5432 is open and password for `postgres` is set

### 6️⃣ Run migrations

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 7️⃣ Run the server

```bash
flask run
```

---

## 📬 API Routes

| Method | Endpoint          | Description     |
| ------ | ----------------- | --------------- |
| GET    | `/api/users`      | Get all users   |
| POST   | `/api/users`      | Create new user |
| GET    | `/api/users/<id>` | Get single user |
| PUT    | `/api/users/<id>` | Update user     |
| DELETE | `/api/users/<id>` | Delete user     |

---

## 🧪 Testing

You can use tools like **Postman**, **Insomnia**, or **cURL** to test the APIs.

---

## 📌 Useful Commands

```bash
flask db migrate -m "message"    # Create migration
flask db upgrade                 # Apply migrations
flask db downgrade               # Rollback migration
```

---

## 👨‍💻 Author

Made with ❤️ by Abhishek Garg
📧 [abhishekgarg2063@gmail.com](mailto:abhishekgarg2063@gmail.com)

---

## 📄 License

This project is licensed under the MIT License.

```

