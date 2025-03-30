import os

# Path to the folder (you can customize this)
folder_path = "locked_folder"

# Check if the folder exists, if not, create it
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Function to lock the folder
def lock_folder(password):
    with open(f"{folder_path}/.lock", "w") as lock_file:
        lock_file.write(password)
    print("Folder is now locked.")

# Function to unlock the folder
def unlock_folder():
    if os.path.exists(f"{folder_path}/.lock"):
        entered_password = input("Enter the password to unlock: ")
        with open(f"{folder_path}/.lock", "r") as lock_file:
            saved_password = lock_file.read()
            if entered_password == saved_password:
                os.remove(f"{folder_path}/.lock")
                print("Folder is now unlocked.")
            else:
                print("Incorrect password!")
    else:
        print("Folder is not locked.")

# Main Menu
def main():
    print("1. Lock Folder")
    print("2. Unlock Folder")
    choice = input("Choose an option (1 or 2): ")
    if choice == "1":
        password = input("Set a password for the folder: ")
        lock_folder(password)
    elif choice == "2":
        unlock_folder()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
