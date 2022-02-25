# Cashbox

# for saving objects
import pickle
# for displaying date of creation
import datetime
# time.sleep()
import time
# clear screen
from os import system


# classes
class Person:

    # class attributes - same every instance
    # pass

    # instance attributes - changes on every instance
    def __init__(self, name):
        self.name = name
        self.balance = 0

        # dicts
        self.debt = {}
        self.repayment = {}
        self.expense = {}
        self.reimbursement = {}
        self.donation = {}

        # fun facts
        self.created = datetime.datetime.now().strftime("%d.%m.%Y")

    # redefinition of output for print(instance)
    def __str__(self):
        return f"{self.name} has a balance of {self.balance}€."


# methods
# register a new person
def createPerson():
    person = input("Name: ")

    # check if the name is already taken or not
    for i, name in enumerate(PersonInstances):
        if PersonInstances[i].name == person:
            clearScreen()
            print("User " + person + " already taken. Please try again or exit.")
            return

    # create person instance
    person = Person(person)
    clearScreen()
    print("User " + person.name + " was created.")
    # add person to list of objects and list of names
    PersonInstances.append(person)

    showUsers()
    return


# show a list of registered users
def showUsers():
    clearScreen()
    print("Registered users:")
    print("# Name")
    # print registered users with an index starting at 1 (readability)
        # TODO: indent str "Name" correctly when 9+ elements
    #  for i, name in enumerate(PersonNames, start=1):
    for i, name in enumerate(PersonInstances):
        #  print(i, name)
        print(i+1, PersonInstances[i].name)


# check if list is empty
def usersRegistered():
    if not PersonInstances:
        clearScreen()
        print("Please register a user.")
        return False
    else:
        return True


# add debt to a user
def addDebt():
    # check if there are registered users
    if usersRegistered() is True:
        clearScreen()
        showUsers()
    else:
        return

    # user index input
    # check if input user index is valid
    person = checkInputInt(input("Add debt for user #"))
    if person is False or person <= 0 or person >=  len(PersonInstances):
        clearScreen()
        print("Please enter valid user index.")
        return

    # amount input
    # check if amount input is valid
    amount = checkInputFloat(input("Amount: "))
    if amount is False:
        clearScreen()
        print("Please enter float value here.")
        return

    # write amount to person
    # get timestamp
    key = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    # get person index
    personIndex = person - 1

    # add amount with timestamp to persons debt dictionary
    PersonInstances[personIndex].debt[key] = amount

    print("Debt of {0:.2f} € added for {1}.".format(PersonInstances[personIndex].debt[key], PersonInstances[personIndex].name))
    

# calculate current balance
def calcBalance(userIndex):

    # get persons stats
    debt            = sum(PersonInstances[userIndex].debt.values())
    repayment       = sum(PersonInstances[userIndex].repayment.values())
    expense         = sum(PersonInstances[userIndex].expense.values())
    reimbursement   = sum(PersonInstances[userIndex].reimbursement.values())
    donation        = sum(PersonInstances[userIndex].donation.values())
    
    # calculate balance
    balance = debt + repayment + expense + reimbursement + donation

    # write balance to object
    PersonInstances[userIndex].balance = balance

    clearScreen()
    print("{0} has a balance of {1:.2f} €.".format(PersonInstances[userIndex].name, balance))
    return


def select_user():
    # check if there are registered users
    if usersRegistered() is True:
        clearScreen()
        showUsers()
    else:
        return

    # user index input
    person = checkInputInt(input("Select user #"))
    # check if input user index is valid
    if person is False or person <= 0 or person >=  len(PersonInstances):
        clearScreen()
        print("Please enter valid user index.")
        return
    else:
        return person-1


# save data
def saveData():
    global PersonInstances
    global PersonNames
    outputFile = 'cashboxObjects.data'
    saveObjects = open(outputFile, 'wb')
    pickle.dump(PersonInstances, saveObjects)
    saveObjects.close()
    outputFile = 'cashboxNames.data'
    saveNames = open(outputFile, 'wb')
    pickle.dump(PersonNames, saveNames)
    saveNames.close()
    clearScreen()
    print("Data successfully saved.")


# load data
def loadData():
    global PersonInstances
    global PersonNames
    inputFile = 'cashboxObjects.data'
    load = open(inputFile, 'rb')
    PersonInstances = pickle.load(load)
    inputFile = 'cashboxNames.data'
    load = open(inputFile, 'rb')
    PersonNames = pickle.load(load)
    clearScreen()
    print("Data successfully restored.")


# check if input is int and typecast value
def checkInputInt(userInput):
    try:
        int(userInput)
        return int(userInput)
    except ValueError:
        return False


# check if input is float and typecast value
def checkInputFloat(userInput):
    try:
        float(userInput)
        return float(userInput)
    except ValueError:
        return False


# clear screen
def clearScreen():
    system('clear')


# show main menu
def MainMenu():
    print("\n### Please select:")
    print("1 - create Person")
    print("2 - add debt")
    print("3 - calculate balance")
    print("4 - save data")
    print("5 - load data")
    print("6 - show users")
    print("0 - exit")

    selection = input("\nWhat you gonna do?\n")

    match selection:
        case '1':
            createPerson()

        case '2':
            addDebt()

        case '3':
            #  userInput = input("Calculate the balance for: ")
            user = select_user()
            calcBalance(user)

        case '4':
            saveData()

        case '5':
            loadData()

        case '6':
            showUsers()

        case '0':
            print("Bye!")
            quit()

        case _:
            print("\nInput not found. Please select again.")


### setup ###
clearScreen()
print("\n--- Cashbox ---")

# initialize person objects
PersonInstances = []
PersonNames     = []

### main ###
while(1):
    MainMenu()
