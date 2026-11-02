import re

def redact_phone_numbers(text):
    return re.sub(r'\+84\d+|\d{10}', '[REDACTED]', text)

print(redact_phone_numbers(" 0912345678 +84912345678"))