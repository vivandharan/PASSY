import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_password(key, password):
    f = Fernet(key)
    return f.encrypt(password.encode()).decode()

def decrypt_password(key, encrypted_password):
    f = Fernet(key)
    return f.decrypt(encrypted_password.encode()).decode()

def add_password():
    service = service_entry.text()
    username = username_entry.text()
    password = password_entry.text()

    if service and username and password:
        encrypted_password = encrypt_password(key, password)
        passwords[service] = {'username': username, 'password': encrypted_password}
        QMessageBox.information(window, "Success", "Password added successfully!")
    else:
        QMessageBox.warning(window, "Error", "Please fill in all the fields.")

def get_password():
    service = service_entry.text()
    if service in passwords:
        encrypted_password = passwords[service]['password']
        decrypted_password = decrypt_password(key, encrypted_password)
        QMessageBox.information(window, "Password", f"Username: {passwords[service]['username']}\nPassword: {decrypted_password}")
    else:
        QMessageBox.warning(window, "Error", "Password not found.")

key = generate_key()
passwords = {}

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Password Manager")
window.setGeometry(100, 100, 400, 300)

layout = QVBoxLayout()

instructions = "To add password, fill all the fields and press 'Add Password'.\nTo view password, enter Account Name and press 'Get Password'."
signature = "Developed by Vivan Dharan & Dhishaa"

instruction_label = QLabel(instructions)
layout.addWidget(instruction_label)

service_entry = QLineEdit()
layout.addWidget(service_entry)

username_entry = QLineEdit()
layout.addWidget(username_entry)

password_entry = QLineEdit()
password_entry.setEchoMode(QLineEdit.Password)
layout.addWidget(password_entry)

add_button = QPushButton("Add Password")
add_button.clicked.connect(add_password)
layout.addWidget(add_button)

get_button = QPushButton("Get Password")
get_button.clicked.connect(get_password)
layout.addWidget(get_button)

signature_label = QLabel(signature)
layout.addWidget(signature_label)

widget = QWidget()
widget.setLayout(layout)
window.setCentralWidget(widget)

window.show()
sys.exit(app.exec_())
