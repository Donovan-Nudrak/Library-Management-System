#!/usr/bin/env python3


class Books: 
    def __init__(self, status, title, genre, pages, price, date, author="Unknown"):
        self.title = title  
        self.genre = genre 
        self.pages = pages 
        self.price = price  
        self.date = date
        self.author = author 
        self.status = status 
    
    def display(self): 
        print(f"""Title:          {self.title}
Genre:          {self.genre}
Pages:          {self.pages}
Author:         {self.author}
Price:          {self.price}
Date:           {self.date}
Status:         {self.status}""")  

    def sell(self): 
        self.status = "Sold"

    def restore(self): 
        self.status = "Restored"
    
    def lend(self): 
        self.status = "Lent"

    def reserve(self):
        self.status = "Reserve"
    
    def add_stock(self): 
        self.status = "Available"
