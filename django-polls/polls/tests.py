import datetime
from django.test import TestCase
from django.utils import timezone

from polls.models import Question

# Create your tests here.
# test methods inside your test class must start with keyword test
class QuestionModelTest(TestCase):
    def test_question_was_published_recently(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
        
