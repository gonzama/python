#Miguel Gonzalez
#Due 3/11/19
#Assignment05

'''This is a program which enables the user to create a to do list followed by its priority.
The user has five of the following options to modify the file.
Please run the program and follow the steps.'''

# Loads the data onto the program
def load_data():
	todo_list = {}
	f = open("Todo.txt", "r")
	for line in f:
		line = line.replace("\n", "")
		if len(line) == 0:
			continue
		key, val = line.split(",")
		todo_list[key] = val
	f.close()
	return todo_list

# Saves the data onto the text file.
def save_data(todo_list):
	f = open("Todo.txt", "w")
	for key in sorted(todo_list):
		f.write("{},{}\n".format(key, todo_list[key]))
	f.close()
	print (" Saved Successfully!")

# Displays the data contained in the text file.
def show_data(todo_list):
	if len(todo_list) == 0:
		print ("This is empty!")
	else:
		print ("--Todo list--")
		for key in sorted(todo_list):
			print (key, "(" + todo_list[key] + ")")

# adds a new item to the text file.
def add_new_item(todo_list):
	choice = input("Enter a task to add followed by a comma and it's priority: (Example: Clean Garden, High) ")
	key, val = choice.split(",")
	todo_list[key] = val
	return todo_list

# Removes a row from the text file.
def remove_existing_item(todo_list):
	print ("--Choose an item to remove--")
	keys = sorted(todo_list)
	for i in range(len(keys)):
		print ("{}. {}".format(i+1, keys[i]))

	# asks the user to enter a number for its command.
	choice = int(input("Enter a choice: "))
	choice_range = [i+1 for i in range(len(keys))]
	while choice not in choice_range:
		choice = int(input("Enter a valid choice: "))
	del todo_list[keys[choice-1]]
	return todo_list

if __name__ == "__main__":

	todo_list = load_data()
	show_data(todo_list)
	print ("")

	while True:
		print ("Welcome the the to-do menu. Please insert a number from the list below.")
		choices = "1. Show current data\n2. Add new item\n3. Remove existing item\n4. Save data to file\n5. Exit"
		print (choices)
		choice = int(input("Enter choice: "))
		print ("")

		while choice not in [1, 2, 3, 4, 5]:
			choice = int(input("Give a valid choice: "))

		if choice == 1:
			show_data(todo_list)
		elif choice == 2:
			todo_list = add_new_item(todo_list)
		elif choice == 3:
			todo_list = remove_existing_item(todo_list)
		elif choice == 4:
			save_data(todo_list)
		else:
			print ("==============")
			break

		print ("==============")
	print ("Thank you for using Miguel's To-do program!")