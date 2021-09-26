from random import randint

player: str = input("Enter your name: ")
points: int = 0
n: int = 1
NAMED_CONSTANT: str = '\U0001F601'


Return '''
    Greetings, welcome to College Applications Simulator. 
    You are in the final crunch season of high school, and you now have to apply to college, YAY!
    All on top of the stress from your high-level final high school course exams. YAY!
    You will now be rejected from countless schools, YAY! 
    You will have a set of essays to write for applications. 
    You can apply to up to seven colleges of your choosing. 
    You may either apply to college, be a corporate slave at a deadened minimum wage job, or take your chances at trade school. 
    Goodluck! There are all wrong answers!'''


def college_path():
    """College Path for Game."""
    global points
    global n
    points_multiplier: int = n * 5
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
    choice: str = input(f"Which path do you seek, {player}? College, McDonalds, Trade-School? ")
    while choice == "College":
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
            unc_cac = unc_cac + i
            duke_cac = duke_cac + i
            ncsu_cac = ncsu_cac + i
            ucla_cac = ucla_cac + i
            howard_cac = howard_cac + i
            cambridge_cac = cambridge_cac + i
            uni_toronto_cac = uni_toronto_cac + i 
        else:
            if key == 2:
                i: int = 2
                print("Narrative: You are killing your exams.")
                points = points + 1
                print(f'''
                You receive a Buff: + 5 % CAC

                Adventure points: {points}''')
                unc_cac = unc_cac - i
                duke_cac = duke_cac - i
                ncsu_cac = ncsu_cac - i
                ucla_cac = ucla_cac - i
                howard_cac = howard_cac - i
                cambridge_cac = cambridge_cac - i
                uni_toronto_cac = uni_toronto_cac - i
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
        if decision == "Heart-felt Essay":
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
            {unc_cac}
            {duke_cac}
            {ncsu_cac}
            {ucla_cac}
            {howard_cac}
            {cambridge_cac}
            {uni_toronto_cac}''')
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
            {unc_cac}
            {duke_cac}
            {ncsu_cac}
            {ucla_cac}
            {howard_cac}
            {cambridge_cac}
            {uni_toronto_cac}''')
        else:
            if decision == "Rushed Essay":
                print("We've all been there. Viel gluck mein Freund! ")
                print("Here is your cac:")
                # CAC for each school: Rushed Essay
                i = 5
                unc_cac = unc_cac - i
                duke_cac = duke_cac - i
                ncsu_cac = ncsu_cac - i
                ucla_cac = ucla_cac + i
                howard_cac = howard_cac - i
                cambridge_cac = cambridge_cac + i
                uni_toronto_cac = uni_toronto_cac + i
                print(f'''
                {unc_cac}
                {duke_cac}
                {ncsu_cac}
                {ucla_cac}
                {howard_cac}
                {cambridge_cac}
                {uni_toronto_cac}''')
        choice: str = input(f"Which path do you now seek, {player}? College, McDonalds, Trade-School? ")
    print('''
        ''')
    return "Game Over"


# before calling mickyds, asked the player how long do they work at mcds. Use that to change the points they earn. Assign points to mcdys parameter and return more points after.


def McDonalds_path(z: int) -> int:
    """McDonalds Career Path."""
    global points
    global n
    key: int = randint(1, 2)
    choice: str = "McDonalds"
    if choice == "McDonalds":
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
    print(f"Your retirement age is {y}, your body decomposed by: {x}, you worked at McDonalds for{z}!")
    print("")
    return int("You adventure points are: {points} !")
    

def body_decomp_from_career(x) -> str:
    """BODY DECOMPISITION RATE, YAY!"""
    y: int = 0
    a: str = ("")
    if x < 35:
        y = (35 // 7) * 1
        a = (f"Body eroded by a margin of {y}%")
    else:
        if x > 35:
            y = (35 // 5) * 2
            a = (f"Your body eroded by a margin of {y}%")
    return a
    

print(college_path())