# Math Quiz
# Ask for user's name
name = input("HEloo what's your name?")
print(f"Hi {name}! Nice to meet you!")
# Introduce the quiz
print("This is a math quiz. We will be testing your skills! Get ready... ")
counter = 0


# Question one
question_one = input("What is 2 + 5?")
q1 = question_one.strip(" ,.!0")
if q1 == "7":
    print("Correct!")
    counter = 0 + 1
else:
    print("Sorry that is incorrect :(")


# Question two
question_two = float(input("Name the first first three digits of pi. (_.__)"))
if question_two == 3.14:
    print("oooo that is correct")
    counter = counter + 1
else:
    print("sorry you're just a little wrong")


# Question three
question_three = input("What is sin^2x + cos^2x equal to?")
q3 = question_three.strip(" .,!0")
if q3 == "1":
    print("wowoowowowowowow I see you have taken jmah's math class")
    counter = counter + 1
else:
    print("hmmm sorry i think you need to brush up on some skills..")


# Question four
question_four =input("What is 4 * 12")
q4= question_four.strip(" .,!0")
if q4 == "48":
    print("righteo")
    counter = counter + 1
else:
    print("incorrect.")


# Question Five
question_five = input("square root of 169")
q5 = question_five.strip(" .,!0")
if q5 == "13":
    print("so smart oh my, correct")
    counter = counter + 1
else:
    print("c'mon man this is so easy, incorrect")


# Results and comments!
print(f"results:{counter}/5")
results = counter / 5 * 100
print(f"{results}% is your mark buddy")
if results == 100:
    print("you got perfect!")
elif results == 80:
    print("sorry dude you just got one question wrong..")
elif results == 60:
    print("shake me head")
elif results == 40:
    print("i have no words :(")
else:
    print("uhhhhhhhhhhhhhhh keep working hard dude")