import base64
import os

FILE = "vault.txt"

def encode_password(password):
    return base64.b64encode(password.encode()).decode()

def decode_password(encoded):
    return base64.b64decode(encoded.encode()).decode()

def add_password():
    website = input("Enter website: ").strip()
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    encoded = encode_password(password)
    with open(FILE, "a") as f:
        f.write(f"{website},{username},{encoded}\n")
    print("✅ Password added successfully!\n")

def view_passwords():
    if not os.path.exists(FILE):
        print("⚠️ No passwords saved yet!\n")
        return

    print("\n🔒 Saved Passwords:")
    with open(FILE, "r") as f:
        for line in f.readlines():
            website, username, encoded = line.strip().split(",")
            print(f"🌐 {website} | 👤 {username} | 🔑 {decode_password(encoded)}")
    print()

def search_password():
    keyword = input("Enter website to search: ").strip().lower()
    found = False
    with open(FILE, "r") as f:
        for line in f.readlines():
            website, username, encoded = line.strip().split(",")
            if keyword in website.lower():
                print(f"🌐 {website} | 👤 {username} | 🔑 {decode_password(encoded)}")
                found = True
    if not found:
        print("❌ No password found for that site.\n")

def main():
    while True:
        print("🔐 MiniVault - Simple Password Manager")
        print("1. Add Password")
        print("2. View All Passwords")
        print("3. Search Password")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            search_password()
        elif choice == "4":
            print("👋 Exiting MiniVault. Stay safe online!")
            break
        else:
            print("❌ Invalid option, try again.\n")

if __name__ == "__main__":
    main()
