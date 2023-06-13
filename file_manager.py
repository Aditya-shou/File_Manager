import os
import shutil

source = "C://Users//Admin//Downloads"
audio_folder="C://Users//Admin//Downloads//Audio"
docx_folder="C://Users//Admin//Downloads//Docx"
pdf_folder="C://Users//Admin//Downloads//Pdf"
video_folder = "C://Users//Admin//Downloads//Video"
html_folder = "C://Users//Admin//Downloads//Html"
image_folder = "C://Users//Admin//Downloads//Images"

files = os.listdir(source)

audio_file_format = ['mp3','wav']
docx_file_format = ['doc','docx']
pdf_file_format = ['pdf']
video_file_format = ['mp4', 'mkv','m4v']
html_file_format = ['html']
image_file_format = ['PNG','jpg','png','jpeg']

for file in files:
    file_ext = file.split('.')[-1]
    if file_ext in docx_file_format:
        shutil.move(file,docx_folder)

    if file_ext in video_file_format:
        shutil.move(file,video_folder)

    if file_ext in pdf_file_format:
        shutil.move(file,pdf_folder)

    if file_ext in audio_file_format:
        shutil.move(file,audio_folder)

    if file_ext in html_file_format:
        shutil.move(file,html_folder)
    if file_ext in image_file_format:
        shutil.move(file,image_folder)


