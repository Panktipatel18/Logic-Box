<div align="center">

# 🧩 Logic Box
### Pattern Generator & Number Analyzer

*A simple, menu-driven Python program that draws triangle patterns and analyzes number ranges.*

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CLI](https://img.shields.io/badge/Interface-CLI-2f5f8f?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-2f6f4f?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-8f2f3f?style=for-the-badge)

</div>

---

## 📌 Problem Statement

Beginners learning Python often need small, self-contained exercises that combine **loops**, **conditionals**, and **user input** in a single program. **Logic Box** solves this by packaging two classic logic-building exercises — pattern printing and number analysis — into one interactive, menu-driven command-line tool. Instead of running separate scripts for each exercise, the user gets a single program that keeps prompting for a choice until they explicitly choose to exit, reinforcing control-flow concepts like `while` loops, nested `for` loops, and `if`/`elif`/`else` branching.

## 🎯 Objectives

- 🔺 Generate a **right-angled triangle star pattern** for a user-specified number of rows.
- 🔢 **Analyze a range of numbers**, classifying each as even or odd and computing their sum.
- 🔁 Keep the program running in a loop so the user can perform multiple operations in one session.
- 🛡️ Validate user input (e.g., reject non-positive row counts, reject an end number smaller than the start number).
- 🚪 Provide a clean, graceful exit option with a farewell message.
- 📚 Demonstrate core programming fundamentals: loops, conditionals, input handling, and string formatting — in a beginner-friendly way.

## 🛠️ Tech Stack

| Category | Technology |
|---|---|
| Language | ![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white) |
| Interface | Command Line Interface (CLI) |
| Core Concepts | `while` loop · `for` loop · `if / elif / else` · `input()` · f-strings |
| Dependencies | None — uses only Python's built-in standard library |

## ✨ Features at a Glance

| Option | Feature | Description |
|:---:|---|---|
| **1** | Right-Angled Triangle Pattern | Prints a star (`*`) triangle with a user-defined number of rows |
| **2** | Number Range Analyzer | Labels each number in a range as *even* or *odd* and prints the total sum |
| **3** | Exit | Ends the program with a goodbye message |

## 🔄 Program Flow

The diagram below shows how the program moves through the welcome screen, the menu decision, each of the three options, input validation, and back to the menu until the user exits.

![Program Flow Diagram](images/program_flow.png)

**Flow summary:**
1. The program prints a welcome message and the menu (`1`, `2`, `3`).
2. It enters an infinite `while True` loop and reads the user's `choice`.
3. **Choice 1** → asks for `rows`; if `rows <= 0` it shows an error and loops back, otherwise it prints the triangle pattern.
4. **Choice 2** → asks for `start` and `end`; if `end < start` it shows an error and loops back, otherwise it labels each number as even/odd and prints the running total.
5. **Choice 3** → prints a goodbye message and `break`s out of the loop, ending the program.
6. Any other input → prints an "Invalid choice!" message and re-shows the menu.

## 🖥️ Sample Output

Example of a session where the user generates a 5-row triangle, analyzes the range `1–6`, then exits:

![Sample Output](images/output_sample.png)

## 🚀 How to Run

```bash
python3 "PR.2 LOGIC BOX.py"
```

Then follow the on-screen menu prompts to choose an option (`1`, `2`, or `3`).

## 📂 Project Structure

```
Logic-Box/
├── PR.2 LOGIC BOX.py     # Main program
├── README.md              # Project documentation (this file)
└── images/
    ├── program_flow.png   # Program flow diagram
    └── output_sample.png  # Sample terminal output
```

## 👩‍💻 Author

**Pankti Patel**
GitHub: [@Panktipatel18](https://github.com/Panktipatel18)
Repository: [Logic-Box](https://github.com/Panktipatel18/Logic-Box)

---

<div align="center">

Made with 🐍 Python and a lot of `for` loops.

</div>
