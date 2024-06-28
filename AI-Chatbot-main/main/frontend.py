#author: Khushal Sharma

import tkinter as tk
from tkinter import scrolledtext

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
        # Call your chatbot logic here and get the response
        response = "Chatbot: Hello! How can I assist you?"
        self.chat_history.insert(tk.END, response + "\n")
        self.user_input.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
