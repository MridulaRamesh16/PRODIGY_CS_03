import re

def check_password_strength(password):
    # Criteria to check for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_character_criteria = re.match(r'[!@#$%^&*(),.?":{}|<>]', password)
    
    # Calculate the overall strength score
    strength_score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria])
    
    # Provide feedback based on the strength score and criteria
    if strength_score == 4:
        return "Strong password!"
    elif strength_score >= 3:
        return "Moderate password, add any special characters to create a strong password."
    elif strength_score >= 2:
        return "Weak password,please add any uppercase letters, numbers, or special characters."
    else:
        return "Very weak password, consider adding more characters, uppercase letters, numbers, or special characters."

# Example usage:
password = input("Enter your password: ")
strength_feedback = check_password_strength(password)
print(strength_feedback)
