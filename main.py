#!/usr/bin/env python
import os


def convert_to_mp4(path: str):
    mp4_path = path.replace(".MOV", ".mp4")
    command = "ffmpeg -i {path} -vcodec h264_videotoolbox -pix_fmt yuv420p -b:v 5000k -acodec aac -b:a 320k {mp4_path}".format(path=path, mp4_path=mp4_path)
    os.system(command)
    
# def convert_to_MOV(path: str):
#     MOV_path = path.replace(".mp4", ".MOV")
#     command = "ffmpeg -i {path} -vcodec h264_videotoolbox -pix_fmt yuv420p -b:v 5000k -acodec aac -b:a 320k {MOV_path}".format(path=path, MOV_path=MOV_path)
#     os.system(command)

def main():
    dir = ""
    
    for file in os.listdir(dir):
        if file.endswith(".MOV"):
            path = os.path.join(dir, file)
            convert_to_mp4(path)
        # if file.endswith(".mp4"):
        #     path = os.path.join(dir, file)
        #     convert_to_MOV(path)
            
            
if __name__ == "__main__":
    main()
