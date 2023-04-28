# creating a variable and storing the text
# that we want to search
search_text1 = "ipv4_forward 10.0.2.2 10.0.1.1"
search_text5 = "ipv4_forward 10.0.2.2 10.0.5.5"

# creating a variable and storing the text
# that we want to add
replace_text1 = "ipv4_drop 10.0.2.2 10.0.1.1"
replace_text5 = "ipv4_drop 10.0.2.2 10.0.5.5"


# s1-command.txt file

# Opening our text file in read only
# mode using the open() function
with open(r's1-commands.txt', 'r') as file:

	# Reading the content of the file
	# using the read() function and storing
	# them in a new variable
	data = file.read()

	# Searching and replacing the text
	# using the replace() function
	data = data.replace(search_text1, replace_text1)

# Opening our text file in write only
# mode to write the replaced content
with open(r's1-commands.txt', 'w') as file:

	# Writing the replaced data in our
	# text file
	file.write(data)

# Printing Text replaced
print("Rule Changed in s1-command.txt")








# s5-command.txt file

# Opening our text file in read only
# mode using the open() function
with open(r's5-commands.txt', 'r') as file:

	# Reading the content of the file
	# using the read() function and storing
	# them in a new variable
	data = file.read()

	# Searching and replacing the text
	# using the replace() function
	data = data.replace(search_text5, replace_text5)

# Opening our text file in write only
# mode to write the replaced content
with open(r's5-commands.txt', 'w') as file:

	# Writing the replaced data in our
	# text file
	file.write(data)

# Printing Text replaced
print("Rule Changed in s5-command.txt")
