# -*- coding: utf-8 -*-
import time # Import the time module that can enable the use of a countdown
import os # Import the os module that can enable for the use of the clearing fucntion
import random # Import the random module that can enable for the use of the random function (important for the randomization of choices in the ask_questions function)
import threading # Import the threading module that can enable for the use of the Timer method
import collections # Import the collections module that can enable for the use of the namedtuple method

def clear(): # Creates a function that clears a line and enables new writing to go above. This will later be important for the threading functionality which requires the calling of a function.
    os.system('cls' if os.name == 'nt' else 'clear')

def exit(): # Creates a function that enables the program to terminate
    os._exit(0)

print "Hello and welcome to Who Wants to be a Loseionnaire?"
#time.sleep(4) # Countdown 5 seconds before preceding to the next line
clear()
print "The rules of this game are very simple."
#time.sleep(3)

def objective():
    print '\nYou will have up to 60 seconds to respond to each and every question in this game before the game automatically exits'
    print "\nIf you reply with the correct response,\nthe level of carbon dioxide in the atmosphere will lower."
    #time.sleep(5)
    print "\nYou will start with a lethal carbon dioxide ppm level of 65000."
    print "and you will work your way towards the normal/healthy 250 ppm."
    print "\nFor a more detailed explanation of the CO2 ppm levels, please visit the README file"
    #time.sleep(8)
    print "\nTake careful notes about what you learn because some day..."
    print "our earth could be heavily affected by this ever-so pressing issue!"
    #time.sleep(8)
    clear()
objective()

def lifeline_explanations(): # This function prints text describing the lifelines available during the game
    print "You will have three lifelines that you can use at any time to answer the questions."
    #time.sleep(5)
    print '\nThe ask the audience lifeline will provide percentages of likelihood that the "audience" (alias the general population) would choose each option.'
    #time.sleep(8)
    print "\nBeware because the top choice will not necessarily mean that it is the correct response!"
    #time.sleep(8)
    print '\nThe choose a friend lifeline will provide the top choice that the "friend" believes is the correct response.'
    #time.sleep(8)
    print '\nYou will get an opportunity at the start of the game to select a "friend" based on three available options with varying levels of knowledge and expertise.'
    #time.sleep(10)
    print "\nChoose your friend wisely because their top choice will not guarantee that you will have chosen the correct response!"
    #time.sleep(8)
    print "\nFinally, the 50/50 lifeline will narrow the options available to two: one correct and one incorrect response."
    #time.sleep(8)
    clear()
lifeline_explanations()

def repeat_rules(): # This function asks the user if they wish to hear again about the lifelines available during the duration of the game
    # The following are 4 thread arguments which call the exit function after 60 seconds if no user input is provided. Since a thread can only be started once within a function, it was essential to create 4 separate threads.
    timer = threading.Timer(60, exit)
    timer2 = threading.Timer(60, exit)
    timer3 = threading.Timer(60, exit)
    timer4 = threading.Timer(60, exit)
    print "Would you like to hear again about the objective or the lifelines of this game?"
    timer.start() # This starts the first thread
    answer = raw_input('Type "one" for objective, "two" for lifelines or "zero" for neither and press enter: ').lower()
    clear()
    if answer == "one" or answer == "1":
        timer.cancel() # This stops the first thread
        print "You selected one which will repeat the objective section for you."
        print "Is this correct?"
        timer2.start()
        answer = raw_input('Type "yes" to repeat the objective or any key to return to the previous menu and press enter: ').lower()
        if answer == "yes" or answer == "y":
            timer2.cancel()
            #time.sleep(2)
            clear()
            print "Objectives:" + "\n"
            objective()
            repeat_rules()
        else:
            timer2.cancel()
            clear()
            print "It seems that you did not mean to make this selection."
            #time.sleep(3)
            print "\nThe program will now redirect you to the previous menu.\n"
            #time.sleep(2)
            clear()
            repeat_rules()
    elif answer == "two" or answer == "2":
        timer.cancel()
        print "You selected two which will repeat the lifeline section for you."
        print "Is this correct?"
        timer3.start()
        answer = raw_input('Type "yes" to repeat the lifelines or any key to return to the previous menu and press enter: ').lower()
        if answer == "yes" or answer == "y":
            timer3.cancel()
            #time.sleep(2)
            clear()
            print "lifelines: " + "\n"
            lifeline_explanations()
            repeat_rules()
        else:
            timer3.cancel()
            clear()
            print "It seems that you did not mean to make this selection."
            #time.sleep(3)
            print "\nThe program will now redirect you to the previous menu.\n"
            #time.sleep(2)
            clear()
            repeat_rules()
    elif answer == "zero" or answer == "0":
        timer.cancel()
        print "You selected zero indicating that you do not want to repeat the rules."
        print "Is this correct?"
        timer4.start()
        answer = raw_input('Type "yes" to proceed to the next section or any key to return to the previous menu and press enter: ').lower()
        if answer == "yes" or answer == "y":
            timer4.cancel()
            #time.sleep(2)
            print "okay, we can now proceed onto the choose a friend lifeline portion of this game!\n"
            clear()
        else:
            timer4.cancel()
            clear()
            print "It seems that you did not mean to make this selection."
            #time.sleep(3)
            print "\nThe program will now redirect you to the previous option menu.\n"
            #time.sleep(2)
            clear()
            repeat_rules()
    else:
        timer.cancel()
        clear()
        print "You didn't write one, two, or zero. Try again!"
        #time.sleep(3)
        clear()
        repeat_rules()
repeat_rules()

Friend = collections.namedtuple('Friend', 'name gender age occupation') # Initiate a tuple that is later used to initiate the friends in the choose_a_friend function

