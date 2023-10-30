class People():
    def __init__(self, name, age, power):
        self.name = name
        self.age = age
        self.power = power

    def get_personal_information(self):
        print(f"Name is: {self.name}")
        print(f"Age is: {self.age}")
        print(f"Power is: {self.power}")

    def __add__(self, other):
        # return self.power + other.power
        name = self.name + other.name
        if self.age > other.age:
            age = self.age
        else:
            age = other.age
        power = self.power + other.power
        return People(name, age, power)

    def __gt__(self, other):
        if self.age > other.age:
            return True
        elif other.age > self.age:
            return False





person1 = People("John", 13, 50)
person2 = People("Jack", 20, 70)
person3 = person1 + person2
# person1.get_personal_information()
# person2.get_personal_information()
# person3.get_personal_information()

if person1 > person2:
    print(f"Greather is {person1.name}")
elif person1 == person2:
    print("Persons are equal")
else:
    print(f"Greather is {person2.name}")

print("Cast to int: ", int(person1))
print("Cast to str:", str(person2))
print("Len of People: ", len(person2))

person4 = person1 + person2 + person3
person4.get_personal_information()