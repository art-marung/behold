from fastapi import FastAPI
from datetime import date
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)

MESSAGES = [
    "Motion continues without confusion.",
    "What exists does not require attention.",
    "Order remains even when unseen.",
    "Silence holds its own structure.",
    "Balance does not announce itself."
]

def log_event(event_name: str) -> None:
    logging.info(f"EVENT: {event_name}")

@app.on_event("startup")
def app_start() -> None:
    log_event("app_start")

@app.get("/")
def daily_message() -> str:
    log_event("request_received")

    try:
        today = date.today().toordinal()
        index = today % len(MESSAGES)
        log_event("generation_success")
        return MESSAGES[index]

    except Exception:
        log_event("generation_failure")
        return "Continuity remains."

