# File Integrity Checker  
COMPANY NAME : CODTECH IT SOLUTIONS 
NAME : SYED MOHAMMED ISHAQ HASAN  
INTERN ID : CTIS7048 
DOMAIN : Cyber Security and Ethical Hacking
DURATION: 4 WEEKS MENTOR: NEELA SANTOSH


# 🔐 File Integrity Checker

A powerful Python-based **File Integrity Checker** that monitors files and folders for unauthorized changes using **SHA-256 hashing**.
This project helps detect **modified, deleted, or tampered files** by comparing current file hashes with a trusted baseline.

---

## 📌 Features

✅ Track single files or entire folders
✅ Generate secure SHA-256 baseline hashes
✅ Detect modified files instantly
✅ Detect deleted files
✅ Real-time monitoring mode
✅ Log events with timestamps
✅ JSON database storage
✅ Simple terminal interface
✅ Lightweight & fast

---

## 🛠️ Technologies Used

* Python 3.x
* hashlib
* os
* json
* time
* datetime

---

## 📂 Project Structure

```bash
File-Integrity-Checker/
│── main.py
│── integrity_db.json
│── integrity_log.txt
│── README.md
```

---

## 🚀 Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/file-integrity-checker.git
cd file-integrity-checker
```

### 2️⃣ Run Program

```bash
python main.py
```

---

## 💻 Usage

When you run the program:

```text
========== FILE INTEGRITY CHECKER ==========
1. Create Baseline (Track File/Folder)
2. Check Integrity
3. Live Monitor
4. Remove File from Tracking
5. Exit
```

### 🔹 Option 1 - Create Baseline

Stores original SHA-256 hash of selected file/folder.

### 🔹 Option 2 - Check Integrity

Compares current file hash with saved baseline.

Output:

```text
[SAFE] File unchanged
[MODIFIED] File altered
[DELETED] File missing
```

### 🔹 Option 3 - Live Monitor

Automatically checks files every few seconds.

### 🔹 Option 4 - Remove File

Stops tracking selected file.

---

## 🔒 How It Works

The program calculates a unique fingerprint using **SHA-256**:

```text
Original File → SHA256 Hash Saved
Later File → New Hash Generated
Compare Both Hashes
```

If hashes differ, the file has been changed.

---

## 📸 Example Output

```text
[2026-04-23 21:40:00] [SAFE] report.pdf
[2026-04-23 21:40:10] [MODIFIED] report.pdf
[2026-04-23 21:40:20] [DELETED] report.pdf
```

---

## 🎯 Use Cases

* Detect unauthorized file changes
* Monitor sensitive documents
* Malware tampering detection
* Backup verification
* Cybersecurity projects
* System integrity monitoring

---

## 📈 Future Improvements

🔹 GUI Version
🔹 Email Alerts
🔹 Folder Auto Scan
🔹 Cloud Backup Logs
🔹 Multi-threaded Monitoring
🔹 Export Reports

---

## 🤝 Contributing

Pull requests are welcome.
For major changes, please open an issue first.

---

## 📜 License

This project is open-source under the MIT License.

---

## 👨‍💻 Author
# out put file

**SYED MOHAMMED ISHAQ HASAN**
📧 [ishaqhasan870@gmail.com](mailto:ishaqhasan870@gmail.com)
🔗 LinkedIn: https://www.linkedin.com/in/syed-mohammed-ishaq-hasan-47a87b254/

---

## ⭐ Support

If you like this project, give it a **star ⭐** on GitHub!
