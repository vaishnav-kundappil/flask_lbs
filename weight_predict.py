import pickle

def predition(height):
    model = pickle.load(open('model.pkl','rb'))
    weight = model.predict(height)
    print(weight)
    return weight