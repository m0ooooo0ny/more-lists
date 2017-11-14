"""Goal: Create code to allow a user to create a shopping list
Minimum requirements:
  * User can enter items which will be stored in the shopping list
  * User can exit item entry mode, which will cause the program to print the contents of the list
Stretch goals:
  * User can delete an item from the list
  * A command user can enter at any time to display the contents of the list

Advice:
  * You want to continue doing this for an unknown number of repetitions - what sort of loop would you use?
  * Remember that break will take you out of a loop, so you could say that if some string were entered - for instance 'exit' - you would do something and exit the loop
  * You're probably going to want to use input() and shopping_list.append()
  * Remember to do this one step at a time.
    * Make sure you can add a single item before you try to loop it.
    * Make sure the loop is working before you worry about how to do more advanced things

There is no automated checking on this one."""

shopping_list = []
exit_opts = ["exit", "'exit'", "Exit", "'Exit'", "EXIT", "'EXIT'"]
view_opts = ["view", "'view'", "View", "'View'", "VIEW", "'VIEW'"]
add_opts = ["add", "'add'", "Add", "'Add'", "ADD", "'ADD'"]
help_opts = ["help", "'help'", "Help", "'Help'", "HELP", "'HELP'"]
delete_opts = ["delete", "'delete'", "Delete", "'Delete'", "DELETE", "'DELETE'"]

cont = True
print("""If you wish to add items to your list, type in 'add'.
If you wish to delete items from your list, type in 'delete'.
If you wish to stop adding items, type in 'exit'.
If you wish to see what you have added, type in 'view'.
If you wish to see available commands, type in 'help'.
""")

def shopping():
    global cont
    global opt
    while cont == True:
        opt = input("What would you like to do?: ")
        if opt in exit_opts:
            exit_mode()
        elif opt in view_opts:
            view_mode()
        elif opt in help_opts:
            help_mode()
        elif opt in delete_opts:
            delete_mode
        elif opt in add_opts:
            add_mode()
        else:
            opt = input("I am sorry but that is not an acceptable response. Please try again.: ")

def exit_mode():
    global cont
    if len(shopping_list) == 0:
        print("""\nYou have exited the program.
You have no items on your shopping list.""")
    else:
        print("""\nYou have exited the program.
Your finalized shopping list is:""")
        print(shopping_list[:])
    cont = False

def view_mode():
    print("""\nYou are now in view mode.""")
    if len(shopping_list) == 0:
        print("""\nYou have no items in your shopping list right now.
        """)
    else:
        print("""\nYour current shopping list is:""")
        print(shopping_list[:],"""
        """)
    shopping()

def help_mode():
    print("""\nYou are now in help mode.
If you wish to exit the program, type 'exit'.
If you wish to add more items, type 'add'.
If you wish to delete items, type 'delete'.
If you wish to ask for help, type 'help' (but you should already know that if
    you're here, you dingus.)
If you wish to view your current list, type 'view'.
""")
    shopping()

def add_mode():
    print("""\nYou are currently in add mode.
Type in what items you would like to add.
If you would like to exit add mode, simply type in 'end'.
You will not be prompted to type in 'end'.
""")
    cont1 = True
    while cont1 == True:
        item = input("What item would you like to add?: ")
        if item == "end":
            print("""\nYou have exited add mode.
            """)
            cont1 = False
            shopping()
        else:
            shopping_list.append(item)

shopping()


opt = input("What would you like to do next?: ")
    #if opt in help_opts:
        #help_mode()
    #if opt in add_opts:
        #add_mode()
    #if opt in exit_opts:
        #exit_mode()
    #if opt in delete_opts:
        #delete_mode()