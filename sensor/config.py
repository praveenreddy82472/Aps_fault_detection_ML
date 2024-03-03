import pymongo
import pandas as pd
import json 
import ssl
from dataclasses import dataclass

#provide the mongodb localhost url to conncet python to mongodb
import os


@dataclass
class EnvironmentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")
    aws_access_key_id:str  = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key:str = os.getenv("AWS_SECRET_ACCESS_KEY")

env_var  = EnvironmentVariable()

mongo_client = pymongo.MongoClient("mongodb+srv://tumatipraveenreddy23:Praveen987@cluster0.wjup0bh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
TARGET_COLUMN = "class"



