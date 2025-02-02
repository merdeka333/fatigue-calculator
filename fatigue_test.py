import time
import random
import json
import chart
import sys
import select

coordinates = []

def ask_question(question, correct_answer, answer_type=str, time_limit=5):
    """
    Ask a question, check the response time, and return whether the answer is correct along with the response time.
    """
    start_time = time.time()
    response = input(question + " ")
    response_time = time.time() - start_time

    try:
        if answer_type == str:
            response = response.lower() # Make response case-sensitive
            correct_answer = correct_answer.lower()
        else:
            response = answer_type(response) # Convert input to specified type

        correct = response == correct_answer
    except ValueError:
        correct = False

    "Assign integer values to true and false to be able to graph"

    if correct == True:
        correctNum = 1
    else:
        correctNum = 2
   
    "Adds the response time and if they answered correctly or not to a tuple to store coordinates. Tuple is then stored in list"
    point = (response_time, correctNum)
    coordinates.append(point)

    return correct, response_time  

def fatigue_test(): # Driver code
    # Explain the program to the user
    print("\nWelcome to the Fatigue Calculator for students.")
    time.sleep(3)
    print("Getting enough rest is super important for cognitive function, performance, and memory.")
    time.sleep(3)
    print("Even though you might be busy studying or doing homework, it's sometimes a better idea to take a break.")
    time.sleep(3)
    print("Let's determine your alertness level to see if it's time to relax!\n")
    time.sleep(3)

    score = 0

    # Self-reported tiredness level
    try:
        tiredness = int(input("On a scale of 1-10, how tired do you feel? "))
    except ValueError:
        print("Invalid input. Defaulting tiredness to 5.")
        tiredness = 5

    if tiredness >= 8:
        score += 3
    elif tiredness >= 5:
        score += 2
    elif tiredness >= 3:
        score += 1

    # Question bank
    question_bank = [
        ("What is 17 + 15?", 32, int),
        ("What is 41 + 25", 66, int),
        ("What comes next in the sequence: 3, 6, 9, __?", 12, int),
        ("What comes next in the sequence: 11, 22, 33, __?", 44, int),
        ("What comes next in the sequence: 2, 4, 8, __?", 16, int),
        ("What is 3 x 8?", 24, int),
        ("What is 6 x 7?", 42, int),
        ("What is 36 divided by 4?", 9, int),
        ("What is 7 squared?", 49, int),
        ("What is 12 squared?", 144, int),
        ("What is the capital of Canada?", "Ottawa", str),
        ("What is the capital of France?", "Paris", str),
        ("What is the main ingredient in guacamole?", "Avocado", str),
        ("What do bees collect to make honey?", "Nectar", str),
        ("Which word doesn't belong: Dolphin, Fish, Tiger, Octopus?", "Tiger", str),
        ("If today is Saturday, what day was it three days ago?", "Wednesday", str)
    ]

    print("Answer these questions as fast as you can:\n")

    num_questions = 3 # Number of questions to ask in each test
    selected_questions = random.sample(question_bank, num_questions)

    for question, correct_answer, q_type in selected_questions:
        correct, response_time = ask_question(question, correct_answer, q_type)

        if not correct:
            print("Incorrect answer!")
            score += 3  # Incorrect answer adds 3 fatigue points
        else:
            print("Correct answer!")
            if response_time > 4:
                score += 2  # Slow response adds 2 fatigue points
            elif response_time > 2:
                score += 1  # Moderate delay adds 1 fatigue point

        print(f"Your answer took {response_time:.2f} seconds.\n") # Print response time to 2 decimal places

        # Reaction speed test
        time.sleep(3)
        print("Let's test your reaction speed.")
        print("When you see 'GO!', press Enter as fast as you can.")

        # Clear any premature input before the reaction test starts
        if select.select([sys.stdin], [], [], 0)[0]:
            sys.stdin.read(1)  # Consume the premature input

        time.sleep(random.randint(2, 5))  # Random delay before showing GO!
        print("GO!")
        start_reaction = time.time()
        input()  # Wait for the user to press Enter
        reaction_time = time.time() - start_reaction

        if reaction_time > 2:
            score += 3 # Slow reaction time adds 3 fatigue points
        elif reaction_time > 1:
            score += 2 # Moderate reaction time adds 2 fatigue points
        elif reaction_time > 0.5:
            score += 1 # Fast reaction time adds 1 fatigue point

        print(f"Your reaction time was {reaction_time:.2f} seconds.\n")

    # Final fatigue assessment
    print("\nCalculating your overall fatigue level...")
    time.sleep(2)
    print(f"Your total fatigue score is: {score}")

    if score >= 8:
        print("You are very tired. Stop studying and rest.")
    elif score >= 5:
        print("You are moderately tired. You might want to take a break soon.")
    else:
        print("You are alert and ready to study!")

    chart.user_chart(coordinates)

if __name__ == "__main__":
    fatigue_test()
