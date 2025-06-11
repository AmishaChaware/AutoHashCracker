import tkinter as tk
from tkinter import messagebox
from itertools import product
import string
from django.contrib.auth.hashers import PBKDF2PasswordHasher

# 🔐 Custom Hasher
class FixedPBKDF2Hasher(PBKDF2PasswordHasher):
    algorithm = "pbkdf2_sha256"
    iterations = 260000

# 🔒 Constants
SALT = "ezqQrGJ7h8MzEsCIHdJRrO"
EXISTING_HASH =  "pbkdf2_sha256$260000$ezqQrGJ7h8MzEsCIHdJRrO$CbdreKERZ1wSBSQ/WfrtboLj3vKlV4VdSbIILvCSviU="

# 🚀 Brute-force function
def brute_force_auto(max_length=4):
    hasher = FixedPBKDF2Hasher()
    charset = string.ascii_lowercase + string.digits  # Add more if needed: + string.ascii_uppercase + string.punctuation
    attempts = 0

    for length in range(1, max_length + 1):
        for combo in product(charset, repeat=length):
            word = ''.join(combo)
            attempts += 1
            generated_hash = hasher.encode(password=word, salt=SALT)

            if generated_hash == EXISTING_HASH:
                messagebox.showinfo("Match Found ✅", f"Password found after {attempts} attempts!\n\n🔑 Password: {word}")
                return

    messagebox.showinfo("❌ No Match", f"No password matched after {attempts} attempts up to length {max_length}.")

# 🖼 GUI Setup
root = tk.Tk()
root.title("🔐 Auto Brute-Forcer")
root.geometry("500x220")
root.resizable(False, False)

tk.Label(root, text="Click the button to start automatic brute-force (max length 4):", font=("Arial", 11)).pack(pady=20)

btn = tk.Button(root, text="🚀 Start Brute Force", font=("Arial", 12), command=lambda: brute_force_auto(8))
btn.pack(pady=10)

root.mainloop()


