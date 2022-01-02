from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []

for ques in question_data:
    quiz_ques = Question(ques['question'], ques['correct_answer'])
    question_bank.append(quiz_ques)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the Quiz")
print(f"Your final score was {quiz.score}/{len(question_bank)}")
