from flask import Flask, render_template, request, jsonify
import json
import random
import nltk
from nltk.stem import WordNetLemmatizer

# Initialize NLTK
nltk.download('punkt')
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()

# Load intents
with open('intents.json') as f:
    intents = json.load(f)

# Tokenize and lemmatize user input
def tokenize_and_lemmatize(sentence):
    words = nltk.word_tokenize(sentence.lower())
    return [lemmatizer.lemmatize(w) for w in words]

# Generate response
def get_response(user_input):
    for intent, data in intents.items():
        for example in data["examples"]:
            if set(tokenize_and_lemmatize(user_input)) & set(tokenize_and_lemmatize(example)):
                return random.choice(data["responses"])
    return "Sorry, I don't understand."

# Initialize Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.form["msg"]
    response = get_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
