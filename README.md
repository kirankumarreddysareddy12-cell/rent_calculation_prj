
---

# 🏠 Shared Rent Calculator

A simple Python program to split rent, food, and electricity bills fairly among roommates.
It supports "even splits" as well as "cent-accurate fair splits" where every paisa/cent is distributed.

---

## 🚀 Features

* Input "rent, food cost, electricity units & charge per unit"
* Calculates "total bill"
* Splits bill among roommates
* Two split methods:

  * "Even split" (float division)
  * "Fair split" (distributes leftover cents fairly)
* Handles invalid inputs with proper validation

---

## 🛠️ Technologies Used

* "Python 3" (no external libraries required)

---

## ▶️ How to Run

### Linux / macOS (bash/zsh terminal)

```bash
python rent_calculator.py
```

### Windows (Command Prompt / PowerShell)

```cmd
python rent_calculator.py
```

---

## 📖 Example Usage

```
=== Shared Bill Splitter ===
(Enter numeric values; decimals allowed)

1) Enter your hostel/flat rent: 5000
2) Enter the total amount of food/snacks ordered: 1200
3) Enter the total electricity units spent: 80
4) Enter the charge per electricity unit: 10
5) Enter the number of persons living in room/flat: 3

--- Bill breakdown ---
Rent:                 5000.00
Food / Snacks:        1200.00
Electricity: (80 units × 10.00)  = 800.00
Total bill:           7000.00

--- Split options ---
Even split (float): Each person will pay = 2333.33

Fair split (distributes leftover cents so sums exactly to total):
 Person 1: 2333.34
 Person 2: 2333.33
 Person 3: 2333.33

Sum of distributed payments = 7000.00  (should equal total bill)
```

---

## 📂 Project Structure

```
rent-calculator/
   ├── rent_calculator.py   # main project file
   └── README.md            # project documentation
```

---

## 📝 Future Enhancements

* Add "expense categories" (internet, gas, maintenance)
* Export bill breakdown to "CSV or PDF"
* Add a "GUI (Tkinter)" for easier usage
* Store past bills for "history tracking"

---

⚡ This project is great for practicing:

* Functions
* Input validation
* Arithmetic operations
* Rounding and fair distribution

---

