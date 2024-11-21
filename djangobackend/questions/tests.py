from django.test import TestCase

from djangobackend.questions.models import Question


# Create your tests here.

class QuestionModelTest(TestCase):
    def test_question_creation(self):
        question = Question.create("What is your name?", "Enter your name")
        self.assertEqual(question.question, "What is your name?")
        self.assertEqual(question.tooltip, "Enter your name")