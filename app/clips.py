import requests
import config
import execute

def get_clips(payload,player_list):
    """ extract json information of clips
        Input: amount, days
        Output: requests object if success or status code if fail
    """
    # current_oauth = 'Bearer ' + config.live_oauth_code
    # headers = {'Client-ID':config.client_id,'Authorization':current_oauth}
    # payload = {'game_id':config.game_id,'first':amount}
    # r = requests.get(config.clips_url,headers=headers,params=payload)
    # if r.status_code != 200:
    #     return r.status_code
    # else:    
    #     return r
    
    response_object = execute.run_get(config.clips_url,payload) 
    list_of_data = response_object.json()['data']
    nlod = get_game_specific_clip_data(list_of_data,player_list)
    return nlod

def clean_clip_data(clip_list):
    """ only keep important info from json
        Input: clip_list
        Output: clean_clip_list
    """
    clean_clip_list = []
    
    return clean_clip_list

def get_game_specific_clip_data(clip_list,player_list):
    """ get list of clips from a specific broadcaster list
        Input: json_object, player_list
        Output: specific_clip_list
    """
    specific_clip_list = []
    for i in clip_list:
        if i["broadcaster_name"] in player_list:
            specific_clip_list.append(i)
        else: 
            pass
    print(len(clip_list))
    print(len(specific_clip_list))
    return specific_clip_list