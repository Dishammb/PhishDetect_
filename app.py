import streamlit as st # type: ignore
import random

# Simulated phishing detection logic
def detect_phishing(email_text):
    phishing_keywords = [
        "urgent", "click here", "verify", "login", 
        "account locked", "password", "invoice", "limited time"
    ]
    score = sum(word in email_text.lower() for word in phishing_keywords) * 20
    label = "Phishing 🚨" if score >= 40 else "Suspicious ⚠️" if score >= 20 else "Safe ✅"
    return label, score
# Set up the Streamlit page
st.set_page_config(page_title="PhishDetect AI", layout="wide")
st.title("📧 PhishDetect AI - Real-Time Email Scanner")
st.markdown("Built by *SmilingCipher*")

st.subheader("📥 Paste an Email Below to Scan")
email = st.text_area("Email Content", height=200)
col1, col2 = st.columns(2)

# Scan Button
with col1:
    if st.button("🔍 Scan Email"):
        if email.strip():
            result, confidence = detect_phishing(email)
            st.success(f"**Result:** {result}")
            st.info(f"**Confidence Score:** {confidence}%")
        else:
            st.warning("Please paste an email first.")

# Sample Email Button
with col2:
    if st.button("🎲 Load Sample Email"):
        samples = [
            "Urgent: Your account has been locked. Click here to verify.",
            "Meeting rescheduled for tomorrow at 2PM.",
            "You have won a lottery! Click to claim your prize.",
            "Reminder: Project deadline approaching next week.",
            "Verify your email and login to reset your password.",
        ]
        sample = random.choice(samples)
        st.text_area("Sample Email Loaded", sample, height=200, key="sample")
