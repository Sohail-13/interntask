import re
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)
name = input("Enter your name: ").strip()
email = input("Enter your email: ").strip()
if not name:
    print("Error: Name cannot be empty.")
elif not email:
    print("Error: Email cannot be empty.")
elif not is_valid_email(email):
    print("Error: Invalid email format.")
else:
    print(f"Received data: Name - {name}, Email - {email}")

