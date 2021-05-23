class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self, q_list):
        return self.question_number != (len(q_list)-1)

    def next_question(self):

        current_question = self.question_list[self.question_number]
        usr_ans = input(f"Q{self.question_number + 1}:{current_question.text} True/False\t")
        self.question_number += 1
        self.check_answer(usr_ans, current_question.answer)

    def check_answer(self, user_answer, current_answer):
        if user_answer.lower() == current_answer.lower():
            print("You Got the right answer\n")
            self.score += 1
            print(f"Your score is {self.score}/{self.question_number}\n")

        else:
            print("You the wrong answer\n")
            print(f"The right answer is {current_answer} ")
            print(f"Your score is {self.score}/{self.question_number}\n")
