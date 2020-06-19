import requests


#######################################################################
############# Version 1.0               Author: DarkNoise #############
#######################################################################

def getGif(API_KEY, tag=""):
    header = {"api_key": API_KEY}

    if tag == "":
        URL = "https://api.giphy.com/v1/gifs/random?"

    else:
        URL = "https://api.giphy.com/v1/gifs/random?&tag=" + tag + "&rating=G"

    # Get request from Url
    r = requests.get(URL, headers=header)

    # Convert request into json
    r_dict = r.json()

    # Get Url from dictionary
    gif_url = r_dict['data']['url']

    # Print URL
    return gif_url
