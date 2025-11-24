Strong Password Generator
A Python-based script that generates strong, cryptographically secure random passwords. This tool ensures that every password meets high-complexity standards by enforcing a mix of character types.

Features
Cryptographically Secure: Uses Python’s secrets module instead of the standard random module, making passwords safe for sensitive credentials.

Enforced Complexity: Every password is guaranteed to contain at least:
One uppercase letter
One lowercase letter
One digit
One punctuation character (symbol)

Randomized Structure: The script shuffles the characters so the required types (like digits or symbols) do not appear in predictable patterns.

Customizable Length: Easily adjust the length variable to generate passwords of any size (minimum 4 characters).

Requirements
Python 3.x

How to Run
Clone or Download this repository.
Open your terminal or command prompt.
Navigate to the folder containing the script.
Run the application:
python password_generator.py

Usage Example
Open the script in a text editor.

Locate the variable password_length = 16 at the bottom of the file.
Change the number to your desired length (e.g., 24).
Save the file and run it in your terminal.
The script will print: Generated Password: r#9Mzp...

Clipboard Integration: Automatically copy the generated password to the clipboard using pyperclip.

Exclude Ambiguous Characters: Add an option to remove characters that look similar (like 1, l, I, 0, O).


Batch Generation: Allow the user to generate multiple passwords at once.
