import json

class Person:
    def __init__(self):
        self.Name = "Inigo Montoya"
        self.Occupation = "Swordsman"
        self.Friends = ["Fezzik", "Dread Pirate Roberts"]

def main():
    p = Person()
    fptr = open("myfile.json", "w")
    json.dump(p.__dict__, fptr)
main()
