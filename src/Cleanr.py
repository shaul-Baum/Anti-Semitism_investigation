import pandas as pd
class Cleanr:
    def __init__(self,dataframe):
        self.dataframe = dataframe
        self.dataframe = self.clean_table()

    def clean_table(self):
        self.dataframe.dropna(inplace=True)
    #     # self.dataframe = self.dataframe[~(self.dataframe == 0).any(axis=1)]
    #
    #     try:
    #         self.dataframe.drop(i, axis=1, inplace=True)
    #     except:
    #             pass
    #
        return self.dataframe
    def gat_dataframe(self):
        return self.dataframe



