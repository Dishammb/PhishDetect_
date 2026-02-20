# 🛡️ PhishDetect AI — Real-Time Phishing Email Scanner

An interactive web app that detects phishing emails using a rule-based AI approach.
Built during the **National Level Conclave – NextEdge: Data Analytics & Cyber Security** organized by **Vivekanand Education Society's Institute of Technology** in collaboration with **IEEE Bombay Section**.

---

## 🚀 What This Project Does

PhishDetect AI analyzes email text and classifies it into:

- 🔴 **Phishing**
- ⚠️ **Suspicious**
- ✅ **Safe**

The system simulates a basic AI security filter by checking for commonly used phishing patterns such as urgency, credential requests, and malicious prompts.

> This project focuses on learning how cybersecurity detection systems work internally — not building a production anti-spam filter.

---

## 🖥️ Demo Features

- Paste any email content and scan instantly
- Auto-generated sample phishing emails
- Confidence score based on detected patterns
- Simple browser interface (Streamlit)

---

## 🧠 Detection Logic

The AI uses handcrafted rules based on common phishing behavior:

| Trigger Type        | Example                          |
|---------------------|----------------------------------|
| Urgency             | "urgent", "limited time"         |
| Credential Theft    | "login", "verify password"       |
| Threat Messages     | "account locked"                 |
| Social Engineering  | "click here", "invoice"          |

Each detected keyword increases a risk score.

```
Score ≥ 40 → Phishing 🚨
Score ≥ 20 → Suspicious ⚠️
Score < 20 → Safe ✅
```

---

## 📂 Project Structure

```
PhishDetect_AI/
│── app.py            # Streamlit web application
│── requirements.txt  # Python dependencies
│── README.md
```

---

## ⚙️ Installation

**1️⃣ Clone the repository**

```bash
git clone https://github.com/Dishammb/PhishDetect_AI.git
cd PhishDetect_AI
```

**2️⃣ Install dependencies**

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Web App

```bash
streamlit run app.py
```

Then open the local URL shown in your terminal (usually):

```
http://localhost:8501
```

---

## 🧪 Example

**Input:**
```
Urgent: Your account has been locked. Click here to verify your password.
```

**Output:**
```
Result: Phishing 🚨
Confidence Score: 60%
```

---

## 🎯 Learning Outcomes

- Rule-based AI decision systems
- Cybersecurity threat indicators
- Social engineering patterns
- Building security tools using Streamlit

---

## 🔮 Future Improvements

- Machine Learning classifier (Naive Bayes / NLP)
- URL feature extraction
- Email header analysis
- Attachment scanning
- Real-time Gmail/Outlook integration

---

## 🙌 Acknowledgements

Developed during the **AI in Cybersecurity** track at the conclave. Thanks to mentors, speakers, and organizers for guidance and inspiration.

---

## ⭐ About

This is a beginner cybersecurity project meant for **educational demonstration purposes**.
