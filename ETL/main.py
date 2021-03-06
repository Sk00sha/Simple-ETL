from sqlite3.dbapi2 import connect
from numpy import True_
from pandas.core.reshape.merge import merge
import requests
import pandas as pd
from sqlalchemy import create_engine
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context


"""extract phase"""
#INFECTED DF
request= requests.get('https://data.korona.gov.sk/api/ag-tests/in-slovakia')
jsonify_tests=request.json()["page"]
infected_dataframe=pd.DataFrame(columns=['id','positivity_rate','date_updated','positive','negative']
,index=range(len(jsonify_tests)))

#REGION Dataframe
reg_dataframe=pd.read_json('https://data.korona.gov.sk/api/regions')

#BED CAPACITY DF
bed_capacity= requests.get("https://data.korona.gov.sk/api/hospital-beds/by-region")
jsonify_bed_capacity=bed_capacity.json()["page"]
free_beds_dataframe=pd.DataFrame(columns=['id','region_id','free_all','capacity_covid',
'occupied_jis_covid','occupied_oaim_covid','occupied_o2_covid',
'occupied_other_covid','updated_at'],index=range(len(jsonify_bed_capacity)))

#HOSPITAL STAFF DF
hospital_staff=requests.get("https://data.korona.gov.sk/api/hospital-staff")
jsonify_staff=hospital_staff.json()["page"]
staff_dataframe=pd.DataFrame(columns=['id','hospital_id','oow_doctors','oow_nurses','oow_other','updated_at'],index=range(len(jsonify_staff)))



"""Transform phase"""
for count,value in enumerate(jsonify_bed_capacity):

     free_beds_dataframe.loc[count].id=value["id"]
     free_beds_dataframe.loc[count].region_id=value["region_id"]
     free_beds_dataframe.loc[count].free_all=value["free_all"]
     free_beds_dataframe.loc[count].capacity_covid=value["occupied_jis_covid"]
     free_beds_dataframe.loc[count].occupied_oaim_covid=value["occupied_oaim_covid"]
     free_beds_dataframe.loc[count].occupied_o2_covid=value["occupied_o2_covid"]
     free_beds_dataframe.loc[count].occupied_other_covid=value["occupied_other_covid"]
     free_beds_dataframe.loc[count].updated_at=value["updated_at"]


for count,value in enumerate(jsonify_tests):
    infected_dataframe.loc[count].id=value["id"]
    infected_dataframe.loc[count].positivity_rate=value["positivity_rate"]
    infected_dataframe.loc[count].date_updated=value["updated_at"]
    infected_dataframe.loc[count].positive=value["positives_count"]
    infected_dataframe.loc[count].negative=value["negatives_count"]

for count,value in enumerate(jsonify_staff):
    staff_dataframe.loc[count].id=value["id"]
    staff_dataframe.loc[count].hospital_id=value["hospital_id"]
    staff_dataframe.loc[count].oow_doctors=value["out_of_work_ratio_doctor"]
    staff_dataframe.loc[count].oow_nurses=value["out_of_work_ratio_nurse"]
    staff_dataframe.loc[count].oow_other=value["out_of_work_ratio_other"]
    staff_dataframe.loc[count].updated_at=value["updated_at"]



print(infected_dataframe)
print(free_beds_dataframe)
print(staff_dataframe)

#merging so that we know what is the name of the ragion that the record is about
merge_beds_region=pd.merge(free_beds_dataframe,reg_dataframe,how="inner",left_on="region_id",right_on="id")

#when merging, two columns with same name get renamed to id_x and id_y for example
merge_beds_region=merge_beds_region.rename(columns={"id_x": "id"})
"""Load phase"""

engine = create_engine('sqlite:///backend/covid.db', echo=False)


infected_dataframe.to_sql('TESTS', con=engine, if_exists='replace',index=False)
merge_beds_region.to_sql('HOSPITALS', con=engine, if_exists='replace',index=False)
staff_dataframe.to_sql('HOSPITAL_STAFF',con=engine, if_exists='replace',index=False)
