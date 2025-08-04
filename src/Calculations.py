import pandas as pd

import math


class Calculations:
    def __init__(self,dataframe):
        self.dataframe =dataframe
        self.dataframe["number_of_letters"] = self.dataframe["Text"].str.len()
        self.on_antisemitic_dataframe = self.dataframe[self.dataframe["Biased"]==0]
        self.antisemitic_dataframe = self.dataframe[self.dataframe["Biased"]==1]
        self.number_of_anti_Semites = {}
        self.words =[]
    def classification_by_anti_Semitism(self):
        self.number_of_anti_Semites = self.dataframe["Biased"].value_counts()
        self.number_of_anti_Semites["__total__"] =self.number_of_anti_Semites[0]+self.number_of_anti_Semites[1]
        return self.number_of_anti_Semites

    def word_count(self,data):
        self.words =[len(i.split(" ")) for i in data["Text"]]
        # print(max(self.words))
        a = sum(self.words)/len(self.words)
        return a
    def amount_of_all_words(self):
        antisemitic = self.word_count(self.antisemitic_dataframe)
        non_antisemitic = self.word_count(self.on_antisemitic_dataframe)
        total = self.word_count(self.dataframe)
        return {"antisemitic":antisemitic,"non_antisemitic":non_antisemitic,"total":total}
    def longest_3_tweets(self):
        antisemitic = self.antisemitic_dataframe.nlargest(3,"number_of_letters")["Text"].to_list()
        non_antisemitic = self.on_antisemitic_dataframe.nlargest(3,"number_of_letters")["Text"].to_list()
        return {"antisemitic":antisemitic,"non_antisemitic":non_antisemitic}
    def max_words(self):
        words = " ".join(self.dataframe["Text"].to_list()).lower().split()
        int_words = pd.Series(words).value_counts()
        return int_words.head(10).keys()
    def upper(self):
        antisemitic_words = " ".join(self.antisemitic_dataframe["Text"].to_list()).split()
        on_antisemitic_words =" ".join(self.on_antisemitic_dataframe["Text"].to_list()).split()
        antisemitic_upper_words =[words for words in antisemitic_words if words.isupper() and words.isalpha()]
        on_antisemitic_upper_words =[words for words in on_antisemitic_words if words.isupper() and words.isalpha()]
        words = " ".join(self.dataframe["Text"].to_list()).lower().split()
        upper_words = [i for i in words if i.isupper() and i.isalpha()]
        return {"antisemitic":len(antisemitic_upper_words),"non_antisemitic":len(on_antisemitic_upper_words),"total":len(upper_words)}

