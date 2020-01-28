#import modules that will be referenced later
import random
import sys
import time

#initialize grade when start game
gradelvl = 100


def choose(number):   #checks to see if player input is an integer in the range given
    choice=""
    while choice=="":
      try:
        choice=int(input("\nWhat do you do? "))
        if (choice>number or choice<1): #check if number in range of options
          print("Invalid command. Try again.")
          choice=""
      except ValueError: #check if input is a integer
        print("Invalid command. Try again.")
    return choice


def grade(change):    #changes grade level when player chooses something during a class and reports letter grade
    global gradelvl, name
    gradelvl+=change #changes grade level based on what reward/consequence given during a class
    if change == 0:
      print("Your grade has not changed.")
    if gradelvl<65: #lose game and exit program
        time.sleep(4)
        print(f"\n\nWelp {name}, you were not smart enough to keep up at Magnet and we are sad to say you dropped out cause you failed school with a {gradelvl}. Have fun at UCC or whatever game you play next!")
        sys.exit()
    if gradelvl>100:
        gradelvl=100

    #print current grade level and give message regarding letter grade
    print(f"\nYour current grade: {gradelvl}")
    if gradelvl==100:
        print("(Hahaha, you thought you could have a grade higher than 100. Welp life doesn't work like that.)")
    if gradelvl>=90 and gradelvl<=100:
        print("You still have an A! Glad you\'re meeting the Magnet standards.")
    if gradelvl>=80 and gradelvl<90:
        print("Uh oh. B is not a good letter. If I got that, that wouldn\'t be good. I\'m an asian not a bsian. Try and get it up.")
    if gradelvl>=70 and gradelvl<80:
        print("Sweetie, what is you doing?!? Having a C is NOT a look!")
    if gradelvl>=65 and gradelvl<70:
        print("BRUH. You\'re border line failing with that D. Better get that up or else that D is going to meet some of it\'s letter friends and become your job at McDonalds.")


