from sensor.entity import artifact_entity,config_entity
from sensor.exception import SensorException
from sensor.logger import logging
from scipy.stats import ks_2samp
import os,sys
import pandas as pd
from typing import Optional



class DataValidation:
    
    
    def __init__(self,data_validation_congif:config_entity.DataValidationConfig):
        try:
            logging.info(f"{'>>'*20} Data validation {'<<'*20}")
            self.data_validation_config  = data_validation_congif
            self.validation_error = dict()
        except Exception as e:
            raise SensorException(e,sys)
        
    
    def drop_missing_values_columns(self,df:pd.DataFrame,)->Optional[d.DataFrame]:
        """
        This function  will drop column whihch contains missing value more than specified threshold
        
        df:Accepts a Pandas DataFrame
        threshold:percentage criteria to drop a column 
        ===============================================================================================
        returns pandas Dataframe  if atleast a sinle column is available after missing columns drop else NoNE
           
        """
        try:
            threshold = self.data_validation_config.missing_threshold
            null_report = df.isna().sum()/df.shape[0]
            #selecting column name which contains null
            logging.info(f"selecting column name which contains null above to {threshold}")
            drop_column_names = null_report[null_report>threshold].index

            logging.info(f"Columns to drop: {list(drop_column_names)}")
            self.validation_error[report_key_name]=list(drop_column_names)
            df.drop(list(drop_column_names),axis=1,inplace=True)
            
            
            #return Nonen no column left
            if len(df.columns)==0:
                return None
            return df
        except Exception as e:
            raise SensorException(e,sys)
        
     
    def is_required_colums_exists(self,base_df:pd.DataFrame,current_df:pd.DataFrame)->bool:
        try:
            base_columns = base_df.columns
            current_columns = current_df.columns
            
            missing_columns= []
            for base_column in base_columns:
                if base_column in current_columns:
                    missing_columns.append(base_column)
                    
        
            if len(missing_columns)>0:
                self.validation_error["Missing columns"]=missing_columns
                return False
            return True                   
        except Exception as e:
            raise SensorException(e,sys)
    
    def initiate_data_validation(self)->artifact_entity.DataValidationArtifact:
        
        pass
    
    