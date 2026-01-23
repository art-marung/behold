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
# Messages are intentionally calm, universal, and non-directive.
MESSAGES = [
    "Light moves across distance without haste, arriving without needing to be noticed.",
    "What holds the stars also steadies the smallest motion, quietly and without claim.",
    "There is an order that continues even when no one pauses to observe it.",
    "Silence is not empty; it carries its own structure and keeps it faithfully.",
    "Balance does not announce itself, yet nothing escapes its reach.",
    "Motion persists without confusion, guided by paths that do not need explanation.",
    "Even what drifts remains within boundaries it does not have to name.",
    "Distance does not weaken what is already held in place.",
    "The unseen supports the seen without effort or demand.",
    "Time advances without argument, allowing each moment to rest where it is.",
    "Nothing here requires attention in order to continue being.",
    "What is vast does not overwhelm what is small; both remain within the same order.",
    "Stillness has shape, even when nothing appears to move.",
    "Continuity does not depend on belief; it remains whether noticed or not."
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
