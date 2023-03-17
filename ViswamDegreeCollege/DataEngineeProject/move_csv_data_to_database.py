import pandas as pd
import sqlalchemy as db


df = pd.read_csv(r'C:\Users\Bhavani_Sai\PycharmProjects\OnlineClasses\ViswamDegreeCollege\DataEngineeProject\Cleaned Data.csv')


engine = db.create_engine('mysql+mysqldb://bindu:Bindu_123bindu@localhost/viswam_degree_college')

df.to_sql('ackodrive_cars_data', engine, if_exists='append', index=False)
# print(df)