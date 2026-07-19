# COCO - Personal Voice Assistant

COCO is a Python-based personal voice assistant that helps users perform everyday tasks using simple voice commands. It utilizes speech recognition and text-to-speech technologies to provide a hands-free and interactive desktop experience.

---

## Features

- **Play Music:** Play your favorite songs directly on YouTube using voice commands.
- **Google Search:** Search Google instantly without opening a browser manually.
- **Wikipedia Search:** Get concise information about people, places, and topics from Wikipedia.
- **Time Assistant:** Ask for the current time and receive a spoken response.
- **Joke Generator:** Listen to random jokes for entertainment.
- **Open Applications:** Launch Google Chrome and Visual Studio Code using voice commands.
- **Speech Recognition:** Understand and process user voice commands.
- **Text-to-Speech:** Respond naturally using an offline speech engine.

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| SpeechRecognition | Voice Recognition |
| pyttsx3 | Text-to-Speech Engine |
| PyWhatKit | YouTube Playback & Google Search |
| Wikipedia | Information Retrieval |
| PyJokes | Joke Generation |
| Google Speech API | Speech Recognition |

---

## 📂 Project Structure

```
COCO-Voice-Assistant/
│
├── assistant.py
├── requirements.txt
├── README.md
├── .gitignore
└── venv/
```

---

# Getting Started

**Prerequisites**

Make sure you have **Python 3.11 or later** installed on your machine.

**Installation**

 Clone the repository:
 ```bash
 git clone https://github.com/YOUR_USERNAME/COCO-Voice-Assistant.git
 cd COCO-Voice-Assistant
 ```

 Create a virtual environment:
 ```bash
 python -m venv venv
 ```

 Activate the virtual environment

**Windows**

 ```bash
 venv\Scripts\activate
 ```

 Install the required dependencies:

 ```bash
 pip install -r requirements.txt
 ```

 Run the assistant:

 ```bash
 python assistant.py
 ```

---

## Example Voice Commands

| Voice Command | Action |
|---------------|--------|
| **Play Believer** | Plays the requested song on YouTube |
| **What's the time?** | Tells the current time |
| **Who is Elon Musk?** | Searches Wikipedia |
| **Search Google for Python** | Opens Google search |
| **Tell me a joke** | Speaks a random joke |
| **Open Chrome** | Launches Google Chrome |
| **Open VS Code** | Opens Visual Studio Code |
| **Exit** | Closes the assistant |

---

## Future Enhancements

- Wake Word Detection ("Hey COCO")
- AI Chat Integration (Gemini / ChatGPT)
- Weather Information
- Volume & Brightness Control
- File Management
- Email Automation
- Calendar & Reminder Support
- Desktop GUI
- Offline Speech Recognition
- Smart Home Integration

---

## 🎤 Demo Commands

```text
🎙️ User: Play Believer
🤖 COCO: Playing Believer on YouTube.

🎙️ User: What's the time?
🤖 COCO: It's 10:35 AM.

🎙️ User: Who is Elon Musk?
🤖 COCO: Elon Musk is a business magnate and entrepreneur...

🎙️ User: Open Chrome
🤖 COCO: Opening Chrome.

🎙️ User: Tell me a joke
🤖 COCO: Why don't programmers like nature? It has too many bugs!
```

## Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

## License

This project is licensed under the MIT License.
