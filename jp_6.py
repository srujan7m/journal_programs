import sys

if len(sys.argv) == 2:
    script_name = sys.argv[0]
    text = sys.argv[1]
else:
    script_name = sys.argv[0]
    text = "Madam"

cleaned_text = ''.join(char.lower() for char in text if char.isalnum())

if cleaned_text == cleaned_text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