def friend_info_randomizer(): # This function returns randomized gender, age and names corresponding with the genders for the three friend options. Please visit the README file for the sources of names and occupations used in this function.
    gender = random.choice(['female', 'male']) # Randomizes gender of friend
    if gender == 'male': # Randomizes name from a male name list if the gender is male
        name = random.choice(['Liam','Noah','William','James','Logan','Benjamin','Mason','Elijah','Oliver','Jacob','Lucas','Michael','Alexander','Ethan','Daniel','Matthew','Aiden','Henry','Joseph','Jackson','Samuel','Sebastian','David','Carter','Wyatt','Jayden','John','Owen','Dylan','Luke','Gabriel','Anthony','Isaac','Grayson','Jack','Julian','Levi','Christopher','Joshua','Andrew','Lincoln','Mateo','Ryan','Jaxon','Nathan','Aaron','Isaiah','Thomas','Charles','Caleb','Josiah','Christian','Hunter','Eli','Jonathan','Connor','Landon','Adrian','Asher','Cameron','Leo','Theodore','Jeremiah','Hudson','Robert','Easton','Nolan','Nicholas','Ezra','Colton','Angel','Brayden','Jordan','Dominic','Austin','Ian','Adam','Elias','Jaxson','Greyson','Jose','Ezekiel','Carson','Evan','Maverick','Bryson','Jace','Cooper','Xavier','Parker','Roman','Jason','Santiago','Chase','Sawyer','Gavin','Leonardo','Kayden','Ayden','Jameson','Kevin','Bentley','Zachary','Everett','Axel','Tyler','Micah','Vincent','Weston','Miles','Wesley','Nathaniel','Harrison','Brandon','Cole','Declan','Luis','Braxton','Damian','Silas','Tristan','Ryder','Bennett','George','Emmett','Justin','Kai','Max','Diego','Luca','Ryker','Carlos','Maxwell','Kingston','Ivan','Maddox','Juan','Ashton','Jayce','Rowan','Kaiden','Giovanni','Eric','Jesus','Calvin','Abel','King','Camden','Amir','Blake','Alex','Brody','Malachi','Emmanuel','Jonah','Beau','Jude','Antonio','Alan','Elliott','Elliot','Waylon','Xander','Timothy','Victor','Bryce','Finn','Brantley','Edward','Abraham','Patrick','Grant','Karter','Hayden','Richard','Miguel','Joel','Gael','Tucker','Rhett','Avery','Steven','Graham','Kaleb','Jasper','Jesse','Matteo','Dean','Zayden','Preston','August','Oscar','Jeremy','Alejandro','Marcus','Dawson','Lorenzo','Messiah','Zion','Maximus','River','Zane','Mark','Brooks','Nicolas','Paxton','Judah','Emiliano','Kaden','Bryan','Kyle','Myles','Peter','Charlie','Kyrie','Thiago','Brian','Kenneth','Andres','Lukas','Aidan','Jax','Caden','Milo','Paul','Beckett','Brady','Colin','Omar','Bradley','Javier','Knox','Jaden','Barrett','Israel','Matias','Jorge','Zander','Derek','Josue','Cayden','Holden','Griffin','Arthur','Leon','Felix','Remington','Jake','Killian','Clayton','Sean','Adriel','Riley','Archer','Legend','Erick','Enzo','Corbin','Francisco','Dallas','Emilio','Gunner','Simon','Andre','Walter','Damien','Chance','Phoenix','Colt','Tanner','Stephen','Kameron','Tobias','Manuel','Amari','Emerson','Louis','Cody','Finley','Iker','Martin','Rafael','Nash','Beckham','Cash','Karson','Rylan','Reid','Theo','Ace','Eduardo','Spencer','Raymond','Maximiliano','Anderson','Ronan','Lane','Cristian','Titus','Travis','Jett','Ricardo','Bodhi','Gideon','Jaiden','Fernando','Mario','Conor','Keegan','Ali','Cesar','Ellis','Jayceon','Walker','Cohen','Arlo','Hector','Dante','Kyler','Garrett','Donovan','Seth','Jeffrey','Tyson','Jase','Desmond','Caiden','Gage','Atlas','Major','Devin','Edwin','Angelo','Orion','Conner','Julius','Marco','Jensen','Daxton','Peyton','Zayn','Collin','Jaylen','Dakota','Prince','Johnny','Kayson','Cruz','Hendrix','Atticus','Troy','Kane','Edgar','Sergio','Kash','Marshall','Johnathan','Romeo','Shane','Warren','Joaquin','Wade','Leonel','Trevor','Dominick','Muhammad','Erik','Odin','Quinn','Jaxton','Dalton','Nehemiah','Frank','Grady','Gregory','Andy','Solomon','Malik','Rory','Clark','Reed','Harvey','Zayne','Jay','Jared','Noel','Shawn','Fabian','Ibrahim','Adonis','Ismael','Pedro','Leland','Malakai','Malcolm','Alexis','Kason','Porter','Sullivan','Raiden','Allen','Ari','Russell','Princeton','Winston','Kendrick','Roberto','Lennox','Hayes','Finnegan','Nasir','Kade','Nico','Emanuel','Landen','Moises','Ruben','Hugo','Abram','Adan','Khalil','Zaiden','Augustus','Marcos','Philip','Phillip','Cyrus','Esteban','Braylen','Albert','Bruce','Kamden','Lawson','Jamison','Sterling','Damon','Gunnar','Kyson','Luka','Franklin','Ezequiel','Pablo','Derrick','Zachariah','Cade','Jonas','Dexter','Kolton','Remy','Hank','Tate','Trenton','Kian','Drew','Mohamed','Dax','Rocco','Bowen','Mathias','Ronald','Francis','Matthias','Milan','Maximilian','Royce','Skyler','Corey','Kasen','Drake','Gerardo','Jayson','Sage','Braylon','Benson','Moses','Alijah','Rhys','Otto','Oakley','Armando','Jaime','Nixon','Saul','Scott','Brycen','Ariel','Enrique','Donald','Chandler','Asa','Eden','Davis','Keith','Frederick','Rowen','Lawrence','Leonidas','Aden','Julio','Darius','Johan','Deacon','Cason','Danny','Nikolai','Taylor','Alec','Royal','Armani','Kieran','Luciano','Omari','Rodrigo','Arjun','Ahmed','Brendan','Cullen','Raul','Raphael','Ronin','Brock','Pierce','Alonzo','Casey','Dillon','Uriel','Dustin','Gianni','Roland','Landyn','Kobe','Dorian','Emmitt','Ryland','Apollo','Aarav','Roy','Duke','Quentin','Sam','Lewis','Tony','Uriah','Dennis','Moshe','Isaias','Braden','Quinton','Cannon','Ayaan','Mathew','Kellan','Niko','Edison','Izaiah','Jerry','Gustavo','Jamari','Marvin','Mauricio','Ahmad','Mohammad','Justice','Trey','Elian','Mohammed','Sincere','Yusuf','Arturo','Callen','Rayan','Keaton','Wilder','Mekhi','Memphis','Cayson','Conrad','Kaison','Kyree','Soren','Colby','Bryant','Lucian','Alfredo','Cassius','Marcelo','Nikolas','Brennan','Darren','Jasiah','Jimmy','Lionel','Reece','Ty','Chris','Forrest','Korbin','Tatum','Jalen','Santino','Case','Leonard','Alvin','Issac','Bo','Quincy','Mack','Samson','Rex','Alberto','Callum','Curtis','Hezekiah','Finnley','Briggs','Kamari','Zeke','Raylan','Neil','Titan','Julien','Kellen','Devon','Kylan','Roger','Axton','Carl','Douglas','Larry','Crosby','Fletcher','Makai','Nelson','Hamza','Lance','Alden','Gary','Wilson','Alessandro','Ares','Kashton','Bruno','Jakob','Stetson','Zain','Cairo','Nathanael','Byron','Harry','Harley','Mitchell','Maurice','Orlando','Kingsley','Kaysen','Sylas','Trent','Ramon','Boston','Lucca','Noe','Jagger','Reyansh','Vihaan','Randy','Thaddeus','Lennon','Kannon','Kohen','Tristen','Valentino','Maxton','Salvador','Abdiel','Langston','Rohan','Kristopher','Yosef','Rayden','Lee','Callan','Tripp','Deandre','Joe','Morgan','Dariel','Colten','Reese','Jedidiah','Ricky','Bronson','Terry','Eddie','Jefferson','Lachlan','Layne','Clay','Madden','Jamir','Tomas','Kareem','Stanley','Brayan','Amos','Kase','Kristian','Clyde','Ernesto','Tommy','Casen','Ford','Crew','Braydon','Brecken','Hassan','Axl','Boone','Leandro','Samir','Jaziel','Magnus','Abdullah','Yousef','Branson','Jadiel','Jaxen','Layton','Franco','Ben','Grey','Kelvin','Chaim','Demetrius','Blaine','Ridge','Colson','Melvin','Anakin','Aryan','Lochlan','Jon','Canaan','Dash','Zechariah','Alonso','Otis','Zaire','Marcel','Brett','Stefan','Aldo','Jeffery','Baylor','Talon','Dominik','Flynn','Carmelo','Dane','Jamal','Kole','Enoch','Graysen','Kye','Vicente','Fisher','Ray','Fox','Jamie','Rey','Zaid','Allan','Emery','Gannon','Joziah','Rodney','Juelz','Sonny','Terrance','Zyaire','Augustine','Cory','Felipe','Aron','Jacoby','Harlan','Marc','Bobby','Joey','Anson','Huxley','Marlon','Anders','Guillermo','Payton','Castiel','Damari','Shepherd','Azariah','Harold','Harper','Henrik','Houston','Kairo','Willie','Elisha','Ameer','Emory','Skylar','Sutton','Alfonso','Brentley','Toby','Blaze','Eugene','Shiloh','Wayne','Darian','Gordon','London','Bodie','Jordy','Jermaine','Denver','Gerald','Merrick','Musa','Vincenzo','Kody','Yahir','Brodie','Trace','Darwin','Tadeo','Bentlee','Billy','Hugh','Reginald','Vance','Westin','Cain','Arian','Dayton','Javion','Terrence','Brysen','Jaxxon','Thatcher','Landry','Rene','Westley','Miller','Alvaro','Cristiano','Eliseo','Ephraim','Adrien','Jerome','Khalid','Aydin','Mayson','Alfred','Duncan','Junior','Kendall','Zavier','Koda','Maison','Caspian','Maxim','Kace','Zackary','Rudy','Coleman','Keagan','Kolten','Maximo','Dario','Davion','Kalel','Briar','Jairo','Misael','Rogelio','Terrell','Heath','Micheal','Wesson','Aaden','Brixton','Draven','Xzavier','Darrell','Keanu','Ronnie','Konnor','Will','Dangelo','Frankie','Kamryn','Salvatore','Santana','Shaun','Coen','Leighton','Mustafa','Reuben','Ayan','Blaise','Dimitri','Keenan','Van','Achilles','Channing','Ishaan','Wells','Benton','Lamar','Nova','Yahya','Dilan','Gibson','Camdyn','Ulises','Alexzander','Valentin','Shepard','Alistair','Eason','Kaiser','Leroy','Zayd','Camilo','Markus','Foster','Davian','Dwayne','Jabari','Judson','Koa','Yehuda','Lyric','Tristian','Agustin','Bridger','Vivaan','Brayson','Emmet','Marley','Mike','Nickolas','Kenny','Leif','Bjorn','Ignacio','Rocky','Chad','Gatlin','Greysen','Kyng','Randall','Reign','Vaughn','Jessie','Louie','Shmuel','Zahir','Ernest','Javon','Khari','Reagan','Avi','Ira','Ledger','Simeon','Yadiel','Maddux','Seamus','Jad','Jeremias','Kylen','Rashad','Santos','Cedric','Craig','Dominique','Gianluca','Jovanni','Bishop','Brenden','Anton','Camron','Giancarlo','Lyle','Alaric','Decker','Eliezer','Ramiro','Yisroel','Howard','Jaxx'])
    else: # Randomizes name from a male name list if the gender is female
        name = random.choice(['Emma','Olivia','Sophia','Isabella','Ava','Mia','Emily','Abigail','Madison','Charlotte','Harper','Sofia','Avery','Elizabeth','Amelia','Evelyn','Ella','Chloe','Victoria','Aubrey','Grace','Zoey','Natalie','Addison','Lillian','Brooklyn','Lily','Hannah','Layla','Scarlett','Aria','Zoe','Samantha','Anna','Leah','Audrey','Ariana','Allison','Savannah','Arianna','Camila','Penelope','Gabriella','Claire','Aaliyah','Sadie','Riley','Skylar','Nora','Sarah','Hailey','Kaylee','Paisley','Kennedy','Ellie','Peyton','Annabelle','Caroline','Madelyn','Serenity','Aubree','Lucy','Alexa','Alexis','Nevaeh','Stella','Violet','Genesis','Mackenzie','Bella','Autumn','Mila','Kylie','Maya','Piper','Alyssa','Taylor','Eleanor','Melanie','Naomi','Faith','Eva','Katherine','Lydia','Brianna','Julia','Ashley','Khloe','Madeline','Ruby','Sophie','Alexandra','London','Lauren','Gianna','Isabelle','Alice','Vivian','Hadley','Jasmine','Morgan','Kayla','Cora','Bailey','Kimberly','Reagan','Hazel','Clara','Sydney','Trinity','Natalia','Valentina','Rylee','Jocelyn','Maria','Aurora','Eliana','Brielle','Liliana','Mary','Elena','Molly','Makayla','Lilly','Andrea','Quinn','Jordyn','Adalynn','Nicole','Delilah','Kendall','Kinsley','Ariel','Payton','Paige','Mariah','Brooke','Willow','Jade','Lyla','Mya','Ximena','Luna','Isabel','Mckenzie','Ivy','Josephine','Amy','Laila','Isla','Eden','Adalyn','Angelina','Londyn','Rachel','Melody','Juliana','Kaitlyn','Brooklynn','Destiny','Emery','Gracie','Norah','Emilia','Reese','Elise','Sara','Aliyah','Margaret','Catherine','Vanessa','Katelyn','Gabrielle','Arabella','Valeria','Valerie','Adriana','Everly','Jessica','Daisy','Makenzie','Summer','Lila','Rebecca','Julianna','Callie','Michelle','Ryleigh','Presley','Alaina','Angela','Alina','Harmony','Rose','Athena','Emerson','Adelyn','Alana','Hayden','Izabella','Cali','Marley','Esther','Fiona','Stephanie','Cecilia','Kate','Kinley','Jayla','Genevieve','Alexandria','Eliza','Kylee','Alivia','Giselle','Arya','Alayna','Leilani','Adeline','Jennifer','Tessa','Ana','Finley','Melissa','Daniela','Aniyah','Daleyza','Keira','Charlie','Lucia','Hope','Gabriela','Mckenna','Brynlee','Parker','Lola','Amaya','Miranda','Maggie','Anastasia','Leila','Lexi','Georgia','Kenzie','Iris','Jacqueline','Jordan','Cassidy','Vivienne','Camille','Noelle','Adrianna','Teagan','Josie','Juliette','Annabella','Allie','Juliet','Kendra','Sienna','Brynn','Kali','Maci','Danielle','Haley','Jenna','Raelynn','Delaney','Paris','Alexia','Lyric','Gemma','Lilliana','Chelsea','Angel','Evangeline','Ayla','Kayleigh','Lena','Katie','Elaina','Olive','Madeleine','Makenna','Dakota','Elsa','Nova','Nadia','Alison','Kaydence','Journey','Jada','Kathryn','Shelby','Nina','Elliana','Diana','Phoebe','Alessandra','Eloise','Nyla','Skyler','Madilyn','Adelynn','Miriam','Ashlyn','Amiyah','Megan','Amber','Rosalie','Annie','Lilah','Charlee','Amanda','Ruth','Adelaide','June','Laura','Daniella','Mikayla','Raegan','Jane','Ashlynn','Kelsey','Erin','Christina','Joanna','Fatima','Allyson','Talia','Mariana','Sabrina','Haven','Ainsley','Cadence','Elsie','Leslie','Heaven','Arielle','Maddison','Alicia','Briella','Lucille','Sawyer','Malia','Selena','Heidi','Kyleigh','Harley','Kira','Lana','Sierra','Kiara','Paislee','Alondra','Daphne','Carly','Jaylah','Kyla','Bianca','Baylee','Cheyenne','Macy','Camilla','Catalina','Gia','Vera','Skye','Aylin','Sloane','Myla','Yaretzi','Giuliana','Macie','Veronica','Esmeralda','Lia','Averie','Addyson','Kamryn','Mckinley','Ada','Carmen','Mallory','Jillian','Ariella','Rylie','Sage','Abby','Scarlet','Logan','Tatum','Bethany','Dylan','Elle','Jazmin','Aspen','Camryn','Malaysia','Haylee','Nayeli','Gracelyn','Kamila','Helen','Marilyn','April','Carolina','Amina','Julie','Raelyn','Blakely','Rowan','Angelique','Miracle','Emely','Jayleen','Kennedi','Amira','Briana','Gwendolyn','Justice','Zara','Aleah','Itzel','Bristol','Francesca','Emersyn','Aubrie','Karina','Nylah','Kelly','Anaya','Maliyah','Evelynn','Ember','Melany','Angelica','Jimena','Madelynn','Kassidy','Tiffany','Kara','Jazmine','Jayda','Dahlia','Alejandra','Sarai','Annabel','Holly','Janelle','Braelyn','Gracelynn','River','Viviana','Serena','Brittany','Annalise','Brinley','Madisyn','Eve','Cataleya','Joy','Caitlyn','Anabelle','Emmalyn','Journee','Celeste','Brylee','Luciana','Marlee','Savanna','Anya','Marissa','Jazlyn','Zuri','Kailey','Crystal','Michaela','Lorelei','Guadalupe','Madilynn','Maeve','Hanna','Priscilla','Kyra','Lacey','Nia','Charley','Jamie','Juniper','Cynthia','Karen','Sylvia','Phoenix','Aleena','Caitlin','Felicity','Elisa','Julissa','Rebekah','Evie','Helena','Imani','Karla','Millie','Lilian','Raven','Harlow','Leia','Ryan','Kailyn','Lillie','Amara','Kadence','Lauryn','Cassandra','Kaylie','Madalyn','Anika','Hayley','Bria','Colette','Henley','Amari','Regina','Alanna','Azalea','Fernanda','Jaliyah','Anabella','Adelina','Lilyana','Skyla','Addisyn','Zariah','Bridget','Braylee','Monica','Jayden','Leighton','Gloria','Johanna','Addilyn','Danna','Selah','Aryanna','Kaylin','Aniya','Willa','Angie','Kaia','Kaliyah','Anne','Tiana','Charleigh','Winter','Danica','Alayah','Aisha','Bailee','Kenley','Aileen','Lexie','Janiyah','Braelynn','Liberty','Katelynn','Mariam','Sasha','Lindsey','Montserrat','Cecelia','Mikaela','Kaelyn','Rosemary','Annika','Tatiana','Cameron','Marie','Dallas','Virginia','Liana','Matilda','Freya','Lainey','Hallie','Jessie','Audrina','Blake','Hattie','Monserrat','Kiera','Laylah','Greta','Alyson','Emilee','Maryam','Melina','Dayana','Jaelynn','Beatrice','Frances','Elisabeth','Saige','Kensley','Meredith','Aranza','Rosa','Shiloh','Charli','Elyse','Alani','Mira','Lylah','Linda','Whitney','Alena','Jaycee','Joselyn','Ansley','Kynlee','Miah','Tenley','Breanna','Emelia','Maia','Edith','Pearl','Anahi','Coraline','Samara','Demi','Chanel','Kimber','Lilith','Malaya','Jemma','Myra','Bryanna','Laney','Jaelyn','Kaylynn','Kallie','Natasha','Nathalie','Perla','Amani','Lilianna','Madalynn','Blair','Elianna','Karsyn','Lindsay','Elaine','Dulce','Ellen','Erica','Maisie','Renata','Kiley','Marina','Remi','Emmy','Ivanna','Amirah','Livia','Amelie','Irene','Mabel','Milan','Armani','Cara','Ciara','Kathleen','Jaylynn','Caylee','Lea','Erika','Paola','Alma','Courtney','Mae','Kassandra','Maleah','Remington','Leyla','Mina','Ariah','Christine','Jasmin','Kora','Chaya','Karlee','Lailah','Mara','Jaylee','Raquel','Siena','Lennon','Desiree','Hadassah','Kenya','Aliana','Wren','Amiya','Isis','Zaniyah','Avah','Amia','Cindy','Eileen','Kayden','Madyson','Celine','Aryana','Everleigh','Isabela','Reyna','Teresa','Jolene','Marjorie','Myah','Clare','Claudia','Leanna','Noemi','Corinne','Simone','Alia','Brenda','Dorothy','Emilie','Elin','Tori','Martha','Ally','Arely','Leona','Patricia','Sky','Thalia','Carolyn','Emory','Nataly','Paityn','Shayla','Averi','Jazlynn','Margot','Lisa','Lizbeth','Nancy','Deborah','Ivory','Khaleesi','Elliot','Meadow','Yareli','Farrah','Milania','Janessa','Milana','Zoie','Adele','Clarissa','Hunter','Lina','Oakley','Sariah','Emmalynn','Galilea','Hailee','Halle','Sutton','Giana','Thea','Denise','Naya','Kristina','Liv','Nathaly','Wendy','Aubrielle','Brenna','Carter','Danika','Monroe','Celia','Dana','Jolie','Taliyah','Casey','Miley','Yamileth','Jaylene','Saylor','Joyce','Milena','Zariyah','Sandra','Ariadne','Aviana','Mollie','Cherish','Alaya','Asia','Nola','Penny','Dixie','Marisol','Adrienne','Rylan','Kori','Kristen','Aimee','Esme','Laurel','Aliza','Roselyn','Sloan','Lorelai','Jenny','Katalina','Lara','Amya','Ayleen','Aubri','Ariya','Carlee','Iliana','Magnolia','Aurelia','Elliott','Evalyn','Natalee','Rayna','Heather','Collins','Estrella','Rory','Hana','Kenna','Jordynn','Rosie','Aiyana','America','Angeline','Janiya','Jessa','Tegan','Susan','Emmalee','Taryn','Temperance','Alissa','Kenia','Abbigail','Briley','Kailee','Zaria','Chana','Lillianna','Barbara','Carla','Aliya','Bonnie','Keyla','Marianna','Paloma','Jewel','Joslyn','Saniyah','Audriana','Giovanna','Hadleigh','Mckayla','Jaida','Salma','Sharon','Emmaline','Kimora','Wynter','Avianna','Amalia','Karlie','Kaidence','Kairi','Libby','Sherlyn','Diamond','Holland','Zendaya','Mariyah','Zainab','Alisha','Ayanna','Ellison','Harlee','Lilyanna','Bryleigh','Julianne','Kaleigh','Miya','Yasmin','Anniston','Estelle','Emmeline','Faye','Kiana','Anabel','Zion','Tara','Astrid','Emerie','Sidney','Zahra','Jaylin','Kinslee','Tabitha','Aubriella','Addilynn','Alyvia','Hadlee','Ingrid','Lilia','Macey','Azaria','Kaitlynn','Neriah','Annabell','Ariyah','Janae','Kaiya','Reina','Rivka','Alisa','Marleigh','Alisson','Maliah','Mercy','Noa','Scarlette','Clementine','Frida','Ann','Sonia','Alannah','Avalynn','Dalia','Ayva','Stevie','Judith','Paulina','Azariah','Estella','Remy','Gwen','Mattie','Milani','Raina','Julieta','Renee','Lesly','Abrielle','Bryn','Carlie','Riya','Karter','Abril','Aubrianna','Jocelynn','Kylah','Louisa','Pyper','Antonia','Magdalena','Moriah','Ryann','Tamia','Kailani','Landry','Aya','Ireland','Mercedes','Rosalyn','Alaysia','Annalee','Patience','Aanya','Paula','Samiyah','Yaritza','Cordelia','Micah','Nala','Belen','Cambria','Natalya','Kaelynn','Kai'])
    age = random.randrange(25,96) # Randomizes age of friend with the range of 25 to 95
    job = random.choice(['actor','air steward','animator','architect','assistant','author','baker','biologist','builder','butcher','career counselor','caretaker','chef','civil servant','clerk','comic book writer','company director','computer programmer','cook','decorator','dentist','designer','diplomat','director','doctor','economist','editor','electrician','engineer','executive','farmer','film director','fisherman','fishmonger','flight attendant','garbage man','geologist','hairdresser','head teacher','jeweler','journalist','judge','juggler','lawyer','lecturer','lexicographer','library assistant','magician','makeup artist','manager','miner','musician','nurse','optician','painter','personal assistant','photographer','pilot','plumber','police officer','politician','porter','printer','prison officer / warder','professional gambler','puppeteer','receptionist','sailor','salesperson','scientist','secretary','shop assistant','sign language Interpreter','singer','soldier','solicitor','surgeon','tailor','teacher','telephone operator','telephonist','translator','travel agent','trucker','TV cameraman','TV presenter','vet','waiter','web designer','writer','unemployed'])
    if age > 70: # Provides retired status for friend if they are over the age of 70
        occupation = 'retired ' + job
    else:
        occupation = job
    return name, gender, age, occupation

