import requests

def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    if response.status_code == 200:
        joke_data = response.json()
        return joke_data['setup'], joke_data['punchline']
    else:
        return "Failed to fetch joke", ""

if __name__ == "__main__":
    setup, punchline = get_random_joke()
    print("Joke: ", setup)
    print("Punchline: ", punchline)