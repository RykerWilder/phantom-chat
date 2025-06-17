# Encrypted Chat with RSA

This is a peer-to-peer (P2P) chat application that uses 3072-bit RSA encryption to secure messages exchanged between two users. Communication occurs via TCP/IP sockets, ensuring that messages are end-to-end encrypted. Upon connection initiation, public keys are automatically exchanged. Support for simultaneous two-way communication via threading.


![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![sentinel](./phantom-chat/assets/phantom-chat.png)

---

## Requirements

- Python 3.x

---

## Installation

1. Clone the repository or download the Python file.
2. Create venv:
```bash
python3 -m venv venv
```
3. Activate venv:
```bash
source venv/bin/activate
```
4. Install dependencies:
```bash
pip install -r requirements.txt
```