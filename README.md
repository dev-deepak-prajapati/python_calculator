# 🧮 Python Calculator Project

A simple and interactive Command Line Interface (CLI) Calculator built using Python. This project includes both a basic calculator script and an advanced calculator script with a continuous loop menu and modular functions.

---

## ✨ Features

- **Basic Calculator (`calculator.py`)**:
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`*`)
  - Division (`/`)
  - Exponentiation / Power (`**`)
  - Error handling for invalid inputs and division by zero.

- **Advanced Calculator (`advance_calculator.py`)**:
  - Modular function architecture (`add`, `subtract`, `multiply`, `divide`, `modulus`, `power`).
  - Interactive loop (`while True`) allowing multiple calculations without restarting.
  - Options for Modulus (`%`) and Power (`**`).
  - Clean exit option (`Exit`).
  - Comprehensive exception handling (`ValueError`, `ZeroDivisionError`).

---

## 📁 Project Structure

```text
python_calculator/
│
├── calculator.py          # Basic CLI Calculator script
├── advance_calculator.py  # Advanced CLI Calculator script with menu loop & functions
└── README.md              # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have **Python 3.10+** installed on your system.

Check Python version:
```bash
python --version
```

---

## ▶️ How to Run

1. **Clone or Download the Repository:**
   ```bash
   git clone https://github.com/dev-deepak-prajapati/python_calculator.git
   cd python_calculator
   ```

2. **Run Basic Calculator:**
   ```bash
   python calculator.py
   ```

3. **Run Advanced Calculator:**
   ```bash
   python advance_calculator.py
   ```

---

## 🛡️ Error Handling

Both scripts handle common runtime errors gracefully:
- **ZeroDivisionError**: Prevents crash when dividing numbers by `0`.
- **ValueError**: Ensures users enter valid numerical inputs.
- **Invalid Choice**: Prompts the user if an out-of-range menu option is chosen.

---

## 👨‍💻 Author

Created with ❤️ by **Deepak Prajapati**.
