# Usage

This guide shows how to run and interact with the **AI Multilingual FAQ Chatbot**.

---

## 1️⃣ Run the Flask App

Open your terminal and navigate to your project folder:

```bash
cd faq-bot
python app.py


🧩 Usage Guide

This guide explains how to use the AI Multilingual FAQ Chatbot, including example questions, multilingual support, and voice input.



1. Example Questions

Try asking the bot questions similar to those in your faq.json. Here are some examples:

Question	Expected Behavior
How long does delivery take?	Bot provides the estimated delivery time.
What is your return policy?	Bot shows return/refund policies.
Can I cancel my order?	Bot responds with cancellation procedure.
What are the payment options?	Bot lists available payment methods.
मेरी ऑर्डर की स्थिति क्या है? (Hindi)	Bot translates & responds in Hindi.
माझी ऑर्डर रद्द करू शकतो का? (Marathi)	Bot translates & responds in Marathi.

✅ The bot uses semantic matching via NLP, so even if your question wording changes slightly, it can still find the closest answer.


How Multilingual Support Works

The user can type a question in any language (English, Hindi, Marathi, etc.).

The bot uses Deep Translator API to detect and translate the question to English.

NLP model finds the best matching answer in English.

The bot translates the answer back to the user’s language before replying.

This ensures accurate answers without the user needing to type in English only.




4. How Voice Input Works

The user can speak their question using the voice input button.

The browser captures the audio and converts it to text using Web Speech API (or a similar method).

The bot processes the text just like a typed question.

Response is displayed on the chat interface in the selected language.

Voice input allows hands-free interaction and a more natural user experience.




5. Auto-learning Unknown Questions

If the bot cannot find a matching answer:

It saves the question to unknown_questions.txt.

You can review new questions and update faq.json to improve the bot’s knowledge over time.

This makes it easy to show your project in action, demonstrate multilingual support, and highlight advanced features like voice input and auto-learning.
