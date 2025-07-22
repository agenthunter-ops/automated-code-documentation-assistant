import re

def clean_commit_message(msg: str) -> str:
    msg = msg.strip()
    msg = re.sub(r"#\\d+", "", msg)  # remove issue numbers
    return msg.lower()
