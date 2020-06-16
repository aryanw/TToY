##############
# module contains methods for returning appropriate requests
import requests
import config

# get new oauth code
def get_oauth():
    return 0
# verify an oauth code
def verify_oauth(oauth):
    # curl -H "Authorization: OAuth qczgwwopz7ezmbodw42x1uo88pgjv1" https://id.twitch.tv/oauth2/validate
    url = 'https://id.twitch.tv/oauth2/validate'
    ## have to change hard coded header
    headers = {'Authorization':'OAuth qczgwwopz7ezmbodw42x1uo88pgjv1'}
    r = requests.get(url,headers=headers)
    r_dict = r.json()
    ## have to check if return code is not a 200
    exp_in = r_dict["expires_in"]
    if exp_in <= 0:
        return 0
    else:
        return 1

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


def main():
    print(verify_oauth(config.live_oauth_code))

if __name__=="__main__": 
    main() 