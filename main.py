import streamlit as st
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled, function_tool
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os
import asyncio
from whatsapp import send_whatsapp_message, send_whatsapp_logic

# 🌟 Load environment variables
load_dotenv()
set_tracing_disabled(True)

API_KEY = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)

# ✅ Tool: Hidden internal rishta data
@function_tool
def get_user_data(min_age: int, gender: str, preferences: str = "") -> list[dict]:
    """
    Hidden rishta database – returns matches based on gender/age/preferences.
    If no real data matches, the agent can create imaginary rishtas.
    """
    all_users = [
        {"name": "Muneeb", "age": 22, "gender": "male", "bio": "Engineer, cricket lover."},
        {"name": "Azan", "age": 19, "gender": "male", "bio": "Student, foodie."},
        {"name": "Ubaid", "age": 25, "gender": "male", "bio": "Banker, family-oriented."},
        {"name": "Ayesha", "age": 20, "gender": "female", "bio": "Designer, creative soul."},
        {"name": "Fatima", "age": 23, "gender": "female", "bio": "Teacher, loves poetry."},
        {"name": "Zainab", "age": 26, "gender": "female", "bio": "Doctor, kind-hearted."},
    ]

    # Step 1: Try to match based on gender and age
    filtered = [u for u in all_users if u["age"] >= min_age and u["gender"] == gender]

    # Step 2: Further filter by preference if provided
    if preferences:
        filtered = [u for u in filtered if preferences.lower() in u["bio"].lower()] or filtered

    # Step 3: Return the filtered results (even if empty)
    return filtered


# ✅ AI Agent Definition
rishta_agent = Agent(
    name="Rishtay Wali Auntie",
    instructions="""
    You are Rishtay Wali Auntie 🤵👰.
    Use the get_user_data tool to find real rishta suggestions based on age, gender, and preferences.
    If no suitable real rishta is found, you may create an imaginary rishta based on user preferences.
    Respond with only 3–4 best matches.
    Keep it polite and rishta-style formal but friendly.
    If WhatsApp is requested, send the result there too.
    """,
    model=model,
    tools=[get_user_data, send_whatsapp_message],
)

# ✅ Streamlit UI
st.set_page_config(page_title="💍 Rishta Finder Agent", page_icon="💌")
st.title("💞 Rishta Finder Agent 💍💞")
st.markdown("Helping you find the perfect match — Rishtay Wali Auntie style! 😄")

# 👤 User inputs
user_gender = st.selectbox("👤 Your Gender", ["male", "female"])
min_age = st.slider("🔞 Minimum Age of Match", 18, 40, 22)
user_query = st.text_area("💬 Your Preferences / Query (e.g. doctor, caring, etc.)")
whatsapp_number = st.text_input("📱 Enter WhatsApp Number (optional)")
send_whatsapp = st.checkbox("Send rishta to WhatsApp")

# Determine opposite gender
preferred_gender = "female" if user_gender == "male" else "male"

# 🔍 Find Rishta button
if st.button("🔍 Find Rishta"):
    with st.spinner("Rishtay dhoondh rahe hain... 💞"):
        prompt = (
            f"The user is a {user_gender} looking for a {preferred_gender}."
            f" Minimum preferred age: {min_age}."
            f" Preferences: {user_query}."
        )
        if send_whatsapp and whatsapp_number:
            prompt += f" Please send suggestions to WhatsApp: {whatsapp_number}."

        chat = [{"role": "user", "content": prompt}]
        result = asyncio.run(Runner.run(starting_agent=rishta_agent, input=chat))

        st.success("🤖 Rishtay Wali Auntie says:")
        st.markdown(result.final_output)

        # 📲 WhatsApp Message
        if send_whatsapp and whatsapp_number:
            try:
                st.info("📨 Sending to WhatsApp...")
                response = send_whatsapp_logic(whatsapp_number, result.final_output)
                st.success("📱 Message sent successfully!")
                st.markdown(response)
            except Exception as e:
                st.error(f"⚠️ WhatsApp send failed: {e}")



