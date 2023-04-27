import sys
import os
import pandas as pd
from Insurance.exception import InsuranceException
from Insurance.utils import load_object
from Insurance.entity.artifact_entity import *





class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
           df = pd.DataFrame(CustomData, index=[0])

           df['region'] = encoder.transform(df['region'])
           df['sex'] = df['sex'].map({'male':1, 'female':0})
           df['smoker'] = df['smoker'].map({'yes':1, 'no':0})

           df = transformer.transform(df)
# dtrain = xg.DMatrix(df)
           y_pred = model.predict(df)
        
        except Exception as e:
            raise InsuranceException(e,sys)



class CustomData:
    def __init__(  self,
        age: int,
        sex: str,
        bmi:int,
        children: int,
        smoker: str,
        region: str,
        ):

        self.age = age

        self.sex = sex

        self.bmi = bmi

        self.children = children

        self.smoker = smoker

        self.region = region

        

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "age": [self.age],
                "sex": [self.sex],
                "bmi": [self.bmi],
                "children": [self.children],
                "smoker": [self.smoker],
                "region": [self.region],
               
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise InsuranceException(e, sys)
