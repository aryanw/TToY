import requests
import config
import rfc3339

def run_get(url,payload):
    """ extract json information of clips
        Input: amount, days
        Output: requests object if success or status code if fail
    """
    current_oauth = 'Bearer ' + config.live_oauth_code
    headers = {'Client-ID':config.client_id,'Authorization':current_oauth}
    current_payload = payload
    r = requests.get(url,headers=headers,params=current_payload)
    if r.status_code != 200:
        return r.status_code
    else:    
        return r

def get_date_string(date_object):
  return rfc3339.rfc3339(date_object)