def senioryear():     #Senior year stage
    global name,seniorclasses,gradelvl
    print(f"\n\n\n------------------------------------------------------------------------\n------------------------------------------------------------------------\n\nWelcome to Senior year at Magnet! Your current grade is a {gradelvl}. You will be taking: ")
    for x in range(len(seniorclasses)): 
      print(seniorclasses[x])
    time.sleep(3)
    random.shuffle(seniorclasses) #Get class schedule
    print(f"\n-----------------------------\nHere is your class schedule:")
    for x in range(len(seniorclasses)): 
      print(seniorclasses[x])
    print("-----------------------------")
    time.sleep(3)
    print(f"\nLet\'s dive right into it!")
    time.sleep(5)
    for course in range(len(seniorclasses)): #goes through every class in Senior year
        print("\n------------------------------------------------------------------------")
        #since course list is randomized, statements below correspond to the correct class that the student has
        if seniorclasses[course]=="Senior Tech": 
            print(f"{seniorclasses[course]}")
            print(f"\nWelcome to Senior Tech! Mrs. Manning comes to greet you annd says \"Today we will be working in AutoCAD! Let's see how much you remember!\" \n1. Press the power button\n2. Let senioritis kick in")
            playerchoice=choose(2)
            if playerchoice==1:
              print("Wow, I did NOT expect that. Are you sure you are a senior? Anyways, Mrs. Manning was so blown away by your exceptional ability to turn on the computer that she restored your grade to a 100.")
              grade(100)
            if playerchoice==2:
              print("Not surprised. Senioritis has plagued the entire school. But Mrs. Manning understands and still gives you credit for the day.")
              grade(2)
        if seniorclasses[course]=="Gym 4":
            print(f"{seniorclasses[course]}")
            print(f"\nWhew! Glad to see one class is looking out for your QPA! This class has purely become a sleep period, and Mr. Stanko fully supports your efforts.")
            grade(2)
        if seniorclasses[course]=="AP Biology":
            print(f"{seniorclasses[course]}")
            print(f"\nMr. Moskowitz lets you do whatever you want, leaving the very grateful seniors to frantically work on their 100000000 projects that all of the other teachers piled on them. You work silently while crying.")
            grade(10)
        if seniorclasses[course]=="AP Physics E&M":
            print(f"{seniorclasses[course]}")
            print(f"\nYour judgement to take E&M was clearly not a good one. Dr. Fang gives you your test grade back and BOY was that NOT pretty. You cry as you see the paper riddled with red scribbles. However, your saving grace might be the curve. I mean, if you did better than everyone else and still got a 40, there may be some hope. Let's see.")
            time.sleep(15)
            search = random.randint(1,5)
            if search == 5:
              print("Holy cow! You got the best grade in the class and Dr. Fang curved your grade to a 100 AND added two points extra credit to your grade!")
              grade(2)
            else:
              print("Sorry, you did not get extra credit and your average dropped 25 points. Only one word can describe this tragedy: oof.")
              grade(-25)
        if seniorclasses[course]=="AP Lang":
            print(f"{seniorclasses[course]}")
            print(f"\nYou did not finish the 50 essays that were do that day and your teacher was not pleased.")
            grade(-20)
        if seniorclasses[course]=="AP Euro":
            print(f"{seniorclasses[course]}")
            print(f"\nMrs. Valley greets you and gives you a Powerpoint and lets you let the senioritis kick in.")
            grade(0)
        if seniorclasses[course]==("Spanish 4" or "AP Spanish Lang" or "AP Spanish Lit"):
            print(f"{seniorclasses[course]}")
            print(f"\nSenor Valverde greets you all an announces that you have a presentation on the movie you did not pay attention to in class.\n1. Leech off of someone else\n2. Go up\n3. Fake being sick")
            playerchoice=choose(3)
            if playerchoice == 1:
              print("You quickly look at your friends notes and give a brief presentation. Senor Valverde was not please but you thought that was very much adequate.")
              grade(-2)
            if playerchoice == 2:
              print(f"You completely choke and start crying in front of the class. Not only did you embarrass yourself in front of your classmates, but Senor Valverde said, \"No has venido preparado {name}. Espero que puedan aprender la próxima vez a prestar atención durante la clase. Por favor toma un pañuelo.\"")
              grade(-4)
            if playerchoice == 3:
              print("You raise your hand and say, \"Senor Valverde, me duele mucho la cabeza. ¿Puedo ir a la enfermería?\" He allows you to go and you evade the presentation for one extra class period.")
              grade(0)
        if seniorclasses[course]=="AP Calc AB":
            print(f"{seniorclasses[course]}")
            a=random.randint(10,500)
            b=random.randint(10,500)
            b=random.randint(10,500)
            c=random.randint(10,500)
            d=random.randint(10,500)
            e=random.randint(2,7)
            print(f"\n\"GOOD MORNING CLASS!\"exclaims Mr. Straut, \"SOLVE THE PROBLEM ON THE BOARD. HARSH STOP LEANING BACK ON YOUR CHAIR.\"\nThe problem on the board reads {a}*{b}+({c}*{d})^{e}.")
            rightans=(a*b)+((c*d)**e)
            choice=""
            while choice=="":
              try:
                choice=int(input("\nWhat is your answer? "))
              except ValueError: #check if input is a integer
                print("Invalid command. Try again.")
            if choice==rightans:
                print("You got the question correct and start bursting out into tears of joy. Your grade raised 2 points.(Did you use a calculator? Be honest. Cause if you did, you violated the holy Academic Honesty Policy.)")
                grade(2)
            else:
                print("\nOof. That was NOT pretty. Mr. Straut murders your grade and will to continue calc.")
                grade(-8)
        if seniorclasses[course]==("AP Calc BC" or "Linear Algebra" or "Math Stat"):
            print(f"{seniorclasses[course]}")
            print("\nHarsh comes sprinting into class and shouts, \"Happy high noon EPIC. GAMERS. How's everyone doing on this fine day?\" Harsh's godly presence immediately makes your day.")
            search=random.randint(1,2)
            if search==2:
                print("Oh no! Dr. J. assigned another GA!")
                a=random.randint(10,500)
                b=random.randint(10,500)
                b=random.randint(10,500)
                c=random.randint(10,500)
                d=random.randint(10,500)
                e=random.randint(2,7)
                print(f"Dr. J. tells all of you to go into test formation and that the exam is NO CALCULATOR. You look at the first question. It says {a}*{b}+({c}*{d})^{e}. What is your answer? ")
                choice=""
                while choice=="":
                  try:
                    choice=int(input("\nWhat is your answer? "))
                  except ValueError: #check if input is a integer
                    print("Invalid command. Try again.")
                if choice==rightans:
                    print("You got the question correct and start bursting out into tears of joy. Your grade raised 2 points.(Did you use a calculator? Be honest. Cause if you did, you violated the holy Academic Honesty Policy.)")
                    grade(2)
                else:
                    print("\nOof. That was NOT pretty. At this point, you're PRAYING that Dr. J. unleashes his \"positive impact\" manuveur.")
                    grade(-10)
                    time.sleep(3)
                    search=random.randint(1,3)
                    if search == 3:
                      positiveimpact = random.randint(1,15)
                      print(f"You received {positiveimpact} points of \"positive impact\" (bless your soul Dr. J.).")
                      grade(positiveimpact)
                    else:
                      print("You did not receive positive impact. :(")
            else:
              print("Whew! No GA today. You say hi to Dr. J.")
              grade(0)
        time.sleep(6)
    print(f"\n\nCongrats {name}, you survived Magnet! Your final grade was a {gradelvl}.")
        


