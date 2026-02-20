# 📧 PhishDetect AI — Real-Time Email Phishing Scanner

PhishDetect AI is a lightweight web application built using **Streamlit** that analyzes email text and detects potential phishing attempts in real time.

It scans emails for commonly used phishing keywords and classifies them as:

- ✅ **Safe**
- ⚠️ **Suspicious**
- 🚨 **Phishing**

> Developed during the **AI in Cybersecurity** track at the *National Level Conclave – NextEdge: Data Analytics & Cyber Security* organized by **Vivekanand Education Society's Institute of Technology** in collaboration with **IEEE Bombay Section**.

---

## 🚀 Features

- ⚡ Instant phishing detection
- 📊 Confidence score output
- 🎲 Random sample email generator
- 🖥️ Clean and interactive UI
- 🔰 Beginner-friendly cybersecurity project

---

## 🧠 How It Works

The app uses a **keyword-based scoring system**. Each suspicious keyword found in the email increases a risk score.

| Keyword Type     | Examples                   |
|------------------|----------------------------|
| Urgency          | urgent, limited time       |
| Account Threat   | account locked, verify     |
| Credential Theft | login, password            |
| Scam Hooks       | click here, invoice        |

**Final Classification:**

| Score | Result        |
|-------|---------------|
| 0–19  | Safe ✅        |
| 20–39 | Suspicious ⚠️ |
| 40+   | Phishing 🚨    |

---

## 🛠️ Tech Stack

| Technology | Usage            |
|------------|------------------|
| Python     | Core logic       |
| Streamlit  | Web UI framework |

---

## 📂 Project Structure

```
PhishDetect_AI/
│── app.py            # Streamlit web application
│── requirements.txt  # Python dependencies
│── README.md
```

---

## 📦 Installation

**1. Clone the repository:**

```bash
git clone https://github.com/Dishammb/PhishDetect_AI.git
cd PhishDetect_AI
```

**2. Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Then open in your browser (usually):

```
http://localhost:8501
```

---

## 💻 App Code Overview

The UI provides two actions:
- **🔍 Scan Email** — paste any email text and get an instant result
- **🎲 Load Sample Email** — auto-load a test email to try the scanner

---

## 🎲 Sample Emails Included

- 📬 Account verification alerts
- 🎰 Lottery scams
- 📅 Meeting reminders
- 🔑 Password reset requests

---

## 📚 Educational Purpose

This project is designed for:

- 🛡️ Cybersecurity beginners
- 🎓 Students learning phishing detection
- 🐍 Python & Streamlit practice

> **Note:** This is a simulation tool and not a production-grade security system.

---

## 🙌 Acknowledgements

Thanks to the mentors, speakers, and organizers of the NextEdge Conclave for guidance and inspiration.

---

## 👨‍💻 Author

**[@dishammb](https://github.com/Dishammb)** 

---

## 📄 License

This project is open-source and free to use for educational purposes.