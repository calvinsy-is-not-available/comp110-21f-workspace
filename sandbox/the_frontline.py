from random import randint
points: int = 0
n: int = 1
NAMED_CONSTANT: str = '\U0001F601'
player: str


welcome_message = f'''
    Greetings, welcome to College Applications Simulator. 
    You are in the final crunch season of high school, and you now have to apply to college, YAY!
    All on top of the stress from your high-level final high school course exams. YAY!
    You will now be rejected from countless schools, YAY! 
    You will have a set of essays to write for applications. 
    You can apply to up to seven colleges of your choosing. 
    You may either apply to college, be a corporate slave at a deadened minimum wage job, or take your chances at trade school. 
    Goodluck! There are all wrong answers! {NAMED_CONSTANT}
    '''


def message_welcome(x: str) -> str:
    """Prints our Welcome message into greet"""
    return x


def greet() -> None:
    """Welcome message."""
    global player
    x = (message_welcome(welcome_message))
    print(x)
    print("")
    player = input("Enter your name: ")
    print(player)
    print(f'''
    You entered: {player}''')
    print("")
    print("")
    print("Ignore None")
    print("")


def McDonalds_path(z: int) -> int:
    """McDonalds Career Path."""
    global player
    global points
    global n
    choice: str = "McDonalds"
    if choice == "McDonalds":
        print('''
        ''')
        print('''A new super-duper awesome study came out detailing that:
        Now there is no-where in the contiguous US that you can live off minimum wage! 
        Welcome to corporate slavery!''')
        print("Years in the franchise is the name of the game here!")
        print("The longer you stay in the industry, the more points you get.")
        print("However, the longer you stay in the business, the faster your body decays. Choose when to retire wisely.")
        # z = the number of years the player selected to work at McDonalds, is equal to the number of your adventure points
        retirement_age: int = int(input(f"What is your reitrement age, {player}? "))
        y = retirement_age
        print(f"You entered: {y} ")
        print('''
        ''')
        x: str = body_decomp_from_career(y)
        points = points + y + z
    print(f"Your retirement age is {y}, {x}!")
    print("")
    print("Your adventure points are: ")
    return points
    

