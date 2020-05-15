# %%
import pandas as pd
import json

# ask for name
# get recent clips from v5 for last 5 hours
    # call get top clips
    # count clips
    # save in df
    # if clips more than zero
    # loop
# get their timestamps
#
#
#
#
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
    
data = open_json(path)
df = json_to_df(data)


# %%
