from google.cloud import storage
import os
import pandas as pd
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '' #give the location of key json file ' 

storage_client = storage.Client()
buckets = list(storage_client.list_buckets())
bucket = storage_client.get_bucket("") # give your storage bucket name

print('Start')

def upload_catalogcsv():
	blob = bucket.blob('/Data/CATALOG.csv')
	blob.upload_from_filename('C:/Users/rishv/OneDrive/Northeastern/SEM4/BigDataAnalytics/Assignments/Assignment1/CATALOG.csv')
	print('upload catalog csv complete')

#df=pd.read_csv('C:/Users/rishv/OneDrive/Northeastern/SEM4/BigDataAnalytics/Assignments/Assignment1/StormEvents_details-ftp_v1.0_d2019_c20210223.csv')
#df1 = df.replace(',',' ', regex=True)
#df1.to_csv('C:/Users/rishv/OneDrive/Northeastern/SEM4/BigDataAnalytics/Assignments/Assignment1/StormEvents.csv',index=False)

def upload_stormcsv():
	blob = bucket.blob('/Data/StormEvents_Loc.csv')
	blob.upload_from_filename('C:/Users/rishv/OneDrive/Northeastern/SEM4/BigDataAnalytics/Assignments/Assignment1/StormEvents_locations-ftp_v1.0_d2018_c20201216.csv')
	print('upload storm csv complete')


upload_catalogcsv()
upload_stormcsv()






