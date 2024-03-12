import secrets
import string
import pyperclip

password_length_default = 18

# set all allowed items to use: abcABC, 0-9, specials as strings
components = [string.ascii_letters, string.digits, "!§$=?*+#-_<>"]

# separate all items in a list of chars
chars = []
for clist in components:
    for c in clist:
        chars.append(c)

# get randomly 18 times items out of the char list,
# put them into a password item list and return them combined as a string
def generate_password():
    password_items = []
    for i in range(password_length_default):
        rnd_char = secrets.choice(chars)
        password_items.append(rnd_char)

    password = "".join(password_items)

    # Copy PW to Clipboard
    pyperclip.copy(password)
    return password

print(generate_password())
