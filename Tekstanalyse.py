import glob
import os
import string
import operator
import math


class WordCollector():


    def __init__(self,path):
        self.path = path
        self.words = {}
        self.numbers_of_files = 0
        self.stopWords = []
        self.ngram_dic = {}

    # Ferdig implementert
    def readFromFile(self,_file):
        """
        Leser teksten fra en fil, legger de til en liste, der bare ord som har alfabetiske char er godkjente
        :param _file: filen som skal bli lest, må være en txt fil
        :return: en liste over alle ordene som var i txt filen, representert bare en gang.
        """
        _words = []
        with open(_file, "r", encoding= "utf-8") as file:
            for line in file:
                for word in line.split():
                    word = word.strip(string.punctuation + string.digits)
                    new_word = ""
                    for char in word:
                        if char.isalpha():
                            new_word += char.lower()
                    if new_word not in _words and new_word != '' and new_word != 'br':
                        _words.append(new_word)
        return _words

    # Ferdig implementert
    def collectWordFromTextFiles(self):
        """
        Henter ut antallet txt filer som hadde ordet x i seg. Dette gjøres ved å itterer over alle txt filene i en gitt mappe
        og hente ut listen over alle de forskjellige ordene i den txt filen. Før de legges til i en dictionary, der values økes med en
        dersom txt filen inneholdt et allerede eksisterende ord i dictionary.
        :param _path: mappe lokasjonen
        :return: en dictionary med key = ord, values = antall txt filer med det ordet "key"
        """
        _words = {}
        number_of_files = 0

        for filename in glob.glob(os.path.join(self.path, '*.txt')):
            number_of_files += 1
            new_words = WordCollector.readFromFile(self,filename)

            for i in range (len(new_words)):
                if new_words[i] not in _words:
                    _words[new_words[i]] = 1
                else:
                    _words[new_words[i]] += 1

        WordCollector.setNumberOfFiles(self, number_of_files)
        WordCollector.setWords(self, _words)


    def collectStopWords(self):
        """
        Henter ut alle ordene fra en fil, i dette tilfellet er det såkaldte stopp ord.
        :param _file: txt fil
        :return: en liste over alle ordene
        """

        _file = "C:/Users/Håvard/GitHub/PLab2TDT4113/data/stop_words.txt"
        _stop_words = []
        with open(_file, "r", encoding="utf-8") as file:
            for line in file:
                _stop_words.append(line.strip())

        WordCollector.setStopWords(self, _stop_words)




    # Ferdig implementert
    def collectNgramWordsFromPath(self, _path):
        _nGram_words = {}

        for filename in glob.glob(os.path.join(_path, '*.txt')):
            new_words = WordCollector.createNGramList(self, filename)

            for i in range(len(new_words)):
                if new_words[i] not in _nGram_words:
                    _nGram_words[new_words[i]] = 1
                else:
                    _nGram_words[new_words[i]] += 1

        WordCollector.setNgram(self, _nGram_words)

    # Ferdig implementert
    def createNGramList(self, _file):
        _words = self.readFromFile(_file)
        nGram_words = []

        firstWords = ""
        secondWords = ""
        for i in range(len(_words) - 1):
            firstWords = _words[i]
            secondWords = _words[i + 1]

            nWord = firstWords + "_" + secondWords
            nGram_words.append(nWord)

        return nGram_words


    def setNgram(self, ngrams):
        self.ngram_dic = ngrams

    def getNgramDic(self):
        return self.ngram_dic

    def setWords(self, words):
        self.words = words

    def getWords(self):
        return self.words

    def getStopWords(self):
        return self.stopWords

    def setStopWords(self,words):
        self.stopWords = words

    def setNumberOfFiles(self, number):
        self.numbers_of_files = number

    def getNumberOfFiles(self):
        return self.numbers_of_files



