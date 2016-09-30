import glob
import os
import string
import operator

def collectWordFromTextFile(_path):
    _word_dic = {}
    number_of_files = 0
    for filename in glob.glob(os.path.join(_path, '*.txt')):
        number_of_files += 1
        with open(filename, "r", encoding = "utf-8") as file:
            for line in file:
                for word in line.split():
                    word = word.strip(string.punctuation + string.digits)
                    new_word = ""
                    for char in word:
                        if char.isalpha():
                            new_word += char.lower()
                    if new_word not in _word_dic:
                        _word_dic[new_word] = 1
                    else:
                        _word_dic[new_word] += 1
    return _word_dic

def findMostPopularWords(_dic):
    list_of__most_popular_words = sorted(_dic.items(), key = operator.itemgetter(1))
    return list_of__most_popular_words[len(list_of__most_popular_words)-26:]

#def removeStopWordsFromDictionary(_dic):
    


collectWordFromTextFile("C:/Users/Håvard/GitHub/PLab2TDT4113/data/subset/train/pos")
collectWordFromTextFile("C:/Users/Håvard/GitHub/PLab2TDT4113/data/subset/train/neg")

