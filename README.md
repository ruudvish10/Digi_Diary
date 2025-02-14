# Digi_Diary - Secure Your Thought 📖

This Digital Diary is your private and secure space to capture ideas or thoughts on the go, as they occur. Never miss anything key, revise and revisit as you like. Digi_Diary is a secure, user-friendly Django web application that allows users to create, manage, and organize personal notes with a structured hierarchy of topics, subtopics, and rich-text entries—all while ensuring data privacy through user authentication

## Features 🌟
- Organize your thoughts and ideas with topics, subtopics, and rich-text entries
- Search functionality to easily find your information at all levels of hierarchy  
- Cascade delete: Removing a topic automatically deletes its subtopics and entries  
- Responsive UI built with Bootstrap for a seamless experience

## Security & User Authentication 🔐
- Private user accounts ensure data is secure and accessible only to the owner  
- Django's built-in authentication for secure login and account management  
- Password encryption for enhanced security 

## Installation & Setup 🛠️  
1. Clone the repository:
   git clone https://github.com/yourusername/Digi_Diary.git
   cd Digi_Diary

2. Create and Activate a Virtual Environment:
    python -m venv venv     
    On Windows: venv\Scripts\activate

3. Install Dependencies:
    pip install -r requirements.txt  (Ensure this file is updated with all packages)

4. Configure the Database:
    After changes to the db, run the following: 
    python manage.py makemigrations 
    python manage.py migrate 

5. Start the Development Server:
    To start the server locally, run:
    python manage.py runserver
    Visit http://127.0.0.1:8000/ in your browser to access Digi_Diary

Usage 📝
- Register and log in to start using Digi_Diary
- Create topics and subtopics, then add rich-text entries
- Use the search bar to quickly find your information at all three levels
- Manage your content with edit and delete options



