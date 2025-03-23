# frontend.py
import streamlit as st
import requests
from datetime import datetime

# Configuration
API_BASE_URL = "http://localhost:8000"
st.set_page_config(page_title="RAG System", layout="wide")

def main():
    st.title("Document Q&A System")
    
    if 'access_token' not in st.session_state:
        st.session_state.access_token = None
        st.session_state.current_user = None
    
    menu = ["Home", "Login", "Register"]
    if st.session_state.access_token:
        menu = ["Home", "Q&A", "Logout"]
    
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice == "Home":
        st.subheader("Home")
        st.write("Welcome to the Document Q&A System")
        
    elif choice == "Login":
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            response = requests.post(
                f"{API_BASE_URL}/token",
                data={"username": username, "password": password}
            )
            if response.status_code == 200:
                st.session_state.access_token = response.json()["access_token"]
                st.success("Logged in successfully")
            else:
                st.error("Invalid credentials")
    
    elif choice == "Register":
        st.subheader("Create New Account")
        new_username = st.text_input("Username")
        new_password = st.text_input("Password", type="password")
        if st.button("Register"):
            try:
                response = requests.post(
                    f"{API_BASE_URL}/register/",
                    json={"username": new_username, "password": new_password}
                )
                if response.status_code == 201:
                    st.success("Account created successfully")
                else:
                    st.error(f"Registration failed: {response.json().get('detail', 'Unknown error')}")
            except requests.exceptions.RequestException as e:
                st.error(f"Failed to connect to the server: {e}")
    
    elif choice == "Q&A":
        st.subheader("Q&A Section")
        
        # Document Upload Section
        st.markdown("### Upload a Document")
        doc_title = st.text_input("Document Title")
        doc_content = st.text_area("Document Content", height=200)
        if st.button("Upload Document"):
            headers = {"Authorization": f"Bearer {st.session_state.access_token}"}
            response = requests.post(
                f"{API_BASE_URL}/ingest/",
                json={"title": doc_title, "content": doc_content},
                headers=headers
            )
            if response.status_code == 200:
                st.success("Document uploaded successfully")
            else:
                st.error("Upload failed")
        
        # Question Section
        st.markdown("### Ask a Question")
        question = st.text_area("Your Question", height=100)
        if st.button("Get Answer"):
            headers = {"Authorization": f"Bearer {st.session_state.access_token}"}
            response = requests.post(
                f"{API_BASE_URL}/ask/",
                json={"question": question},
                headers=headers
            )
            if response.status_code == 200:
                answer = response.json().get("answer")
                st.subheader("Answer:")
                st.write(answer)
            else:
                st.error("Failed to get answer")
    
    elif choice == "Logout":
        st.session_state.access_token = None
        st.session_state.current_user = None
        st.success("Logged out successfully")

if __name__ == "__main__":
    main()