import requests
import os

folderName='ㄇㄚˊ幾兔－表情貼'
sticonId='5cbc35d6040ab16170b524e0'
startId=39
endId=40

os.makedirs('./allSticker/'+folderName+'/',exist_ok=True)

for stickerId in range(startId,endId+1):
    stickerId=str(stickerId)
    # static
    url='https://stickershop.line-scdn.net/sticonshop/v1/sticon/'+sticonId+'/iPhone/'+stickerId.zfill(3)+'.png'
    # animation
    # url='https://stickershop.line-scdn.net/sticonshop/v1/sticon/'+sticonId+'/iPhone/'+stickerId.zfill(3)+'_animation.png'
    r=requests.get(url)
    with open('./allSticker/'+folderName+'/'+stickerId+'.png','wb') as f:
        f.write(r.content)