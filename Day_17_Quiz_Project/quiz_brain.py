class QuizBrain:
    def __init__(self, question_l):
        self.question_no = 0
        self.question_list = question_l
        self.current_score = 0

    def still_has_ques(self):
        if self.question_no < len(self.question_list):
            return True
        else:
            print("You've completed the Quiz ")
            print(f"Your final score was : {self.current_score}/{len(self.question_list)}")
            return False

    def check_answer(self, u, a):
        if u.lower() == a.lower():
            return True
        else:
            return False

    def next_question(self):
        current = self.question_list[self.question_no].text
        ans = self.question_list[self.question_no].answer
        self.question_no += 1
        user_answer = input(f"Q.{self.question_no}: {current} (True/False)?: ")
        if self.check_answer(user_answer, ans):
            print("You got it ! ")
            self.current_score += 1
        else:
            print("That's Wrong")
        print(f"The correct answer was: {ans}")
        print(f"Your current score is: {self.current_score}/{self.question_no}\n")
