import json
import re
import sys

REQUIRED_FIELDS = ["firstName", "lastName", "email", "phone"]
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

def validate(payload: dict) -> list:
    errors = []

    for field in REQUIRED_FIELDS:
        if field not in payload or not str(payload[field]).strip():
            errors.append(f"Missing or empty required field: {field}")

    email = str(payload.get("email", "")).strip()
    if email and not EMAIL_RE.match(email):
        errors.append("Invalid email format")

    return errors

def main():
    if len(sys.argv) != 2:
        print("Usage: python scripts/validate_payload.py <path-to-json>")
        sys.exit(2)

    path = sys.argv[1]
    with open(path, "r", encoding="utf-8") as f:
        payload = json.load(f)

    errors = validate(payload)

    if errors:
        print("❌ Payload invalid:")
        for e in errors:
            print(f"- {e}")
        sys.exit(1)

    print("✅ Payload valid")
    sys.exit(0)

if __name__ == "__main__":
    main()
