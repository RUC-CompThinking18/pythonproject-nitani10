import time # Import the time module that can enable the use of a countdown
import os # Import the os module that can enable for the use of the clearing fucntion
import random # Import the random module that can enable for the use of the random function (important for the randomization of choices in the ask_questions function)
def clear(): # Creates a function that clears a line and enables new writing to go above
    os.system('cls' if os.name == 'nt' else 'clear')

print "Hello and welcome to Who Wants to be a Loseionnaire?"
time.sleep(4) # Countdown 5 seconds before preceding to the next line
clear()
print "The rules of this game are very simple."
time.sleep(3)

def objective():
    print "\nIf you reply with the correct response,\nthe level of carbon dioxide in the atmosphere will lower."
    time.sleep(5)
    print "\nYou will start with a lethal carbon dioxide ppm level of 40000."
    print "and you will work your way towards the normal/healthy 250 ppm."
    time.sleep(5)
    print "\nTake careful notes about what you learn because some day..."
    print "our earth could be heavily affected by this ever-so pressing issue!"
    time.sleep(8)
    clear()
objective()

def lifeline_explanations(): # This function prints text describing the lifelines available during the game
    print "You will have three lifelines that you can use at any time to answer the questions."
    time.sleep(5)
    print '\nThe ask the audience lifeline will provide percentages of likelihood that the "audience" (alias the general population) would choose each option.'
    time.sleep(8)
    print "\nBeware because the top choice will not necessarily mean that it is the correct response!"
    time.sleep(8)
    print '\nThe choose a friend lifeline will provide the top choice that the "friend" believes is the correct response.'
    time.sleep(8)
    print '\nYou will get an opportunity at the start of the game to select a "friend" based on three available options with varying levels of knowledge and expertise.'
    time.sleep(10)
    print "\nChoose your friend wisely because their top choice will not guarantee that you will have chosen the correct response!"
    time.sleep(8)
    print "\nFinally, the 50/50 lifeline will narrow the options available to two: one correct and one incorrect response."
    time.sleep(8)
    clear()
lifeline_explanations()

def repeat_rules(): # This function asks the user if they wish to hear again about the lifelines available during the duration of the game
    print "Would you like to hear again about the objective or the lifelines of this game?"
    answer = raw_input('Type "one" for objective, "two" for lifelines or "zero" for neither and press enter: ').lower()
    clear()
    if answer == "one" or answer == "1":
        print "You selected one which will repeat the objective section for you."
        print "Is this correct?"
        answer = raw_input('Type "yes" to repeat the objective or any key to return to the previous menu and press enter: ').lower()
        if answer == "yes" or answer == "y":
            time.sleep(2)
            clear()
            print "Objectives:" + "\n"
            objective()
            repeat_rules()
        else:
            clear()
            print "It seems that you did not mean to make this selection."
            time.sleep(3)
            print "\nThe program will now redirect you to the previous menu.\n"
            time.sleep(2)
            clear()
            repeat_rules()
    elif answer == "two" or answer == "2":
        print "You selected two which will repeat the lifeline section for you."
        print "Is this correct?"
        answer = raw_input('Type "yes" to repeat the lifelines or any key to return to the previous menu and press enter: ').lower()
        if answer == "yes" or answer == "y":
            time.sleep(2)
            clear()
            print "lifelines: " + "\n"
            lifeline_explanations()
            repeat_rules()
        else:
            clear()
            print "It seems that you did not mean to make this selection."
            time.sleep(3)
            print "\nThe program will now redirect you to the previous menu.\n"
            time.sleep(2)
            clear()
            repeat_rules()
    elif answer == "zero" or answer == "0":
        print "You selected zero indicating that you do not want to repeat the rules."
        print "Is this correct?"
        answer = raw_input('Type "yes" to proceed to the next section or any key to return to the previous menu and press enter: ').lower()
        if answer == "yes" or answer == "y":
            time.sleep(2)
            print "okay, we can now proceed onto the choose a friend lifeline portion of this game!\n"
            clear()
        else:
            clear()
            print "It seems that you did not mean to make this selection."
            time.sleep(3)
            print "\nThe program will now redirect you to the previous option menu.\n"
            time.sleep(2)
            clear()
            repeat_rules()
    else:
        clear()
        print "You didn't write one, two, or zero. Try again!"
        time.sleep(3)
        clear()
        repeat_rules()
