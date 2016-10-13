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

    print("De meste populære ordene blandt de negative ordene FØR stop ordene er fjernet")
    printWords(most_positive_words)

    print("De mest populære ordene blandt de negative ordene ETTER stop ordene er fjernet")
    printWords(most_positive_after)

# Ferdig implementert, deloppgave 4
def runInformationValue():

    c = Tekstanalyse.RemoveAndCalculate()
    most_pop_pos, most_pop_neg, pop, neg = c.getInformationValueFromWord()
    print("De 25 ordene som har høyest informasjonsverdi av de positive")
    printWords(most_pop_pos)
    print("De 25 ordene som har høyest informasjonsverdi av de negative")
    printWords(most_pop_neg)

# Ferdig implementer, deloppgave 5
def runPrune():
    c = Tekstanalyse.RemoveAndCalculate()
    print("25 mest populære ordene etter å ha prunet bort ord")
    pos, neg = c.removeWordsWithLowePruneFactor()

    pop_pos = c.findMostPopularWords(pos, 1000)
    pop_neg = c.findMostPopularWords(neg, 1000)

    printWords(pop_pos)
    printWords(pop_neg)

# Ferdig implementert deloppgave 6
def nGram():
    c = Tekstanalyse.RemoveAndCalculate()


    finael_dictionary_pos = c.createFinalDictionatyeWords("C:/Users/Håvard/GitHub/PLab2TDT4113/data/subset/train/pos")
    finael_dictionary_neg = c.createFinalDictionatyeWords("C:/Users/Håvard/GitHub/PLab2TDT4113/data/subset/train/neg")

    new_dic, prune_dic = c.calculatePruneValue(finael_dictionary_pos, 1000)
    y = c.removeLowPruneWords(new_dic, prune_dic)

    z = c.findMostPopularWords(y, 1000)

    print("Mest populære ordene blandt de positive anmeldelsene etter ngram")
    printWords(z)

    new_dic, prune_dic = c.calculatePruneValue(finael_dictionary_neg, 1000)
    y = c.removeLowPruneWords(new_dic, prune_dic)

    z = c.findMostPopularWords(y, 1000)
    print("Mest populære ordene blandt de negative anmeldelsene etter ngram")
    printWords(z)

# Ferdig implementert deloppgave 7 og 8
def godhet():
    c = Tekstanalyse.RemoveAndCalculate()
    pos_from_pos, ned_from_pos, pos_from_neg, neg_from_neg = c.godhet()

    noyaktighet_pos = len(pos_from_pos)/(len(pos_from_pos) + len(pos_from_neg))
    noyaktighet_neg = len(neg_from_neg)/(len(neg_from_neg) + len(pos_from_neg))
    print("Nøyaktighet for de positive dokumentene   : " + str(noyaktighet_pos))
    print("Nøyaktighet for de negative dokumentene   : " + str(noyaktighet_neg))

def run():

    # Deloppgave 1,2 og 3

    print("Deloppgave 1,2,3")
    print("-" * 100)
    runForPositiv()
    runForNegative()

    print("\n" * 5 )
    print("Deloppgave 4")
    print("-" * 100)
    # Deloppgave 4
    runInformationValue()

    print("\n" * 5 )
    print("Deloppgave 5")
    print("-" * 100)
    # Deloppgave 5
    runPrune()

    print("\n" * 5 )
    print("Deloppgave 6")
    print("-" * 100)
    # Deloppgave 6
    nGram()

    print("\n" * 5 )
    print("Deloppgave 7,8")
    print("-" * 100)
    # Deloppgave 7
    godhet()

run()
