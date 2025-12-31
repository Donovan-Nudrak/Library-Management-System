# Library Management System

## Overview

The **Library Management System** is a Python project designed as a practice in **Object-Oriented Programming (OOP)**.  
It simulates a library environment, allowing users to **view inventory**, **sell**, **restore**, **lend**, **reserve**, and **add books**.  
The system leverages classes and objects to represent books and their attributes, providing a foundation for future expansion.

---

## Project Structure

LIBRARY/
├─ main.py # Entry point, handles user interaction and menu
├─ modules/
│ ├─ utils.py # Utility functions: pause, clear, loading bar, logging
│ ├─ inventory.py # Inventory management: load/save books, add, retrieve, execute actions
│ ├─ objects.py # Books class definition with attributes and action methods
│ └─ operator.py # Functions for performing operations on the inventory (sell, lend, reserve, etc.)
├─ inventory.json # JSON file for persisting library data
└─ logs.txt # Log file recording program events


---

## Program Flow

1. **Initialization**  
   - `main.py` imports necessary modules and functions.  
   - The program starts with `start()`, displaying a loading bar and logging program start.

2. **User Interaction**  
   - A menu is displayed with all available actions.  
   - Users select an option by entering a number.

3. **Option Selection**  
   - Input is validated: non-numeric or out-of-range entries are rejected.

4. **Action Execution**  
   - Each menu option corresponds to a function in `operator.py`.  
   - Functions interact with the `Inventory` object, performing the requested operation.

5. **Inventory Management**  
   - `Inventory` maintains all books in a dictionary (`self.objects`).  
   - Each book is an instance of `Books`, with attributes: `title`, `author`, `genre`, `pages`, `price`, `date`, `status`.

6. **Data Persistence**  
   - Inventory is loaded from `inventory.json` at startup.  
   - All modifications (additions, updates) are saved automatically.

7. **Logging**  
   - All actions (program start/end, book operations) are logged in `logs.txt` with timestamps.

8. **Program Termination**  
   - The loop continues until the user selects **Exit**.  
   - Program logs the termination and displays a loading bar during exit.

---

## Key Modules and Functions

### 1. `main.py`
- **Functions:**
  - `start()`: Initializes the program, displays a loading bar, and logs program start.
  - `main()`: Displays the main menu, handles user input, and executes selected actions.
- **Variables:**
  - `options`: List of menu option names.
  - `functions`: List of functions corresponding to the menu options.

### 2. `modules/utils.py`
- **Functions:**
  - `pause(sleep=2)`: Pauses execution for a given number of seconds.
  - `clear()`: Clears the console screen.
  - `pause_clear()`: Pauses and then clears the screen.
  - `loading_bar(text, times=100)`: Displays a progress bar for user feedback.
  - `logs(log)`: Appends a log entry with timestamp to `logs.txt`.

### 3. `modules/objects.py`
- **Class:** `Books`
  - **Attributes:** `title`, `author`, `genre`, `pages`, `price`, `date`, `status`.
  - **Methods:** `sell()`, `restore()`, `lend()`, `reserve()`, `add_stock()`, `display()`.

### 4. `modules/inventory.py`
- **Class:** `Inventory`
  - **Attributes:** `self.objects` — dictionary mapping book IDs to `Books` objects.
  - **Methods:**  
    `add()`, `get()`, `list()`, `execute()`, `save_json()`, `load_json()`, `load_initial()`, `generate_id()`.

### 5. `modules/operator.py`
- **Functions:**
  - `stock()`: Displays the current inventory.
  - `sell()`, `restore()`, `lend()`, `reserve()`, `add_stock()`: Execute the respective action on a selected book.
  - `add_object()`: Adds a new book to the inventory with user-provided attributes.

---

## Key Variables

|          Variable          |       Type       |              Description                |
|----------------------------|------------------|-----------------------------------------|
| `options` (main.py)        | list[str]        | Menu option names                       |
| `functions` (main.py)      | list[function]   | Functions corresponding to menu options |
| `self.objects` (Inventory) | dict             | Mapping of book IDs to `Books` objects  |
| `id_o`                     | str              | Unique book ID                          |
| `book`                     | `Books` object   | Represents a single book                |

---

## Design Choices

- **Object-Oriented Design:** Classes (`Books`, `Inventory`) provide modularity and scalability.  
- **JSON Persistence:** Stores and loads library data between sessions.  
- **Modular Code:** Separates utilities, operations, data, and models.  
- **Error Handling:** Input validation and try-except blocks prevent program crashes.  
- **Logging:** Tracks program activity in `logs.txt`.

---

## Potential Enhancements

- Implement a **graphical user interface (GUI)**.  
- Add **search and filter functionality** for books.  
- Introduce **robust data validation** for numeric fields.  
- Extend system with **user accounts and overdue management**.  
- Migrate from JSON to a **database system** (SQLite, PostgreSQL) for scalability.

---

## Conclusion

The **Library Management System** demonstrates **OOP principles**, modular design, and data persistence in Python.  
It is a solid foundation for developing more advanced library management applications.

