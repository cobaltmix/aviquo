from django.db import models
from django.contrib.auth.models import User
import json

class Message(models.Model):
    content = models.TextField()
    # we'd sync this up somehow once the website is ready
    # sender = models.ForeignKey(User, on_delete=models.CASCADE)
    sender = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.sender} at {self.timestamp}'
    
    def to_json_dict(self):
        return json.dumps({
            'sender' : self.sender,
            'text' : self.content,
        })

