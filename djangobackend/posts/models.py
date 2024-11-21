from django.db import models


class SocialMediaPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    hashtags = models.JSONField()

    def __str__(self):
        return self.title

    def to_json(self):
        return {
            "title": self.title,
            "content": self.content,
            "hashtags": self.hashtags
        }

    @classmethod
    def create(cls, title, content, hashtags):
        return cls.objects.create(title=title, content=content, hashtags=hashtags)