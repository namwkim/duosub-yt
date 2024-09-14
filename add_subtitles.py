from concurrent.futures import thread
from copyreg import constructor
import sys
# from pytube import YouTube
from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip

korean_generator = lambda txt: TextClip(txt, font='NanumGothic-ExtraBold.ttf', fontsize=36, color='white')#.set_position((5,500))#bg_color="black", 
english_generator = lambda txt: TextClip(txt, font='Arial', fontsize=28, color='white')#.set_position((5,500))#bg_color="black", 
if __name__ == "__main__":
    # if len(sys.argv)>0:
    #     print("Download URL:", sys.argv[1])
        # YouTube('https://youtu.be/9bZkp7q19f0').streams.first().download()

    # for x in TextClip.list('font'):
    #     if "Nanum" in x:
    #         print(x)

    sub = SubtitlesClip("[English] HOW DEBT CAN GENERATE INCOME -ROBERT KIYOSAKI.srt", english_generator)
    sub_kor = SubtitlesClip("[Korean] HOW DEBT CAN GENERATE INCOME -ROBERT KIYOSAKI.srt", korean_generator)
    sub = sub.set_position(("center", 607))
    sub_kor =  sub_kor.set_position(("center", 558))

    clip = VideoFileClip("HOW DEBT CAN GENERATE INCOME -ROBERT KIYOSAKI.mp4")
    clip = clip.resize((1280, 720))

    # audio = AudioFileClip("Steve Jobs on Failure.mp4")
    # clip.audio = audio
    # print(list(sub_kor))
    subtitles = list(sub_kor)
    # bgr_clips = []
    # for span in list(sub_kor):
    #     sub_bgr = ImageClip("subtitle_background_1280x720.png")
    #     sub_bgr.set_start(span[0][0])
    #     sub_bgr.set_end(span[0][1])    
    #     bgr_clips.append(sub_bgr)
    bgr_clips = []
    sub_bgr = ImageClip("subtitle_background_1280x720.png")
    curr = subtitles.pop(0)
    print("start",curr[0][0])
    sub_bgr = sub_bgr.set_start(curr[0][0])
    while len(subtitles)>0:
        
        next = subtitles.pop(0)
        # print(next[0][0], curr[0][1])
        if (next[0][0] - curr[0][1])>2:        
            sub_bgr = sub_bgr.set_end(curr[0][1])
            print(sub_bgr.start, "-", sub_bgr.end)
            bgr_clips.append(sub_bgr)

            sub_bgr = ImageClip("subtitle_background_1280x720.png")
            sub_bgr = sub_bgr.set_start(next[0][0])

        curr = next
    
    sub_bgr = sub_bgr.set_end(curr[0][1])
    print(sub_bgr.start, "-", sub_bgr.end)
    bgr_clips.append(sub_bgr)
    print(len(bgr_clips))
    



    # print(bgr_clips)

    # empty_clip = ColorClip((1280, 720), (0,0,0,0), duration=clip.duration)
    # empty_clip = empty_clip.set_opacity(0)
    # Say that you want it to appear 10s at the center of the screen
    # txt_clip = txt_clip.set_pos('center').set_duration(10)

    # Overlay the text clip on the first video clip
    # video = CompositeVideoClip([clip, sub_bgr, sub, sub_kor])


    video = CompositeVideoClip( [clip] + bgr_clips + [sub, sub_kor], size=(1280,720))

    # debug
    video.save_frame("debug.png", t=30) # saves the frame a t=2s

    # video.show(10.5, interactive = True)
    # video.preview(fps=15, audio=False) # don't generate/play the audio.

    # video = video.subclip(25,60)
    video.write_videofile("[Composite] HOW DEBT CAN GENERATE INCOME -ROBERT KIYOSAKI.mp4", threads=4, fps=clip.fps, temp_audiofile='temp-audio.m4a', remove_temp=True, codec="libx264", audio_codec="aac")