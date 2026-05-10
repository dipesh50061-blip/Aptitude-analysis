name = input("Enter Name: ")
print("Welcome to the Quiz", name)


def ask_questions(question_no, question, A, B, C, D, correct_answer):

    print("\nQuestion", question_no)
    print(question)
    print("A.", A)
    print("B.", B)
    print("C.", C)
    print("D.", D)

    ans = input("Enter your answer: ")
    ans = ans.upper()

    if ans == correct_answer:
        print("Correct")
        return 1
    else:
        print("Wrong")
        return 0


while True:

    score = 0

    score = score + ask_questions(
        "1",
        "What is 20*12?",
        "190",
        "160",
        "240",
        "250",
        "C"
    )

    print("Current Score:", score)

    score = score + ask_questions(
        "2",
        "What is 25% of 200?",
        "65",
        "50",
        "60",
        "75",
        "B"
    )

    print("Current Score:", score)

    score = score + ask_questions(
        "3",
        "2,4,8,16,?",
        "24",
        "32",
        "36",
        "40",
        "B"
    )

    print("Current Score:", score)

    score = score + ask_questions(
        "4",
        "What is 15 + 27?",
        "40",
        "42",
        "45",
        "50",
        "B"
    )

    print("Current Score:", score)

    score = score + ask_questions(
        "5",
        "What is 30% of 150?",
        "35",
        "40",
        "45",
        "50",
        "C"
    )

    print("Current Score:", score)

    score = score + ask_questions(
        "6",
        "Which is the odd one out?",
        "Apple",
        "Mango",
        "Banana",
        "Car",
        "D"
    )

    print("Current Score:", score)

    score = score + ask_questions(
        "7",
        "What is the square of 12?",
        "124",
        "144",
        "154",
        "164",
        "B"
    )

    print("Current Score:", score)

    score = score + ask_questions(
        "8",
        "If a train travels 60 km in 1 hour, how far in 3 hours?",
        "120 km",
        "150 km",
        "180 km",
        "200 km",
        "C"
    )

    print("Current Score:", score)

    score = score + ask_questions(
        "9",
        "A pen costs ₹10. What is the cost of 7 pens?",
        "60",
        "65",
        "70",
        "75",
        "C"
    )

    print("Current Score:", score)

    score = score + ask_questions(
        "10",
        "Rahul is the brother of Neha. Neha is the daughter of Sunil. How is Sunil related to Rahul?",
        "Father",
        "Brother",
        "Uncle",
        "Grandfather",
        "A"
    )

    print("Current Score:", score)

    score = score + ask_questions(
    "11",
    "A boy walks north, then turns right. Which direction is he facing now?",
    "South",
    "East",
    "West",
    "North",
    "B"
    )

    print("Current Score:", score)
    
    score = score + ask_questions(
    "12",
    "If all roses are flowers and some flowers fade quickly, are all roses guaranteed to fade quickly?",
    "Yes",
    "No",
    "Maybe",
    "Cannot Say",
    "B"
    )

    print("Current Score:", score)

    score = score + ask_questions(
    "13",
    "Unscramble the word: 'ETARW'",
    "Water",
    "Earth",
    "Tiger",
    "River",
    "A"
    )

    print("Current Score:", score)

    score = score + ask_questions(
    "14",
    "Unscramble the word: 'NOHTPY'",
    "Java",
    "Ruby",
    "Python",
    "Swift",
    "C"
    )

    print("Current Score:", score)

    score = score + ask_questions(
    "15",
    "Rahul walks 10 meters north, then turns right and walks 5 meters. He then turns right again and walks 10 meters. In which direction is Rahul now from his starting point?",
    "North",
    "South",
    "East",
    "West",
    "C"
    )

    print("Current Score:", score)

    print("\nQuiz Finished!")
    print("Final Score:", score, "out of 15")

    percentage = (score / 15) * 100

    print("Percentage:", round(percentage, 2), "%")

    if score >=12:
        print("Performance: Excellent")
    elif score >= 10:
        print("Performance: Good")
    else:
        print("Performance: Needs Improvement")

    print("Thanks for playing the quiz!")

    play_again = input("\nDo you want to play again? (yes/no): ")
    play_again = play_again.lower()

    if play_again != "yes":
        print("Thanks for playing, Goodbye!")
        break
