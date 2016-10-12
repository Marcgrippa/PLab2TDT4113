import Tekstanalyse

def printWords(_list):
    """
    Printer ut ordene i listen
    :param _list: liste over ord
    :return:
    """

    for key in _list:
        print(key)
    print("-" * 100)


# Ferdig implementert, deloppgave 1, 2 og 3
def runForPositiv():
    p = Tekstanalyse.WordCollector("C:/Users/Håvard/GitHub/PLab2TDT4113/data/subset/train/pos")
    p.collectWordFromTextFiles()
    p.collectStopWords()
    c = Tekstanalyse.RemoveAndCalculate()
    stop_words = p.getStopWords()


    most_positive_words = c.findMostPopularWords(p.getWords(), p.getNumberOfFiles())

    positive_words_after = c.removeStopWordsFromDictionary(p.getWords(), stop_words)
    most_positive_after = c.findMostPopularWords(positive_words_after, p.getNumberOfFiles())

    print("De meste populære ordene blandt de positive ordene FØR stop ordene er fjernet")
    printWords(most_positive_words)

    print("De mest populære ordene blandt de positive ordene ETTER stop ordene er fjernet")
    printWords(most_positive_after)

# Ferdig implementert, deloppgave 1, 2 og 3
def runForNegative():
    p = Tekstanalyse.WordCollector("C:/Users/Håvard/GitHub/PLab2TDT4113/data/subset/train/neg")
    p.collectWordFromTextFiles()
    p.collectStopWords()
    c = Tekstanalyse.RemoveAndCalculate()
    stop_words = p.getStopWords()

    most_positive_words = c.findMostPopularWords(p.getWords(), p.getNumberOfFiles())

    positive_words_after = c.removeStopWordsFromDictionary(p.getWords(), stop_words)
    most_positive_after = c.findMostPopularWords(positive_words_after, p.getNumberOfFiles())

    print("De meste populære ordene blandt de positive ordene FØR stop ordene er fjernet")
    printWords(most_positive_words)

    print("De mest populære ordene blandt de positive ordene ETTER stop ordene er fjernet")
    printWords(most_positive_after)



# Ferdig implementert, deloppgave 4
def runInformationValue():

    c = Tekstanalyse.RemoveAndCalculate()
    pos, neg = c.getInformationValueFromWord()
    printWords(pos)
    printWords(neg)


# Ferdig implementer, deloppgave 5
def runPrune():
    c = Tekstanalyse.RemoveAndCalculate()
    c.removeWordsWithLowePruneFactor()


# Ferdig implementert deloppgave 6
def nGram():
    c = Tekstanalyse.RemoveAndCalculate()


    finael_dictionary_pos = c.createFinalDictionatyeWords("C:/Users/Håvard/GitHub/PLab2TDT4113/data/subset/train/pos")
    finael_dictionary_neg = c.createFinalDictionatyeWords("C:/Users/Håvard/GitHub/PLab2TDT4113/data/subset/train/neg")

    new_dic, prune_dic = c.calculatePruneValue(finael_dictionary_pos, 1000)
    y = c.removeLowPruneWords(new_dic, prune_dic)

    z = c.findMostPopularWords(y, 1000)

    printWords(z)
    #printWords(finael_dictionary_pos)

def godhet():
    c = Tekstanalyse.RemoveAndCalculate()

    finael_dictionary_pos = c.createFinalDictionatyeWords("C:/Users/Håvard/GitHub/PLab2TDT4113/data/subset/train/pos")
    finael_dictionary_neg = c.createFinalDictionatyeWords("C:/Users/Håvard/GitHub/PLab2TDT4113/data/subset/train/neg")

    test1, test2, test3, test4 = c.godhet(finael_dictionary_pos)
    print(len(test1))
    print(len(test2))
    print(len(test3))
    print(len(test4))
    for i in test3:

        print(i)


def run():

    # Deloppgave 1,2 og 3
    #runForPositiv()
    #runForNegative()

    # Deloppgave 4
    runInformationValue()

    # Deloppgave 5
    #runPrune()

    # Deloppgave 6
    nGram()

    # Deloppgave 7
    #godhet()
run()
