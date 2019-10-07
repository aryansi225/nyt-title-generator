# NYT Title Generator
Generate new title for new york times articles

This a Flask application that spits generated title text based on the entered seed phrase and number of words that are entered to be generated.
The model was created using keras and ipython notebook for the same is in the scripts folder.

Following are the steps followed in the notebook:

1. The data was taken from kaggle New York Times Comments (https://www.kaggle.com/aashita/nyt-comments) dataset.
2. Preprocessing is done to get the headlines from the dataset.
3. N-gram tokens are generated and padded to make lengths equal.
4. An LSTM model is created with one dropout layer.

The models or pickeled objects are not in models folder since it would increase the size of repository, but it can be easily created by running the notebook.

LIVE DEMO HERE -> https://nyttitlegenerator.appspot.com/

# Screenshot

![image](https://user-images.githubusercontent.com/16362957/66316876-f53d7800-e907-11e9-87b1-e8143d9cef95.png)

![image](https://user-images.githubusercontent.com/16362957/66316957-29b13400-e908-11e9-9b97-efd8dd9889e7.png)

# Dependencies

Flask, Tensorflow, Keras

# Credit
https://www.kaggle.com/shivamb/beginners-guide-to-text-generation-using-lstms
