import re

def check_password(password):
    score = 0
    
    
    if len(password) < 8:
        score += 0
    elif 8 <= len(password) <= 10:
        score += 2
    elif 11 <= len(password) <= 14:
        score += 3
    else: 
        score += 4

    
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*]", password):
        score += 2  

   
    if score >= 8:
        strength = "Strong 💪"
    elif score >= 5:
        strength = "Medium 🙂"
    else:
        strength = "Weak ⚠️"
    
    return score, strength
    


password = input("Enter the password: ")
score, strength = check_password(password)
print(f"Password Score: {score}/10")
print(f"Password Strength: {strength}")