def junioryear():     #Junior year stage
    global name,juniorclasses,gradelvl
    print(f"\n\n\n------------------------------------------------------------------------\n------------------------------------------------------------------------\n\nWelcome to Junior year at Magnet! Your current grade is a {gradelvl}. You will be taking: ")
    for x in range(len(juniorclasses)): 
      print(juniorclasses[x])
    time.sleep(3)
    random.shuffle(juniorclasses)#Get class schedule
    print(f"\n-----------------------------\nHere is your class schedule:")
    for x in range(len(juniorclasses)): 
      print(juniorclasses[x])
    print("-----------------------------")
    time.sleep(3)
    print(f"\nLet\'s dive right into it!")
    time.sleep(5)
    for course in range(len(juniorclasses)): #goes through every class in Junior year
        print("\n------------------------------------------------------------------------")
        #since course list is randomized, statements below correspond to the correct class that the student has
        if juniorclasses[course]=="Junior Tech":
            print(f"{juniorclasses[course]}") 
            print(f"\nMrs. Gerstein greets her fellow coders and begins the lesson. Seeing that the kids won't commit to the lesson, she pushes the students to collaborate together to master the concepts. The students let out a burst of excitement and gratitude as they are much stressed over their terrible grades.")
            grade(0)
        if juniorclasses[course]=="Gym 3":
            print(f"{juniorclasses[course]}")
            print(f"\nWhew! Glad to see one class is looking out for your QPA! This class has purely become a study/sleep period. On the downside, no matter who tells you, you\'re not going to become buff by sitting on your rear doing nothing instead of lifting weights.")
            grade(2)
        if juniorclasses[course]=="AP Chemistry":
            print(f"{juniorclasses[course]}")
            print(f"\nMr. Raite comes to greet you annd says \"Please go to your lab stations and perform the titrations\" \n1. You spill the acid\n2. You fool around\n3. You catch on fire (how I don't know)")
            playerchoice=choose(3)
            if playerchoice == 1:
              print("Mr. Raite was not pleased that you didn't follow the rules and took off points from your grade. The acid is still burning through the table.")
              grade(-4)
            if playerchoice == 2:
              print("By sheer dumb luck you manage to perform the titration correctly and get credit for the lab.")
              grade(1)
            if playerchoice == 3:
              print("The room engulfs in chaos as Mr. Raite frantically tries to put out the fire. Looks like you won't be in any labs any time soon.")
              grade(-8)
        if juniorclasses[course]=="AP Physics Mech":
            print(f"{juniorclasses[course]}")
            print(f"\nDr. Fang gives you your test grade back and BOY was that NOT pretty. Hopefully you get grading points and a curve? Also, you might need a tutor, just saying...")
            grade(-9)
        if juniorclasses[course]=="Modern American Lit":
            print(f"{juniorclasses[course]}")
            print(f"\nMs. Arnold gives you a free period to conduct research for your upcoming research paper. \n1. Do research\n2. Go on your phone")
            playerchoice=choose(2)
            if playerchoice == 1:
              print("You get on top of your work and find some good sources.")
              grade(2)
            if playerchoice == 2:
              print(f"Ms. Arnold catches you and gives you a 0 for the day.")
              grade(-2)
        if juniorclasses[course]=="US History 2":
            print(f"{juniorclasses[course]}")
            print(f"\nOh no! Sanservino gives you a pop quiz and you didn't do the reading! You...")
            time.sleep(5)
            search=random.randint(1,1000)
            if search==1000:
                  print("\npassed! Are you God?")
                  grade(20)
            else:
                  print("\nfailed! I mean, come on, what did you expect?")
                  grade(-70)
        if juniorclasses[course]==("Spanish 3" or "Spanish 4" or "AP Spanish Lang"):
            print(f"{juniorclasses[course]}")
            print(f"\nSenor Valverde greets you all an announces that you have a presentation on the movie you did not pay attention to in class.\n1. Leech off of someone else\n2. Go up\n3. Fake being sick")
            playerchoice=choose(3)
            if playerchoice == 1:
              print("You quickly look at your friends notes and give a brief presentation. Senor Valverde was not please but you thought that was very much adequate.")
              grade(-2)
            if playerchoice == 2:
              print(f"You completely choke and start crying in front of the class. Not only did you embarrass yourself in front of your classmates, but Senor Valverde said, \"No has venido preparado {name}. Espero que puedan aprender la próxima vez a prestar atención durante la clase. Por favor toma un pañuelo.\"")
              grade(-4)
            if playerchoice == 3:
              print("You raise your hand and say, \"Senor Valverde, me duele mucho la cabeza. ¿Puedo ir a la enfermería?\" He allows you to go and you evade the presentation for one extra class period.")
              grade(0)
        if juniorclasses[course]=="Math Analysis":
            print(f"{juniorclasses[course]}")
            print(f"\nMrs. Draesal puts a problem on the board that reads 3 * 5 + 2 * 4 = \n")
            choice=""
            while choice=="":
              try:
                choice=int(input("\nWhat is your answer? "))
              except ValueError: #check if input is a integer
                print("Invalid command. Try again.")
            if choice == 23:
              print("Congrats! You solved the problem right and proved you did your homework. Mrs. Draesal gives you homework credit.")
              grade(1)
            else:
              print("Mrs. Draesal is not happy that you did not do the practice problems for homework and makes you do them during class. He also marked you for a 0 on homework.")
              grade(-2)
        if juniorclasses[course]=="AP Calc AB":
            print(f"{juniorclasses[course]}")
            a=random.randint(10,500)
            b=random.randint(10,500)
            b=random.randint(10,500)
            c=random.randint(10,500)
            d=random.randint(10,500)
            e=random.randint(2,7)
            print(f"\n\"GOOD MORNING CLASS!\"exclaims Mr. Straut, \"SOLVE THE PROBLEM ON THE BOARD. HARSH STOP LEANING BACK ON YOUR CHAIR.\"\nThe problem on the board reads {a}*{b}+({c}*{d})^{e}.")
            rightans=(a*b)+((c*d)**e)
            choice=""
            while choice=="":
              try:
                choice=int(input("\nWhat is your answer? "))
              except ValueError: #check if input is a integer
                print("Invalid command. Try again.")
            if choice==rightans:
                print("You got the question correct and start bursting out into tears of joy. Your grade raised 2 points.(Did you use a calculator? Be honest. Cause if you did, you violated the holy Academic Honesty Policy.)")
                grade(2)
            else:
                print("\nOof. That was NOT pretty. Mr. Straut murders your grade and will to continue calc.")
                grade(-8)
        if juniorclasses[course]==("AP Calc BC" or "Multi/Linear Algebra"):
            print(f"{juniorclasses[course]}")
            print("\nHarsh comes sprinting into class and shouts, \"Happy high noon EPIC. GAMERS. How's everyone doing on this fine day?\" Harsh's godly presence immediately makes your day.")
            search=random.randint(1,2)
            if search==2:
                print("Oh no! Dr. J. assigned another GA!")
                a=random.randint(10,500)
                b=random.randint(10,500)
                b=random.randint(10,500)
                c=random.randint(10,500)
                d=random.randint(10,500)
                e=random.randint(2,7)
                print(f"Dr. J. tells all of you to go into test formation and that the exam is NO CALCULATOR. You look at the first question. It says {a}*{b}+({c}*{d})^{e}. What is your answer? ")
                choice=""
                while choice=="":
                  try:
                    choice=int(input("\nWhat is your answer? "))
                  except ValueError: #check if input is a integer
                    print("Invalid command. Try again.")
                if choice==rightans:
                    print("You got the question correct and start bursting out into tears of joy. Your grade raised 2 points.(Did you use a calculator? Be honest. Cause if you did, you violated the holy Academic Honesty Policy.)")
                    grade(2)
                else:
                    print("\nOof. That was NOT pretty. At this point, you're PRAYING that Dr. J. unleashes his \"positive impact\" manuveur.")
                    grade(-10)
                    time.sleep(3)
                    search=random.randint(1,3)
                    if search == 3:
                      positiveimpact = random.randint(1,15)
                      print(f"You received {positiveimpact} points of \"positive impact\" (bless your soul Dr. J.).")
                      grade(positiveimpact)
                    else:
                      print("You did not receive positive impact. :(")
            else:
              print("Whew! No GA today. You say hi to Dr. J.")
              grade(0)
        time.sleep(6)
    print(f"\n\nCongrats {name}, you finished Junior year! Your current grade is a {gradelvl}.")
    time.sleep(5)
    #go to senior year
    senioryear()
        


