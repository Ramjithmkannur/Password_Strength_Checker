# Password Strength Checker
# This script evaluates the strength of a given password based on various security criteria.
# It is made by Ramjith M (https://github.com/Ramjithmkannur)

import re

def check_password_strength(password):
    # Initialize the score
    score = 0
    tips = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        tips.append("Password should be at least 8 characters long.")

    # Uppercase, lowercase, number, and special character checks
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        tips.append("Add at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        tips.append("Add at least one lowercase letter.")

    if re.search(r'\d', password):
        score += 1
    else:
        tips.append("Add at least one number.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        tips.append("Add at least one special character (!@#$%^&* etc.).")

    # Common passwords check
    common_passwords = ["password", "123456", "123456789", "qwerty", "abc123"]
    if password.lower() in common_passwords:
        tips.append("Avoid using common passwords like 'password' or '123456'.")
        score = max(0, score - 1)

    # Evaluate strength
    if score >= 4:
        strength = "Strong"
    elif 2 <= score < 4:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, tips


if __name__ == "__main__":
    while True:
        # Get user input
        user_password = input("Enter your password (or press 0 to Exit): ")
        if user_password == "0":
            print("Exiting the program. Stay secure!")
            break
        
        strength, improvement_tips = check_password_strength(user_password)

        # Output the result
        print(f"Password Strength: {strength}")
        if strength == "Strong":
            print("Your password is strong. Good job!")
            break
        else:
            print("Tips to improve your password:")
            for tip in improvement_tips:
                print(f"- {tip}")
            print("Please try again.")
