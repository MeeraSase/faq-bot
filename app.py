"""from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

with open("faq.json") as f:
    faq_data = json.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot():
    user_msg = request.json.get("message").lower()

    for item in faq_data:
        if user_msg in item["question"].lower():
            return jsonify({"reply": item["answer"]})

    return jsonify({"reply": "Sorry, I don't understand."})

if __name__ == "__main__":
    app.run(debug=True)"""




"""from flask import Flask, render_template, request, jsonify
import json
from sentence_transformers import SentenceTransformer, util

app = Flask(__name__)

# Load AI model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load FAQ data
with open("faq.json") as f:
    faq_data = json.load(f)

faq_questions = [item["question"] for item in faq_data]
faq_embeddings = model.encode(faq_questions, convert_to_tensor=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot():
    user_msg = request.json.get("message")

    user_embedding = model.encode(user_msg, convert_to_tensor=True)

    similarities = util.cos_sim(user_embedding, faq_embeddings)
    best_match = similarities.argmax().item()

    if similarities[0][best_match] > 0.5:
        return jsonify({"reply": faq_data[best_match]["answer"]})

    return jsonify({"reply": "Sorry, I don't understand."})

if __name__ == "__main__":
    app.run(debug=True)"""


from flask import Flask, render_template, request, jsonify
import json
import os   # NEW
from sentence_transformers import SentenceTransformer, util
from deep_translator import GoogleTranslator

app = Flask(__name__)

# Load AI model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load FAQ data
with open("faq.json") as f:
    faq_data = json.load(f)

faq_questions = [item["question"] for item in faq_data]
faq_embeddings = model.encode(faq_questions, convert_to_tensor=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot():
    user_msg = request.json.get("message")

    # Translate user message to English
    translated_msg = GoogleTranslator(source='auto', target='en').translate(user_msg)

    # AI Matching
    user_embedding = model.encode(translated_msg, convert_to_tensor=True)
    similarities = util.cos_sim(user_embedding, faq_embeddings)
    best_match = similarities.argmax().item()

    if similarities[0][best_match] > 0.5:

        answer = faq_data[best_match]["answer"]

        # Translate answer back
        final_answer = GoogleTranslator(source='en', target='auto').translate(answer)

        return jsonify({"reply": final_answer})

    # ⭐ AUTO LEARNING FEATURE
    else:

        # Create file if not exists
        if not os.path.exists("unknown_questions.txt"):
            open("unknown_questions.txt", "w").close()

        # Save unknown question
        with open("unknown_questions.txt", "a", encoding="utf-8") as file:
            file.write(user_msg + "\n")

        return jsonify({"reply": "I am still learning. Your question is saved."})

if __name__ == "__main__":
    app.run(debug=True)