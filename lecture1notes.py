### Store.py

# from [filename] import [class name]
from Category import Category

class Store: #Camelcase for class names
    # attributes - name, categories, 

    # constructor - the function that runs every time we create a new instance
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories
        self.employees = []

    def __str__(self): #this prints a string when Store instance is called
        # return a string representing a store
        output = f'Welcome to {self.name}: '
        i = 1
        for cat in self.categories:
            output += f'\n {i} {str(cat.name)}'
            i += 1
        return output

    def __repr__(self):
        # also returns a string, is mostly meant for developers for debugging so the output is info focused rather than UX focused
        # the code that created that create the object for devs to understand how it structured
        return f'self.name = {self.name} ; self.categories = {self.categories}'
 
running_category = Category('Running', "For your running need", [])
baseball_category = Category('Baseball', "homeruns from us!", [])
basketball_category = Category('Basketball', 'indoor stuff and outdoor', [])

sports_store = Store('Slammy', [ running_category, baseball_category, basketball_category])
# produce_store = Store('Megamart', ['milk', 'produce', 'bread'])
# print(sports_store)
print(repr(sports_store))

choice = -1
print('Type 0 to quit')

while choice != 0:
    ## User interface, REPL
    # read, evaluate print loop
    # Read
    choice = input('Please choose a category (#)')
    try: 
        if (choice == 'q'):
            break
        choice = int(choice)- 1
        if choice >= 0 and choice < len(sports_store.categories):
            # Evaluate
            #print
            print(sports_store.categories[int(choice) - 1])
            # Loop
        else:
            print('out of range')
    except ValueError:
        print('Please enter a valid number')

 
