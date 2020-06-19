#################################################################################################
#   This app extracts clip urls from twitch api, combines the videos and uploads them on youtube
#       the app should compute in aws while calling twitch api and youtube api
#  
# check authentication
    # verify oauth  {COMPLETED}
    # refresh oauth if expired
# get urls of top clips 
    # extract all urls depending on description {INPROGRESS}
    # select appropriate urls
    # classify urls
# combine clips into a video
    # download clips from urls
    # add streamer names
    # combine them into a compilation (will contain the choosing logic)
    # add intro and outro
# upload the video on youtube

# have to implement rate_limit (code 429 returns if too many requests) 