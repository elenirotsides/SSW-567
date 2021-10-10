import unittest
from unittest.mock import patch,  MagicMock

from githubAPI import user_info


class TestGithubAPI(unittest.TestCase):

    def test_num_of_repos(self):

        m1 = MagicMock()
        m1.return_value.json = [{'name': 'Repo1'}, {
            'name': 'Repo2'}, {'name': 'A-Really-Cool-Repo'}, {'name': 'Repo4'}, {'name': 'Repo5'}]

        m2 = MagicMock()
        m2.return_value.json = [{'blah': 'blah'}, {'blah': 'blah'}, {
            'blah': 'blah'}, {'blah': 'blah'}, {'blah': 'blah'}]

        with patch('requests.get', return_value=m1):
            with patch('requests.get', return_value=m2):
                self.assertEqual(len(user_info('elenirotsides')), 5)

    def test_commit_count(self):
        info = user_info('elenirotsides')
        commitCount = info['Trivia-Bot-Website']
        self.assertEqual(commitCount, 8)


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
