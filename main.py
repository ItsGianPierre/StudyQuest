import random

# File where the game history will be stored
HISTORY_FILE = "history.txt"

# Categories and questions
QUESTIONS = {
    "Mathematics": [
        ("What is 8 x 7?", "56"),
        ("What is 15 + 9?", "24"),
        ("What is 100 ÷ 4?", "25"),
        ("What is 12 - 5?", "7"),
        ("What is 9 x 9?", "81")
    ],

    "Science": [
        ("Which planet is known as the Red Planet?", "mars"),
        ("Which organ pumps blood through the body?", "heart"),
        ("Which gas do we breathe to survive?", "oxygen"),
        ("What is the star of our solar system?", "sun"),
        ("In what state is water at 0°C?", "solid")
    ],

    "General Knowledge": [
        ("What is the capital of Peru?", "lima"),
        ("How many continents are there?", "7"),
        ("What is the largest ocean in the world?", "pacific"),
        ("In which country are the Pyramids of Giza located?", "egypt"),
        ("Who wrote Don Quixote?", "cervantes")
    ]
}


def show_welcome():
    print("=" * 40)
    print("          STUDYQUEST")
    print("   Academic Trivia in Python")
    print("=" * 40)
    print()


def show_menu():
    print("\nMAIN MENU")
    print("1. Play")
    print("2. View History")
    print("3. Exit")


def get_menu_option():
    while True:
        option = input("Select an option: ")

        if option in ["1", "2", "3"]:
            return option
        else:
            print("Invalid option. Please try again.")


def ask_name():
    while True:
        name = input("Enter your name: ").strip()

        if name != "":
            return name
        else:
            print("Name cannot be empty.")


def select_category():
    categories = list(QUESTIONS.keys())

    print("\nAVAILABLE CATEGORIES")

    for i in range(len(categories)):
        print(f"{i + 1}. {categories[i]}")

    while True:
        option = input("Select a category: ")

        if option in ["1", "2", "3"]:
            return categories[int(option) - 1]
        else:
            print("Invalid option.")


def run_quiz(category):
    questions = QUESTIONS[category].copy()

    # Shuffle questions randomly
    random.shuffle(questions)

    score = 0
    total = len(questions)

    print("\n" + "=" * 40)
    print("STARTING QUIZ")
    print("=" * 40)

    for i in range(total):
        question, correct_answer = questions[i]

        print(f"\nQuestion {i + 1} of {total}")
        print(question)

        user_answer = input("Your answer: ").strip().lower()

        if user_answer == correct_answer.lower():
            print(" Correct!")
            score += 1
        else:
            print(" Incorrect.")
            print("The correct answer was:", correct_answer)

    return score, total


def start_game():
    name = ask_name()

    print(f"\nWelcome, {name}!")

    category = select_category()

    print("\nYou selected:", category)

    score, total = run_quiz(category)

    print("\n" + "=" * 40)
    print("RESULTS")
    print("=" * 40)

    print("Player:", name)
    print(f"Score: {score}/{total}")

    percentage = (score / total) * 100

    print(f"Percentage: {percentage:.1f}%")


def main():
    show_welcome()

    while True:
        show_menu()

        option = get_menu_option()

        if option == "1":
            start_game()

        elif option == "2":
            print("\n[View history coming soon]\n")

        elif option == "3":
            print("\nThank you for playing StudyQuest!")
            break


if __name__ == "__main__":
    main()