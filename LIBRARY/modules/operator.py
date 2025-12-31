#!/usr/bin/env python3


from modules.utils import pause_clear, pause, clear, loading_bar, logs
from modules.inventory import Inventory
from modules.objects import Books


ACTIONS = ["sell", "restore", "lend", "reserve", "add_stock"]

inventory = Inventory()
inventory.load_json()
inventory.load_initial()


def execute_action(action): 
    if action not in ACTIONS:
        print(f"Action: {action} invalid")
        return 

    stock() 
    id_book = input(f"ID of the book to {action}: ")

    try:
        loading_bar(f"{action.capitalize()} {id_book}...", 5)
        inventory.execute(id_book, action)
        logs(f"Book: {id_book} => {action}") 
        print(f"Book: {id_book} => {action} successfully") 
    except Exception as e:
        print("Error: ", e)

def stock():
    for id_book, book in inventory.list():
        print("\n==================")
        book.display()
        print(f"ID: {id_book}")
        print("==================\n")

def add_object():
    print("\n===Add book===")

    title = input("Title: ")
    genre = input("Genre: ")
    pages = int(input("Pages: "))
    price = float(input("Price: "))
    date = input("Date: ")
    author = input("Author: ")

    book = Books(
            "Available",
            title,
            genre,
            pages,
            price,
            date,
            author
        )

    new_id = inventory.add(book)
    inventory.save_json()
    logs(f"Book added: {title} - {new_id}")
    print(f"Book added: {title} - {new_id}")
    

def sell():
    execute_action("sell")

def lend():
    execute_action("lend")

def restore():
    execute_action("restore")

def reserve():
    execute_action("reserve")

def add_stock():
    execute_action("add_stock")
