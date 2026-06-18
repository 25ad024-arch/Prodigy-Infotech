import re

def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"\d", password):
        score += 1

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    print("\nPassword Analysis")
    print("-" * 30)
    print("Password Length:", len(password))

    if score == 5:
        print("Strength: Very Strong")
        print("Feedback: Excellent password!")
    elif score == 4:
        print("Strength: Strong")
        print("Feedback: Good password. Consider adding more special characters.")
    elif score == 3:
        print("Strength: Medium")
        print("Feedback: Add uppercase letters, numbers, or symbols.")
    else:
        print("Strength: Weak")
        print("Feedback: Use at least 8 characters with uppercase, lowercase, numbers, and special characters.")

password = input("Enter your password: ")
check_password_strength(password)