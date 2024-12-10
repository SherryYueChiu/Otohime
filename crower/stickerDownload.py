import requests
import os

startId=8344563
endId=8344563
folderName='ㄇㄚˊ幾兔（動幾來2）'

os.makedirs('./allSticker/'+folderName+'/',exist_ok=True)

for stickerId in range(startId,endId+1):
    stickerId=str(stickerId)
    # low resolution
    # url='https://stickershop.line-scdn.net/stickershop/v1/sticker/'+stickerId+'/android/sticker.png'
    # high resolution
    url='https://stickershop.line-scdn.net/stickershop/v1/sticker/'+stickerId+'/iPhone/sticker@2x.png'
    # animation
    # url='https://stickershop.line-scdn.net/stickershop/v1/sticker/'+stickerId+'/iPhone/sticker_animation@2x.png'
    # message sticker
    # url='https://stickershop.line-scdn.net/stickershop/v1/sticker/'+stickerId+'/iPhone/base/plus/sticker@2x.png'
    r=requests.get(url)
    with open('./allSticker/'+folderName+'/'+stickerId+'.png','wb') as f:
        f.write(r.content)