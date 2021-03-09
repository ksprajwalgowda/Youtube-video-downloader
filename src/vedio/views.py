from django.shortcuts import render, redirect

# Create your views here.
from .models import Videos
from pytube import YouTube
 
# Create your views here.
 
def upload_video(request):
     
    if request.method == 'POST': 
         
        link = request.POST['link']
        try:

            v = YouTube(link).streams.first().download("media\\temp")
        except Exception as e:
            return render(request,'upload.html')

       
        content = Videos(title=link, video=v)
        content.save()
        return redirect('videos')
     
    return render(request,'upload.html')
 
 
def display(request):
    
    videos = Videos.objects.last()
    context ={
        'videos':videos,
    }
     
    return render(request,'videos.html',context)