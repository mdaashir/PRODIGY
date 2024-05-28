import re

def check_criteria(password):
    # Check various criteria for password strength.
    criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r'[A-Z]', password)),
        "lowercase": bool(re.search(r'[a-z]', password)),
        "number": bool(re.search(r'[0-9]', password)),
        "special": bool(re.search(r'[\W_]', password))  # \W matches any non-alphanumeric character
    }
    return criteria

def calculate_score(criteria):
    # Calculate the score based on the criteria met.
    weights = {
        "length": 2,
        "uppercase": 1,
        "lowercase": 1,
        "number": 1,
        "special": 2
    }
    
    score = sum(weights[key] for key, met in criteria.items() if met)
    return score

def generate_feedback(criteria):
    # Generate feedback messages based on the criteria met.
    feedback = []
    
    if criteria["length"]:
        feedback.append("✓ Length is sufficient")
    else:
        feedback.append("✗ Length should be at least 8 characters")

    if criteria["uppercase"]:
        feedback.append("✓ Contains uppercase letter(s)")
    else:
        feedback.append("✗ Should contain at least one uppercase letter")

    if criteria["lowercase"]:
        feedback.append("✓ Contains lowercase letter(s)")
    else:
        feedback.append("✗ Should contain at least one lowercase letter")

    if criteria["number"]:
        feedback.append("✓ Contains number(s)")
    else:
        feedback.append("✗ Should contain at least one number")

    if criteria["special"]:
        feedback.append("✓ Contains special character(s)")
    else:
        feedback.append("✗ Should contain at least one special character")

    return feedback

def determine_strength(score):
    # Determine the strength level based on the score.
    if score >= 7:
        return "Very Strong"
    elif score >= 5:
        return "Strong"
    elif score >= 3:
        return "Moderate"
    else:
        return "Weak"

def assess_password_strength(password):
    # Assess the strength of a password and provide feedback.
    criteria = check_criteria(password)
    score = calculate_score(criteria)
    feedback = generate_feedback(criteria)
    strength = determine_strength(score)
    
    return strength, feedback

def log_password(password, strength):
    # Log the password and its strength to the history file.
    with open("history.txt", "a") as file:
        file.write(f"{password} | {strength}\n")

def main():
    # Main function to run the password strength checker.
    password = input("Enter your password: ")
    strength, feedback = assess_password_strength(password)

    print(f"Password Strength: {strength}")
    for comment in feedback:
        print(comment)
    
    log_password(password, strength)

# Entry point
if __name__ == "__main__":
    main()