repeat_rules()

class friend(): # Initiate a class that takes 4 commands - "name, gender, age and occupation"
    def __init__(self, name, gender, age , occupation):
        self.name = name
        self.gender = gender
        self.age = age
        self.occupation = occupation

def choose_a_friend(): # Tells the user the information about each friend choice and enables user to choose the friend
    print "You will now be able to choose a friend that can help you narrow down one of the questions."
    time.sleep(5)
    print "\nRemmember that choosing the right friend can save you from making the wrong and environmentally unsound judgement!"
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
    while counter < 1: # A while loop that enables the user to choose a friend and avoids nonapplicable answers
        print "\nWhich one of these three friends would you like to choose to help you out?"
        time.sleep(2)
        answer = raw_input('\nType "one" for friend # 1, "two" for friend # 2 or "three" for friend # 3 and press enter: ').lower()
        if answer == "one" or answer == "1":
            counter = 1
            clear()
            return Option1 # Returns friend number 1
        elif answer == "two" or answer == "2":
            counter = 1
            clear()
            return Option2 # Returns friend number 2
        elif answer == "three" or answer == "3":
            counter = 1
            clear()
            return Option3 # Returns friend number 3
        else:
            print "\nYou did not choose a friend. Try again!"
            time.sleep(2)
            clear()
            print "Friend # 1: \n" + "Hello, my name is " + Option1.name + "\nI am a " + Option1.gender + "\nI am " + Option1.age + " years old" + "\nMy occupation is " + Option1.occupation
            print "\nFriend # 2: \n" + "Hello, my name is " + Option2.name + "\nI am a " + Option2.gender + "\nI am " + Option2.age + " years old" + "\nMy occupation is " + Option2.occupation
            print "\nFriend # 3: \n" + "Hello, my name is " + Option3.name + "\nI am a " + Option3.gender + "\nI am " + Option3.age + " years old" + "\nMy occupation is " + Option3.occupation
            counter = 0
friend = choose_a_friend()


class questions(): # Initiate a class that takes 5 commands - "question_asked, top_choice, second_choice , third_choice, worst_choice"
# The level of choices is strictly important for the ask the audience lifeline
    def __init__(self, question_asked, top_choice, second_choice , third_choice, worst_choice):
        self.question_asked = question_asked
        self.top_choice = top_choice
        self.second_choice = second_choice
        self.third_choice = third_choice
        self.worst_choice = worst_choice

# Below are initialized questions and their corresponding response sets
question1 = questions('Harmful human activity causes which of the following environmental issues to occur?', 'Extinction of species and habitats', 'Driving related casualties', 'Conservation of forests', 'Revival of species and habitats')
question2 = questions('Which of the following is one of the biggest health risks in the world?', 'Dirty water', 'Polar caps', 'Fatty foods','Lack of exercise')
question3 = questions('How does fossil fuel consumption lead to global warming and climate change?', 'It results in emission of Greenhouse gases', 'It utilizes fires which increase the temperature and hence heat of the atmosphere', 'This is a trick question! Fossil fuel consumption does not lead to global warming and climate change', 'This is a trick question! Fossil fuel consumption helps with global warming and climate change issues')
question4 = questions('Which of the following are not caused by pollutants?', 'Deforestation', 'Lack of fresh air', 'Respiratory diseases like Asthma and cardiac-vascular problems', 'Harmful environmental effects')
question5 = questions('Which agricultural practices significantly intensify environmental issues?', 'The use of chemical fertilizer, pesticides and insecticides', 'Raising livestock', 'Field plowing', 'Planting trees')
question6 = questions('Which pair of sources account for the most amount of pollutants?', 'Industry and motor vehicles', 'Volcanoes and fires', 'Cigarettes and other smoking mechanisms', 'Electricity and household cleaning products')
question7 = questions('What is a consequence of increased atmospheric temperatures?', 'The spread of certain infectious diseases like Dengue', 'Colder winter months and warmer summer months', 'Plant perspiration', 'Human perspiration')
question8 = questions('Which of the following can be caused by global warming?', 'Flash floods', 'Ocean acidification', 'Loss of oxygen in the atmosphere', 'Pollution')
question9 = questions('Which of the following is not one of the harmful effects of climate change?', 'Acid rain', 'Occurrences of new diseases', 'Changes in seasons', 'Changes in weather')
question10 = questions('What can humans do to increase the amount of clean, potable water?', 'Desalinization', 'Create more water wells', 'This is a trick question! We cannot increase the amount of clean, portable water', 'Scientifically produce clean, potable water in labs')
question11 = questions('How do climate change and global warming relate?', 'A rise in global warming causes climate change', 'Climate change causes global warming', 'Climate change causes global warming and global warming causes climate change', 'Climate change and global warming do not relate')
question12 = questions('What is the size of land comparable to the amount of tree cover that is lost yearly?', 'The country of Panama', 'The state of New Jersey', 'The country of Israel', 'The state of Hawaii')
question13 = questions('What causes ocean acidification?', 'Excessive production of CO2', 'Acid rain', 'Climate change', 'Fossil fuel consumption')
question14 = questions('Which chemicals are found in acid rain?', 'Sulfur dioxide and nitrogen oxides', 'Sodium hydroxide and acetic acid', 'Carbon dioxide and acetonitrile', 'Benzene and sodium azide')
print "Now we can move on to the questions"
time.sleep(2)

