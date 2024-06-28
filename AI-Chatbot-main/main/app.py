# -*- coding: utf-8 -*-
"""
Title: AI Chatbot for Customer Service
Industry: CRM - Customer Relationship Management
@author: Tabish Ali Ansari
"""

from flask import Flask, request, jsonify
import spacy

app = Flask(__name__)

nlp = spacy.load("en_core_web_sm")

user_data = {}

@app.route("/message", methods=["POST"])
def handle_message():

    user_message = request.json["message"]
    
    doc = nlp(user_message)
    
    intent = "dummy_intent"
    
    if intent == "dummy_intent":
        response = "This is a dummy response."
    else:
        response = "Sorry, I didn't understand that."
    
    user_id = request.json["user_id"]
    if user_id not in user_data:
        user_data[user_id] = []
    user_data[user_id].append({"message": user_message, "response": response})
    
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
