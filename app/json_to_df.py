# %%
import pandas as pd
import json


# wget https://repo.continuum.io/archive/Anaconda3-2020.02-Linux-x86_64.sh
# /home/aryanwagadre/workstation/TwitchApi/jsons
path = '/home/aryanwagadre/workstation/TwitchApi/jsons/anomaly_live_test.json'

def open_json(path):
    with open(path) as json_file:
        data = json.load(json_file)
    return data

def json_to_df(data):
    df = pd.DataFrame(pd.json_normalize(data))    
    return df

def return_ten_latest_clip_links(df):
    #sort ascending by time given in url in vod
    result  = 0 
    return result

def json_to_dict():
    return 0


if __name__=="__main__": 
    main() 

# %%

###########################################################
# func: get clips of the week
#     input: game, subcatagory in game string (NoPixel)
#     output: list of urls

def main():
    # retrieve data of all the CLIPS from this weeks streams
    # only keep ones with right subcatagory (check in vod names)
    # save in a dict
    # find best top 20 clips
    # save in a dict
    
    data = open_json(path)
    df = json_to_df(data)

  
    