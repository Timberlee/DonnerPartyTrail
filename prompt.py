#Shebang omitted altogether; run this on command line with python3
import sys
import os.path
from os import path
import json

print("Hello!")
print("I am interpreting this file: " + sys.executable)
print("Here is the full file path of this file being run: " + __file__)

data_file_path = r"data/data_file.json"
print("This is a data file path: " + data_file_path)
def exit_program():
    print("Goodbye!")
    exit()

def main():
    print("=" * 80)
    user_input = input("Type 'help' for the help menu or 'exit' to exit program: ")
# https://www.freecodecamp.org/news/python-switch-statement-switch-case-example/
    match user_input:
        case "exit":
            exit_program()
        case "help":
            help_menu()
        case "create":
            create_person()
        case "stack":
            show_stack()
        case "drop":
            drop_stack()
        case "finalize":
            write_json_file()
        case "show":
            show_existing_data()

def help_menu():
    print("Help Menu:")
    print("help - print this help menu")
    print("exit - exit the program")
    print("create - create a new person object")
    print("stack - show list of items currently on the stack")
    print("drop - clear all items from the stack")
    print("finalize - add stack to json file")
    print("show - show existing data in json file")

#https://stackoverflow.com/questions/11637293/iterate-over-object-attributes-in-python
class HumanPerson:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    # Seems like I can either use __dict__ here or in show_stack to the same effect
    # def __iter__(self):
    #     return(self)
    #     for attr, value in self.__dict__.iteritems():
    #         yield attr,value

# Nested Dictionary
people_dict = {}
def show_stack():
    for x in people_dict:
        print(people_dict[x])


def create_person():
    print("Creating person...")
    fname = input("Enter first name: ")
    lname = input("Enter last name: ")
    ageyears = input("Enter age in years: ")
    new_person = HumanPerson(fname, lname, ageyears)
    # print(dir(x))
    #print(vars(x))
    print(new_person.__dict__)
#https://www.edureka.co/community/31967/how-to-print-objects-of-class-using-print-function-in-python

    next_action = input("Is this correct? Enter y to create, n to edit (only one edit is supported) or x to cancel: ")
    match next_action:
        case "y":
            dict_key = fname + lname
            people_dict[dict_key] = new_person.__dict__
            print(f"Added {new_person.__dict__} to stack")
            #TODO: fix this
        case "n":
            edit_field = input("Enter name of field: ")
            edit_value = input("Enter new value: ")
            new_person[edit_field] = edit_value
            print(new_person.__dict__)
        case "x":
            del new_person
            print("Deleted")

def drop_stack():
    people_dict = {}
    for item in people_dict:
        print(item)

def show_existing_data():
# TODO: figure out how to variablize the file path
    if(os.path.exists(data_file_path)):
    #Can also incorporate f = open("myfile.txt", "x/w/a")
        with open(data_file_path, "r") as data_file:
            data_jsonized = json.load(data_file)
            print("Printing contents of existing data file")
            print(data_jsonized)


# This feels a bit redundant with the exit_program() function
status_running = True
#This loop will run infinitely but will not continually execute the print statements in main() since there is the input() function
while status_running == True:
    main()
