from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question_obj = Question(item['question'], item['correct_answer'])
    question_bank.append(question_obj)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions(question_bank):
    quiz.next_question()
print("You have completed quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")



