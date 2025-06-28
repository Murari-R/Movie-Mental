# 🎬 MOVIE MENTAL

**MOVIE MENTAL** is a local, lightweight movie recommendation system that lets users discover movies based on **actor names** and **genres**. It fetches smart suggestions using the **TMDb API**, wrapped in a creative, minimal frontend and a Python Flask backend — all running locally without hosting or login.

---

## 📌 Features

- 🎭 Search by **Actor Name**
- 🎞️ Filter by **Genre**
- 🚀 Top 5 most popular suggestions
- 🖥️ Clean and creative browser UI
- 🔒 No signup or hosting needed — runs locally

---

## 🧰 Tech Stack

| Layer     | Tech                  |
|-----------|------------------------|
| Frontend  | HTML, CSS, JavaScript  |
| Backend   | Python, Flask, Flask-CORS |
| API       | TMDb (The Movie Database) |
| Tools     | Virtualenv, Local Filesystem |

---

## 🗂️ Project Structure

```
movie-mental/
│
├── backend/
│   ├── app.py             # Flask API server
│   ├── tmdb.py            # TMDb API logic
│   ├── requirements.txt   # Python dependencies
│   └── venv/              # Python virtual environment
│
└── frontend/
    ├── index.html         # Main UI
    ├── style.css          # UI styling
    └── script.js          # Frontend logic
```

---

## 🔑 Get TMDb API Key

1. Visit: [https://www.themoviedb.org](https://www.themoviedb.org)
2. Log in → Click your avatar → Settings → API
3. Under **API v3 auth**, click **Create**
4. Fill in:
   - App Name: `Movie Mental`
   - App Type: `Hobby/Personal`
   - App URL: `http://localhost:5000`
   - Description:  
     > A personal movie suggestion app that recommends movies by actor and genre using TMDb API.
5. Once submitted, copy your API Key.
6. Open `tmdb.py` and paste:
```python
TMDB_API_KEY = "your_api_key_here"
```

---

## ⚙️ Installation (Windows)

### 📁 Backend Setup

```bash
cd movie-mental\backend
python -m venv venv
venv\Scripts\activate
pip install flask flask-cors requests
```

_Optional:_

```bash
pip freeze > requirements.txt
```

### ▶️ Run Backend

```bash
python app.py
```

Should display:
```
Running on http://127.0.0.1:5000/
```

---

## 🌐 Frontend Usage

1. Open `movie-mental/frontend/index.html` in any browser
2. Enter an actor (e.g. Ranbir Kapoor) and genre (e.g. Romance)
3. Click **"Get Suggestions"**
4. Top 5 movie suggestions are displayed

---

## 🔄 System Flowchart

```
User Input (actor + genre)
     ↓
Frontend (JS fetch request)
     ↓
Backend (Flask receives request)
     ↓
TMDb API (searches actor + genre)
     ↓
Returns JSON with 5 movies
     ↓
Frontend renders movie titles + descriptions
```

---

## 🔮 Future Upgrades

- 🖼️ Show posters and trailers using TMDb media links
- 📺 Add OTT platform filters using JustWatch or uNoGS APIs
- 😄 Add mood filters like "feel good", "heartbreak", "intense"
- 💾 Save favorite movies locally using browser storage
- 🎙️ Add speech-based input for voice commands

---

## 🧽 Cleanup

To deactivate virtual environment:

```bash
deactivate
```

To remove:

```bash
rd /s /q venv
```

---

## 📜 License

This project is for personal and educational use only.  
Built using the free **TMDb API**. This product is not endorsed or certified by TMDb.

---

## 🙌 Credits

- API: [TMDb - The Movie Database](https://www.themoviedb.org)
- Project by: [Your Name]