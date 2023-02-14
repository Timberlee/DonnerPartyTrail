#Shebang omitted altogether; run this on command line with python3
import sys
import os.path
from os import path
import json

print("Hello!")
print("I am interpreting this file: " + sys.executable)
print("Here is the full file path of this file being run: " + __file__)

#prepend with r to indicate raw file path?
json_data_dir = "data/"
json_data_file = "data.json"
full_data_file_path = os.path.join(json_data_dir, json_data_file)
print(full_data_file_path)
# print("This is a data file path: " + data_file_path)
def exit_program():
    print("Goodbye!")
    exit()

def main():
    print("=" * 80)
    user_input = input("Type 'help' for the help menu or 'exit' to exit program: ")
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
        case "compare":
            compare_stack_to_file()
        case "validate":
            validate_file(full_data_file_path)
        case "json":
            try_json2(full_data_file_path)

def help_menu():
    print("Help Menu:")
    print("help - print this help menu")
    print("exit - exit the program")
    print("create - create a new person object")
    print("stack - show list of items currently on the stack")
    print("drop - clear all items from the stack")
    print("finalize - add stack to json file")
    print("show - show existing data in json file")

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

def try_json(*args):
    try:
        json.load(args[0])
    except ValueError as e:
        return False
    return True

def try_json2(*args):
    try:
        json.load(args[0])
    except ValueError as e:
        print("Bad json")
    print ("Good json")

# Accepts a file path, and either 1 to confirm the file is not empty or 0 to skip it
def validate_file(*args):
    is_valid = False
    is_valid = True if os.path.exists(args[0]) else False
    if(args[1]):
        file = open(args[0], "r")
        file_contents = file.read()
        is_valid = True if file_contents != "" else False
    return is_valid

def show_existing_data():
# TODO: figure out how to variablize the file path
    if(validate_file(full_data_file_path, 1)):
    #Can also incorporate f = open("myfile.txt", "x/w/a")
    #'with open' closes the file for you at the end of the block
    #'r' for read is the default, but you can also make it explicit
        with open(f"{full_data_file_path}", "r") as data_file:
        #json.loads gets very unhappy if passed non-json
            if(try_json(data_file)):
                #Otherwise use json.loads(data_file.read())
                data_dejsonized = json.load(data_file)
                print("Printing contents of existing data file")
                print(data_dejsonized)
            else:
                print(f"{full_data_file_path} does not contain valid JSON")
    else:
        print("File " + full_data_file_path + " does not exist or is empty.")

def write_json_file():
    if(validate_file(full_data_file_path, 0)):
        with open(f"{full_data_file_path}", "w") as data_file:
            data_to_write = json.dumps(people_dict)
            if(data_to_write != "{}"):
                # with open(f"{full_data_file_path}", "w") as data_file_write:
                print("Writing stack to file:")
                print(data_to_write)
                json.dump(people_dict, data_file)
            else:
                print("Stack is empty, add some objects to write to data file")
    else:
        print(f"{full_data_file_path} does not exist")

# This feels a bit redundant with the exit_program() function
status_running = True
#This loop will run infinitely but will not continually execute the print statements in main() since there is the input() function
while status_running == True:
    main()
