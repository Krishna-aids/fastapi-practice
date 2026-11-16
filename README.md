# 🏥 Patient Management System


## 📌 Project Overview

The **Patient Management System** is a web-based application that allows users to manage patient records through a user-friendly interface.

It uses FastAPI to build RESTful APIs and Streamlit to create an interactive frontend.

Users can add, view, search, update, delete, sort, and analyze patient information.

## 🚀 Live Demo

| Component         | Link                                                                |
| ----------------- | ------------------------------------------------------------------- |
| Backend API       | [Render API](https://patient-management-api-6zki.onrender.com)      |
| API Documentation | [Swagger UI](https://patient-management-api-6zki.onrender.com/docs) |
| Frontend          | https://patient-management-api-6zki.streamlit.app/                  |

## ✨ Features

- ➕ **Add Patient:** Create new patient records.
- 👁️ **View Patients:** Display all registered patients.
- 🔍 **Search Patient:** Find patients using their unique ID.
- ✏️ **Update Patient:** Modify existing patient details.
- 🗑️ **Delete Patient:** Remove patient records.
- 📊 **Sort Patients:** Sort records by height, weight, or BMI.
- 🧮 **BMI Calculation:** Automatically calculate Body Mass Index.
- 📈 **Health Verdict:** Generate a basic BMI-based category.
- 📖 **API Documentation:** Explore and test APIs using Swagger UI.

## 🛠️ Tech Stack

| Technology      | Purpose              |
| --------------- | -------------------- |
| Python          | Programming language |
| FastAPI         | Backend framework    |
| Streamlit       | Frontend framework   |
| Pydantic        | Data validation      |
| Requests        | API communication    |
| JSON            | Demo data storage    |
| Git & GitHub    | Version control      |
| Render          | Backend deployment   |
| Streamlit Cloud | Frontend deployment  |

## 📂 Project Structure

```text
fastapi-practice/
│
├── main.py                 # FastAPI backend
├── patient_frontend.py     # Streamlit frontend
├── patients.json           # Patient records (demo data)
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
└── .gitignore              # Ignored files
```

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Krishna-aids/fastapi-practice.git
```

### 2. Navigate to the project directory

```bash
cd fastapi-practice
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application Locally

The backend and frontend run separately.

### Start FastAPI Backend

Open your first terminal:

```bash
uvicorn main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

### Start Streamlit Frontend

Open a second terminal:

```bash
streamlit run patient_frontend.py
```

Frontend URL:

```text
http://localhost:8501
```

## 🔗 API Endpoints

| Method | Endpoint        | Description          |
| ------ | --------------- | -------------------- |
| GET    | `/`             | Home                 |
| GET    | `/about`        | About API            |
| GET    | `/view`         | View all patients    |
| GET    | `/patient/{id}` | Get patient by ID    |
| GET    | `/sort`         | Sort patient records |
| POST   | `/create`       | Create a patient     |
| PUT    | `/edit/{id}`    | Update patient       |
| DELETE | `/delete/{id}`  | Delete patient       |

### Example API Request

**POST — Create Patient**

```json
{
  "id": "P001",
  "name": "Rahul",
  "city": "Indore",
  "age": 21,
  "gender": "Male",
  "height": 1.75,
  "weight": 70
}
```

*Note: This example assumes your Patient model uses the fields and validation rules shown.*

## ☁️ Deployment

### Backend Deployment — Render

1. Push your project to GitHub.
2. Open [Render](https://render.com/).
3. Create a new Web Service.
4. Connect your GitHub repository.
5. Configure:

**Build Command:**

```bash
pip install -r requirements.txt
```

**Start Command:**

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

### Frontend Deployment — Streamlit Cloud

1. Open [Streamlit Community Cloud](https://share.streamlit.io/).
2. Connect your GitHub repository.
3. Select `patient_frontend.py` as the main file.
4. Deploy the application.
5. Configure your app secrets:

```toml
API_URL = "https://patient-management-api-6zki.onrender.com"
```

## 🔮 Future Improvements

- [ ] Integrate PostgreSQL database.
- [ ] Add user authentication and authorization.
- [ ] Add patient medical history.
- [ ] Add dashboard analytics and visualizations.
- [ ] Improve input validation and error handling.
- [ ] Add automated API testing using Pytest.

## 👨‍💻 Author

**Krishna Kumrawat**

- GitHub: [Krishna-aids](https://github.com/Krishna-aids)

 

