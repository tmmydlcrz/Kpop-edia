# Kpop-edia 🎶

Kpop-edia is a web application dedicated to providing information about K-pop artists, groups, and discographies. Built with **React** for the frontend and **Django + Django REST Framework (DRF)** for the backend, this project enables users to explore and manage K-pop-related data efficiently.

## 🚀 Features

- 🖼️ Dynamic K-pop artist profiles  
- 🎵 CRUD operations for managing artists and albums  
- 🔎 Search and filter functionality  
- 🎨 Responsive UI with background customization  

## 🛠️ Tech Stack

**Frontend:**  
- React  
- CSS (Styled Components / Tailwind)  

**Backend:**  
- Django  
- Django REST Framework (DRF)  
- PostgreSQL / SQLite  

## 📂 Project Structure

```
Kpop-edia/
│── frontend/        # React Frontend
│   ├── public/      # Static assets (e.g., images, favicon, index.html)
│   ├── src/
│   │   ├── components/   # Reusable UI components (e.g., ArtistList.js)
│   │   ├── services/     # API calls (e.g., api.js)
│   │   ├── styles/       # CSS files (e.g., styles.css, index.css)
│   │   ├── App.js        # Main React component
│   │   ├── index.js      # Entry point
│   ├── package.json      # Dependencies and scripts
│   ├── .gitignore        # Ignored files for Git
│── backend/         # Django Backend
│   ├── kpopedia/    # Django project files
│   │   ├── settings.py   # Django settings (DB, REST Framework)
│   │   ├── urls.py       # API routing
│   │   ├── wsgi.py       # Web Server Gateway Interface
│   │   ├── asgi.py       # Async Server Gateway Interface
│   ├── api/         # API App for handling requests
│   │   ├── models.py     # Database models
│   │   ├── serializers.py # DRF Serializers
│   │   ├── views.py      # API Views
│   │   ├── urls.py       # API Endpoints
│   ├── db.sqlite3        # SQLite database (or PostgreSQL)
│   ├── manage.py         # Django CLI tool
│   ├── requirements.txt  # Python dependencies
│── README.md        # Project documentation
│── .gitignore       # Ignored files for Git


```


###2️⃣ Backend Setup (Django)
```
bash
Copy
Edit
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
###3️⃣ Frontend Setup (React)
```
bash
Copy
Edit
cd frontend
npm install
npm start
```
🌟 Contributing
Feel free to contribute! Fork the repository, make changes, and submit a pull request.

📜 License
This project is licensed under the MIT License.
