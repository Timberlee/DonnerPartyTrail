#Shebang omitted altogether; run this on command line with python3
import sys
import os.path
print("Hello!")
print("I am interpreting this file: " + sys.executable)
print("Here is the full file path of this file being run: " + __file__)


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

    # if(user_input == "exit"):
    #     exit_program()
        # print(user_input)
    # exit()

def help_menu():
    print("Help Menu:")
    print("help - print this help menu")
    print("exit - exit the program")
    print("create - create a new person object")

#https://stackoverflow.com/questions/11637293/iterate-over-object-attributes-in-python
class HumanPerson:
    firstname = ""
    lastname = ""
    age = 0
    # def __iter__(self):
    #     for attr, value in self.__dict__.iteritems():
    #         yield attr,value



def create_person():
    print("Creating person...")
    x = HumanPerson()
    # print(dir(x))
    #print(vars(x))
    # print(iter(x))

status_running = True
#This loop will run infinitely but will not continually execute the print statements in main() since there is the input() function
while status_running == True:
    main()
