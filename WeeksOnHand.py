import streamlit as st
import pandas as pd
import sqlalchemy

file_date = pd.Timestamp.today().strftime('_%Y%m%d%H%M%S')
username = 'D365FO'
password = 'g3Vj0dbiKS8Mhqz7lLbt'
server = 'az06gl-prd-azsql01.database.windows.net'
database = 'D365FO_Operations_Prod'

conn_str = (
    f"mssql+pyodbc://{username}:{password}@{server}/{database}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
)

query = "select * from dbo.DIO_BH_WeeksOnHandTbl"
engine = sqlalchemy.create_engine(conn_str)
df = pd.read_sql_query(query,engine)
df_tofile = df.to_excel(sheet_name='WOH')

st.download_button(
    label="Download Weeks On-Hand Report",
    data=df_tofile,
    file_name=f'WeeksOnHand{file_date}.xlsx',
    mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
)
