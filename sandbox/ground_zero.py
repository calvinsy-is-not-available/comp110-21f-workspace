NAMED_CONSTANT: str = '\U0001F601'


def college_decisions(a: int, b: int, c: int, d: int, e: int, f: int, g: int) -> str:
    """Calculates/Returns College Admission Decisions"""
    if a > 25:
        print("Congratulations, you have been granted admission into...")
        print('''
        UNC Chapel Hill:

        Tar Heels not only think, but they innovate and raise the greatness from the hearts of each attendant of the university. 
        We are honored to offer you admission. We hope to see you in the fall.
        ''')
    else: 
        print("We regret to inform you that you did not receive admission to:")
        print('''
        UNC Chapel Hill:

        Dear sucker, thank you for the 70 dollars.. 
        Erm… I mean.. Heartfelt essay. 
        Perhaps you were meant to be a student to at a fellow University of North Carolina allied institution of higher learning.
        Fortune be upon you.
        ''')
    if b > 14:
        print("Congratulations, you have been granted admission into...")
        print('''
        Duke: 
        
        How did we let you in? Must've been a mistake, sorry. --Oh…. It’s not a mistake? How? They’re not even in the country club! 
        They’re gifted and show insane potential?!! What does that have to do with anything? Ugh, fine… Guess we’ll see you in the fall.   
        Loser
        ''')
    else: 
        print("We regret to inform you that you did not receive admission to:")
        print('''
        Duke:

        Sorry, you do not smell of the exquisiteness of 70,000 dollars a year. 
        Perhaps you should crawl back to your domicile. 
        Or perhaps… Apply to Carolina.
        ''')
    if c > 26:
        print("Congratulations, you have been granted admission into...")
        print('''
        NCSU:

        We are honored to offer you admission to the largest public engineering school in the Great State of North Carolina. 
        Here we invite all of our students to think and do. We craft out pupils into the leaders and innovators of tomorrow. 
        We are honored and look forward to seeing you in the fall.

        ''')
    else:
        print("We regret to inform you that you did not receive admission to:")
        print('''
        NCSU:

        Howdy, we regret to inform you that you are not a part of the Wolf Pack. Not everyone is a wolf, some people are Yorkies.
        ''')
    if d > 14:
        print("Congratulations, you have been granted admission into...")
        print('''
        UCLA:

        Ugh, cool, I guess. Welcome to the UNI. We know the weather’s awesome. 
        Enjoy the town, hit the beach, juice up your Finsta. 
        Do all your homework at 10:34 the night it’s due. 
        It’s simple. We’ll catch you in the fall.

        ''')
    else:
        print("We regret to inform you that you did not receive admission to:")
        print('''
        UCLA:

        Ha. Loser.
        ''')
    if e > 31:
        print("Congratulations, you have been granted admission into...")
        print('''
        Howard:

        Young leader, we are pleased to offer you admission to our program. 
        Thank you for your interest. We’ll see you this fall.

        ''')
    else:
        print("We regret to inform you that you did not receive admission to:")
        print('''
        Howard:

        We regret to inform you that you were not chosen to attend this prestigious institution of higher learning. 
        We wish you the best. 
        Try again next application season.
        ''')
    if f > 12:
        print("Congratulations, you have been granted admission into...")
        print('''
        Cambridge:

        What else is there to say. 
        You made it into Cambridge. 
        You will most likely be a key part of your generation. 
        See you space cowboy…
        ''')
    else:
        print("We regret to inform you that you did not receive admission to:")
        print('''
        Tilly Ho! Tilly Ho! Ha, you smell neigh of decadent extraordinary aged threads and enchanted ephemeral wisened olfactions. 
        That’s probably what you thought we sounded like. 
        We’re not Duke, we’re respectable. 
        Unfortunately we cannot offer you admission this fall, but we know you’re smart. 
        You’ll do great things wherever you go, because that’s you!
        ''')
    if g > 33:
        print("Congratulations, you have been granted admission into...")
        print('''
       University of Toronto:

        …Cups of the Rosé… 
        Oh… Erm… 
        Didn’t see you there. 
        Well, uh, congrats on getting in… 
        Do you know Drake?.... 
        He's from here if you didn't know.
        Oh yeah, congrats, I guess...
        ''')
    else:
        print("We regret to inform you that you did not receive admission to:")
        print('''
        University of Toronto:

        Did you know that Drake is from here? 
        Like THE DRAKE. 
        Oh, by the way, you did not make the cut. 
        Goodluck with your future endeavors. 
        …Cups of the Rosé… 
        Oh… Erm… Sorry…  
        I was listening to my obligatory Drake for the day. 
        Bye… again.
        ''')
    lasting_mesage: str = f'''
    Deciding to go to college has ended up being one of the most important and triumphant decsions you've made in your life
    No matter your race, heritage, gender expression or sexuality,
    you find life-long friends, opportunities, memories of exquisite joy, and your significant other at college.
    But if you like or have liked Nickleback:
    You will never find happiness and will be forever alone! {NAMED_CONSTANT}'''
    print('''
    Lasting Message:
    ''')
    return lasting_mesage



  print('''
    ''')
    choice: str = input(f"Which path do you seek, {player}? College, McDonalds, Trade-School? ")
    return choice
# College Path
    while choice == "College":
        print("gg")
    # McDonalds Path
    while choice == "McDonalds":
        print("How long do you want to work at McDonalds?")
        points = points + 5
        print("gg")
    # Trade-School
    while choice == "Trade-School":
        print('''
        ''')
        print(f"You entered: {choice}")
        print('''
        ''')
        print(f"You {player} rock! You will either become a blue collar cynic, OR a fabulous billionaire! Goodluck!")
        print('''
        ''')
        if key == 1:
            global points
            print("WHOOO HOOOOOO, You won the Game of Thrones!! You have greated a series of innovations that will fundamentally change how we live our lives!!")
            print("You are our new god-like overlord! Who needs Jeff Bezos when we have you ??!!!")
            points = points + 1
            print(f"Your adventure points are: {points * points_multiplier}")
            print('''
            ''')
            print("End Game")
            if key == 2:
                print("WHA WHA WHAAAAN. You are a struggling artesian in a world of pure immitations and blue-pilled zombies.")
                print("The world probably needs more people like you, but thanks to societal-natural-selection you will persih a lowly Starbucks Manager.")
                points = points - 1
                print(f"Your adventure points are: {points}")
                print("End Game")
    question: str = input('''Do you want to keep playing? 
    Type:  y or n ''')
    while question == "y" or "n":
        if question == "y":
            print(f"Your adventure points are: {points}")
            return main()
        else:
            if question == "n":
                question = "q"
    print("Game Over. Thanks for playing.")
    print("")
    return