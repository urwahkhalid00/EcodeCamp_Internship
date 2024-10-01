questions = [
 {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Lisbon"],
        "answer": 2
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": 1
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": 3
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Jupiter", "Saturn", "Mars"],
        "answer": 1
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["Charles Dickens", "Mark Twain", "William Shakespeare", "Jane Austen"],
        "answer": 2
    },
    {
        "question": "What is the capital of Japan?",
        "options": ["Beijing", "Seoul", "Tokyo", "Bangkok"],
        "answer": 2
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["O2", "H2O", "CO2", "NaCl"],
        "answer": 1
    },
    {
        "question": "What is the powerhouse of the cell?",
        "options": ["Nucleus", "Ribosome", "Mitochondria", "Endoplasmic reticulum"],
        "answer": 2
    },
    {
        "question": "Who was the first president of the United States?",
        "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
        "answer": 2
    },
    {
        "question": "In which year did the Titanic sink?",
        "options": ["1910", "1912", "1914", "1920"],
        "answer": 1
    },
    {
        "question": "Which river is the longest in the world?",
        "options": ["Amazon", "Nile", "Yangtze", "Mississippi"],
        "answer": 1
    },
    {
        "question": "Which country has the most natural lakes?",
        "options": ["Canada", "Russia", "USA", "Sweden"],
        "answer": 0
    },
    {
        "question": "Which movie won the Academy Award for Best Picture in 1994?",
        "options": ["Pulp Fiction", "Forrest Gump", "The Shawshank Redemption", "Braveheart"],
        "answer": 1
    },
    {
        "question": "Who is known as the 'King of Pop'?",
        "options": ["Elvis Presley", "Michael Jackson", "Prince", "Justin Bieber"],
        "answer": 1
    },
    {
        "question": "What is the name of the fictional wizarding school in Harry Potter?",
        "options": ["Hogwarts", "Beauxbatons", "Durmstrang", "Ilvermorny"],
        "answer": 0
    },
    {
        "question": "In which novel would you find the character Atticus Finch?",
        "options": ["The Great Gatsby", "To Kill a Mockingbird", "1984", "Moby Dick"],
        "answer": 1
    },
    {
        "question": "Who is the co-founder of Microsoft?",
        "options": ["Steve Jobs", "Mark Zuckerberg", "Bill Gates", "Larry Page"],
        "answer": 2
    },
    {
        "question": "What does HTTP stand for?",
        "options": ["HyperText Transfer Protocol", "HyperText Transport Protocol", "HighText Transfer Protocol", "HyperText Transmission Protocol"],
        "answer": 0
    }
]

def run_quiz():
    score = 0
    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Your answer: ")
        if answer.upper() == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")
    print(f"Your final score is {score}/{len(questions)}.")

if __name__ == "__main__":
    run_quiz()
