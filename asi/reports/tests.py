from django.test import TestCase
from django.utils import timezone
import datetime
from .models import Report
# Create your tests here.
class ModelTest(TestCase):
    def test_was_published_recently(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Report(dateReport=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Report(dateReport=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Report(dateReport=time)
        self.assertIs(recent_question.was_published_recently(), True)