def body_decomp_from_career(x) -> str:
    """BODY DECOMPISITION RATE, YAY!"""
    y: int = 0
    a: str = ("")
    if x < 35:
        y = (35 // 7) * 1
        a = (f" your body eroded by a margin of {y}%")
    else:
        if x > 35:
            y = (35 // 5) * 2
            a = (f"your body eroded by a margin of {y}%")
    return a


def college_path():
    """College Path for Game."""
    global points
    global n
    key: int = randint(1, 2)
    # CAR for each school, (constant) variables:
    unc_car: int = 21
    duke_car: int = 17
    ncsu_car: int = 30
    ucla_car: int = 19
    howard_car: int = 35
    cambridge_car: int = 6
    uni_toronto_car: int = 27
    # CAC for each school: Initial
    i: int = 0
    unc_cac: int = unc_car + i
    duke_cac: int = duke_car + i
    ncsu_cac: int = ncsu_car + i
    ucla_cac: int = ucla_car + i
    howard_cac: int = howard_car + i
    cambridge_cac: int = cambridge_car + i
    uni_toronto_cac: int = uni_toronto_car + i
    choice: str = ("College")
    points = points + 1
    if choice == "College":
        print(f"Yay! {player} You now apply up to seven colleges!")
        print("Each university has its own respective: ‘College Acceptance Rate’ that will not be affected by your choices.")
        print("Also, each university will report your College Acceptance Chance which WILL be affected by your choices.") 
        print("Such choices may be: ‘The choice of essay you choose to submit’.")
        print("These colleges are fiesty, goodluck!")
        print("Your seven choices of college goes as follows: ")
        print('''
        UNC Chapel Hill
        Duke 
        NCSU
        UCLA
        Howard
        Cambridge
        University of Toronto''')
        print('''
        ''')
        print("")
        print("Here is each colleges' CAR (College Acceptance Rate)")
        print('''
        UNC Chapel Hill - 21%
        Duke - 17%
        NCSU - 30%
        UCLA - 19%
        Howard - 35%
        Cambridge - 6%
        University of Toronto - 27%''')
        print('''
        ''')
    if key == 1:
        i: int = 2
        print("Narrative: You are stressed from course exams. Sometimes life is hard, we understand but College admissions may not always be empathetic.")
        print("You receive a debuff: -5% to CAC (College Admission Chance), but you also receive:")
        print('''
            1 x Hug
            1 x Cookie''')
        unc_cac = unc_cac - i
        duke_cac = duke_cac - i
        ncsu_cac = ncsu_cac - i
        ucla_cac = ucla_cac - i
        howard_cac = howard_cac - i
        cambridge_cac = cambridge_cac - i
        uni_toronto_cac = uni_toronto_cac - i 
        print("")
        print("Narrative: It's time for you to submit your first rounds of college essays.")
        print("While you are brainstorming, you have three choices of how to craft essays. ")
        print("It occurs to you that you can create a(n): ")
        print('''
        1 x Heartfelt Essay
        1 x Well-planned Essay
        1 x Rushed Essays furvent with passion (you need only type 'Rushed Essay')''')
        print('''
        ''')
        decision: str = input(f"What type of essay will you now craft, {player}: ")
        print('''
        ''')
        print(f"You entered: {decision}")
        print('''
        ''')
        print('''Narrative: Some colleges prefer some essays over others.
        You shouldn't beat yourself up over it.... buuut.... 
        college will probably make you cry at some point, regardless of what you do.
        So why not cry now?''')
        if decision == "Heartfelt Essay":
            # CAC for each school: Heartfelt Essay
            i = 5
            unc_cac = unc_cac + i
            duke_cac = duke_cac - i
            ncsu_cac = ncsu_cac + i
            ucla_cac = ucla_cac + i
            howard_cac = howard_cac + i
            cambridge_cac = cambridge_cac + i
            uni_toronto_cac = uni_toronto_cac + i
            print("This was a smart choice, but sadly some colleges may not think that.")
            print("So, consequentially, here is your cac:")
            print(f'''
            UNC: {unc_cac}%
            Duke: {duke_cac}%
            NCSU: {ncsu_cac}%
            UCLA: {ucla_cac}%
            Howard: {howard_cac}%                    
            Cambridge: {cambridge_cac}%
            UNI Toronto: {uni_toronto_cac}%''')
    else:
        if key == 2:
            i: int = 2
            print("Narrative: You are killing your exams.")
            points = points + 1
            print(f'''
            You receive a Buff: + 5 % CAC

            Adventure points: {points}''')
            unc_cac = unc_cac + i
            duke_cac = duke_cac + i
            ncsu_cac = ncsu_cac + i
            ucla_cac = ucla_cac + i
            howard_cac = howard_cac + i
            cambridge_cac = cambridge_cac + i
            uni_toronto_cac = uni_toronto_cac + i
            print('''
            ''')
            print('''
                ''')
            print("Narrative: It's time for you to submit your first rounds of college essays.")
            print("While you are brainstorming, you have three choices of how to craft essays. ")
            print("It occurs to you that you can create a(n): ")
            print('''
            1 x Heartfelt Essay
            1 x Well-planned Essay
            1 x Rushed Essays furvent with passion (you need only type 'Rushed Essay')''')
            print('''
            ''')
            decision: str = input(f"What type of essay will you now craft, {player}: ")
            print('''
            ''')
            print(f"You entered: {decision}")
            print('''
            ''')
            print('''Narrative: Some colleges prefer some essays over others.
            You shouldn't beat yourself up over it.... buuut.... 
            college will probably make you cry at some point, regardless of what you do.
            So why not cry now?''')
            if decision == "Heartfelt Essay":
                # CAC for each school: Heartfelt Essay
                i = 5
                unc_cac = unc_cac + i
                duke_cac = duke_cac - i
                ncsu_cac = ncsu_cac + i
                ucla_cac = ucla_cac + i
                howard_cac = howard_cac + i
                cambridge_cac = cambridge_cac + i
                uni_toronto_cac = uni_toronto_cac + i
                print("This was a smart choice, but sadly some colleges may not think that.")
                print("So, consequentially, here is your cac:")
                print(f'''
                UNC: {unc_cac}%
                Duke: {duke_cac}%
                NCSU: {ncsu_cac}%
                UCLA: {ucla_cac}%
                Howard: {howard_cac}%                    
                Cambridge: {cambridge_cac}%
                UNI Toronto: {uni_toronto_cac}%''')
            elif decision == "Well-planned Essay":
                # CAC for each school: Well-planned Essay
                i = 5
                unc_cac = unc_cac + i
                duke_cac = duke_cac - i
                ncsu_cac = ncsu_cac + i
                ucla_cac = ucla_cac - i
                howard_cac = howard_cac + i
                cambridge_cac = cambridge_cac + i
                uni_toronto_cac = uni_toronto_cac - i
                print("Very respectable decision, let's see if the colleges think that way; ")
                print("here is your cac:")
                print(f'''
                UNC: {unc_cac}%
                Duke: {duke_cac}%
                NCSU: {ncsu_cac}%
                UCLA: {ucla_cac}%
                Howard: {howard_cac}%                    
                Cambridge: {cambridge_cac}%
                UNI Toronto: {uni_toronto_cac}%''')
            else:
                if decision == "Rushed Essay":
                    print("We've all been there. Viel gluck mein Freund! ")
                    print("Here is your cac:")
                    # CAC for each school: Rushed Essay
                    i = 5
                    unc_cac = unc_cac - i
                    duke_cac = duke_cac + i
                    ncsu_cac = ncsu_cac - i
                    ucla_cac = ucla_cac + i
                    howard_cac = howard_cac - i
                    cambridge_cac = cambridge_cac + i
                    uni_toronto_cac = uni_toronto_cac + i
                    print(f'''
                    UNC: {unc_cac}%
                    Duke: {duke_cac}%
                    NCSU: {ncsu_cac}%
                    UCLA: {ucla_cac}%
                    Howard: {howard_cac}%                    
                    Cambridge: {cambridge_cac}%
                    UNI Toronto: {uni_toronto_cac}%''')
    points = points + 1
    print(college_decisions(unc_cac, duke_cac, ncsu_cac, ucla_cac, howard_cac, cambridge_cac, uni_toronto_cac,))
    print('''
        ''')
    print(f"Your adventure points are: {points}")
    return "Game Over"


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
    Deciding to go to college has ended up being one of the most important and triumphant decsions you've made in your life.
    No matter your race, heritage, gender expression or sexuality,
    you find life-long friends, opportunities, memories of exquisite joy, and your significant other at college.
    But if you like or have liked Nickleback:
    You will never find happiness and will be forever alone! {NAMED_CONSTANT}'''
    print('''
    Lasting Message:
    ''')
    return lasting_mesage


def main() -> None:
    """A main function."""
    global points
    global n
    global player
    print(greet())
    print('''
    ''')
    choice: str = input(f"Which path do you seek, {player}? College, McDonalds, Trade-School? ")
    # College Path
    if choice == "College":
        print(college_path())


if __name__ == "__main__":
    main()