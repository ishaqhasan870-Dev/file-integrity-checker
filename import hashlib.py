import os
import json
import time
import hashlib
from datetime import datetime

# ======================================================
# FIXED ADVANCED FILE INTEGRITY CHECKER
# ======================================================

DB_FILE = "integrity_db.json"
LOG_FILE = "integrity_log.txt"


# ======================================================
# UTILITIES
# ======================================================

def log_event(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}"
    print(entry)

    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(entry + "\n")


def sha256_hash(filepath):
    try:
        hash_obj = hashlib.sha256()

        with open(filepath, "rb") as file:
            while True:
                chunk = file.read(8192)
                if not chunk:
                    break
                hash_obj.update(chunk)

        return hash_obj.hexdigest()

    except Exception:
        return None


def load_database():
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r") as file:
                return json.load(file)
        except:
            return {}
    return {}


def save_database(data):
    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=4)


# ======================================================
# FILE SCANNER
# ======================================================

def get_all_files(path):
    files = []

    if os.path.isfile(path):
        files.append(os.path.abspath(path))

    elif os.path.isdir(path):
        for root, dirs, filenames in os.walk(path):
            for name in filenames:
                files.append(os.path.abspath(os.path.join(root, name)))

    return files


# ======================================================
# CREATE BASELINE
# ======================================================

def create_baseline():
    path = input("Enter file/folder path: ").strip()

    if not os.path.exists(path):
        log_event("Invalid path.")
        return

    db = load_database()
    files = get_all_files(path)

    for file in files:
        file_hash = sha256_hash(file)

        if file_hash:
            db[file] = file_hash
            log_event(f"Tracking: {file}")

    save_database(db)
    log_event("Baseline created successfully.")


# ======================================================
# CHECK INTEGRITY
# ======================================================

def check_integrity():
    db = load_database()

    if not db:
        log_event("No tracked files found.")
        return

    log_event("Checking file integrity...")

    for file, old_hash in db.items():

        if not os.path.exists(file):
            log_event(f"[DELETED] {file}")
            continue

        new_hash = sha256_hash(file)

        if new_hash == old_hash:
            log_event(f"[SAFE] {file}")
        else:
            log_event(f"[MODIFIED] {file}")

    log_event("Integrity check complete.")


# ======================================================
# LIVE MONITOR
# ======================================================

def monitor():
    sec = input("Check every how many seconds? ").strip()

    if not sec.isdigit():
        sec = 10
    else:
        sec = int(sec)

    log_event("Live monitoring started. Press Ctrl+C to stop.")

    try:
        while True:
            check_integrity()
            time.sleep(sec)

    except KeyboardInterrupt:
        log_event("Monitoring stopped.")


# ======================================================
# REMOVE FILE
# ======================================================

def remove_file():
    path = input("Enter exact tracked file path: ").strip()
    path = os.path.abspath(path)

    db = load_database()

    if path in db:
        del db[path]
        save_database(db)
        log_event("Removed successfully.")
    else:
        log_event("File not found in database.")


# ======================================================
# MAIN MENU
# ======================================================

def menu():
    while True:
        print("\n========== FILE INTEGRITY CHECKER ==========")
        print("1. Create Baseline (Track File/Folder)")
        print("2. Check Integrity")
        print("3. Live Monitor")
        print("4. Remove File")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            create_baseline()

        elif choice == "2":
            check_integrity()

        elif choice == "3":
            monitor()

        elif choice == "4":
            remove_file()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid option. Please enter 1 to 5.")


# ======================================================
# START PROGRAM
# ======================================================

if __name__ == "__main__":
    menu()