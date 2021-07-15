import os
import pandas as pd
from pydub import AudioSegment, audio_segment
from gtts import gTTS

def texttospeech(text,filename):
    mytext=str(text)
    language='hi'
    myobj=gTTS(text=mytext,lang=language,slow=True)
    myobj.save(filename)

def mergeAudio(audios):
    combined=AudioSegment.empty()
    for audio in audios:
        combined+=AudioSegment.from_mp3(audio)
    return combined

def generateskeleton():
    audio = AudioSegment.from_mp3("railway2.mp3")

    # 1 generating yatrigan kripiya dhayn de
    start = 0
    end = 2500
    audioProcessed = audio[start:end]
    audioProcessed.export("1.mp3",format="mp3")

    # 5 generate se chalkr
    # audio = AudioSegment.from_mp3("railway2.mp3")
    start = 6300
    end = 7300
    audioProcessed = audio[start:end]
    audioProcessed.export("5.mp3",format="mp3")

    # 7 ke raste
    # audio = AudioSegment.from_mp3("railway2.mp3")
    start = 3800
    end = 4700
    audioProcessed = audio[start:end]
    audioProcessed.export("7.mp3",format="mp3")

    # 9 jane wali 
    # audio = AudioSegment.from_mp3("railway2.mp3")
    start = 8500
    end = 9700
    audioProcessed = audio[start:end]
    audioProcessed.export("9.mp3",format="mp3")

    # 10 platform 
    # audio = AudioSegment.from_mp3("railway2.mp3")
    start = 9800
    end = 11100
    audioProcessed = audio[start:end]
    audioProcessed.export("10.mp3",format="mp3")

    # 12 pr khadi h
    # audio = AudioSegment.from_mp3("railway2.mp3")
    start = 11500
    end = 13000
    audioProcessed = audio[start:end]
    audioProcessed.export("12.mp3",format="mp3")


def generateAnnouncement(filename):
    df=pd.read_excel(filename)
    print(df)
    for index,item in df.iterrows():
        # 2 generate train number
        texttospeech(item['Train No'],'2.mp3')
        # 3 train name
        texttospeech(item['Train Name'],'3.mp3')
        # 4 from city
        texttospeech(item['From'],'4.mp3')
        # 6 via city
        texttospeech(item['Via'],'6.mp3')
        # 8 to city
        texttospeech(item['To'],'8.mp3')
        # 11 platform no
        texttospeech(item['Plateform No'],'11.mp3')

        audios=[f"{i}.mp3" for i in range(1,13)]
        announcement=mergeAudio(audios)
        announcement.export(f"accouncement_{index+1}.mp3",format="mp3")




if __name__ == '__main__':
    print("Generating Skeleton")
    generateskeleton()
    print("Now Generating Announcement....")
    generateAnnouncement("train.xls")
    