NAMED_CONSTANT: str = '\U0001F601'
player: str 
points: int = 0

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
    

# Above greet function is complete excluding the None returned at the end
print(greet())


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


print()