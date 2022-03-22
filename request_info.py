import requests
from pprint import pprint

API_URL = 'https://api.github.com'

def print_user_property(data, key):
    #print(f"{key}")
    if key in data:
        #print("pup: 1")
        val = data[key]
        #print(f"val: {val}")
        if val !=  None and val != '':
            print(f"{key} is {data[key]}")
    
# get data from the user/login dictionary
def get_user_info( login):
    response = requests.get(API_URL+"/users/"+login)
    data = response.json()
    pprint(data)
    for k in ["name","login","company","location","hireable",
              "followers","following" ]:
        print_user_property(data, k)

'''
'hireable': True,
'followers_url': 'https://api.github.com/users/roannav/followers',
'following_url': 'https://api.github.com/users/roannav/following{/other_user}'
'''


def get_repos_info():
    # Same as
    # "repos_url": "https://api.github.com/users/roannav/repos",
    response = requests.get(API_URL+"/users/roannav/repos")
    repos = response.json()
    pprint(repos)

    num_repos = len(repos)
    print(f"Number of repos is {num_repos}")
    for i in range(num_repos):
        print_user_property(repos[i],"name")
        print_user_property(repos[i],"language")
        print_user_property(repos[i],"stargazers_count")

'''
'name': 'word_doc',
'language': 'Python',
'stargazers_count': 0,
'pushed_at': '2022-02-21T06:37:47Z',
'updated_at': '2022-02-18T21:00:41Z',
'''



# get data from the followers dictionary
def get_followers_info():
    # Same as
    #'followers_url': 'https://api.github.com/users/roannav/followers',
    response = requests.get(API_URL+"/users/roannav/followers")
    followers = response.json()
    pprint(followers)

    # num_followers is different (older data) than 
    # the followers key from the login dict.
    # num_followers is the number of records in the followers dict.
    num_followers = len(followers)
    print(f"Number of followers is {num_followers}")
    for i in range(num_followers):
        print_user_property(followers[i],"login")
        print_user_property(followers[i],"url")
        # 'url': 'https://api.github.com/users/Ambush3'
        # 'followers_url': 'https://api.github.com/users/Ambush3/followers',


get_user_info("roannav")


get_followers_info()


get_repos_info()


'''
#224  curl https://api.github.com/users/roannav/followers

response = requests.get(API_URL+"/zen")
print(response)  # <Response [200]>
'''


