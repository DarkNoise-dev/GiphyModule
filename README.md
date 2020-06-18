This module make it possible to request random gifs to be with or without gifs.



How to use the module:

1. Create a Giphy account. You can create an account at https://giphy.com/join 
2. Create a Giphy App. https://developers.giphy.com/docs/sdk/
3. After creating a Giphy App copy your API Key. 
4. Now you are ready to use the module/package. Download the package and copy the file giphyApi.py into your project.

After you done that go to your main file and import giphyApi.
Now you need to define your API Key, you can do it with API_KEY = giphyApi.API_KEY = "".

Now you can call the function giphyApi.getGif() as argument you have to use the api key.
If you want to search gifs to a specific topic you also need to define tag, you can do it with tag = "".
After you done it you simply need to add tag as argument.




Function Arguments:

	API_KEY (require)

	tag (optional)
  
 	giphyApi.GetGif(API_KEY= , tag= )
  
