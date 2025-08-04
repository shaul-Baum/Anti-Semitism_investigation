import pandas as pd

class Loader:
    def __init__(self):
        try:
            self.dataframe = pd.read_csv("C:/Users/user1/PycharmProjects/PythonProject/Anti-Semitism_investigation/data/tweets_dataset.csv")
            self.loaded = True
        except Exception as e:
            self.loaded = False
            print("Error loading dataset:", e)
    def gat_dataframe(self):
        if self.loaded:
            return self.dataframe
        else:
            return None
