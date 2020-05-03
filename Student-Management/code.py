# --------------
# Code starts here

# Create the lists 
class_1 = ["Geoggrey Hinton", "Andrew Ng", "Sebestiona Raschka", "Yoshua bengio"]
class_2 = ["Hilary mason", "Carla Gentry", "Corinna Cortes"]
# Concatenate both the strings
new_class = class_1 + class_2
print(new_class)

# Append the list
new_class.append("Peter warden")
# Print updated list
print(new_class)

# Remove the element from the list
new_class.remove("Carla Gentry")
# Print the list
print(new_class)


# Create the Dictionary
courses = {
    'Math' : 65,
    'English' : 70,
    'History' : 80,
    'French' : 70,
    'Science' : 60
}
print(courses)

# Slice the dict and stores  the all subjects marks in variable
total = 0
for s in courses:
    total += courses[s]
print(total)

# Store the all the subject in one variable `Total`
Total = []
for s in courses:
    Total.append(s)
# Print the total
print(Total)
# Insert percentage formula
percentage = (total * 100) / 500
# Print the percentage
print(percentage)



# Create the Dictionary
mathematics = {
     'Geoffrey Hinton' : 78,
     'Andrew Ng' : 95,
     'Sebastian Raschka' : 65,
     'Yoshua Benjio' : 50,
     'Hilary Mason' : 70,
     'Corinna Cortes' : 66,
     'Peter Warden' : 75
 }
topper = ''
mark = 0
for m in mathematics:
    if mathematics[m] > mark:
        mark = mathematics[m]
        topper = m
print(topper)


# Given string
topper = topper.split(" ")

# Create variable first_name 
first_name = topper[0]
# Create variable Last_name and store last two element in the list
last_name = topper[1]
# Concatenate the string
full_name = last_name+" "+first_name
# print the full_name
print(full_name)
# print the name in upper case
certificate_name = full_name.upper()
print(certificate_name)
# Code ends here

