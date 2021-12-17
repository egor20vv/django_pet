import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question


def create_question(question_text: str, days: int):
    """
    Create a question with given text and publish the given number of days offset to now
    :param question_text: question text
    :param days: days offset to now
    :return: crated Question
    """
    offset_data = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_data=offset_data)


class QuestionModelTests(TestCase):

    def test_no_questions(self) -> None:
        """
        If no questions exists, appropriate message is displayed
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls are available')
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self) -> None:
        """
        Questions with pub_data in the past are displayed on the polls index page
        """
        question = create_question('Past question', -30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question]
        )

    def test_future_question(self) -> None:
        """
        Question with pub_data in the future are not displayed on the polls index page
        """
        create_question('Future question', 30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, 'No polls are available')
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            []
        )

    def test_future_n_past_question(self) -> None:
        """
        Even if past and future questions are exists,
        only past questions are displayed
        """
        past_question = create_question('Past question', -30)
        create_question('Future question', 30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [past_question]
        )

    def test_two_past_questions(self) -> None:
        """
        The questions index page may display multiple questions
        """
        past_q1 = create_question('Past1', -30)
        past_q2 = create_question('Past1', -1)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [past_q2, past_q1]
        )

    def test_was_published_recently_with_future_question(self) -> None:
        """
        was_published_recently returns False for questions whose pub_date
        in the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_data=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_past_question(self) -> None:
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_data=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self) -> None:
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_data=time)
        self.assertIs(recent_question.was_published_recently(), True)


class QuestionDetailViewTests(TestCase):
    def test_future_question(self) -> None:
        """
        The detail view of question with a pub_data in the future return 404 not found
        """
        future_question = create_question('Future question', 30)
        url = reverse('polls:details', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self) -> None:
        """
        The detail view of question with a pub_data in the past displays the question's text
        """
        past_question = create_question('Past question', -30)
        url = reverse('polls:details', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)



# if __name__ == '__main__':
#     test = QuestionModelTests()
#     test.test_was_published_recently_with_recent_question()
#     test.test_was_published_recently_with_past_question()
#     test.test_was_published_recently_with_future_question()
