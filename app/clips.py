import requests
import config
def get_clips(amount,days):
    """ extract json information of clips
        Input: amount, days
        Output: list of json dictionaries
    """
    current_oauth = 'Bearer ' + config.live_oauth_code
    headers = {'Client-ID':config.client_id,'Authorization':current_oauth}
    payload = {'game_id':config.game_id,'first':amount}
    r = requests.get(config.clips_url,headers=headers,params=payload)
    if r.status_code != 200:
        return r.status_code
    else:    
        return r

#print(get_clips(2,2))

"""
curl -H 'Client-ID: b97x1nm62wdg8s975hoc8m57ag2t0q' \
    -H 'Authorization: OAuth qczgwwopz7ezmbodw42x1uo88pgjv1' \
    -X GET 'https://api.twitch.tv/helix/clips?game_id=32982&first=2'
"""