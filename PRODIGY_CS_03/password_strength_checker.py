import re

def assess_password_strength(password):
    # Criteria weights
    length_weight = 2
    uppercase_weight = 1
    lowercase_weight = 1
    number_weight = 1
    special_weight = 2

    # Criteria checks
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_criteria = bool(re.search(r'[\W_]', password))  # \W matches any non-alphanumeric character

    # Calculate score
    score = 0
    score += length_weight if length_criteria else 0
    score += uppercase_weight if uppercase_criteria else 0
    score += lowercase_weight if lowercase_criteria else 0
    score += number_weight if number_criteria else 0
    score += special_weight if special_criteria else 0

    # Feedback messages
    feedback = []
    if length_criteria:
        feedback.append("✓ Length is sufficient")
    else:
        feedback.append("✗ Length should be at least 8 characters")

    if uppercase_criteria:
        feedback.append("✓ Contains uppercase letter(s)")
    else:
        feedback.append("✗ Should contain at least one uppercase letter")

    if lowercase_criteria:
        feedback.append("✓ Contains lowercase letter(s)")
    else:
        feedback.append("✗ Should contain at least one lowercase letter")

    if number_criteria:
        feedback.append("✓ Contains number(s)")
    else:
        feedback.append("✗ Should contain at least one number")

    if special_criteria:
        feedback.append("✓ Contains special character(s)")
    else:
        feedback.append("✗ Should contain at least one special character")

    # Determine strength level
    if score >= 7:
        strength = "Very Strong"
    elif score >= 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

# Example usage
password = input("Enter your password: ")
strength, feedback = assess_password_strength(password)

print(f"Password Strength: {strength}")
for comment in feedback:
    print(comment)
