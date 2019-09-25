from polls.models import Question, Choice

def find_polls_for_text(text):
    return Question.objects.filter(question_text__contains= str(text))

