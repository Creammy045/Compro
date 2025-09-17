import requests

respones = requests.get('https://api.github.com/users/octocat')

if respones.status_code == 200:
    user_data = respones.json()
    
    print(f"Username: {user_data['login']}")
    print(f"Name: {user_data['name']}")
    print(f"Bio: {user_data['bio']}")
    print(f"Public Repos: {user_data['public_repos']}")
    print(f"Followers: {user_data['followers']}")
    print(f"Following: {user_data['following']}")
else:
    print(f"Failed to retrieve data.: {respones.status_code_code}")