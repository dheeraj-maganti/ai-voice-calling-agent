import os, requests
from dotenv import load_dotenv
load_dotenv()

name = input("Who should I call? ")
number = input("Their number (like +15551234567): ")
message = input("What should I tell them? ")

r = requests.post(
    "https://api.vapi.ai/call",
    headers={"Authorization": f"Bearer {os.getenv('VAPI_API_KEY')}"},
    json={
        "assistantId": os.getenv("ASSISTANT_ID"),
        "phoneNumberId": os.getenv("VAPI_PHONE_NUMBER_ID"),
        "customer": {"number": number, "name": name},
        "assistantOverrides": {"variableValues": {"message": message}},
    },
)
print(r.status_code, r.json())
