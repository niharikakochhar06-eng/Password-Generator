import string
import secrets

def generate_strong_password(length=12):

    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    all_characters = string.ascii_letters + string.digits + string.punctuation

    password = []
    password.append(secrets.choice(string.ascii_lowercase))
    password.append(secrets.choice(string.ascii_uppercase))
    password.append(secrets.choice(string.digits))
    password.append(secrets.choice(string.punctuation))

    for _ in range(length - 4):
        password.append(secrets.choice(all_characters))

    secrets.SystemRandom().shuffle(password)

    return "".join(password)

# Example usage:
password_length = 16
new_password = generate_strong_password(password_length)
print(f"Generated Password: {new_password}")
