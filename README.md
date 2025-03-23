# 🚀 RAG-Based Document Q&A System

Welcome to the **RAG-Based Document Q&A System**! This project combines **FastAPI**, **Streamlit**, **PostgreSQL**, and **Machine Learning** to provide an interactive document-based Q&A system. Users can **upload documents, ask questions**, and retrieve answers based on semantic similarity using **SentenceTransformers**. 🔥

## 📌 Features
✅ **User Authentication** (Registration & Login)
✅ **Token-based Authentication using JWT**
✅ **Document Ingestion & Storage**
✅ **Semantic Search using Sentence Transformers**
✅ **Real-time Q&A System**
✅ **Streamlit Frontend for Easy Interaction**
✅ **PostgreSQL Database Support**
✅ **Toggle Document Active/Inactive**

---

## 🛠️ Installation Guide
Follow these steps to set up the project on your local machine:

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/satvikbh/RAG_Application
```

### 2️⃣ Set Up PostgreSQL Database
Ensure you have **PostgreSQL** installed and running. You can install it using:

#### For Ubuntu:
```sh
sudo apt update
sudo apt install postgresql postgresql-contrib
```

#### For macOS (Using Homebrew):
```sh
brew install postgresql
brew services start postgresql
```

#### For Windows:
Download and install PostgreSQL from [here](https://www.postgresql.org/download/).

Once installed, open the **PostgreSQL Shell (psql)** and create a database:
```sql
CREATE DATABASE ragdb;
```
You may also need to set up a user:
```sql
CREATE USER postgres WITH ENCRYPTED PASSWORD '1111';
ALTER ROLE postgres SET client_encoding TO 'utf8';
GRANT ALL PRIVILEGES ON DATABASE ragdb TO postgres;
```

To test the connection, use:
```sh
psql -U postgres -d ragdb
```
If connected successfully, you're all set! 🎯

---

### 3️⃣ Install Dependencies
We use Python's `venv` to manage dependencies:
```sh
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

---

### 4️⃣ Run the Backend Server
```sh
uvicorn main:app --reload
```
Your FastAPI backend should now be running at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) 🎯

---

### 5️⃣ Run the Frontend (Streamlit)
```sh
streamlit run app.py
```
Your frontend should now be running at: [http://localhost:8501](http://localhost:8501) 🎨

---

## 🔑 API Structure
The following API endpoints are available:

### 🏷️ **User Authentication**
- **Register**: `POST /register/` - Register a new user.
- **Login**: `POST /token` - Obtain an authentication token.

### 📄 **Document Management**
- **Upload Document**: `POST /ingest/` - Upload a document with embeddings.
- **Toggle Document Active Status**: `PUT /toggle-document/{doc_id}` - Enable/Disable a document.

### ❓ **Q&A System**
- **Ask a Question**: `POST /ask/` - Get an answer based on the uploaded documents.

---

## 🐞 Common Issues & Fixes

🔹 **Issue**: *Database connection error*
   - **Fix**: Ensure PostgreSQL is running, and the `DATABASE_URL` in `main.py` is correct.
   - Use `pg_isready` to check if PostgreSQL is running.

🔹 **Issue**: *ModuleNotFoundError*
   - **Fix**: Run `pip install -r requirements.txt`.

🔹 **Issue**: *FastAPI not starting*
   - **Fix**: Ensure `uvicorn` is installed (`pip install uvicorn`).

🔹 **Issue**: *Frontend not displaying*
   - **Fix**: Ensure Streamlit is installed (`pip install streamlit`) and running.

🔹 **Issue**: *JWT Token Expired*
   - **Fix**: Log in again to obtain a fresh token.

🔹 **Issue**: *Document not being retrieved*
   - **Fix**: Ensure the document is active (`PUT /toggle-document/{doc_id}` to toggle status).

🔹 **Issue**: *Embedding model not found*
   - **Fix**: Ensure SentenceTransformers is installed: `pip install sentence-transformers`.

---

## 🎯 Future Enhancements
🔹 Add support for **multiple users** and **role-based access**
🔹 Implement **document summarization**
🔹 Enhance **UI/UX** of the frontend
🔹 Add **batch document ingestion**
🔹 Implement **chatbot-like conversation**

---

## 🤝 Contributing
Want to improve this project? Fork the repo, make your changes, and submit a PR! 🎉

---

## 📜 License
This project is licensed under the **MIT License**.

💡 *Enjoy building AI-powered Q&A systems!* 🚀

