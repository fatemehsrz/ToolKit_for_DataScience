
from utils import TextLoader
import argparse

if __name__== "__main__":
 
   data_utils = TextLoader(input= './data/emotion_dataset.csv', device= 'cpu' ) 
   parser= argparse.ArgumentParser( description= "load data")
   parser.add_argument ("action_type", help= "action_type" )

   args= parser.parse_args()

   if args.action_type=="cleantext":
       
       df= data_utils.load_data()
       df["Text"] = df["Text"].apply(lambda x: data_utils.clean_text(x))
       print("text" , df["Text"].tolist()[:3])                              
       

   if args.action_type=="savefile":
       
       df= data_utils.load_data()
       df["Text"] = df["Text"].apply(lambda x: data_utils.clean_text(x))
      
       data_utils .save_csv(df)   





   
