class Worker:
  'doc class Worker'
  count = 0
  def __init__(self,name,surname):
    self.name = name
    self.surname = surname
    Worker.count += 1
  def display(self):
    print("Worker:")
    print("{} {}".format(self.name,self.surname))
    
class Animal:
    count = 0 
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Animal.count += 1  
        self.instance_id = Animal.count 

    def display(self):
        print(f"Animal id: {self.instance_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

w1 = Worker("Ivan", "Ivanov")
print("w1.count: ", w1.count)
w2 = Worker("Alexei", "Petrov")
print("w2.count: ", w2.count)
print("w1.count: ", w1.count)
print("Worker.count: {0} \n".format(Worker.count))
print("Worker.__name__: ", Worker.__name__)
print("Worker.__dict__: ", Worker.__dict__)
print("Worker.__doc__: ", Worker.__doc__)
print("Worker.__bases__: ", Worker.__bases__)

#7
animal1 = Animal("Lion", 5)
animal2 = Animal("Cat", 4)
animal3 = Animal("Dog", 3)
animal1.display()
animal2.display()
animal3.display()

#8
#id повышается на 1 при создании экземпляра класса Animal

#9