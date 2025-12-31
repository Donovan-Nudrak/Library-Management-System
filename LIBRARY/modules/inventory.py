#!/usr/bin/env python3


from modules.objects import Books
import json

class Inventory: 
    def __init__(self):
        self.objects = {}  

    def save_json(self, file="inventory.json"):
        data = {}  

        for id_o, book in self.objects.items():
            data[id_o] = {
                    "title": book.title,
                    "author": book.author,
                    "genre": book.genre,
                    "pages": book.pages,
                    "price": book.price,
                    "date": book.date,
                    "status": book.status
            }
        with open(file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)


    def load_json(self, file="inventory.json"):  
        try:
            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)

            for id_o, info in data.items():
                book = Books(
                        info["status"],
                        info["title"],
                        info["genre"],
                        info["pages"],
                        info["price"],
                        info["date"],
                        info["author"]
                )
                self.objects[id_o] = book
        except FileNotFoundError:
            pass            


    def generate_id(self): 
        if not self.objects: 
            return "T1"      

        last = max(int(R[1:]) for R in self.objects.keys())
        return f"T{last + 1}" 



    def add(self, book: Books):  
        if not isinstance(book, Books): 
            raise TypeError("Only objects of type Books can be added")  

        id_o = self.generate_id()  
        self.objects[id_o] = book 
        return id_o 



    def get(self, id_o): 
        return self.objects.get(id_o) 


    def list(self): 
        return self.objects.items() 

    def execute(self, id_o, action: str): 
        obj = self.get(id_o)  
        if not obj: 
            raise ValueError("Invalid ID") 
        
        if not hasattr(obj, action): 
            raise ValueError(f"The action '{action}' does not exist")

        method = getattr(obj, action) 
        method() 


    def load_initial(self):
        self.add(Books("Available", "Hamlet", "Theater", "319", "1,400", "1601", "William Shakespeare"))
        self.add(Books("Available", "The Divine Comedy", "Poetry", "988", "2,043", "1304", "Dante Alighieri"))
        self.add(Books("Available", "Moby Dick", "Novel", "298", "1,044", "1851", "Herman Melville"))
