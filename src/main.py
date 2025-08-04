from Loader import Loader
from Cleanr import Cleanr
from Calculations import Calculations
data_frame = Loader()
data_clan = Cleanr(data_frame.gat_dataframe())
Calculations =Calculations(data_clan.gat_dataframe())
Calculations.Classification_by_anti_Semitism()
# print()