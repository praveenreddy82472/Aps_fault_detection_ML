import pandas as pd
import json 
from dataclasses import dataclass
from pymongo import MongoClient, server_api
import certifi
ca = certifi.where()
#provide the mongodb localhost url to conncet python to mongodb
import os


@dataclass
class EnvironmentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")
    aws_access_key_id:str  = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key:str = os.getenv("AWS_SECRET_ACCESS_KEY")

env_var  = EnvironmentVariable()
mongo_client = MongoClient(env_var.mongo_db_url,server_api=server_api.ServerApi('1'), tlsCAFile=ca)

TARGET_COLUMN = "class"




