import re

# ── Raw Data ──────────────────────────────────────────────────────────────────
data = [
    "User: Mahipal | Phone: 9876543210 | Email: mahi@gmail.com | Amount: Rs.5000",
    "User: Ravi | Phone: 98765abc10 | Email: ravi#gmail.com | Amount: USD300",
    "User: NULL | Phone: 9123456789 | Email: test@yahoo.com | Amount: Rs.7000",
    "User: Ankit | Phone: 9999999999 | Email: ankit@gmail.com | Amount: Rs.0",
    "User: Sita | Phone: 8888888888 | Email: sita@gmail.com | Amount: Rs.-100",
]

error_log = []
clean_dataset = []

for i, record in enumerate(data):
    try:
        # ── STEP 3: REGEX EXTRACTION ──────────────────────────────────────
        # Extract raw fields using regex
        name_match    = re.search(r"User:\s*(\S+)",record)
        phone_match   = re.search(r"Phone:\s*(\S+)",record)
        email_match   = re.search(r"Email:\s*(\S+)",record)
        amount_match  = re.search(r"Amount:\s*(\S+)",record)

        raw_name   = name_match.group(1)   if name_match   else None
        raw_phone  = phone_match.group(1)  if phone_match  else None
        raw_email  = email_match.group(1)  if email_match  else None
        raw_amount = amount_match.group(1) if amount_match else None

        # ── STEP 2: ASSERT – user name not NULL ───────────────────────────
        assert raw_name and raw_name.upper() != "NULL", \
            f"Record {i}: User name is NULL or missing"

        # ── STEP 3 (cont.): validate phone – exactly 10 digits ───────────
        assert raw_phone and re.fullmatch(r"\d{10}", raw_phone), \
            f"Record {i}: Invalid phone '{raw_phone}' (must be 10 digits)"

        # ── STEP 3 (cont.): validate email – standard format ─────────────
        assert raw_email and re.fullmatch(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", raw_email), \
            f"Record {i}: Invalid email '{raw_email}'"

        # ── STEP 4: ADVANCED REGEX – extract currency & numeric amount ────
        currency_match = re.search(r"(Rs|USD)", raw_amount, re.IGNORECASE)
        number_match   = re.search(r"-?\d+",    raw_amount)

        currency = currency_match.group(1) if currency_match else "unknown"
        amount   = int(number_match.group()) if number_match else 0

        # ── STEP 2 (cont.): ASSERT – amount must be > 0 ──────────────────
        assert amount > 0, \
            f"Record {i}: Amount must be > 0, got {amount}"

        # ── STEP 5: STRING CLEANING ───────────────────────────────────────
        clean_name     = re.sub(r"[^a-z0-9]", "", raw_name.lower())
        clean_email    = raw_email.lower()
        clean_currency = re.sub(r"[^a-z]", "", currency.lower())

        # ── STEP 6: BUILD CLEAN RECORD ────────────────────────────────────
        clean_dataset.append({
            "name":     clean_name,
            "phone":    raw_phone,
            "email":    clean_email,
            "amount":   amount,
            "currency": clean_currency,
        })

    except AssertionError as e:
        error_log.append(f"{e}")
    except Exception as e:
        error_log.append(f"{e}")


# ── Print Results ─────────────────────────────────────────────────────────────
print("  ERROR LOG (skipped records)")
if error_log:
    for err in error_log:
        print(f"{err}")
else:
    print("  (none)")

print()
print("  CLEAN DATASET")
for rec in clean_dataset:
    print(f"{rec}")

