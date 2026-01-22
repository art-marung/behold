"""
Behold is a stateless presence system.

It delivers one contemplative message per day.
It does not persist memory.
It does not adapt to audience behavior.
Failures are handled calmly without intervention.

This system is intentionally simple.
"""

from fastapi import FastAPI
from datetime import date
import logging

app = FastAPI()

# Logging is used only for operational continuity,
# not for analytics, profiling, or audience measurement.
logging.basicConfig(level=logging.INFO)

# A finite set of contemplative messages.
# Messages are intentionally simple and timeless.
MESSAGES = [
    "Motion continues without confusion.",
    "What exists does not require attention.",
    "Order remains even when unseen.",
    "Silence holds its own structure.",
    "Balance does not announce itself."
]

def log_event(event_name: str) -> None:
    """
    Log operational events only.
    These logs exist to confirm continuity of execution,
    not to interpret or optimize behavior.
    """
    logging.info(f"EVENT: {event_name}")

@app.on_event("startup")
def app_start() -> None:
    """
    Application startup hook.
    Used solely to confirm successful initialization.
    """
    log_event("app_start")

@app.get("/")
def daily_message() -> str:
    """
    Return the daily contemplative message.

    Deterministic daily message selection:
    - The same message is returned to all visitors on a given day.
    - The message changes only with the calendar date.
    - No state, memory, or user context is involved.
    """
    log_event("request_received")

    try:
        # Deterministic daily message selection
        today = date.today().toordinal()
        index = today % len(MESSAGES)

        log_event("generation_success")
        return MESSAGES[index]

    except Exception:
        # Quiet failure: return a calm fallback message
        # without exposing errors or requiring intervention.
        log_event("generation_failure")
        return "Continuity remains."
