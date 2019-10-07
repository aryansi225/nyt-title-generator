import pickle
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model

def get_model():
    global model
    model = load_model('static/models/model.h5')

def make_prediction(seed, quantity):
    with open('static/models/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
        for _ in range(quantity):
            token_list = tokenizer.texts_to_sequences([seed])[0]
            token_list = pad_sequences([token_list], maxlen=16, padding='pre')
            predicted = model.predict_classes(token_list, verbose=0)
            output_word=""
            for word, index in tokenizer.word_index.items():
                if index == predicted:
                    output_word = word
                    break
            seed += " "+output_word
        return seed.title()

def predict(seed, quantity):
    quantity = int(quantity)
    if len(seed) > 100:
        seed = seed[:100]
    if quantity < 1:
        quantity = 1
    if quantity > 20:
        quantity = 20
    predictions = make_prediction(seed, quantity)
    return (seed, quantity, predictions)

if __name__ == '__main__':
    get_model()
    seed, quantity, predictions = predict("Climate Change", 20)
    print(seed)
    print(quantity)
    print(predictions)