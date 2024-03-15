import time

class Ticket:
    def __init__(self, date, name, deadline):
        self.createDate = date
        self.owner = name
        self.deadline = deadline
        
    def __del__(self):
        print("Delete ticket:", time.strftime("%d %b %Y %H:%M:%S", self.createDate))
    
    def display(self):
        print("Ticket:")
        print(" createDate: ", time.strftime("%d %b %Y %H:%M:%S", self.createDate))
        print(" owner: ", self.owner)
        print(" deadline: ", time.strftime("%d %b %Y %H:%M:%S", self.deadline))
#
ticket1 = Ticket(time.localtime(), "Ivan Ivanov", time.strptime("17.12.2017", "%d.%m.%Y"))
ticket1.display()
print("Owner: ", ticket1.owner)
print("Owner(getattr): ", getattr(ticket1, "owner"))
print("hasattr: ", hasattr(ticket1, "owner"))
setattr(ticket1, "owner", "Alexei Petrov")
print("Owner(setattr): ", ticket1.owner)

#2
print("delattr: ", ticket1.owner)
delattr(ticket1, "owner")

#3
del ticket1 
#print(ticket1)
#Удалили ticket1, нечего выводить

#4
ticket2 = Ticket(time.localtime(), "Ivan Ivanov", time.strptime("14.12.2017", "%d.%m.%Y"))
ticket2.display()

#5
datetime_str = "17.07.2017 10:53:00"

# Используем strptime из модуля time для преобразования строки в struct_time
datetime_object = time.strptime(datetime_str, "%d.%m.%Y %H:%M:%S")

print(datetime_object)

print(time.strftime("%d %b %Y %H:%M:%S", datetime_object))