question_list = [question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11, question12, question13, question14]

def ask_questions(question_number):
    question_option_list = [question_list[question_number].worst_choice, question_list[question_number].top_choice, question_list[question_number].third_choice, question_list[question_number].second_choice]
    print question_list[question_number].question_asked
    worst_choice = question_list[question_number].worst_choice
    top_choice = question_list[question_number].top_choice
    third_choice = question_list[question_number].third_choice
    second_choice = question_list[question_number].second_choice
    answer1 = question_option_list.pop(random.randrange(len(question_option_list)))
    answer2 = question_option_list.pop(random.randrange(len(question_option_list)))
    answer3 = question_option_list.pop(random.randrange(len(question_option_list)))
    answer4 = question_option_list.pop(random.randrange(len(question_option_list)))
    print "a) " + str(answer1)
    print "b) " + str(answer2)
    print "c) " + str(answer3)
    print "d) " + str(answer4)
    # The following lines account for the randomized order of the choice options in the game_loop function
    # This is essential for both the ask the audience lifeline and the classification of right/wrong questions
    if answer1 == top_choice and answer2 == second_choice and answer3 == third_choice and answer4 == worst_choice:
        return "a", top_choice, "b", second_choice, "c", third_choice, "d", worst_choice
    if answer1 == top_choice and answer2 == second_choice and answer3 == worst_choice and answer4 == third_choice:
        return "a", top_choice, "b", second_choice, "d", third_choice, "c", worst_choice
    if answer1 == top_choice and answer2 == third_choice and answer3 == second_choice and answer4 == worst_choice:
        return "a", top_choice, "c", second_choice, "b", third_choice, "d", worst_choice
    if answer1 == top_choice and answer2 == third_choice and answer3 == worst_choice and answer4 == second_choice:
        return "a", top_choice, "d", second_choice, "b", third_choice, "c", worst_choice
    if answer1 == top_choice and answer2 == worst_choice and answer3 == third_choice and answer4 == second_choice:
        return "a", top_choice, "d", second_choice, "c", third_choice, "b", worst_choice
    if answer1 == top_choice and answer2 == worst_choice and answer3 == second_choice and answer4 == third_choice:
        return "a", top_choice, "c", second_choice, "d", third_choice, "b", worst_choice
    if answer1 == second_choice and answer2 == top_choice and answer3 == third_choice and answer4 == worst_choice:
        return "b", top_choice, "a", second_choice, "c", third_choice, "d", worst_choice
    if answer1 == second_choice and answer2 == top_choice and answer3 == worst_choice and answer4 == third_choice:
        return "b", top_choice, "a", second_choice, "d", third_choice, "c", worst_choice
    if answer1 == second_choice and answer2 == third_choice and answer3 == top_choice and answer4 == worst_choice:
        return "c", top_choice, "a", second_choice, "b", third_choice, "d", worst_choice
    if answer1 == second_choice and answer2 == third_choice and answer3 == worst_choice and answer4 == top_choice:
        return "d", top_choice, "a", second_choice, "b", third_choice, "c", worst_choice
    if answer1 == second_choice and answer2 == worst_choice and answer3 == third_choice and answer4 == top_choice:
        return "d", top_choice, "a", second_choice, "c", third_choice, "b", worst_choice
    if answer1 == second_choice and answer2 == worst_choice and answer3 == top_choice and answer4 == third_choice:
        return "c", top_choice, "a", second_choice, "d", third_choice, "b", worst_choice
    if answer1 == third_choice and answer2 == second_choice and answer3 == top_choice and answer4 == worst_choice:
        return "c", top_choice, "b", second_choice, "a", third_choice, "d", worst_choice
    if answer1 == third_choice and answer2 == second_choice and answer3 == worst_choice and answer4 == top_choice:
        return "d", top_choice, "b", second_choice, "a", third_choice, "c", worst_choice
    if answer1 == third_choice and answer2 == top_choice and answer3 == second_choice and answer4 == worst_choice:
        return "b", top_choice, "c", second_choice, "a", third_choice, "d", worst_choice
    if answer1 == third_choice and answer2 == top_choice and answer3 == worst_choice and answer4 == second_choice:
        return "b", top_choice, "d", second_choice, "a", third_choice, "c", worst_choice
    if answer1 == third_choice and answer2 == worst_choice and answer3 == top_choice and answer4 == second_choice:
        return "c", top_choice, "d", second_choice, "a", third_choice, "b", worst_choice
    if answer1 == third_choice and answer2 == worst_choice and answer3 == second_choice and answer4 == top_choice:
        return "d", top_choice, "c", second_choice, "a", third_choice, "b", worst_choice
    if answer1 == worst_choice and answer2 == second_choice and answer3 == third_choice and answer4 == top_choice:
        return "d", top_choice, "b", second_choice, "c", third_choice, "a", worst_choice
    if answer1 == worst_choice and answer2 == second_choice and answer3 == top_choice and answer4 == third_choice:
        return "c", top_choice, "b", second_choice, "d", third_choice, "a", worst_choice
    if answer1 == worst_choice and answer2 == third_choice and answer3 == second_choice and answer4 == top_choice:
        return "d", top_choice, "c", second_choice, "b", third_choice, "a", worst_choice
    if answer1 == worst_choice and answer2 == third_choice and answer3 == top_choice and answer4 == second_choice:
        return "c", top_choice, "d", second_choice, "b", third_choice, "a", worst_choice
    if answer1 == worst_choice and answer2 == top_choice and answer3 == third_choice and answer4 == second_choice:
        return "b", top_choice, "d", second_choice, "c", third_choice, "a", worst_choice
    if answer1 == worst_choice and answer2 == top_choice and answer3 == second_choice and answer4 == third_choice:
        return "b", top_choice, "c", second_choice, "d", third_choice, "a", worst_choice

