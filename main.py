from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for dict in question_data:
    text = dict["question"]
    answer = dict["correct_answer"]

    new_q = Question(text, answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print(f"You have completed the quiz.\nYour final score was: {quiz.score}/{len(quiz.question_list)}")