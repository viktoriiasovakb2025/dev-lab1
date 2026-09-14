# Main script to test security helper functions
from lib import check_password_length, generate_masked_email
def main():
    print("Security Tools Test")
    #Password length check
    user_pass = "my_secret_123"
    status = check_password_length(user_pass)
    print(f"Password status for '{user_pass}': {status}")
    #Email masking for privacy
    user_email = "student.kb.2025@lpnu.ua"
    masked = generate_masked_email(user_email)
    print(f"Original email: {user_email}")
    print(f"Masked version: {masked}")
if __name__ == "__main__":
    main()