print("Welcome to the quiz game!")

playing = input("Would you like to play? (yes/no) ").lower()

if playing != "yes":
    quit()

print("Okay! Let's play.")

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ").lower()
if answer == "power supply unit":
    print("Correct!")
else:
    print("Incorrect!")