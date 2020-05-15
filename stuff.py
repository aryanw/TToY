print("python is on ")  


"id": "32982",
"name": "Grand Theft Auto V",
"box_art_url": "https://static-cdn.jtvnw.net/ttv-boxart/Grand%20Theft%20Auto%20V-{width}x{height}.jpg"
            
curl -H 'Client-ID: b97x1nm62wdg8s975hoc8m57ag2t0q' \
-H 'Authorization: Bearer 7g4vp1vtxptdok1tsconaozhgpp3ba' \
-X GET 'https://api.twitch.tv/helix/streams?user_name=summit1g'



curl -H 'Client-ID: b97x1nm62wdg8s975hoc8m57ag2t0q' \
-H 'Authorization: Bearer 7g4vp1vtxptdok1tsconaozhgpp3ba' \
-X GET 'https://api.twitch.tv/helix/analytics/games?first=5'

curl -H 'Client-ID: b97x1nm62wdg8s975hoc8m57ag2t0q' \
-X GET 'https://api.twitch.tv/helix/games?id=1234&first=5'

# get top games
curl -H 'Client-ID: b97x1nm62wdg8s975hoc8m57ag2t0q' \
-X GET 'https://api.twitch.tv/helix/games/top'
# get gta
curl -H 'Client-ID: b97x1nm62wdg8s975hoc8m57ag2t0q' \
-X GET 'https://api.twitch.tv/helix/games?id=32982' 
# get stream
curl -H 'Client-ID: b97x1nm62wdg8s975hoc8m57ag2t0q' \
-X GET 'https://api.twitch.tv/helix/streams?first=2&game_id=32982'
# get clip
curl -H 'Client-ID: b97x1nm62wdg8s975hoc8m57ag2t0q' \
-X GET 'https://api.twitch.tv/helix/clips?broadcaster_id=69759951'

# v5 tests
curl -H 'Accept: application/vnd.twitchtv.v5+json' \
-H 'Client-ID: b97x1nm62wdg8s975hoc8m57ag2t0q' \
-X GET 'https://api.twitch.tv/kraken/users?login=dallas,dallasnchains'

# get clips v5
curl -H 'Accept: application/vnd.twitchtv.v5+json' \
-H 'Client-ID: b97x1nm62wdg8s975hoc8m57ag2t0q' \
-X GET 'https://api.twitch.tv/kraken/clips/HonorableMoralFiddleheadsOhMyDog' > clipDataTest_v5.json

#get top clips game
curl -H 'Accept: application/vnd.twitchtv.v5+json' \
-H 'Client-ID: b97x1nm62wdg8s975hoc8m57ag2t0q' \
-X GET 'https://api.twitch.tv/kraken/clips/top?game=Grand Theft Auto V&period=day&limit=1&language=en'

#get top clips channel
curl -H 'Accept: application/vnd.twitchtv.v5+json' \
-H 'Client-ID: b97x1nm62wdg8s975hoc8m57ag2t0q' \
-X GET 'https://api.twitch.tv/kraken/clips/top?channel=anomaly&period=day&language=en'

#get game
curl -H 'Accept: application/vnd.twitchtv.v5+json' \
-H 'Client-ID: b97x1nm62wdg8s975hoc8m57ag2t0q' \
-X GET 'https://api.twitch.tv/kraken/search/games?query=grand'

#get channel names
curl -H 'Accept: application/vnd.twitchtv.v5+json' \
-H 'Client-ID: b97x1nm62wdg8s975hoc8m57ag2t0q' \
-X GET 'https://api.twitch.tv/kraken/search/channels?query=dasmehdi' > single_channel_in_gta.json

# get vids of a channel v5
curl -H 'Accept: application/vnd.twitchtv.v5+json' \
-H 'Client-ID: b97x1nm62wdg8s975hoc8m57ag2t0q' \
-X GET 'https://api.twitch.tv/kraken/channels/69759951/videos' > vader_video_list.json

# get clip tests v5
curl -H 'Accept: application/vnd.twitchtv.v5+json' \
-H 'Client-ID: b97x1nm62wdg8s975hoc8m57ag2t0q' \
-X GET 'https://api.twitch.tv/kraken/clips/MushyVenomousSnakeOpieOP' > test.json

https://clips.twitch.tv/OutstandingAbrasiveChamoisKreygasm
https://clips.twitch.tv/HardBlightedLyrebirdTBCheesePull

# clip i created
curl -H 'Accept: application/vnd.twitchtv.v5+json' \
-H 'Client-ID: b97x1nm62wdg8s975hoc8m57ag2t0q' \
-X GET 'https://api.twitch.tv/kraken/clips/HardBlightedLyrebirdTBCheesePull' > clip_i_made_v5.json