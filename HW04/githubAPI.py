import requests
# from secret import password


def user_info(userID):
    response = requests.get(
        f"https://api.github.com/users/{userID}/repos")
    response = response.json()

    userStats = {}
    counter = 0

    userInfo = {}

    for repo in response:
        # name = repo["name"]
        commitResponse = requests.get(
            f"https://api.github.com/repos/{userID}/{repo['name']}/commits")
        commitResponse = len(commitResponse.json())
        userStats[counter] = f"Repo: {repo['name']} Number of commits: {commitResponse}"
        userInfo[repo['name']] = commitResponse
        counter += 1

    for value in userStats.values():
        print(value)

    return userInfo


# user_info('elenirotsides')
