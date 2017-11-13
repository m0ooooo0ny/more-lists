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

cont = True
print("""If at any time you wish to stop adding items, type in 'exit'.
If at any time you wish to see what you have added, type in 'view'.
If you wish to see commands at any time, type in 'help'.
You are currently in item entry mode.
""")

def shopping():
    global cont
    global opt
    while cont == True:
        opt = input("""What item would you like to add?: """)
        if opt in exit_opts:
            print("""
You have exited the program.""")
            cont = False
        elif opt in view_opts:
            print("""
You are now in view mode.
Your current shopping list contains:""")
            if len(shopping_list) == 0:
                print("""
There is nothing in your list.""")
            else:
                print(shopping_list[:])
            entry = input("""
Would you like to return to item entry mode? [Y/N]: """)
            if entry == "Y" or entry == "y":
                cont = True
            if entry == "N" or entry == "n":
                cont = False
        elif opt in help_opts:
            print("""
exit = exiting item entry
view = view current list
anything else = adds what is typed to list.""")
        else:
            shopping_list.append(opt)



shopping()

print("""
Your finalized shopping list contains:""")
print(shopping_list[:])