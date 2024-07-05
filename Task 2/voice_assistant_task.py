import speech_recognition as sr
import pyttsx3
import sqlite3

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"Recognized: {command}")
        return command
    except sr.UnknownValueError:
        return "Sorry, I did not understand that."
    except sr.RequestError:
        return "Could not request results; check your network connection."

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def create_database():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT)''')
    conn.commit()
    conn.close()

def add_task(task):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO tasks (task) VALUES (?)''', (task,))
    conn.commit()
    conn.close()
    return f"Task '{task}' added to your task list."

def list_tasks():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT task FROM tasks''')
    tasks = cursor.fetchall()
    conn.close()
    return "Your tasks are: " + ", ".join([task[0] for task in tasks])

def handle_command(command):
    if "add" in command.lower():
        task = command.replace("add", "").strip()
        return add_task(task)
    elif "list" in command.lower():
        return list_tasks()
    elif "hello" in command.lower():
        return "Hello! How can I assist you today?"
    return "I'm not sure how to respond to that."

def main():
    create_database()
    command = listen()
    response = handle_command(command)
    speak(response)
    return command, response