# The following three lines call and store the friend_info_randomizer function three times, provided that the names, ages and occupations are all different and there is at least one of every gender.
while True:
    friend_info = friend_info_randomizer()
    friend2_info = friend_info_randomizer()
    friend3_info = friend_info_randomizer()
    if friend_info[0] != friend2_info[0] and friend_info[0] != friend3_info[0] and friend2_info[0] != friend3_info[0]:
        pass
    else:
        continue
    if friend_info[2] != friend2_info[2] and friend_info[2] != friend3_info[2] and friend2_info[2] != friend3_info[2]:
        pass
    else:
        continue
    if friend_info[3] != friend2_info[3] and friend_info[3] != friend3_info[3] and friend2_info[3] != friend3_info[3]:
        pass
    else:
        continue
    if friend_info[1] == friend2_info[1] and friend_info[1] == friend3_info[1]:
        continue
    else:
        break

def choose_a_friend(): # Tells the user the information about each friend choice and enables user to choose the friend. The gender and age are both randomized within a set range of male/female and 18 to 95 years of age.
    timer = threading.Timer(60, exit)
    print "You will now be able to choose a friend that can help you narrow down one of the questions."
    #time.sleep(5)
    print "\nRemmember that choosing the right friend can save you from making the wrong and environmentally unsound judgement!"
    #time.sleep(7)
    print "\nBelow is the information about friend # 1:"
    #time.sleep(3)
    Option1 = Friend(name = str(friend_info[0]), gender = str(friend_info[1]), age = str(friend_info[2]), occupation = str(friend_info[3]))
    print "Hello, my name is " + Option1[0] + "\nI am a " + Option1[1] + "\nI am " + Option1[2] + " years old" + "\nMy occupation is a " + Option1[3]
    #time.sleep(12)
    print "\nNext is the information about friend # 2:"
    #time.sleep(3)
    Option2 = Friend(name = str(friend2_info[0]), gender = str(friend2_info[1]), age = str(friend2_info[2]), occupation = str(friend2_info[3]))
    print "Hello, my name is " + Option2[0] + "\nI am a " + Option2[1] + "\nI am " + Option2[2] + " years old" + "\nMy occupation is a " + Option2[3]
    #time.sleep(12)
    print "\nFinally, here is the information for friend # 3:"
    #time.sleep(3)
    Option3 = Friend(name = str(friend3_info[0]), gender = str(friend3_info[1]), age = str(friend3_info[2]), occupation = str(friend3_info[3]))
    print "Hello, my name is " + Option3[0] + "\nI am a " + Option3[1] + "\nI am " + Option3[2] + " years old" + "\nMy occupation is a " + Option3[3]
    #time.sleep(12)
    while True: # A while loop that enables the user to choose a friend and avoids nonapplicable answers
        print "\nWhich one of these three friends would you like to choose to help you out?"
        #time.sleep(2)
        timer.start()
        answer = raw_input('Type "one" for friend # 1, "two" for friend # 2 or "three" for friend # 3 and press enter: ').lower()
        if answer == "one" or answer == "1":
            timer.cancel()
            clear()
            return Option1 # Returns friend number 1
        elif answer == "two" or answer == "2":
            timer.cancel()
            clear()
            return Option2 # Returns friend number 2
        elif answer == "three" or answer == "3":
            timer.cancel()
            clear()
            return Option3 # Returns friend number 3
        else:
            timer.cancel()
            print "\nYou did not choose a friend. Try again!"
            #time.sleep(2)
            clear()
            print "Friend # 1: \n" + "Name: " + Option1[0]+ "\nGender: " + Option1[1] + "\nAge: " + Option1[2] + "\nOccupation: " + Option1[3]
            print "\nFriend # 1: \n" + "Name: " + Option2[0]+ "\nGender: " + Option2[1] + "\nAge: " + Option2[2] + "\nOccupation: " + Option2[3]
            print "\nFriend # 1: \n" + "Name: " + Option3[0]+ "\nGender: " + Option3[1] + "\nAge: " + Option3[2] + "\nOccupation: " + Option3[3]
            continue

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
#time.sleep(2)

