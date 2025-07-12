# 💬 RoleBot — Your Personal Chat Persona Companion

Welcome to **RoleBot**, a customizable, ChatGPT-style chatbot built with [Streamlit](https://streamlit.io/) and [OpenAI](https://openai.com/) APIs.  
Switch personas, chat with style, and experience a bot that responds how you want.

---

## 🚀 Features

- 🎭 **Persona Selector** — Choose how your bot behaves (friendly, sarcastic, emotional, etc.)
- 📜 **Chat History** — Ongoing conversation thread that scrolls with ease
- 🎨 **Right-Aligned User Input** — Elegant chat layout just like ChatGPT
- 🧹 **Clear Chat** Button — Start fresh any time
- 💞 **Responsive UI** — Sleek CSS styling with alignment magic
- 🌐 **Powered by GPT** — Smart replies based on the selected persona

---

## 🛠️ Setup Instructions

```bash
git clone https://github.com/saket0x07/rolebot.git
cd rolebot
pip install -r requirements.txt

---
Create a .env file in the root directory:

GITHUB_TOKEN=your_api_key_or_token_here

---
Then run the app:

streamlit run app.py
---

🎭 Persona System
Define personas inside config/personas.json like this:

json
{
  "Sweetheart Machine": {
    "prompt": "You are a loving, warm-hearted assistant who speaks like a caring friend.",
    "description": "Soft-spoken, kind, and always uplifting."
  },
  "Sarcastic Genius": {
    "prompt": "You're witty and brilliant, but never hold back your sass.",
    "description": "Sharp humor and intelligence combined."
  }
}
Feel free to add more — your bot will adapt in real time ✨

🤝 Credits
Built with ❤️ by saket0x07 Crafted using OpenAI + Streamlit + Python magic 🧙
