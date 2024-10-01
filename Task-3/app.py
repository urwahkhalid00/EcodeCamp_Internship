from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    {
        "question": "What does HTML stand for?",
        "options": ["HyperText Markup Language", "HighText Markup Language", "HyperText Multiple Language", "HighText Multiple Language"],
        "answer": 1
    },
    {
        "question": "Which language is primarily used for web development on the client side?",
        "options": ["Python", "Java", "JavaScript", "C#"],
        "answer": 3
    },
    {
        "question": "Which of the following is a Python framework for web development?",
        "options": ["Django", "Flask", "Ruby on Rails", "Both a and b"],
        "answer": 4
    },
    {
        "question": "What is the output of `print(2 ** 3)` in Python?",
        "options": ["6", "8", "9", "4"],
        "answer": 2
    },
    {
        "question": "What is the main purpose of CSS?",
        "options": ["To structure content", "To define styles and layout", "To program server-side logic", "To create databases"],
        "answer": 2
    },
    {
        "question": "Which data structure uses LIFO (Last In, First Out)?",
        "options": ["Queue", "Stack", "Array", "Linked List"],
        "answer": 2
    },
    {
        "question": "Which of the following is not a programming language?",
        "options": ["Python", "HTML", "Java", "C++"],
        "answer": 2
    },
    {
        "question": "What is the keyword used to define a function in Python?",
        "options": ["func", "define", "def", "function"],
        "answer": 3
    },
    {
        "question": "In Java, which keyword is used to create an object?",
        "options": ["new", "create", "object", "this"],
        "answer": 1
    },
    {
        "question": "What does SQL stand for?",
        "options": ["Structured Query Language", "Simple Query Language", "Sequential Query Language", "Schematic Query Language"],
        "answer": 1
    },
    {
        "question": "Who is the co-founder of Microsoft?",
        "options": ["Steve Jobs", "Mark Zuckerberg", "Bill Gates", "Larry Page"],
        "answer": 3
    },
    {
        "question": "What does HTTP stand for?",
        "options": ["HyperText Transfer Protocol", "HyperText Transport Protocol", "HighText Transfer Protocol", "HyperText Transmission Protocol"],
        "answer": 1
    },
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Lisbon"],
        "answer": 3
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": 2
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": 4
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Jupiter", "Saturn", "Mars"],
        "answer": 2
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["Charles Dickens", "Mark Twain", "William Shakespeare", "Jane Austen"],
        "answer": 3
    },
    {
        "question": "What is the capital of Japan?",
        "options": ["Beijing", "Seoul", "Tokyo", "Bangkok"],
        "answer": 3
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["O2", "H2O", "CO2", "NaCl"],
        "answer": 2
    },
    {
        "question": "What is the powerhouse of the cell?",
        "options": ["Nucleus", "Ribosome", "Mitochondria", "Endoplasmic reticulum"],
        "answer": 3
    },
    {
        "question": "Who was the first president of the United States?",
        "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
        "answer": 3
    },
    {
        "question": "In which year did the Titanic sink?",
        "options": ["1910", "1912", "1914", "1920"],
        "answer": 2
    },
    {
        "question": "Which river is the longest in the world?",
        "options": ["Amazon", "Nile", "Yangtze", "Mississippi"],
        "answer": 2
    },
    {
        "question": "Which country has the most natural lakes?",
        "options": ["Canada", "Russia", "USA", "Sweden"],
        "answer": 1
    },
    {
        "question": "Which movie won the Academy Award for Best Picture in 1994?",
        "options": ["Pulp Fiction", "Forrest Gump", "The Shawshank Redemption", "Braveheart"],
        "answer": 2
    },
    {
        "question": "Who is known as the 'King of Pop'?",
        "options": ["Elvis Presley", "Michael Jackson", "Prince", "Justin Bieber"],
        "answer": 2
    },
    {
        "question": "What is the name of the fictional wizarding school in Harry Potter?",
        "options": ["Hogwarts", "Beauxbatons", "Durmstrang", "Ilvermorny"],
        "answer": 1
    },
    {
        "question": "In which novel would you find the character Atticus Finch?",
        "options": ["The Great Gatsby", "To Kill a Mockingbird", "1984", "Moby Dick"],
        "answer": 1
    },
]

@app.route('/')
def home():
    return render_template('index.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    with open('answers.txt', 'a') as f:  
        for i, q in enumerate(questions):
            user_answer = int(request.form.get(f'question_{i}'))
            question_number = i + 1  
            if user_answer == q['answer']:
                score += 1
                f.write(f'Question {question_number}: Correct Answer {user_answer}\n')  
            else:
                f.write(f'Question {question_number}: Incorrect Answer {user_answer}, Correct Answer {q["answer"]}\n')  # Save the wrong answer
    return render_template('result.html', score=score, total=len(questions))




if __name__ == "__main__":
    app.run(debug=True)
