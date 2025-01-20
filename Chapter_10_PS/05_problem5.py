# Q5: Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under TrenItalia.

from random import randint

class Train:
    company = "TrenItalia"

    def __init__(self, trr):
        self.trr = trr
    
    def get_status(self, dep, arr):
        print(f"\nTrain no. {self.trr}, from '{dep}' to '{arr}' is running on time.")

    def book_ticket(self, name, dep, arr):
        print(f"\nTICKET CONFIRMED!!")
        print(f"Train no. {self.trr}, {self.company}\nYour name: {name}\nDeparture: {dep}\nArrival: {arr}")
    
    def get_fare(self, dep, arr):
        print(f"\nTrain fare from '{dep}' to '{arr}' is: €{randint(16,45)}")

trainNo = int(input("Enter Train no. "))
name = input("Enter your name: ")
dep = input("Enter Departure: ")
arr = input("Enter Arrival: ")

a = Train(trainNo)
a.get_fare(dep, arr)
a.get_status(dep, arr)
a.book_ticket(name, dep, arr)