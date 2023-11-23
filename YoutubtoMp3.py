import sys
from pytube import YouTube
from datetime import datetime


def shorten_title(title, max_length):
    # 제목을 지정된 최대 길이에 맞추어 자릅니다.
    return title if len(title) <= max_length else title[: max_length - 3] + "..."


def download_youtube_audio(url):
    base_path = ""
    path = "D:\deeplearning\sjcu_working\20232\Resource\Audio"
    output_path = base_path + path

    output_path="D:/deeplearning/sjcu_working/20232/Resource/Audio/"
    # 파일 이름에 사용할 수 있는 최대 길이를 지정합니다.

    yt = YouTube(url)
    title = yt.title

    max_title_length = 100
    short_title = shorten_title(title, max_title_length)
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    #now=""
    filename = f"{now} - {short_title}.mp3"
    filename = filename.replace(" ", "").replace("|", "")

    audio_stream = yt.streams.filter(only_audio=True).first()
    print(output_path)
    filename = filename.replace(" ", "").replace("|", "")
    audio_stream.download(output_path, filename=filename)
   
    #print(f"{filename} has downloaded at {path}")



if __name__ == "__main__":

    #url = sys.argv[1]
    url="https://youtu.be/7vYWRlsmOVQ?si=n9FDHQRz7WcfgLMH"       

    download_youtube_audio(url)

    ''''
    if len(sys.argv) < 2:
        print("사용법: python extract_audio.py [YouTube URL]")
    else:
        url = sys.argv[1]
        url="https://youtu.be/7vYWRlsmOVQ?si=n9FDHQRz7WcfgLMH"       

        download_youtube_audio(url)

        '''