question_list = [question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11, question12, question13, question14]

def ask_questions(question_counter): # This function stores and iterates through the questions and response sets
    question_option_list = [question_list[question_counter].top_choice, question_list[question_counter].second_choice, question_list[question_counter].third_choice, question_list[question_counter].worst_choice]
    print question_list[question_counter].question_asked # Prints the question
    random_response_list = random.sample(question_option_list, len(question_option_list)) # Initiate a new randomized order for the response options and stores it in a new list
    choice_list = ["a","b","c","d"] # Initiate a list of the text-based response options. This is important for the response sets
    index_list = [random_response_list.index(question_list[question_counter].top_choice), random_response_list.index(question_list[question_counter].second_choice), random_response_list.index(question_list[question_counter].third_choice), random_response_list.index(question_list[question_counter].worst_choice)] # Initiates list of the indexex (order within list) of each available choice - top_choice, second_choice, etc.
    print "a) " + str(random_response_list[0]), "\nb) " + str(random_response_list[1]), "\nc) " + str(random_response_list[2]), "\nd) " + str(random_response_list[3]) # Prints the choice options
    return index_list, choice_list, random_response_list, question_list[question_counter].question_asked


def ppm_bank(question_counter): # This function stores and iterates through the ppm level
    ppm_list = [65000, 60000, 55000, 50000, 40000, 35000, 30000, 25000, 20000, 12000, 5000, 2500, 2000, 1800, 1000]
    return "your ppm level is " + str(ppm_list[question_counter])

