# Helper functions for basic password security options
def check_password_length(password):
    # Checks if the password meets the minimum length requirement
    if len(password) >= 10:
        return "Strong length"
    return "Too short"
def generate_masked_email(email):
    # Hides part of the email for privacy 
    if "@" not in email:
        return "Invalid email"
    parts = email.split("@")
    name = parts[0]
    domain = parts[1]
    return f"{name[0]}***@{domain}"