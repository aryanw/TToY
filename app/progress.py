#################################################################################################
#   This app extracts clip urls from twitch api, combines the videos and uploads them on youtube
#       the app should compute in aws while calling twitch api and youtube api
#  
# check authentication
    # verify oauth  COMPLETED
    # refresh oauth if expired
# get urls of top clips 
    # generate command for linux using client_id and oauth
    # run command on linux
    # save output in a dict
    # extract urls and views from all the clips
# combine clips into a video
    # download clips from urls
    # add streamer names
    # combine them into a compilation (will contain the choosing logic)
    # add intro and outro
# upload the video on youtube