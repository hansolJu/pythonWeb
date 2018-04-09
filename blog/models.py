from django.db import models
from django.urls import reverse
from tagging.fields import TagField


# Create your models here.

class Post(models.Model):
    title = models.CharField('TITLE', max_length=50)
    slug = models.SlugField(max_length=255,unique=True)
    # slug = models.SlugField = ('SLUG',unique = True,allow_unicode = True,help_text='one word for title alias')  # help_text = ('')
    # slug = models.SlugField = (_('slug'),unique=True)
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text')
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    modify_date = models.DateTimeField('Modify_Date', auto_now_add=True)
    tag = TagField()

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'my_post'
        ordering = ('-modify_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))
        # return reverse('blog:post_detail', kwargs={'slug':self.slug })

    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    def get_next_post(self):
        return self.get_next_by_modify_date()