def game_loop():
    question_counter = 0
    while question_counter < 14:
        clear()
        print "Question " + str(question_counter + 1) + ":\n"
        choice = ask_questions(question_counter)
        answer = raw_input('\nType "a", "b", "c", or "d": ').lower()
        if answer == choice[0]:
            print "\nWould you like to lock in this answer?"
            answer = raw_input('Type "yes" to lock the answer or no to lock in a different value: ').lower()
            if answer == "yes" or answer == "y":
                question_counter +=1
            else:
                print "You will now be redirected to the original question"
                time.sleep(2)
                question_counter = question_counter
        elif answer == choice[2] or answer == choice[4] or answer == choice[6]:
            print "\nWould you like to lock in this answer?"
            answer = raw_input('Type "yes" to lock the answer or no to lock in a different value: ').lower()
            if answer == "yes" or answer == "y":
                print "\nYou did not choose the correct answer"
                time.sleep(1)
                print "The correct response was: " + str(choice[1]).lower()
                question_counter = 15
            else:
                print "You will now be redirected to the original question"
                time.sleep(2)
                question_counter = question_counter
        else:
            print "You did not choose a valid reponse"
            time.sleep(2)
            print "You will now be redirected to the original question"
            time.sleep(2)
            question_counter = question_counter
        if question_counter == 14: #If a person answers all 14 questions correctly, the following occurs
            print "Congrats! You answered all of the questions correctly"
            time.sleep(2)
            print "You might have realized that the atm level is still at an unhealthy level"
            time.sleep(2)
            print "This is because it is important to realize that it's not just about knowing these environmentally sound facts...."
            time.sleep(2)
            print "You must inform others and find beneficial ways in which to help save the environment"

game_loop()
