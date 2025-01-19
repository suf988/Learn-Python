# Q5: Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under TrenItalia.

from random import randint

class Train:
    company = "TrenItalia"
    seats = 70

    def __init__(self, train):
        self.train = train
        
    def getStatus(self):
        print(f"\nTrain no. {self.train} of {self.company} running on-time\nNo. of Seats: {self.seats}\nFare: €{randint(15,45)}")
    
    def bookTicket(self, name, dep, arr):
        print(f"\nTICKET CONFIRMED")
        print(F"Your Name: {name}\nJourney: {dep} to {arr}\nTrain no. IT{self.train}")

trr = int(input("Enter Train no: "))
name = input("Enter Your name: ")
dep = input("Departure from: ")
arr = input("Arrival to: ")

user1 = Train(trr)
user1.getStatus()
user1.bookTicket(name, dep, arr)