def friend_lifeline(question_counter, choice): # This function randomly generates the top two options and bottom two options for the ask a friend lifeline
    top_options = random.sample([choice[2][choice[0][0]].lower(), choice[2][choice[0][1]].lower()], 2)
    bottom_options = random.sample([choice[2][choice[0][2]].lower(), choice[2][choice[0][3]].lower()], 2)
    print "Question " + str(question_counter+1) + ": \n" + str(choice[3]) + "\n" + str(choice[1][0]) + ") " + str(choice[2][0]) + "\n" + str(choice[1][1]) + ") " + str(choice[2][1]) + "\n" + str(choice[1][2]) + ") " + str(choice[2][2]) + "\n" + str(choice[1][3]) + ") " + str(choice[2][3]) + "\n"
    print str(friend[0]) + ': \n\n"Here is what I think -"'
    print '"My top choice is ' + str(top_options[0]) + '"\n"My second choice is ' + str(top_options[1]) + '"\nMy third choice is ' + str(bottom_options[0]) + '"\nMy fourth choice is ' + str(bottom_options[1]) + '"\n'

def ask_audience_lifeline(question_counter, choice): # This function generates varying percentages for the ask the audience lifeline and prints these values alongside the resposne set
    top_response_percentage = random.randrange(41,67)
    second_response_percentage = random.randrange(23,49)
    third_response_percentage = random.randrange(7,33)
    worst_response_percentage = random.randrange(1, 26)
    response_percentage_list = [top_response_percentage, second_response_percentage, third_response_percentage, worst_response_percentage]
    if sum(response_percentage_list) == 100:
        print "Question " + str(question_counter+1) + ": \n" + str(choice[3]) + "\n" + str(choice[1][0]) + ") " + str(choice[2][0]) + "\n" + str(choice[1][1]) + ") " + str(choice[2][1]) + "\n" + str(choice[1][2]) + ") " + str(choice[2][2]) + "\n" + str(choice[1][3]) + ") " + str(choice[2][3]) + "\n"
    else:
        ask_audience_lifeline(question_counter, choice)

