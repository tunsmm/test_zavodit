from django.db import models
from django.utils.html import mark_safe
from taggit.managers import TaggableManager


class News(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images/%Y/%m/%d/', blank=True)
    tags = TaggableManager()
    
    class Meta:
        verbose_name_plural = "News"
    
    def image_tag(self):
        current_path_to_img = str(self.image)
        if current_path_to_img.startswith('news'):
            return mark_safe('<img src="%s"/>' % (current_path_to_img[5:]))
        return mark_safe('<img src="%s"/>' % (current_path_to_img))

    image_tag.short_description = 'Image'    

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return "/news/%i" % self.id
