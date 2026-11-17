# AI Voice Calling Agent

A personal assistant that makes real phone calls for me. I tell it who to call and what to say. The AI agent dials the number, delivers the message and holds a natural conversation with the person on the line.

Built with **Vapi** (voice AI and phone numbers), **Claude Sonnet** as the conversation model, and a **Python** script that starts each call through the Vapi API.

## How it works

1. I run `make_call.py` and answer three prompts: who to call, their number, and the message.
2. The script sends a request to the Vapi API with my assistant, my Vapi phone number and the message.
3. Vapi places the call. The assistant (Claude Sonnet, configured in Vapi) speaks the message, listens and responds in real time.
4. After the call, the transcript and outcome are available in Vapi for me to review.

```
You ──► make_call.py ──► Vapi API ──► phone call ──► the person you're calling
                              │
                              └── Claude Sonnet runs the conversation
```

The message is passed in as a variable (`{{message}}`), so one assistant can deliver any message without editing its prompt.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a file named `.env` in this folder (see `.env.example`) with your own Vapi values:

```
VAPI_API_KEY=your-vapi-api-key
VAPI_PHONE_NUMBER_ID=your-vapi-phone-number-id
ASSISTANT_ID=your-vapi-assistant-id
```

`.env` is listed in `.gitignore`, so keys never leave your machine.

Then run:

```bash
python make_call.py
```

## Status

- Inbound and browser test calls work end to end.
- Outbound calls authenticate through the API; Vapi-provided numbers have a daily outbound-call limit, which I hit during testing.

## Roadmap

- Book restaurant and event reservations for me and friends
- Send email and SMS invites after a booking
- WhatsApp calling for international numbers
- Take notes during the call and send me a written summary

## Tech

Python · Vapi · Claude Sonnet · REST API · python-dotenv
