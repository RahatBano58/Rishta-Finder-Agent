import requests
import os
from agents import function_tool

# ✅ Function logic to send WhatsApp message using UltraMsg API
def send_whatsapp_logic(number: str, message: str) -> str:
    instance_id = os.getenv("INSTANCE_ID")
    token = os.getenv("API_TOKEN")

    if not instance_id or not token:
        return "❌ Missing INSTANCE_ID or API_TOKEN in environment variables."

    url = f"https://api.ultramsg.com/{instance_id}/messages/chat"
    payload = {
        "token": token,
        "to": number,
        "body": message
    }

    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            return f"📤 Message sent successfully to {number}"
        else:
            return f"❌ Failed to send message. Error: {response.text}"
    except Exception as e:
        return f"❌ Exception occurred: {str(e)}"

# ✅ Wrap the logic with FunctionTool for agent use
send_whatsapp_message = function_tool(send_whatsapp_logic)
