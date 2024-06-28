
import tkinter as tk
from tkinter import scrolledtext
import random

class ChatbotApp:
    def __init__(self, master):
        self.master = master
        master.title("Chatbot")

        self.chat_history = scrolledtext.ScrolledText(master, width=60, height=20)
        self.chat_history.pack(pady=10)

        self.user_input = tk.Entry(master, width=50)
        self.user_input.pack(pady=10)

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.pack()

    def send_message(self):
        user_input_text = self.user_input.get()
        self.chat_history.insert(tk.END, "User: " + user_input_text + "\n")
        response = self.generate_response(user_input_text)
        self.chat_history.insert(tk.END, "Chatbot: " + response + "\n")
        self.user_input.delete(0, tk.END)

    def generate_response(self, user_input):
        responses = {
            "hello": "Hello! How can I assist you?",
            "how are you": "I'm doing well, thank you for asking.",
            "bye": "Goodbye! Have a great day!",
        }
        
        for query, response in responses.items():
            if query in user_input.lower():
                return response
                
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

def main():
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
