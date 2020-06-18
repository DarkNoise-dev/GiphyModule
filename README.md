This module allows to request random gifs with or without topic.

You find an example in the project folder, it's called example.py

How to use the module:

1. Create a Giphy account. You can create an account at https://giphy.com/join 
2. Create a Giphy App. https://developers.giphy.com/docs/sdk/


![image](https://user-images.githubusercontent.com/42913703/85049731-66227880-b195-11ea-8972-4c2787ad43b1.png)

Click get started.

![image](https://user-images.githubusercontent.com/42913703/85049843-85210a80-b195-11ea-8dbe-b5abf8f79a36.png)

Click create an app.



3. After creating a Giphy App copy your API Key. 

![test](https://user-images.githubusercontent.com/42913703/85050288-2314d500-b196-11ea-8e93-c66981b1cc5d.png)



4. Now you are ready to use the module/package. Download the package and copy the file giphyApi.py into your project.

![image](https://user-images.githubusercontent.com/42913703/85050498-7850e680-b196-11ea-961a-cf9fe45a5958.png)

![image](https://user-images.githubusercontent.com/42913703/85051053-4c823080-b197-11ea-8cc5-e7f5de71a126.png)

When you have done that go to your main file and import giphyApi.

![image](https://user-images.githubusercontent.com/42913703/85050582-9ae2ff80-b196-11ea-81b0-31761382e380.png)


Now you need to define your API Key, you can do it with API_KEY = giphyApi.API_KEY = "".

![image](https://user-images.githubusercontent.com/42913703/85050752-d7166000-b196-11ea-8cb9-9e3bbbfc90dd.png)


Now you can call the function giphyApi.getGif() use the api key as argument.
If you want to search gifs for a specific topic you need to define the tag, key in tag = "".

![image](https://user-images.githubusercontent.com/42913703/85050984-35dbd980-b197-11ea-8c52-6170f4306f05.png)


After you've done it you simply need to add tag as argument.




Function Arguments:

![image](https://user-images.githubusercontent.com/42913703/85050889-16dd4780-b197-11ea-9d5c-a92d71dc0ce6.png)




	API_KEY (require)

	tag (optional)
  
 	giphyApi.GetGif(API_KEY= , tag= )
  
