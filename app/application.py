##############################################################################################################################################################
#   This app extracts clip urls from twitch api, download selected urls as videos, combines the videos in selected order and uploads them on youtube
#       the app should compute in aws while interacting with twitch api and youtube api
#
##############################################################################################################################################################
# %%
# imports
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
        payload = {'game_id':config.game_id,'first':50}
        # print(execute.run_get(config.clips_url,payload))
        temp = clips.get_clips(payload,channel_list.nopixel_list)
        # print(list_of_data)
        # print(temp.json()['pagination'])

        # searching for catagories is available.
        # Search Channels can be use to find queries like 'nopixel'
        for i in temp:
            print(i["broadcaster_name"])

if __name__=="__main__": 
	main() 


# %%