def sophomoreyear():     #Sophomore year stage
    global name,sophomoreclasses,gradelvl
    print(f"\n\n\n------------------------------------------------------------------------\n------------------------------------------------------------------------\n\nWelcome to Sophomore year at Magnet! Your current grade is a {gradelvl}. You will be taking: ")
    for x in range(len(sophomoreclasses)): 
      print(sophomoreclasses[x])
    time.sleep(3)
    random.shuffle(sophomoreclasses)#Get class schedule
    print(f"\n-----------------------------\nHere is your class schedule:")
    for x in range(len(sophomoreclasses)): 
      print(sophomoreclasses[x])
    print("-----------------------------")
    time.sleep(3)
    print(f"\nLet\'s dive right into it!")
    time.sleep(5)
    for course in range(len(sophomoreclasses)): #goes through every class in Sophomore year
        print("\n------------------------------------------------------------------------")
        #since course list is randomized, statements below correspond to the correct class that the student has
        if sophomoreclasses[course]=="Sophomore Tech":
            print(f"{sophomoreclasses[course]}")
            print(f"\nWelcome to Sophomore Tech! Mrs. O'Connor comes to greet you annd says \"Who\'s ready to build some carbon-fueled cars?!?\" \n1. You cut your hand on the saw\n2. You fool around\n3. You build the car")
            playerchoice=choose(3)
            if playerchoice == 1:
              print("Mrs. O'Connor was not pleased that you didn't follow the rules in the Makerspace and took off points from your grade. You're still bleeding(oops).")
              grade(-3)
            if playerchoice == 2:
              print("Mrs. O'Connor was not pleased that you didn't stay on task and took off points from your grade.")
              grade(-1)
            if playerchoice == 3:
              print("Since you didn't procrastinate, your car speeded to victory and won! Mrs. O'Connor decided to give you extra credit.")
              grade(2) 
        if sophomoreclasses[course]=="Gym 2":
            print(f"{sophomoreclasses[course]}")
            print(f"\nWhew! Glad to see one class is looking out for your QPA! Even though you start slacking off, Mr. Brooks still gives you full marks.")
            grade(2)
        if sophomoreclasses[course]=="Chemistry":
            print(f"{sophomoreclasses[course]}")
            print(f"\nMrs. Wickerhauser comes to greet you annd says \"Please go to your lab stations and perform the titrations\" \n1. You spill the acid\n2. You fool around\n3. You catch on fire (how I don't know)")
            playerchoice=choose(3)
            if playerchoice == 1:
              print("Mrs. Wickerhauser was not pleased that you didn't follow the rules and took off points from your grade. The acid is still burning through the table.")
              grade(-3)
            if playerchoice == 2:
              print("By sheer dumb luck you manage to perform the titration correctly and get credit for the lab.")
              grade(3)
            if playerchoice == 3:
              print("The room engulfs in chaos as Mrs. Wickerhauser frantically tries to put out the fire. Looks like you won't be in any labs any time soon.")
              grade(-8) 
        if sophomoreclasses[course]=="Physics":
            print(f"{sophomoreclasses[course]}")
            print(f"\nDr. Fang gives you your test grade back and BOY was that NOT pretty. Tears start streaming down your face as your grade drops 7 POINTS. AHHHHHHH")
            grade(-7)
        if sophomoreclasses[course]=="Early American Lit":
            print(f"{sophomoreclasses[course]}")
            print(f"\nOh no! Mrs. Pinto gives you a pop on the reading! You...")
            time.sleep(4)
            search=random.randint(1,3)
            if search==3:
                  print("\nYou ace the pop!")
                  grade(2)
            else:
                  print("\nYou fail the pop!")
                  grade(-4)
        if sophomoreclasses[course]=="US History 1":
            print(f"{sophomoreclasses[course]}")
            print(f"\nMrs. Valley greets you and gives you a Powerpoint.")
            grade(0)
        if sophomoreclasses[course]=="Spanish 2":
            print(f"{sophomoreclasses[course]}")
            print(f"\n\"Hola clase!\" exclaimed Senora Mejia. \"Hoy aprenderemos a conjugar verbos en español.\"\n1. What?\n2. Estoy tan emocionada!\n3. Yo soyo mucho gusto en espanolo (sorry Nicole)")
            playerchoice=choose(3)
            if playerchoice == 1:
              print("Senora Mejia did not appreciate you using english in your response and took off of your class participation points.")
              grade(-1)
            if playerchoice == 2:
              print(f"Senora Mejia responded\"Eso es genial {name}! ¡Te daré un punto para la participación en clase!")
              grade(1)
            if playerchoice == 3:
              search=random.randint(1,3)
              if search==3:
                print("As Nicole tries to correct you, Senora Mejia takes pity on you and your horrible Spanish speaking skills. She awards you class participation.")
                grade(1)
              else:
                print("Nicole, sitting in class next to you, did not appreciate the intentional butchered Spanish and threw her chancla at you. The chancla hits you in the head and you get a concussion (I wonder why this sounds familiar?). Anyways, you miss a bunch of test and fall really behind the other students. Your grades reflect this.")
                grade(-5)
        if sophomoreclasses[course]==("Spanish 3" or "Spanish 4"):
            print(f"{sophomoreclasses[course]}")
            print(f"\nSenor Valverde greets you all an announces that you have a presentation on the movie you did not pay attention to in class.\n1. Leech off of someone else\n2. Go up\n3. Fake being sick")
            playerchoice=choose(3)
            if playerchoice == 1:
              print("You quickly look at your friends notes and give a brief presentation. Senor Valverde was not please but you thought that was very much adequate.")
              grade(-2)
            if playerchoice == 2:
              print(f"You completely choke and start crying in front of the class. Not only did you embarrass yourself in front of your classmates, but Senor Valverde said, \"No has venido preparado {name}. Espero que puedan aprender la próxima vez a prestar atención durante la clase. Por favor toma un pañuelo.\"")
              grade(-4)
            if playerchoice == 3:
              print("You raise your hand and say, \"Senor Valverde, me duele mucho la cabeza. ¿Puedo ir a la enfermería?\" He allows you to go and you evade the presentation for one extra class period.")
              grade(0)
        if sophomoreclasses[course]=="Geo/Trig":
            print(f"{sophomoreclasses[course]}")
            print(f"\nMr. Liu puts a problem on the board that reads \"What is sin(2pi)?\" = \n")
            choice=""
            while choice=="":
              try:
                choice=int(input("\nWhat is your answer? "))
              except ValueError: #check if input is a integer
                print("Invalid command. Try again.")
            if choice == 0:
              print("Congrats! You solved the trig problem right and proved you did your homework. Mr. Liu gives you homework credit.")
              grade(1)
            else:
              print("Mr. Liu is not happy that you did not do the practice problems for homework and makes you do them during class. He also marked you for a 0 on homework.")
              grade(-2)
        if sophomoreclasses[course]=="Math Analysis":
            print(f"{sophomoreclasses[course]}")
            print(f"\nMrs. Draesal puts a problem on the board that reads 3 * 5 + 2 * 4 = \n")
            choice=""
            while choice=="":
              try:
                choice=int(input("\nWhat is your answer? "))
              except ValueError: #check if input is a integer
                print("Invalid command. Try again.")
            if choice == 23:
              print("Congrats! You solved the problem right and proved you did your homework. Mrs. Draesal gives you homework credit.")
              grade(1)
            else:
              print("Mrs. Draesal is not happy that you did not do the practice problems for homework and makes you do them during class. He also marked you for a 0 on homework.")
              grade(-2)
        if sophomoreclasses[course]=="AP Calc AB":
            print(f"{sophomoreclasses[course]}")
            a=random.randint(10,500)
            b=random.randint(10,500)
            b=random.randint(10,500)
            c=random.randint(10,500)
            d=random.randint(10,500)
            e=random.randint(2,7)
            print(f"\n\"GOOD MORNING CLASS!\"exclaims Mr. Straut, \"SOLVE THE PROBLEM ON THE BOARD. HARSH STOP LEANING BACK ON YOUR CHAIR.\"\nThe problem on the board reads {a}*{b}+({c}*{d})^{e}.")
            rightans=(a*b)+((c*d)**e)
            choice=""
            while choice=="":
              try:
                choice=int(input("\nWhat is your answer? "))
              except ValueError: #check if input is a integer
                print("Invalid command. Try again.")
            if choice==rightans:
                print("You got the question correct and start bursting out into tears of joy. Your grade raised 2 points.(Did you use a calculator? Be honest. Cause if you did, you violated the holy Academic Honesty Policy.)")
                grade(2)
            else:
                print("\nOof. That was NOT pretty. Mr. Straut murders your grade and will to continue calc.")
                grade(-8)
        if sophomoreclasses[course]=="AP Calc BC":
            print(f"{sophomoreclasses[course]}")
            print("\nHarsh comes sprinting into class and shouts, \"Happy high noon EPIC. GAMERS. How's everyone doing on this fine day?\" Harsh's godly presence immediately makes your day.")
            search=random.randint(1,2)
            if search==2:
                print("Oh no! Dr. J. assigned another GA!")
                a=random.randint(10,500)
                b=random.randint(10,500)
                b=random.randint(10,500)
                c=random.randint(10,500)
                d=random.randint(10,500)
                e=random.randint(2,7)
                print(f"Dr. J. tells all of you to go into test formation and that the exam is NO CALCULATOR. You look at the first question. It says {a}*{b}+({c}*{d})^{e}. What is your answer? ")
                choice=""
                while choice=="":
                  try:
                    choice=int(input("\nWhat is your answer? "))
                  except ValueError: #check if input is a integer
                    print("Invalid command. Try again.")
                if choice==rightans:
                    print("You got the question correct and start bursting out into tears of joy. Your grade raised 2 points.(Did you use a calculator? Be honest. Cause if you did, you violated the holy Academic Honesty Policy.)")
                    grade(2)
                else:
                    print("\nOof. That was NOT pretty. At this point, you're PRAYING that Dr. J. unleashes his \"positive impact\" manuveur.")
                    grade(-10)
                    time.sleep(3)
                    search=random.randint(1,3)
                    if search == 3:
                      positiveimpact = random.randint(1,15)
                      print(f"You received {positiveimpact} points of \"positive impact\" (bless your soul Dr. J.).")
                      grade(positiveimpact)
                    else:
                      print("You did not receive positive impact. :(") 
            else:
              print("Whew! No GA today. You say hi to Dr. J.")
              grade(0)
        time.sleep(6)
    print(f"\n\nCongrats {name}, you finished Sophomore year! Your current grade is a {gradelvl}.")
    time.sleep(5)
    #go to junior year
    junioryear()
        



