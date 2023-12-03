from question_model import Question
from data import question_data, question_data_another
from quiz_brain import QuizBrain

question_bank = []

for data in question_data:
    question_text = data['text']
    question_answer = data['answer']
    question_bank.append(Question(question_text, question_answer))

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.is_correct()

quiz.exit_quiz()

another_question_bank = []

for data in question_data_another:
    question_text = data['question']
    question_answer = data['correct_answer']
    another_question_bank.append(Question(question_text, question_answer))

another_quiz = QuizBrain(another_question_bank)
while another_quiz.still_has_question():
    another_quiz.is_correct()

another_quiz.exit_quiz()

