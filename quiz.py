# Math Quiz
print("Hello User, This is a math quiz. We will be testing your skills! Get ready...")
counter = 0
question_one = float(input("What is 2 + 5?"))
if question_one == 7:
    print("Correct!")
    counter = 0 +1
else:
    print("Sorry that is incorrect :(")


question_two = float(input("Name the first first three digits of pi."))
if question_two == 3.14:
    print("oooo that is correct")
    counter = counter + 1
else:
    print("sorry you're just a little wrong")

question_three = float(input("What is sin^2x + cos^2x equal to?"))
if question_three == 1:
    print("wowoowowowowowow I see you have taken jmah's math class")
    counter = counter + 1
else:
    print("hmmm sorry i think you need to brush up on some skills..")

question_four =float(input("What is 4 * 12"))
if question_four == 48:
    print("righteo")
    counter = counter + 1
else:
    print("incorrect.")

question_five = float(input("square root of 169"))
if question_five == 13:
    print("so smart oh my, correct")
    counter = counter + 1
else:
    print("c'mon man this is so easy, incorrect")

print(f"results:{counter}/5")
results = counter / 5 * 100
print(f"{results}%")