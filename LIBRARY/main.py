#!/usr/bin/env python3

# Author: Nudrak
# Object-Oriented Programming (OOP) Practice

from modules.utils import pause_clear, loading_bar, logs
from modules.operator import stock, sell, lend, restore, reserve, add_stock, add_object

options = [
        "View inventory",
        "Sell",
        "Restore",
        "Lend",
        "Reserve",
        "Add to Stock",
        "Add Book",
        "Exit"
]

functions = [
        stock,
        sell,
        restore,
        lend,
        reserve,
        add_stock,
        add_object
]

def start():
    pause_clear()
    logs("Program start")
    print("The program will start in 10 seconds")
    loading_bar("STARTING PROGRAM", 10)
    pause_clear()

def main():
    while True:
        print("======= LIBRARY =======")
        print("Available options")
        for i, option in enumerate(options, 1):
            print(f"{i}) {option}")
        print("========================")

        try:
            OP = int(input("Select an option: "))
        except ValueError: 
            print("Invalid option...")
            pause_clear()
            continue 

        if OP == len(options):
            logs("Program end")
            loading_bar("Exiting", 10)
            pause_clear()
            break 
             
        elif 1 <= OP < len(options):
            logs(f"Access: {options[OP-1]}")
            print(options[OP-1])
            pause_clear()
            functions[OP-1]()
        else:
            print("Invalid option number")
            pause_clear()

if __name__ == "__main__":
    start()
    main()
