
dog_age=(input("Enter the dog's age"))
flag=False
try:
    dog_age = float (dog_age) 
    dog_age_in_Human_years=0
    if dog_age <0:
        flag = True
    elif 0 < dog_age <=1:
        dog_age_in_Human_years += dog_age*15.0
    elif 1< dog_age <=2:
        dog_age_in_Human_years += dog_age*12.0
    elif 2< dog_age <+3:
        dog_age_in_Human_years += dog_age*9.3
    elif 3< dog_age <=4:
        dog_age_in_Human_years += dog_age*8.0
    elif 4< dog_age <=5:
        dog_age_in_Human_years += dog_age*7.2
    else:
        dog_age_in_Human_years += 5*7.2+(dog_age-7) *7.0
except ValueError as e:
    print("Your imput is invalid")
if flag == False:
    print("The given dog age", dog_age, "is", round (dog_age_in_Human_years,2), "in human years.")
else:
    print("Age cannot be a negative number")
    