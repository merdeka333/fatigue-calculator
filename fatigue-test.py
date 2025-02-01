import time
import random

coordinates = []

def ask_question(question, correct_answer, answer_type=str, time_limit=5):
    """
    Ask a question, check the response time, and return whether the answer is correct along with the response time.
    """
    start_time = time.time()
    response = input(question + " ")
    response_time = time.time() - start_time

    try:
        response = answer_type(response)
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

def fatigue_test():
    print("\nWelcome to the Fatigue Calculator! Let's determine your alertness level.\n")

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

    # Timed Questions
    questions = [
        ("What is 17 + 15?", 32, int),
        ("What comes next in the pattern: 3, 6, 9, __?", 12, int),
        ("What is 20 x 20?", 400, int)
    ]

    for question, correct_answer, q_type in questions:
        correct, response_time = ask_question(question, correct_answer, q_type)

        if not correct:
            print("Incorrect answer!")
            score += 3  # More fatigue points for incorrect answers
        else:
            print("Correct answer!")
            if response_time > 4:
                score += 2  # Slow response increases fatigue
            elif response_time > 2:
                score += 1  # Moderate delay increases fatigue slightly

        print(f"Your answer took {response_time:.2f} seconds.\n")

        # Reaction speed test
        print("Now, let's test your reaction speed.")
        print("When you see 'GO!', press Enter as fast as you can.")
        time.sleep(random.randint(2, 5))  # Random delay before showing "GO!"
        print("GO!")
        start_reaction = time.time()
        input()  # Wait for the user to press Enter
        reaction_time = time.time() - start_reaction

        if reaction_time > 2:
            score += 3
        elif reaction_time > 1:
            score += 2
        elif reaction_time > 0.5:
            score += 1

        print(f"Your reaction time was {reaction_time:.2f} seconds.\n")

    # Final Fatigue Assessment
    print("\nCalculating your overall fatigue level...")
    time.sleep(2)
    print(f"Your total fatigue score is: {score}")

    if score >= 7:
        print("You are very tired. Stop studying and rest.")
    elif score >= 4:
        print("You are moderately tired. Take a break soon.")
    else:
        print("You are alert and ready to study!")

if __name__ == "__main__":
    fatigue_test()
