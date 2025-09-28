import tkinter as tk
from tkinter import scrolledtext

# Function to handle chat response
def send_message():
    user_msg = entry.get()
    if user_msg.strip() == "":
        return
    chat_window.insert(tk.END, "You: " + user_msg + "\n", "user")
    entry.delete(0, tk.END)

    # Simple chatbot logic
    user_msg_lower = user_msg.lower()

    if "hello" in user_msg_lower:
        bot_msg = "Hi! How can I help you?"
    elif "how are you" in user_msg_lower:
        bot_msg = "I'm glowing in neon! 😎"
    elif "bye" in user_msg_lower:
        bot_msg = "Goodbye! Have a great day 🌟"
    elif "what is my name" in user_msg_lower:
        bot_msg = "Your name is Bandi Bhargav."
    elif "what is your name" in user_msg_lower:
        bot_msg = "I'm NeonBot, your glowing assistant!"
    elif "what can you do" in user_msg_lower:
        bot_msg = "I can chat with you, tell jokes, answer simple questions, and brighten your day!"
    elif "tell me a joke" in user_msg_lower:
        bot_msg = "Why don't programmers like nature? It has too many bugs! 😂"
    elif "who made you" in user_msg_lower:
        bot_msg = "I was created by Bandi Bhargav using Python and Tkinter!"
    elif "what is python" in user_msg_lower:
        bot_msg = "Python is a powerful programming language that's great for automation, AI, and more!"
    elif "openai" in user_msg_lower:
        bot_msg = "OpenAI is an AI research lab that created ChatGPT — pretty cool, right?"
    elif "thanks" in user_msg_lower or "thank you" in user_msg_lower:
        bot_msg = "You're welcome! 😊"
    else:
        bot_msg = "I didn't understand that, try asking something else."

    chat_window.insert(tk.END, "Bot: " + bot_msg + "\n", "bot")
    chat_window.see(tk.END)

# main window
root = tk.Tk()
root.title("Neon ChatBot")
root.geometry("500x500")
root.configure(bg="black")

# styled chat window
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, bg="black", fg="#39FF14", font=("Courier", 12))
chat_window.pack(pady=10)
chat_window.tag_config("user", foreground="#00FFFF")  
chat_window.tag_config("bot", foreground="#FF10F0")    

# Entry field
entry = tk.Entry(root, width=40, font=("Courier", 12), bg="black", fg="#39FF14", insertbackground="white")
entry.pack(side=tk.LEFT, padx=10, pady=10)

# Send button
send_btn = tk.Button(root, text="Send", command=send_message, font=("Courier", 12), bg="black", fg="#00FFFF", activebackground="#FF10F0", activeforeground="white")
send_btn.pack(side=tk.LEFT, pady=10)

root.mainloop()
