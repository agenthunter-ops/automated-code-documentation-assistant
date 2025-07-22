import os
import aiosmtplib
from email.message import EmailMessage
from src.core.config import settings

SMTP_HOST = os.getenv("SMTP_HOST", "localhost")
SMTP_PORT = int(os.getenv("SMTP_PORT", 25))
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASS = os.getenv("SMTP_PASS", "")
FROM_ADDR = os.getenv("FROM_ADDR", "acda@localhost")
TO_ADDR = os.getenv("TO_ADDR", "developers@localhost")


async def send(subject: str, body: str) -> None:
    msg = EmailMessage()
    msg["From"] = FROM_ADDR
    msg["To"] = TO_ADDR
    msg["Subject"] = subject
    msg.set_content(body)

    await aiosmtplib.send(
        msg,
        hostname=SMTP_HOST,
        port=SMTP_PORT,
        username=SMTP_USER or None,
        password=SMTP_PASS or None,
        use_tls=False,
    )
