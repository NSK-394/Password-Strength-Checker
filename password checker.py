import re

def check_password(password):
    score=0
    if len(password)<=8:
        score+=1
    if len(password)<=12:
        score+=2
    if re.search(r"\d",password):
        score+=2
    if re.search(r"[A-Z]",password) is None:
        score+=2
    if re.search(r"[a-z]",password) is None:
        score+=2
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None:
        score+=1

    if score>=8:
        strength = "Strong"
    elif score>=5:
        strength = "Medium"
    else:
        strength = "Weak"
    return score,strength
    
password=input("Enter the password: ")
score,strength =check_password(password)
print(f"Password Score:{score}/10")
print(f"Password Strength:{strength}")
