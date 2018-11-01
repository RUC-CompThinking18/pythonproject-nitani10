import time # import the time module that can enable the use of a countdown
import os
def clear(): # Creates a function that clears a line and enables new writing to go above
    os.system('cls' if os.name == 'nt' else 'clear')
print "Hello and welcome to Who Wants to be a Loseionnaire?"
time.sleep(5) # countdown 5 seconds before preceding to the next line
clear()
print "The rules of this game are very simple."
time.sleep(5)
def objective():
    print "If you reply with the correct response,\nthe level of carbon dioxide in the atmosphere will lower."
    time.sleep(5)
    print "You will start with a lethal carbon dioxide ppm level of 40000."
    print "and you will work your way towards the normal/healthy 250 ppm."
    time.sleep(5)
    print "Take careful notes about what you learn because some day..."
    print "our earth could be heavily affected by this ever-so pressing issue!"
    time.sleep(8)
    clear()
objective()
def lifeline_explanations(): # This function prints text describing the lifelines available during the game
    print "\n\nYou will have three lifelines that you can use at any time to answer the questions."
    time.sleep(5)
    print 'The ask the audience lifeline will provide percentages of likelihood that the "audience" (alias the general population) would choose each option.'
    time.sleep(8)
    print"Beware because the top choice will not necessarily mean that it is the correct response!"
    time.sleep(8)
    print 'The choose a friend lifeline will provide the top choice that the "friend" believes is the correct response.'
    time.sleep(8)
    print 'You will get an opportunity at the start of the game to select a "friend" based on three available options with varying levels of knowledge and expertise.'
    time.sleep(10)
    print "Choose your friend wisely because their top choice will not guarantee that you will have chosen the correct response!"
    time.sleep(8)
    print "Finally, the 50/50 lifeline will narrow the options available to two: one correct and one incorrect response."
    time.sleep(8)
    clear()
lifeline_explanations()
def repeat_rules(): # This function asks the user if they wish to hear again about the lifelines available during the duration of the game
    print "Would you like to hear again about the objective or the lifelines of this game?"
    answer = raw_input('Type "one" for objective, "two" for lifelines or "zero" for neither: ').lower()
    clear()
    if answer == "one" or answer == "1":
        print "\nYou selected one which will repeat the objective section for you."
        print "Is this correct?"
        answer = raw_input('Type "yes" to repeat the objective or any key to return to the previous menu: ').lower()
        if answer == "yes" or answer == "y":
            time.sleep(2)
            clear()
            objective()
            repeat_rules()
        else:
            print "It seems that you did not mean to make this selection."
            time.sleep(3)
            print "The program will now redirect you to the previous menu.\n"
            time.sleep(2)
            clear()
            repeat_rules()
    elif answer == "two" or answer == "2":
        print "\nYou selected two which will repeat the lifeline section for you."
        print "Is this correct?"
        answer = raw_input('Type "yes" to repeat the lifelines or any key to return to the previous menu: ').lower()
        if answer == "yes" or answer == "y":
            time.sleep(2)
            clear()
            lifeline_explanations()
            repeat_rules()
        else:
            print "It seems that you did not mean to make this selection."
            time.sleep(3)
            print "The program will now redirect you to the previous menu.\n"
            time.sleep(2)
            clear()
            repeat_rules()
    elif answer == "zero" or answer == "0":
        print "\nYou selected zero indicating that you do not want to repeat the rules."
        print "Is this correct?"
        answer = raw_input('Type "yes" to proceed to the next section or any key to return to the previous menu: ').lower()
        if answer == "yes" or answer == "y":
            time.sleep(2)
            print "okay, we can now proceed onto the choose a friend lifeline portion of this game!\n"
            clear()
        else:
            print "It seems that you did not mean to make this selection."
            time.sleep(3)
            print "The program will now redirect you to the previous option menu.\n"
            time.sleep(2)
            clear()
            repeat_rules()
    else:
        print "You didn't write one, two, or zero. Try again!"
        time.sleep(2)
        repeat_rules()
repeat_rules()

class friend(): #Initiate a class that takes 4 commands - "name, gender, age and occupation"
    def __init__(self, name, gender, age , occupation):
        self.name = name
        self.gender = gender
        self.age = age
        self.occupation = occupation
def choose_a_friend(): #Tells the user the information about each friend choice and enables user to choose the friend
    print "You will now be able to choose a friend that can help you narrow down one of the questions."
    time.sleep(5)
    print "Remmember that choosing the right friend can save you from making the wrong and environmentally unsound judgement!"
    time.sleep(7)
    print "\nBelow is the information about friend # 1:"
    time.sleep(3)
    Option1 = friend('Jane', 'female', '25', 'student')
    print "Hello, my name is " + Option1.name + "\nI am a " + Option1.gender + "\nI am " + Option1.age + " years old" + "\nMy occupation is " + Option1.occupation
    time.sleep(12)
    print "\nNext is the information about friend # 2:"
    time.sleep(3)
    Option2 = friend('Andrew', 'male', '45', 'professor')
    print "Hello, my name is " + Option2.name + "\nI am a " + Option2.gender + "\nI am " + Option2.age + " years old" + "\nMy occupation is " + Option2.occupation
    time.sleep(12)
    print "\nFinally, here is the information for friend # 3:"
    time.sleep(3)
    Option3 = friend('Daniel', 'male', '30', 'unemployed')
    print "Hello, my name is " + Option3.name + "\nI am a " + Option3.gender + "\nI am " + Option3.age + " years old" + "\nMy occupation is " + Option3.occupation
    time.sleep(12)
    counter = 0
    while counter < 1: #A while loop that enables the user to choose a friend and avoids nonapplicable answers
        print "\nWhich one of these three friends would you like to choose to help you out?"
        time.sleep(5)
        answer = raw_input('Type "one" for friend # 1, "two" for friend # 2 or "three" for friend # 3: ').lower()
        if answer == "one" or answer == "1":
            counter = 1
            clear()
            return Option1 #returns friend number 1
        elif answer == "two" or answer == "2":
            counter = 1
            clear()
            return Option2 #returns friend number 2
        elif answer == "three" or answer == "3":
            counter = 1
            clear()
            return Option3 #returns friend number 3
        else:
            print "You did not choose a friend. Try again!"
            counter = 0
friend = choose_a_friend()
