from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank =[]
for n in question_data:
    new_n = Question(n['question'], n['correct_answer'])
    question_bank.append(new_n)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
else:
    print('You have completed the quiz')
    print(f"Your final score is {quiz.score} / {quiz.question_number}")