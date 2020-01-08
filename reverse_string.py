import re

def reverse_sentence_complicated(sentence):
    words = []
    word = ""
    final_sentence = ""
    sentence_len = len(sentence)

    #find the words in the sentence
    for i in sentence:
        if i.isspace() != True:
            word += i
        else:
            words.append(word)
            word = ""

        #set word to the list of words        
    words.append(word)

    #format the sentence, but reversed
    for j in words:
        if final_sentence == "":
            final_sentence = j
        else:
            final_sentence = j + " " + final_sentence

    return final_sentence

def reverse_sentence_simple(sentence):
    #separate the words in the sentence
    words = sentence.split(" ")

    #format the sentence, but reversed
    for i in words:
        if words[0] == i:
            final_sentence = i
        else:
            final_sentence = i + " " + final_sentence

    return final_sentence

sentence = "Go BYU Cougars"

reversed_sentence = reverse_sentence_complicated(sentence)
second_reversed_sentence = reverse_sentence_simple(sentence)

print(sentence)
print(reversed_sentence)
print(second_reversed_sentence)
