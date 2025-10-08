from random import randint
class Train:
    def __init__(self, trainNo, fro, to):
        self.trainNo = trainNo
        self.fro = fro
        self.to = to

    def book(self):
        print(f"Ticket is booked in train no {self.trainNo} from {self.fro} to {self.to}")

    def status(self):
        print(f"There are {randint(1, 100)} seats left in train no {self.trainNo}")

    def fare(self):
        print(f"Ticket fare in train no {self.trainNo} from {self.fro} to {self.to} is {randint(100, 10000)}")


trainNo = int(input("Enter the train number: "))
fro = input("Enter from where you are going to board the train: ")
to = input("Enter your destination: ")


t = Train(trainNo, fro, to)
t.book()
t.status()
t.fare()