def fifty_lifeline(question_counter, choice):
    print "Question " + str(question_counter+1) + ": \n" + str(choice[3]) + "\n" + str(choice[1][0]) + ") " + str(choice[2][0]) + "\n" + str(choice[1][1]) + ") " + str(choice[2][1]) + "\n" + str(choice[1][2]) + ") " + str(choice[2][2]) + "\n" + str(choice[1][3]) + ") " + str(choice[2][3]) + "\n"
    # The following if/else sequence will insurance that the options written are provided in alphabetical order
    if choice[0][0] < choice[0][1]:
        print "The remaining options are: \n" + choice[1][choice[0][0]] + ") " + choice[2][choice[0][0]].lower() + "\n" + choice[1][choice[0][1]] + ") " + choice[2][choice[0][1]].lower() + "\n"
    else:
        print "The remaining options are: \n" + choice[1][choice[0][1]] + ") " + choice[2][choice[0][1]].lower() + "\n" + choice[1][choice[0][0]] + ") " + choice[2][choice[0][0]].lower() + "\n"
def lifeline_use(question_counter, choice): # This function stores and calls the lifeline functions
    timer = threading.Timer(60, exit)
    timer2 = threading.Timer(60, exit)
    timer3 = threading.Timer(60, exit)
    while True:
        print "\nWould you like to use a lifeline?"
        timer.start()
        answer = raw_input('Type "yes" or "no": ').lower()
        if answer == 'yes' or answer == 'y':
            timer.cancel()
            clear()
            while True:
                print "Which lifeline would you like to use?"
                timer2.start()
                lifeline_choice = raw_input('Type "one" for the ask a friend lifeline, \nType "two" for the ask the ask the audience lifeline, \nType "three" for the 50/50 lifeline, \nType "four" if you do not want to use a lifeline\nAnswer: ').lower()
                if lifeline_choice == "one" or lifeline_choice == "1":
                    timer2.cancel()
                    clear()
                    friend_lifeline(question_counter, choice)
                    timer3.start()
                    input = raw_input('Type "a", "b", "c", or "d": ').lower()
                    return input
                    timer3.cancel()
                    break
                elif lifeline_choice == "two" or lifeline_choice == "2":
                    timer2.cancel()
                    clear()
                    ask_audience_lifeline(question_counter, choice)
                    timer3.start()
                    input = raw_input('Type "a", "b", "c", or "d": ').lower()
                    return input
                    timer3.cancel()
                    break
                elif lifeline_choice == "three" or lifeline_choice == "3":
                    timer2.cancel()
                    clear()
                    fifty_lifeline(question_counter, choice)
                    if choice[0][0] < choice[0][1]:
                        timer3.start()
                        input = raw_input('Type "' + choice[1][choice[0][0]] + '" or "' + choice[1][choice[0][1]] + '": ').lower()
                        return input
                        timer3.cancel()
                    else:
                        timer3.start()
                        input = raw_input('Type "' + choice[1][choice[0][1]] + '" or "' + choice[1][choice[0][0]] + '": ').lower()
                        return input
                        timer3.cancel()
                    break
                elif lifeline_choice == "four" or lifeline_choice == "4":
                    timer2.cancel()
                    clear()
                    print "Question " + str(question_counter+1) + ": \n" + str(choice[3]) + "\n" + str(choice[1][0]) + ") " + str(choice[2][0]) + "\n" + str(choice[1][1]) + ") " + str(choice[2][1]) + "\n" + str(choice[1][2]) + ") " + str(choice[2][2]) + "\n" + str(choice[1][3]) + ") " + str(choice[2][3]) + "\n"
                    timer3.start()
                    input = raw_input('Type "a", "b", "c", or "d": ').lower()
                    return input
                    timer3.cancel()
                    break
                else:
                    timer2.cancel()
                    continue
            break
        elif answer == 'no' or answer == 'n':
            timer.cancel()
            clear()
            print "Question " + str(question_counter+1) + ": \n" + str(choice[3]) + "\n" + str(choice[1][0]) + ") " + str(choice[2][0]) + "\n" + str(choice[1][1]) + ") " + str(choice[2][1]) + "\n" + str(choice[1][2]) + ") " + str(choice[2][2]) + "\n" + str(choice[1][3]) + ") " + str(choice[2][3]) + "\n"
            timer3.start()
            input = raw_input('Type "a", "b", "c", or "d": ').lower()
            return input
            timer3.cancel()
            break
        else:
            timer.cancel()
            continue

