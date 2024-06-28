import spacy
from spacy.matcher import Matcher
import sqlite3

# Load English language model
nlp = spacy.load("en_core_web_sm")

# Define patterns for rule-based matching
patterns = [
    {"label": "GREETING", "pattern": [{"LOWER": "hi"}, {"LOWER": "there"}]},
    {"label": "GREETING", "pattern": [{"LOWER": "hello"}]},
    {"label": "GOODBYE", "pattern": [{"LOWER": "bye"}]},
]

# Add patterns to matcher
matcher = Matcher(nlp.vocab)
for pattern in patterns:
    matcher.add(pattern["label"], None, pattern["pattern"])

# Define chatbot response for each label
responses = {
    "GREETING": "Hello! How can I help you?",
    "GOODBYE": "Goodbye! Have a great day!",
    "DEFAULT": "I'm sorry, I didn't understand that.",
}

# Initialize SQLite database
conn = sqlite3.connect("chatbot.db")
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS interactions (id INTEGER PRIMARY KEY, user_input TEXT, chatbot_response TEXT)''')
conn.commit()

# Process user input and generate response
def chatbot_response(user_input):
    doc = nlp(user_input)
    matches = matcher(doc)
    for match_id, start, end in matches:
        label = nlp.vocab.strings[match_id]
        return responses.get(label, responses["DEFAULT"])

# Save user interaction to the database
def save_interaction(user_input, chatbot_response):
    c.execute('''INSERT INTO interactions (user_input, chatbot_response) VALUES (?, ?)''', (user_input, chatbot_response))
    conn.commit()

# Retrieve chatbot response from the database (fallback)
def get_response_from_db(user_input):
    c.execute('''SELECT chatbot_response FROM interactions WHERE user_input = ?''', (user_input,))
    row = c.fetchone()
    return row[0] if row else None

# Main function to interact with the chatbot
def main():
    print("Chatbot: Hello! How can I assist you? (Type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        if response is None:
            response = get_response_from_db(user_input)
        else:
            save_interaction(user_input, response)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()

# Close database connection
conn.close()
