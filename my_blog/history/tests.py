import random
import string
from django.contrib.auth.models import User
from django.test import TestCase
from history.models import History


class HistoryTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username="testuser",
            password="12345",
        )
        History.objects.create(name="Python", code=123, owner=self.test_user)
        History.objects.create(name="Docker", code=789, owner=self.test_user)

        history_test_num = 20
        self.mock_names = [
            "".join(
                [
                    random.choice((string.ascii_letters + string.digits))
                    for _ in range(random.randint(4, 20))
                ]
            )
            for _ in range(history_test_num)
        ]
        self.mock_codes = [
            int(
                "".join(
                    [
                        random.choice((string.digits))
                        for _ in range(random.randint(3, 9))
                    ]
                )
            )
            for _ in range(history_test_num)
        ]

        for mock_name, mock_code in zip(self.mock_names, self.mock_codes):
            History.objects.create(name=mock_name, code=mock_code, owner=self.test_user)

    def test_history_model(self):
        """Historys creation are correctly identified"""
        python_history = History.objects.get(name="Python")
        docker_history = History.objects.get(name="Docker")
        self.assertEqual(python_history.owner.username, "testuser")
        self.assertEqual(docker_history.owner.username, "testuser")
        self.assertEqual(python_history.code, 123)
        self.assertEqual(docker_history.code, 789)

    def test_history_list(self):
        for mock_name, mock_code in zip(self.mock_names, self.mock_codes):
            history_test = History.objects.get(name=mock_name)
            self.assertEqual(history_test.owner.username, "testuser")
            self.assertEqual(history_test.code, mock_code)
