
from youtube_dl import YoutubeDL
# Sample 1: Download a single youtube video
dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=dH3GlkIfScY']) # Remember to put your video in a list, eventhough one video is downloaded

# Sample 2: Download multiple youtube videos
d1 = YoutubeDL()
d1.download(['https://www.youtube.com/watch?v=XqZsoesa55w','https://www.youtube.com/watch?v=C4yYU4r1NgA'])
# Sample 3: Download audio
options = {
    'format':'bestaudo/audio',
}
d2 = YoutubeDL()
d2.download(['https://www.youtube.com/watch?v=gRs_9Tt8lKk'])

# Sample 4: Search and then download the first video
op2 = {
    'default_search': 'ytsearch',
    'max_downloads':1
}
d3 = YoutubeDL(options)
d3.download(['con điên TAMKA PKL'])
# Sample 5: Search and then download the first audio
options = {
    'default_search': 'ytsearch',
    'max_downloads': 1,
    'format': 'bestaudio/audio'
}
d4 = YoutubeDL(options)
d4.download(['baby shark tik tok'])
