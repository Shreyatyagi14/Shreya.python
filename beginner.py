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


#format function to insert values
def format_string(num, char):
    return "The number is {} and the character is {}".format(num, char)
# Calling the function with 145 and 'o'
result = format_string(145, 'o')
print(result)



#given values
radius = 84
pi = 3.14
water_per_square_meter = 1.4
#calculating area of pond
area_of_pond = pi * (radius ** 2)
#calculating total amount of water in liters
total_water = area_of_pond * water_per_square_meter
#print statement to print the result    
print("Area of the pond:", area_of_pond)
print("Total water in the pond (in liters):", int(total_water))  # Print without decimal



#given values
distance = 490  # meters
time_minutes = 7
#converting time to seconds (1 minute = 60 seconds)
time_seconds = time_minutes * 60
#calculating speed (Speed = Distance / Time)
speed = distance / time_seconds
#print statement to print the result  
print(int(speed))  # converting speed to an int value to print without a decimal


--------------------------------------------------------------------------------------------TASK-3--------------------------------------------------------------------------------------------


#list of justice league members
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Initial Justice League:", justice_league)



#calculating number of members
num_members = len(justice_league)
print(f"Number of members: {num_members}")



#Batman recruiting Batgirl and Nightwing as new members
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("After adding Batgirl and Nightwing:", justice_league)



#Wonder Woman is the leader (move her to the beginning)
justice_league.remove("Wonder Woman")  # Remove her current position
justice_league.insert(0, "Wonder Woman")  # Insert at the beginning
print("After making Wonder Woman the leader:", justice_league)



#Move "Green Lantern" between Aquaman and Flash to separate them
justice_league.remove("Green Lantern")  # Remove Green Lantern from current position
flash_index = justice_league.index("Flash")
justice_league.insert(flash_index, "Green Lantern")  # Insert before Flash
print("After moving Green Lantern between Aquaman and Flash:", justice_league)



#Replacing the existing team with new members
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("After replacing the team:", justice_league)



#Sorting the Justice League alphabetically
justice_league.sort()
print("After sorting alphabetically:", justice_league)



# Bonus: Predict the new leader (first member of sorted list)
new_leader = justice_league[0]
print(f"New leader of the Justice League is: {new_leader}")

--------------------------------------------------------------------------------------------TASK-5--------------------------------------------------------------------------------------------



#random module to generate random number for a dice
import random
#assigning variables to track counts
rolling_6 = 0
rolling_1 = 0
consecutive_6s = 0
previous_roll = None
#simulating rolling a six-sided die 30 times
for i in range(30):
    roll = random.randint(1, 6)  #rolling the die (random number between 1 and 6)
    #counting how many times we roll a 6 or 1
    if roll == 6:
        rolling_6 += 1
    if roll == 1:
        rolling_1 += 1
    #counting how many times we roll two 6s in a row
    if previous_roll == 6 and roll == 6:
        consecutive_6s += 1
    #updating the previous roll for consecutive check
    previous_roll = roll
#printing the stats
print(f"Total times rolled a 6: {rolling_6}")
print(f"Total times rolled a 1: {rolling_1}")
print(f"Total times rolled two 6s in a row: {consecutive_6s}")



#assigning variables
total_jumping_jacks = 100
sets_completed = 0
jumping_jacks_done = 0
#my workout loop
while jumping_jacks_done < total_jumping_jacks:
    #performing  a set of 10 jumping jacks at a time
    sets_completed += 1
    jumping_jacks_done += 10
    #ask the user if he/she is tired?
    tired = input(f"Set {sets_completed}: You have completed {jumping_jacks_done} jumping jacks. Are you tired? (yes/no): ").strip().lower()
    #checking if the user is tired and wants to stop
    if tired in ["yes", "y"]:
        skip = input("Do you want to skip the remaining sets? (yes/no): ").strip().lower()
        if skip in ["yes", "y"]:
            print(f"You completed a total of {jumping_jacks_done} jumping jacks.")
            break
    else:
        remaining_jumping_jacks = total_jumping_jacks - jumping_jacks_done
        print(f"{remaining_jumping_jacks} jumping jacks remaining.")
     # If all 100 jumping jacks are completed, congratulate the user
    if jumping_jacks_done == total_jumping_jacks:
        print("Congratulations! You completed the workout.")


--------------------------------------------------------------------------------------------TASK-4--------------------------------------------------------------------------------------------


#user input for height and weight
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))
#calculating BMI
bmi = weight / (height ** 2)
#determining BMI category
if bmi >= 30:
    print("Obesity")
elif 25 <= bmi < 30:
    print("Overweight")
elif 18.5 <= bmi < 25:
    print("Normal")
else:
    print("Underweight")



#List of cities per country
australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
#city name input from user
city = input("Enter a city name: ")
#determining the country of the city
if city in australia:
    print(f"{city} is in Australia")
elif city in uae:
    print(f"{city} is in UAE")
elif city in india:
    print(f"{city} is in India")
else:
    print(f"{city} is not in the list of known cities")



#List of cities per country
australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
#input for two cities from the user
city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")
#checking if both cities belong to the same country
if city1 in australia and city2 in australia:
    print("Both cities are in Australia")
elif city1 in uae and city2 in uae:
    print("Both cities are in UAE")
elif city1 in india and city2 in india:
    print("Both cities are in India")



