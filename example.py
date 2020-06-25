import giphyApi

#######################################################################
############# Version 1.0               Author: DarkNoise #############
#######################################################################


# Set Api key
API_KEY = giphyApi.API_KEY = ""

if API_KEY == "":
    print("Please enter an Api Key")
    exit(0)

# topic to search
tag = "game-of-thrones"

# Get GIF
gifUrl = giphyApi.getGif(API_KEY=API_KEY, tag=tag)

print(gifUrl)
