import pandas as pd

class Calculations:
    def __init__(self,dataframe):
        self.dataframe =dataframe
        self.Number_of_anti_Semites = []
        self.not_Anti_Semite = 0
    def Classification_by_anti_Semitism(self):
        self.Number_of_anti_Semites = self.dataframe["Biased"].value_counts()
        print(self.Number_of_anti_Semites.keys())

