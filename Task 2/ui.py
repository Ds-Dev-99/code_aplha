import tkinter as tk
from voice_assistant_task import main

def on_start():
    command, response = main()
    command_label.config(text=f"Command: {command}")
    response_label.config(text=f"Response: {response}")

app = tk.Tk()
app.title("Voice Assistant with Task Management")

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

button = tk.Button(frame, text="Start Listening", command=on_start)
button.pack(pady=5)

command_label = tk.Label(frame, text="Command: ")
command_label.pack(pady=5)

response_label = tk.Label(frame, text="Response: ")
response_label.pack(pady=5)

app.mainloop()
