import numpy as np
import pandas as pd
import warnings
import re
warnings.filterwarnings('ignore')
from pandas import ExcelWriter
import os


class TextLoader(object):

    def __init__(self, device='cuda:0', input=None):
  
        self.device = device
        self.input= input    
    
    def clean_text(self, text):

        text = re.sub(r"(#[\d\w\.]+)", '', text)
        text = re.sub(r"(@[\d\w\.]+)", '', text)
        text = re.sub(r"http\S+", "", text)
        text = re.sub(r'(@.*?)[\s]', ' ', text)
        text = re.sub(r'&amp;', '&', text)
        text = re.sub(r"(?:\@|https?\://)\S+", "", text) #remove links and mentions
        text = re.sub(r'\s+', ' ', text).strip()
        text= re.sub(r'[0-9]+', '',text)

        cleaned_text = ' '.join([word for word in text.split()])
    
        return cleaned_text
    

    
    def load_data(self):       
        
        df = pd.read_csv(self.input)


        return df



    def save_csv(self, df):
      
        df.to_csv('emotion_clean_text.csv', sep=',')








       