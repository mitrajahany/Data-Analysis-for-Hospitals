import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
general, prenatal, sports = [pd.read_csv(r'test\general.csv'),
                             pd.read_csv(r'test\prenatal.csv'),
                             pd.read_csv(r'test\sports.csv')]

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
# pd.set_option('display.max_rows', None)
sports.columns = prenatal.columns = general.columns
demo = pd.concat([general, prenatal, sports], ignore_index=True)
demo.drop(columns='Unnamed: 0', inplace=True)
demo = demo.dropna(how='all')
demo = demo.fillna(0)
demo['gender'] = demo['gender'].replace({'man': 'm', 'male': 'm', 'woman': 'f', 'female': 'f', 0: 'f'})
demo.children = demo.children.astype(int)
demo.set_index('hospital', inplace=True)
d = demo.loc[['general', 'sports'], ['age', 'bmi', 'diagnosis']]

print(demo.describe())
