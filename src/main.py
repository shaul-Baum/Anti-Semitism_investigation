from Loader import Loader
from Cleanr import Cleanr
from Calculations import Calculations
dict_0 ={}
data_frame = Loader()
data_clan = Cleanr(data_frame.gat_dataframe())
Calculations =Calculations(data_clan.gat_dataframe())
number_of_anti_Semites = Calculations.classification_by_anti_Semitism()
dict_0["total_tweets"] ={}
dict_0["total_tweets"]["antisemitic"] =int(number_of_anti_Semites[1])
dict_0["total_tweets"]["non_antisemitic"] =int(number_of_anti_Semites[0])
dict_0["total_tweets"]["total"] =int(number_of_anti_Semites["__total__"])
dict_0["common_words"] ={}
dict_0["common_words"]["total"] =Calculations.max_words()
dict_0["average_length"] =Calculations.amount_of_all_words()
dict_0["average_length"]["longest_3_tweets"]=Calculations.longest_3_tweets()
dict_0["uppercase_words"] =Calculations.upper()
print(dict_0)