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

        temp = clips.get_clips(50,2)
        list_of_data = temp.json()['data'] # list of json info
        # print(list_of_data)
        # print(temp.json()['pagination'])


        new_list = clips.get_game_specific_clip_data(list_of_data,config.nopixel_list)
        for i in new_list:
            print(i["broadcaster_name"])
if __name__=="__main__": 
	main() 


# %%