def game_loop(): # This function runs through the ppm_bank, the lifeline_use, and the ask_questions functions the amount of times that corresponds with whether the user provides the correct response or not
    timer4 = threading.Timer(60, exit)
    timer5 = threading.Timer(60, exit)
    question_counter = 0
    while question_counter < 14:
        clear()
        print "Question " + str(question_counter + 1) + ":"
        choice = ask_questions(question_counter)
        answer = lifeline_use(question_counter, choice)
        if answer == choice[1][choice[0][0]]: # This is the string letter choice for the correct response
            while True:
                print "\nyou chose: " + answer
                #time.sleep(2)
                print "Would you like to lock in this answer?"
                timer4.start()
                answer = raw_input('Type "yes" to lock the answer or "no" to lock in a different value: ').lower()
                if answer == "yes" or answer == "y":
                    timer4.cancel()
                    print "Your answer is correct!"
                    #time.sleep(2)
                    question_counter +=1
                    print ppm_bank(question_counter)
                    #time.sleep(3)
                    break
                elif answer == "no" or answer == "n":
                    timer4.cancel()
                    print "You will now be redirected to the original question"
                    #time.sleep(2)
                    question_counter = question_counter
                    break
                else:
                    timer4.cancel()
                    print "You did not choose a valid reponse"
                    #time.sleep(2)
                    continue
        elif answer == choice[1][choice[0][1]] or answer == choice[1][choice[0][2]] or answer == choice[1][choice[0][3]]: # These are the string letter choices for the incorrect responses
            while True:
                print "\nyou chose: " + answer
                #time.sleep(2)
                print "Would you like to lock in this answer?"
                timer5.start()
                answer = raw_input('Type "yes" to lock the answer or no to lock in a different value: ').lower()
                if answer == "yes" or answer == "y":
                    timer5.cancel()
                    print "\nYou did not choose the correct answer"
                    #time.sleep(1)
                    print "The correct response was: " + str(choice[2][choice[0][0]]).lower()
                    if question_counter < 5: # Provides the beginning ppm level if user does not reach first threshold
                        print ppm_bank(0)
                    elif question_counter > 5 and question_counter < 10: # Provides the 5th ppm level if user does not reach second threshold
                        print ppm_bank(4)
                    elif question_counter > 10 and question_counter < 14: # Provides the 10th ppm level if user does not answer all questions correctly
                        print ppm_bank(9)
                    question_counter = 15
                    break
                elif answer == "no" or answer == "n":
                    timer5.cancel()
                    print "You will now be redirected to the original question"
                    #time.sleep(2)
                    question_counter = question_counter
                    break
                else:
                    timer5.cancel()
                    print "You did not choose a valid reponse"
                    #time.sleep(2)
                    continue
        else:
            print "You did not choose a valid reponse"
            #time.sleep(2)
            print "You will now be redirected to the original question"
            #time.sleep(2)
            question_counter = question_counter
        if question_counter == 14: # If a person answers all 14 questions correctly, the following occurs
            print ppm_bank(question_counter)
            print "Congrats! You answered all of the questions correctly"
            #time.sleep(2)
            print "You might have realized that the atm level is still at an unhealthy level"
            #time.sleep(2)
            print "This is because it is important to realize that it's not just about knowing these environmentally sound facts...."
            #time.sleep(2)
            print "You must inform others and find beneficial ways in which to help save the environment"

game_loop()