class RemoveAndCalculate():

    def __init__(self):
        self.posWords = WordCollector("C:/Users/Håvard/GitHub/PLab2TDT4113/data/subset/train/pos")
        self.negWords = WordCollector("C:/Users/Håvard/GitHub/PLab2TDT4113/data/subset/train/neg")
        self.posWords.collectStopWords()
        self.negWords.collectStopWords()
        self.posWords.collectWordFromTextFiles()
        self.negWords.collectWordFromTextFiles()

    # Ferdig implementert
    def removeStopWordsFromDictionary(self, _dic, _stopwords):
        """
        Setter alle forekomster av stopp ord i biblioteket til 0, slik at alle stopordene blir ignorert.
        :param _dic: bibliotek med key = ord og value = antall forekomster av ordet
        :param _stopwords: liste med stop ord
        :return: et bibliotek der alle antall forekomster til stopordene er satt til 0
        """
        for key in _dic:
            if key in _stopwords or key == '' or key == 'br':
                _dic[key] = 0
        return _dic

    def calculateMostPopularInformativWord(self, _dic):
        """
        Finner de 25 ordene med høyest informativ verdi
        :param _dic: dictionary
        :return: liste med 25 elementer
        """

        list = sorted(_dic.items(), key=operator.itemgetter(1))
        return list[len(list) - 25:]

    def calculateInformationValues(self, _dic1, _dic2):
        """
        Regner ut informasjonsverdien til ordene, basert på to dictionary.
        :param _dic1: dictionary
        :param _dic2:  dictionary
        :return: en dictionary med informasjonsverdien til de gitte ordene.
        """

        infoValues = {}
        for key in _dic1:
            if key in _dic2 and _dic2[key] != 0:
                value = _dic1[key] / _dic2[key]
                infoValues[key] = value
        return infoValues

    def findTotalNumberOfWords(self, _dic1, _dic2):
        """
        Finner totalt antall forekomester av ordet x i to dictionary.
        :param _dic1: dictionary
        :param _dic2: dictionary
        :return: en dictionary med key = ord og values = totalt antall txt filer som har hatt ordet x i seg.
        """

        infoValue = {}
        for key in _dic1:
            if key in _dic2:
                value = _dic1[key] + _dic2[key]
                infoValue[key] = value

        return infoValue

    # Ferdig implementert
    def removeLowPruneWords(self, _dic, _dic_prune):
        new_dic = {}

        for key in _dic:
            if key in _dic_prune:
                new_dic[key] = _dic[key]

        return new_dic

    # Ferdig implementert
    def calculatePruneValue(self, _dic, number_of_files):
        pruneValue = {}
        new_dic = {}
        for key in _dic:
            _prosent = (_dic[key] / number_of_files) * 100
            if (_prosent) > 5:
                new_dic[key] = _dic[key]
                pruneValue[key] = _prosent
        return new_dic, pruneValue




    # Ferdig implementert
    def createFinalDictionatyeWords(self, path):
        w = WordCollector(path)
        w.collectWordFromTextFiles()
        w.collectNgramWordsFromPath(path)
        w.collectStopWords()
        words_dic = w.getWords()

        ngram_dic = w.getNgramDic()



        dictionary = {}

        for key in ngram_dic:
            dictionary[key] = ngram_dic[key]

        for key in words_dic:
            dictionary[key] = words_dic[key]

        stopWords = self.posWords.getStopWords()

        final_dictionary = RemoveAndCalculate.removeStopWordsFromDictionary(self, dictionary, stopWords)

        return final_dictionary


    def getInformationValueFromWord(self):
        """
        Regner ut informasjonsverdien til ordene.
        :return: to lister med de mest populære informasjonsverdiene til positive og negative anmeldelser
        """

        stop_words = self.posWords.getStopWords()

        # Er to dictionary
        positive_words_after_stop_words = RemoveAndCalculate.removeStopWordsFromDictionary(self, self.posWords.getWords(), stop_words)
        negative_words_after_stop_words = RemoveAndCalculate.removeStopWordsFromDictionary(self, self.negWords.getWords(), stop_words)

        # Antall forskjellige ord bland positive og negative anmeldelser
        total_number_of_words_in_pos_and_neg = RemoveAndCalculate.findTotalNumberOfWords(self, positive_words_after_stop_words,
                                                                      negative_words_after_stop_words)

        # To dictionary som har informasjonsverdien til de positive og negative ordene
        infoValuePos = RemoveAndCalculate.calculateInformationValues(self, positive_words_after_stop_words, total_number_of_words_in_pos_and_neg)
        infoValueNeg = RemoveAndCalculate.calculateInformationValues(self, negative_words_after_stop_words, total_number_of_words_in_pos_and_neg)

        mostPopularPositive = RemoveAndCalculate.calculateMostPopularInformativWord(self, infoValuePos)
        mostPopularNegative = RemoveAndCalculate.calculateMostPopularInformativWord(self, infoValueNeg)

        return mostPopularPositive, mostPopularNegative

    def removeWordsWithLowePruneFactor(self):
        stop_words = self.posWords.getStopWords()

        files_totalts = self.posWords.getNumberOfFiles() + self.negWords.getNumberOfFiles()

        # Er to dictionary
        positive_words_after_stop_words = RemoveAndCalculate.removeStopWordsFromDictionary(self, self.posWords.getWords(), stop_words)
        negative_words_after_stop_words = RemoveAndCalculate.removeStopWordsFromDictionary(self, self.negWords.getWords(), stop_words)

        # Antall forskjellige ord bland positive og negative anmeldelser
        total_number_of_word_in_pos_and_neg = RemoveAndCalculate.findTotalNumberOfWords(self, positive_words_after_stop_words,
                                                                     negative_words_after_stop_words)

        # Dictionary med de ordene som har høyere prune verdi og en dictionary med prune verdiene
        new_dic, _pruneValue = RemoveAndCalculate.calculatePruneValue(self, total_number_of_word_in_pos_and_neg, files_totalts)

        # MÅ nå gå gjennom dictinary og ta ut alle ordene som ikke er i x, fordi de har for lav prune verdi

        new_pos_dic = RemoveAndCalculate.removeLowPruneWords(self, positive_words_after_stop_words, new_dic)
        new_neg_dic = RemoveAndCalculate.removeLowPruneWords(self, negative_words_after_stop_words, new_dic)

        # To dictionary som har informasjonsverdien til de positive og negative ordene
        infoValuePos = RemoveAndCalculate.calculateInformationValues(self, new_pos_dic, total_number_of_word_in_pos_and_neg)
        infoValueNeg = RemoveAndCalculate.calculateInformationValues(self, new_neg_dic, total_number_of_word_in_pos_and_neg)

        pop_pos = RemoveAndCalculate.findMostPopularWords(self, infoValuePos, files_totalts)
        pop_neg = RemoveAndCalculate.findMostPopularWords(self, infoValueNeg, files_totalts)

        printWords(pop_pos)
        printWords(pop_neg)

        return new_pos_dic, new_neg_dic

    # Ferdig implementert
    def findMostPopularWords(self, _words, number_of_files):
        """
        Finner det mest populære ordet fra en dictionary, ved å ta antall funn av ordet og dele på antall txt filer som har blitt lest.
        :param _words: dicitonary
        :param number_of_files: antall filer totalt
        :return: liste med de 25 mest populære ordene
        """

        most_popular_words = []
        for key in _words:
            _words[key] = _words[key] / number_of_files
        most_popular_words = sorted(_words.items(), key=operator.itemgetter(1))

        return most_popular_words[len(most_popular_words) - 25:]


    def godhet(self, _dic):
        """

        :param _complete_dic: inneholder populariteten til ordene, fra ligning 1
        :return:
        """

        # Går gjennom en og en tekstfil og ser om de ordene som er i tekstfilen
        # er i den komplette dic
        c = RemoveAndCalculate()

        p = WordCollector("C:/Users/Håvard/GitHub/PLab2TDT4113/data/subset/train/pos")
        n = WordCollector("C:/Users/Håvard/GitHub/PLab2TDT4113/data/subset/train/neg")
        p.collectWordFromTextFiles()
        n.collectWordFromTextFiles()

        train_pos = p.getWords()
        train_neg = n.getWords()

        path1 = "C:/Users/Håvard/GitHub/PLab2TDT4113/data/subset/test/pos"
        path2 = "C:/Users/Håvard/GitHub/PLab2TDT4113/data/subset/test/neg"

        doc_pos_path1 = []
        doc_neg_path1 = []

        doc_pos_path2 = []
        doc_neg_path2 = []
        for filname in glob.glob(os.path.join(path1, '*.txt')):
            popularitet_pos = 0
            popularitet_neg = 0
            # Henter ut ordene fra file x
            words_in_file = p.readFromFile(filname)

            # Tester om ordene er i train_pos

            for word in words_in_file:
                if word in train_pos:
                    popularitet_pos = popularitet_pos + math.log(train_pos[word])

                elif word in train_neg:
                    popularitet_neg = popularitet_neg + math.log(train_neg[word])

                else:
                    popularitet_pos = popularitet_pos + math.log(0.02)

            if popularitet_pos > popularitet_neg:
                doc_pos_path1.append(filname[57::])
            elif popularitet_pos <= popularitet_neg:
                doc_neg_path1.append(filname[57::])

        for filname in glob.glob(os.path.join(path2, '*.txt')):
            popularitet_pos = 0
            popularitet_neg = 0
            # Henter ut ordene fra file x
            words_in_file = p.readFromFile(filname)

            # Tester om ordene er i train_pos

            for word in words_in_file:
                if word in train_pos:
                    popularitet_pos = popularitet_pos + math.log(train_pos[word])

                elif word in train_neg:
                    popularitet_neg = popularitet_neg + math.log(train_neg[word])

                else:
                    popularitet_pos = popularitet_pos + math.log(0.02)

            if popularitet_pos >= popularitet_neg:
                doc_pos_path2.append(filname[57::])
            elif popularitet_pos < popularitet_neg:
                doc_neg_path2.append(filname[57::])

        return doc_pos_path1, doc_neg_path1, doc_pos_path2, doc_neg_path2


def printWords(_list):
    """
    Printer ut ordene i listen
    :param _list: liste over ord
    :return:
    """

    for key in _list:
        print(key)
    print("-" * 100)

