import requests


#######################################################################
############# Version 1.0               Author: DarkNoise #############
#######################################################################


def gif_random():
    URL = "https://api.giphy.com/v1/gifs/random?"
    API_KEY = ""
    header = {"api_key": API_KEY}

    # Get request from Url
    r = requests.get(URL, headers=header)

    # Convert request into json
    r_dict = r.json()

    # Get Url from dictionary
    gif_url = r_dict['data']['url']

    # Print URL
    print(gif_url)


def gif_random_tag(Thema):
    # Url
    URL = "https://api.giphy.com/v1/gifs/random?api_key=nHtX1O9HDLnDpVi25LOdd3A5mXJGK8PD&tag=" + Thema + "&rating=G"

    # Get request from Url
    r = requests.get(URL)

    # Convert request into json
    r_dict = r.json()

    # Get Url from dictionary
    random_gif_url = r_dict['data']['url']

    # Print random gif url
    print(random_gif_url)


gif_random_tag(Thema="game of thrones")
gif_random()
