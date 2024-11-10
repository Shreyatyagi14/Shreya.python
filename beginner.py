--------------------------------------------------------------------------------------------TASK-1--------------------------------------------------------------------------------------------
# variable pi is created and value 22/7 is stores
pi = 22 / 7
#now we check the data type of the variable 
print("Value of pi:", pi)
print("Data type of pi:", type(pi))



#using for to store value of 4
for = 4  
#this is will cause syntax error because its a reserved keyword , to solve this we will take any other variable name which is not a reserved keyword

  

#storing principal , rate of interest and time in different variables
principal = 1000  #assumed principal amount
rate_of_interest = 5  #assumed rate of interest
time = 3  #given time
#calculating simple interest using the formula: SI = P * R * T / 100
simple_interest = (principal * rate_of_interest * time) / 100
# Display the calculated Simple Interest
print("Simple Interest for", time, "years is:", simple_interest)

--------------------------------------------------------------------------------------------TASK-2--------------------------------------------------------------------------------------------
def format_string(num, char):
    return "The number is {} and the character is {}".format(num, char)

# Call the function with 145 and 'o'
result = format_string(145, 'o')
print(result)

