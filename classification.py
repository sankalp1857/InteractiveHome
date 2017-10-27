import json
import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy as np
from math_util import sigmoid

stemmer = LancasterStemmer()
ERROR_THRESHOLD = 0.2
synapse_file = 'model/synapses-tan.json'
with open(synapse_file) as data_file:
    synapse = json.load(data_file)
    synapse_0 = np.asarray(synapse['synapse0'])
    synapse_1 = np.asarray(synapse['synapse1'])
    classes = np.asarray(synapse['classes'])
    words = np.asarray(synapse['words'])


def clean_up_sentence(sentence):
    # tokenize the pattern
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words


def bow(sentence, words, show_details=False):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)

    return np.array(bag)


def think(sentence, show_details=False):
    x = bow(sentence.lower(), words, show_details)
    if show_details:
        print ("sentence:", sentence, "\n bow:", x)
    # input layer is our bag of words
    l0 = x
    # matrix multiplication of input and hidden layer
    l1 = sigmoid(np.dot(l0, synapse_0))
    # output layer
    l2 = sigmoid(np.dot(l1, synapse_1))
    return l2


def classify(sentence, show_details=False):
    results = think(sentence, show_details)
    results = [[i, r] for i, r in enumerate(results) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_results = [str(classes[r[0]]) for r in results]
    return return_results


found_classes = classify("turn off")
print found_classes

rooms = {"bedroom", "living_room"}
states = {"on", "off", "value"}
appliances = {"light", "fan", "ac"}

r = [x for x in found_classes if x in rooms]
a = [x for x in found_classes if x in appliances]
s = [x for x in found_classes if x in states]
room = r[0] if r else None
appliance = a[0] if a else None
state = s[0] if s else None

'''
if room == rooms[0]:
    if appliance == appliances[0]:
        if state == states[0]:
            action(0, 1)
        elif state == states[1]:
            action(0, 0)
        else:
            feedback("ask", "")
    elif appliance == appliances[1]:
        if state == states[0]:
            action(1, 1)
        elif state == states[1]:
            action(1, 0)
        else:
            feedback("ask", "")
    elif appliance == appliances[2]:
        if state == states[0]:
            action(2, 1)
        elif state == states[1]:
            action(2, 0)
        elif state == state[2]:
            action(2, value)
        else:
            feedback("ask", "")
elif room == rooms[1]:
    if appliance == appliances[0]:
        if state == states[0]:
            action(3, 1)
        elif state == states[1]:
            action(3, 0)
        else:
            feedback("ask", "")
    elif appliance == appliances[1]:
        if state == states[0]:
            action(4, 1)
        elif state == states[1]:
            action(4, 0)
        else:
            feedback("ask", "")
    elif appliance == appliances[2]:
        if state == states[0]:
            action(5, 1)
        elif state == states[1]:
            action(5, 0)
        elif state == state[2]:
            action(5, value)
        else:
            feedback("ask", "")
'''