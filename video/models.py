from django.db import models



class Video(models.Model):
    name = models.CharField(max_length=100)
    image_path = models.ImageField(upload_to='images/')
    video_path = models.FileField(upload_to='videos/')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table ='videos'
    