def freshmenyear():     #Freshmen year stage
    global name,freshmenclasses,gradelvl
    print("\n\n\n------------------------------------------------------------------------\n------------------------------------------------------------------------\n\nWelcome to Freshmen year at Magnet! We\'ll be nice and start you out with a 100. Time to go to your first class!")
    for course in range(len(freshmenclasses)): #goes through every class in Freshmen year based on schedule
        print("\n------------------------------------------------------------------------")
        #since course list is randomized, statements below correspond to the correct class that the student has
        if freshmenclasses[course]=="Freshmen Tech": 
            print(f"{freshmenclasses[course]}")
            print(f"\nWelcome to Freshmen Tech! Mrs. Kipp (rip) comes to greet you and says \"Hello my chickadees! Today we will be doing a Kahoot on architectural scales!\" \n1. Join the Kahoot\n2. Not play\n3. Sleep")
            playerchoice=choose(3)
            if playerchoice == 1:
              print("You got first in the Kahoot and got to pick out of Mrs. Kipp\'s prize bin!")
              grade(2)
            if playerchoice == 2:
              print("Oh no! The whole test was on the Kahoot game that you didn\'t pay attention to! If you have\'t guessed, you didn\'t do too hot on that test and your grade reflects it.")
              grade(-3)
            if playerchoice == 3:
              search=random.randint(1,3)
              if search==3:
                  print("Whew! You were lucky that Mrs. Kipp didn\'t see you! Luckily you were able to get the notes from your friend and pass the test on the Kahoot game.")
                  grade(1)
              else:
                  print("Mrs. Kipp say you and called you out for your lack or respect in front of the entire class, giving you a detention in the process and a 0 for the day.")
                  grade(-3)
        if freshmenclasses[course]=="Gym 1":
            print(f"{freshmenclasses[course]}")
            print(f"\nWhew! Glad to see one class is looking out for your QPA! As a tryhard freshmen, Mr. DelPrete has taken a liking to you and your work ethic and decides to give you full marks.")
            grade(1)
        if freshmenclasses[course]=="Biology":
            print(f"{freshmenclasses[course]}")
            print(f"\nYou walk into the Biology room when Dr. Gupta stops you immediately in your tracks. She says, \"{name}, why are you late to my class?\" \n1. Say you came from across campus\n2. Say you were finishing up a test\n3. Give her a late pass")
            playerchoice=choose(3)
            if playerchoice == 1:
              print("Dr Gupta replies, \"Nonsense! Next time show up to my class on time. I am going to deduct points off your gr- HARSH, STOP LEANING BACK ON THE CHAIR!\"")
              time.sleep(2)
              print("Thanks to Harsh always leaning back on his chair, Dr. Gupta forgot to deduct points from your grade.")
              grade(0)
            if playerchoice == 2:
              print(f"Dr Gupta replies, \"Nonsense! You kids give me a headache! Go find your seat quickly {name}.\" Dr. Gupta took off points for you being late.")
              grade(-2)
            if playerchoice == 3:
              print("Dr. Gupta takes the late pass reluctantly and continues teaching her lesson. She only had to offer to a student to spray water on them to wake them up twice during the period.")
              grade(0)
        if freshmenclasses[course]=="SIA":
            print(f"{freshmenclasses[course]}")
            print(f"\nWelcome to SIA, the most utterly useless course(sorry Mr. Moskowitz)! Mr. Moskowitz tells you to continue your projects in class and put in a 100 for class participation.")
            grade(1)
        if freshmenclasses[course]=="World Lit":
            print(f"{freshmenclasses[course]}")
            print(f"\nMr. Nowakoski (rip) is in the middle of explaining derivational morphology and recounting everything he ever did (except Greek sailing of course). However, the room is very hot. \n1. Fight to keep your eyes open\n2. Give into the sleep deprivation")
            playerchoice=choose(2)
            if playerchoice == 1:
              print("Since you're a freshmen, you fought the will to fall asleep (good for you). This task will prove to be tougher as you progress through the years.")
              grade(0)
            if playerchoice == 2:
              search=random.randint(1,3)
              if search==3:
                  print("You fell asleep just as Mr. Nowakoski started talking about \"fire trucks\" and did not miss material for the test.")
                  grade(0)
              else:
                  print("whut??? You fell asleep the entire class and remember NOTHING. You get your recent test back and learn your lesson to never fall asleep in class again (we both know that was never learned).")
                  grade(-4)
        if freshmenclasses[course]=="World History":
            print(f"{freshmenclasses[course]}")
            print(f"\nMr. McMenamin (rip) comes blazing into class in his patrick star shorts and announces its Test Review day. You answer the question correctly and its your turn to slide the magic eraser. Your shaking violently as you pray to the Magnet gods that you get the billion points and become the lord and savior of your group (plus you really need the extra credit). You slide the eraser and it inches so closely to the billion points. And the eraser...")
            time.sleep(15)
            search=random.randint(1,100)
            if search==100:
                print("\nLANDS AT THE BILLION MARKER! Your group lifts you on their shoulders and start chanting(should we be concerned?) and you all get 2 points extra credit.")
                grade(2)
            else:
                print("\nflies off of the board :( Your group was so upset that they tore up your notes, making you fail the open-book test.")
                grade(-4)
        if freshmenclasses[course]==("Spanish 1" or "Spanish 2"):
            print(f"{freshmenclasses[course]}")
            print(f"\n\"Hola clase!\" exclaimed Senora Mejia. \"Hoy aprenderemos a conjugar verbos en español.\"\n1. What?\n2. Estoy tan emocionada!\n3. Yo soyo mucho gusto en espanolo (sorry Nicole)")
            playerchoice=choose(3)
            if playerchoice == 1:
              print("Senora Mejia did not appreciate you using english in your response and took off of your class participation points.")
              grade(-1)
            if playerchoice == 2:
              print(f"Senora Mejia responded\"Eso es genial {name}! ¡Te daré un punto para la participación en clase!")
              grade(1)
            if playerchoice == 3:
              search=random.randint(1,3)
              if search==3:
                print("As Nicole tries to correct you, Senora Mejia takes pity on you and your horrible Spanish speaking skills. She awards you class participation.")
                grade(1)
              else:
                print("Nicole, sitting in class next to you, did not appreciate the intentional butchered Spanish and threw her chancla at you. The chancla hits you in the head and you get a concussion (I wonder why this sounds familiar?). Anyways, you miss a bunch of test and fall really behind the other students. Your grades reflect this.")
                grade(-5)
        if freshmenclasses[course]=="Spanish 3":
            print(f"{freshmenclasses[course]}")
            print(f"\nSenor Valverde greets you all an announces that you have a presentation on the movie you did not pay attention to in class.\n1. Leech off of someone else\n2. Go up\n3. Fake being sick")
            playerchoice=choose(3)
            if playerchoice == 1:
              print("You quickly look at your friends notes and give a brief presentation. Senor Valverde was not please but you thought **that was very much adequate**.")
              grade(-2)
            if playerchoice == 2:
              print(f"You completely choke and start crying in front of the class. Not only did you embarrass yourself in front of your classmates, but Senor Valverde said, \"No has venido preparado {name}. Espero que puedan aprender la próxima vez a prestar atención durante la clase. Por favor toma un pañuelo.\"")
              grade(-4)
            if playerchoice == 3:
              print("You raise your hand and say, \"Senor Valverde, me duele mucho la cabeza. ¿Puedo ir a la enfermería?\" He allows you to go and you evade the presentation for one extra class period.")
              grade(0)
        if freshmenclasses[course]=="Combined 1":
            print(f"{freshmenclasses[course]}")
            print(f"\nMrs. Draesal puts a problem on the board that reads 3 * 5 = \n")
            choice=""
            while choice=="":
              try:
                choice=int(input("\nWhat is your answer? "))
              except ValueError: #check if input is a integer
                print("Invalid command. Try again.")
            if choice == 15:
              print("Congrats! You can do basic math!")
              grade(1)
            else:
              print("I'm sorry, you failed the placement test AND this easy question. You are not cut out for Magnet.")
              grade(-40)
        if freshmenclasses[course]=="Geo/Trig":
            print(f"{freshmenclasses[course]}")
            print(f"\nMr. Liu puts a problem on the board that reads \"What is sin(2pi)?\" = \n")
            choice=""
            while choice=="":
              try:
                choice=int(input("\nWhat is your answer? "))
              except ValueError: #check if input is a integer
                print("Invalid command. Try again.")
            if choice == 0:
              print("Congrats! You solved the trig problem right and proved you did your homework. Mr. Liu gives you homework credit.")
              grade(1)
            else:
              print("Mr. Liu is not happy that you did not do the practice problems for homework and makes you do them during class. He also marked you for a 0 on homework.")
              grade(-2)
        if freshmenclasses[course]=="Math Analysis":
            print(f"{freshmenclasses[course]}")
            print(f"\nMrs. Draesal puts a problem on the board that reads 3 * 5 + 2 * 4 = \n")
            choice=""
            while choice=="":
              try:
                choice=int(input("\nWhat is your answer? "))
              except ValueError: #check if input is a integer
                print("Invalid command. Try again.")
            if choice == 23:
              print("Congrats! You solved the problem right and proved you did your homework. Mrs. Draesal gives you homework credit.")
              grade(1)
            else:
              print("Mrs. Draesal is not happy that you did not do the practice problems for homework and makes you do them during class. He also marked you for a 0 on homework.")
              grade(-2)
        if freshmenclasses[course]=="AP Calc AB":
            print(f"{freshmenclasses[course]}")
            a=random.randint(10,500)
            b=random.randint(10,500)
            b=random.randint(10,500)
            c=random.randint(10,500)
            d=random.randint(10,500)
            e=random.randint(2,7)
            print(f"\n\"GOOD MORNING CLASS!\"exclaims Mr. Straut, \"SOLVE THE PROBLEM ON THE BOARD. HARSH STOP LEANING BACK ON YOUR CHAIR.\"\nThe problem on the board reads {a}*{b}+({c}*{d})^{e}.")
            rightans=(a*b)+((c*d)**e)
            choice=""
            while choice=="":
              try:
                choice=int(input("\nWhat is your answer? "))
              except ValueError: #check if input is a integer
                print("Invalid command. Try again.")
            if choice==rightans:
                print("You got the question correct and start bursting out into tears of joy. Your grade raised 2 points.(Did you use a calculator? Be honest. Cause if you did, you violated the holy Academic Honesty Policy.)")
                grade(2)
            else:
                print("\nOof. That was NOT pretty. Mr. Straut murders your grade and will to continue calc.")
                grade(-8)
        time.sleep(6)
    print(f"\n\nCongrats {name}, you finished Freshmen year! Your current grade is a {gradelvl}.")
    time.sleep(5)
    #go to sophomore year
    sophomoreyear()
        



