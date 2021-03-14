from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []
for items in question_data:
    txt = items["question"]
    ans = items["correct_answer"]
    question_bank.append(Question(txt, ans))
quiz = QuizBrain(question_bank)
while quiz.still_has_ques():
    quiz.next_question()
    