##############################################################################################################################################################
#   This app extracts clip urls from twitch api, download selected urls as videos, combines the videos in selected order and uploads them on youtube
#       the app should compute in aws while interacting with twitch api and youtube api
#
##############################################################################################################################################################
# %%
# imports
from datetime import datetime, timedelta
from tzlocal import get_localzone

import authentication
import clips
import config
import channel_list
import execute
# funcs
def main():
    if not authentication.verify_oauth():
        ## have to add refresh_oauth
        print('loss') 
    else:
        print('boss')
        # verified
        # get me top 20 clips of last 5 weeks
        """
        while ended_at is not of current date
            get 100 clips into list (get url, broadcaster_id,broadcaster_name, video_id, language, view_count, created_at)
            ** if videos_id is not available, verifying nopixel is difficult.
                have to use brodcaster_id and search previous broadca
            ** so i will check if nopixel streamer from hardcoded config
            clean list
            add to master list 
            increase pagination
        """
        day = timedelta(1)
        local_tz = get_localzone()
        ended_at = datetime.now(local_tz)    # todays datetime
        started_at = local_tz.normalize(ended_at - 7*day) # a week before today
        payload = {'game_id':config.game_id,'first':50,'started_at':execute.get_date_string(started_at),'ended_at':execute.get_date_string(ended_at)}
        print(started_at,ended_at)
        
        # print(execute.run_get(config.clips_url,payload))
        temp = clips.get_clips(payload,channel_list.nopixel_list)
        # print(list_of_data)
        # print(temp.json()['pagination'])

        # searching for catagories is available.
        # Search Channels can be use to find queries like 'nopixel'
        for i in temp:
            print(i["broadcaster_name"],i['created_at'])

if __name__=="__main__": 
	main() 


# %%