def startup():      #Initialize classes student takes as well as gets important variables such as name.
    print("Welcome to Surviving Magnet, the game where you have to survive Magnet (I thought that was self-explanatory. If you couldn\'t get that, maybe this isn\'t the right game for you). \n The goal of the game is to get the highest grade possible without crying. But of course, if you don\'t get above a 90, are you really a Magnet student?\n You fail when you FAIL (duh). Try not to drop out.")
    #Get name of player and save
    global name
    name=input("\nLet\'s get started. What is your name? ").title()
    print(f"Well hello {name}, welcome to Magnet. First we need to choose your classes for Freshmen year. You will have to be placed into math and spanish classes.")
    
    #Get spanish placement
    global spanishclasses
    spanishclasses = ["Spanish 1", "Spanish 2", "Spanish 3", "Spanish 4", "AP Spanish Lang", "AP Spanish Lit"]
    spanishknowledge=input("\nLet\'s see if you know basic spanish. What is hello in spanish? ")
    if spanishknowledge=="hola":
      spanishlevel=random.choice(spanishclasses[1:3])
      print(f"Thank god you know that hello in spanish is hola, you will be placed in {spanishlevel}.")
      spanishpos = spanishclasses.index(spanishlevel)
      spanishclasses = spanishclasses[spanishpos:] #delete lower spanish classes from list
    else:
      print(f"How could you NOT know that hola is hello in spanish?!? For that you deserve to be placed in {spanishclasses[0]}. I\'m seriously reconsidering your place in this game.")
    
    #Get math placement
    global mathclasses
    mathclasses = ["Combined Algebra", "Geo/Trig", "Math Analysis", "AP Calc AB", "AP Calc BC", "Multi/Linear Algebra", "Math Stat"]
    mathknowledge=input("\nLet\'s see if you know basic math. What is 1 + 1? ")
    if mathknowledge=="2":
      mathlevel=random.choice(mathclasses[1:4])
      print(f"Thank god you know basic math, you will be placed in {mathlevel}.")
      mathpos = mathclasses.index(mathlevel)
      mathclasses = mathclasses[mathpos:] #delete lower math classes from list
    else:
      print(f"You are SERIOUSLY disappointing me right now. For that you deserve to be placed in {mathclasses[0]}.")
   
   #Assign classes for all years according to spanish and math placement level
    global freshmenclasses,sophomoreclasses,juniorclasses,seniorclasses
    freshmenclasses = ["Freshmen Tech","Gym 1","Biology","SIA","World Lit","World History", spanishclasses[0], mathclasses[0]]
    sophomoreclasses = ["Sophomore Tech","Gym 2","Chemistry","Physics","Early American Lit","US History 1", spanishclasses[1], mathclasses[1]]
    juniorclasses = ["Junior Tech","Gym 3","AP Chemistry","AP Physics Mech","Modern American Lit","US History 2", spanishclasses[2], mathclasses[2]]
    seniorclasses = ["Senior Tech","Gym 4","AP Biology","AP Physics E&M","AP Lang","AP Euro", spanishclasses[3], mathclasses[3]]

    print(f"\nWell that\'s settled, you will be taking: ")
    for x in range(len(freshmenclasses)): 
      print(freshmenclasses[x])
    time.sleep(3)
    #Get class schedule
    random.shuffle(freshmenclasses)
    print(f"\n-----------------------------\nHere is your class schedule:")
    for x in range(len(freshmenclasses)): 
      print(freshmenclasses[x])
    print("-----------------------------")
    time.sleep(3)
    print(f"\nBest of luck to you, {name}, you will need it.")
    time.sleep(5)
    #go to freshman year
    freshmenyear()
    
startup()