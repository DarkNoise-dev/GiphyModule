import requests


#######################################################################
############# Version 1.0               Author: DarkNoise #############
#######################################################################

def gif_random(API_KEY):
    URL = "https://api.giphy.com/v1/gifs/random?"
    header = {"api_key": API_KEY}

    # Get request from Url
    r = requests.get(URL, headers=header)

    # Convert request into json
    r_dict = r.json()

    # Get Url from dictionary
    gif_url = r_dict['data']['url']

    # Print URL
    print(gif_url)


def gif_random_tag(tag, API_KEY):
    # Url
    URL = "https://api.giphy.com/v1/gifs/random?api_key=nHtX1O9HDLnDpVi25LOdd3A5mXJGK8PD&tag=" + tag + "&rating=G"
    header = {"api_key": API_KEY}
    # Get request from Url
    r = requests.get(URL, headers=header)

    # Convert request into json
    r_dict = r.json()

    # Get Url from dictionary
    random_gif_url = r_dict['data']['url']

    # Print random gif url
    print(random_gif_url)
