# 💞 Rishta Finder Agent 💍 (Gemini 2.5 + WhatsApp)

**Rishtay Wali Auntie 🤵👰 is here to help you find the perfect match — now with WhatsApp support!**

This project is an intelligent matchmaking assistant built with:

- 🌐 **Streamlit** (for UI)
- 🧠 **Gemini 2.5 Flash** model (via `agents` SDK)
- 📩 **UltraMsg API** (to send rishta suggestions via WhatsApp)
- ⚙️ Custom tool calling (`get_user_data`, `send_whatsapp_message`)

---

## 📦 Features
- Match boys and girls based on age, gender, and preferences
- Auto-generated imaginary rishtas if no real ones are found
- Clean Streamlit UI with form-style inputs
- Optional WhatsApp delivery of rishta suggestions
- Agent-style reasoning using Gemini API and `agents` SDK

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
git clone https://github.com/RahatBano58/Rishta-Finder-Agent.git
cd Rishta-Finder-Agent

### 2. Create and Activate a Virtual Environment
uv venv
.venv\Scripts\activate

### 3.Create a .env File
**Add your credentials**:
GEMINI_API_KEY=your_gemini_api_key
INSTANCE_ID=your_ultramsg_instance_id
API_TOKEN=your_ultramsg_api_token

### 🚀 Run the App
streamlit run main.py

---

### 🧠 Agent Logic
- Name: Rishtay Wali Auntie
- Model: Gemini 2.5 Flash
- Tools Used:
       - get_user_data(min_age, gender, preferences): Fetch rishta suggestions.
       - send_whatsapp_message(number, message): Deliver match details to WhatsApp.
       - Fallback: If no real rishtas are found, the agent can generate imaginary ones.

---

### 📝 Example Prompt
"I'm a female looking for a decent boy, age 25+, caring and family-oriented. Send it to WhatsApp."

---

### 📞 WhatsApp Integration (UltraMsg)
You must have:
- A valid UltraMsg account
- Your INSTANCE_ID and API_TOKEN from the UltraMsg dashboard

---

### 🧪 Sample Rishta Profiles
**The app uses a small internal dataset like:**

- {"name": "Ayesha", "age": 20, "gender": "female", "bio": "Designer, creative soul."}
- {"name": "Ubaid", "age": 25, "gender": "male", "bio": "Banker, family-oriented."}
  *If no real matches are found, the agent intelligently generates suitable ones*.

---

### 🧕 Built With ❤️ by Rahat Bano
“Rishtay dhoondhna ab AI ka kaam hai!”

---

### 📬 Contact
**For feedback or collaboration:**
📧 rahatbano142@gmail.com
📱 WhatsApp Enabled via UltraMsg API

