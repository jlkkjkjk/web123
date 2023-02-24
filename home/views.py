from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.http import request
import random
import string










def index(request):
    return render (request ,'index.html')


def download_video(request):
    if request.method == 'POST':
        youtube_link = request.POST['youtube_link']
        # Use pytube to download the video
        from pytube import YouTube
        yt = YouTube(youtube_link)
        video = yt.streams.get_highest_resolution()
        print(f'Video: {video}')
        file_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        video.download(filename=file_name)
        

        # Use ffmpeg to convert the video to MP4
        import os
        os.system(f"ffmpeg -i {file_name} {file_name}.mp4")
        response = HttpResponse(open(f"{file_name}", 'rb'), content_type='video/mp4')
        response['Content-Disposition'] = f'attachment; filename={file_name}.mp4'
        return response
    
    # If the request method is not POST, render the form template
    return render(request, 'success.html')

        
    






  

