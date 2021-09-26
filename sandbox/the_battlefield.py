from random import randint

player: str = input("Enter your name: ")
points: int = 0
n: int = 1
NAMED_CONSTANT: str = '\U0001F601'


def main() -> None:
    """A main function."""
    print(greet())
    print('''
    ''')
    global points
    global n
    points_multiplier: int = n * 5
    key: int = randint(1, 2)
    choice: str = input(f"Which path do you seek, {player}? College, McDonalds, Trade-School? ")
    while choice == "College":
        print(f"Yay! {player} You now apply up to seven colleges!")
        print("Each university has its own respective: ‘College Acceptance Rate’ that will not be affected by your choices.")
        print("Also, each university will report your College Acceptance Chance which WILL be affected by your choices.") 
        print("Such choices may be: ‘The choice of essay you choose to submit’.")
        print("These colleges are fiesty, goodluck!")
        print("You're seven choices of college goes as follows: ")
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
            print("You are stressed from course exams. Sometimes life is hard, we understand but College admissions may not always be empathetic.")
            print("You receive a debuff: -5% to CAC (College Admission Chance), but you also receive:")
            print('''
            1 x Hug
            1 x Cookie''')
        else:
            if key == 2:
                print("You are killing your exams.")
                points = points + 1
                print(f'''
                You receive a Buff: + 5 % CAC
                Adventure pints: {points}''')
    while choice == "McDonalds":
        points
        print("A new super-duper awesome study came out detailing that now there is no-where in the contiguous US that you can live off minimum wage! Welcome to corporate slavery!")
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


welcome_message = '''
    Greetings, welcome to College Applications Simulator. 
    You are in the final crunch season of high school, and you now have to apply to college, YAY!
    All on top of the stress from your high-level final high school course exams. YAY!
    You will now be rejected from countless schools, YAY! 
    You will have a set of essays to write for applications. 
    You can apply to up to seven colleges of your choosing. 
    You may either apply to college, be a corporate slave at a deadened minimum wage job, or take your chances at trade school. 
    Goodluck! There are all wrong answers!
    '''


def message_welcome(x: str) -> str:
    """Prints our Welcome message into greet"""
    return x


def greet() -> None:
    """Welcome message."""
    print('''
        ''')
    print("Welcome Message.")
    return greet()
    
    

if __name__ == "__main__":
    main()