import pymongo
import pandas as pd
import json 

client = pymongo.MongoClient("mongodb://localhost:27017")


DATA_FILE_PATH = "D:\Ineuron\ML Projects\AirPressureSystem\Airps_failure_training_set1.csv"
DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor"


if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and Columns:{df.shape}")
    
    #convert dataframe to josn so that we can dump theese record in mongodb
    
    df.reset_index(drop=True,inplace=True)
    
    json_record  = list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    
    #insert converted json record to mongodb
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
    
    
    
    
