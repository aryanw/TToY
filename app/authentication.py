##############
# module contains methods for returning appropriate requests
import requests
import config

# get new oauth code
def get_oauth():
    return 0

def verify_oauth():
    """ verify an oauth code
        Input: None
        Output: 1 if not expired, 0 if expired, error code if error
    """
    current_oauth = 'OAuth ' + config.live_oauth_code
    headers = {'Authorization':current_oauth}
    r = requests.get(config.validate_url,headers=headers)
    if r.status_code != 200:
        return r.status_code
    else:    
        r_dict = r.json()
        exp_in = r_dict["expires_in"]
        return 0 if exp_in <= 0 else 1

# refresh oauth code
def refresh_oauth(oauth):
    ## have to be implemented
    '''POST https://id.twitch.tv/oauth2/token
    --data-urlencode
    ?grant_type=refresh_token
    &refresh_token=<your refresh token>
    &client_id=<your client ID>
    &client_secret=<your client secret>'''
    return 0

