import pandas as pd
import re

df = pd.read_csv(r'C:\Users\Bhavani_Sai\PycharmProjects\OnlineClasses\ViswamDegreeCollege\DataEngineeProject\Final Cars Data2.csv')
# print(df)

def string_cleaner(x):
    x = x.replace(' Seater', '')
    print(x)
    return x
def vaiant_cleaner(x):
    x = x.replace(' variants', '').replace('/','\\')
    return x

def price_cleaner(x):
    x = re.sub('[^0-9\.]', '', x)
    return x

df['Seat_Updated'] = df['Seat'].apply(string_cleaner)
df['Variant_update'] = df['Variant'].apply(vaiant_cleaner)
df['Offer Price_update'] = df['Offer Price'].apply(price_cleaner)
df['Original Price_update'] = df['Original Price'].apply(price_cleaner)


df.to_csv('Cleaned Data.csv', index=False)