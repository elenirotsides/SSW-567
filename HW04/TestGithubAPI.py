import unittest

from githubAPI import user_info


class TestGithubAPI(unittest.TestCase):

    def test_num_of_repos(self):
        numOfRepos = len(user_info('elenirotsides'))
        self.assertEqual(numOfRepos, 16)

    def test_commit_count(self):
        info = user_info('elenirotsides')
        commitCount = info['Trivia-Bot-Website']
        self.assertEqual(commitCount, 8)


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
