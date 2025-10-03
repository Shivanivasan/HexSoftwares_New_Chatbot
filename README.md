Chatbot Project
Overview

This project is a simple yet interactive chatbot application. It combines a Flask backend with a clean frontend interface designed in HTML, CSS, and JavaScript. The chatbot follows a messenger-style design with a light aesthetic and multiple engaging features.

Features

Modern and clean chat interface

Emoji and sticker support

Story option with like functionality

Last seen status display

Language switching option (includes Japanese style)

Chatbot responses powered by intents.json

Flask backend to process and serve responses

Project Structure
chatbot-project/
│
├── main.py            # Flask backend server
├── intents.json       # Chatbot intents and responses
├── templates/
│   └── index.html     # Frontend HTML (chat interface)
├── static/
│   ├── style.css      # CSS styling
│   └── script.js      # JavaScript (chat functionality)
└── README.md          # Project documentation

Requirements

Python 3.7+

Flask

nltk

Installation

Clone or download the repository:

git clone https://github.com/your-username/chatbot-project.git
cd chatbot-project


Create and activate a virtual environment:

python -m venv chatbotenv
chatbotenv\Scripts\activate   # On Windows
source chatbotenv/bin/activate  # On Mac/Linux


Install dependencies:

pip install flask nltk


Download NLTK data (only the first time):

python
>>> import nltk
>>> nltk.download('punkt')
>>> nltk.download('wordnet')

Running the Project

Start the Flask server:

python main.py


Open your browser and visit:

http://127.0.0.1:5000/

Customization

Update intents.json to add or edit chatbot responses (e.g., greetings, thank you, happy birthday, story replies).

Modify index.html and style.css to adjust the look and feel of the chat interface.

Add new stickers or emojis in the frontend for a more personalized experience.

License

This project is open-source and free to use for personal or educational purposes.

Do you want me to also add a sample intents.json snippet inside the README, so anyone new can quickly see how to add replies?
