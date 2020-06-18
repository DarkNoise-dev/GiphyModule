import giphy_api


# Set Api key
API_KEY = giphy_api.API_KEY = ""

# topic to search
tag = "Auto"


# Get random GIF
giphy_api.gif_random(API_KEY)

# Search for gif with tag
giphy_api.gif_random_tag(tag=tag, API_KEY=API_KEY)
