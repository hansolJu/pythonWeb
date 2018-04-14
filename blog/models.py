from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
# slug 필드를 자동으로 채루기 위해 slugify()함수 사용.
# slugify()함수는 원래 단어를 알파벳 고문자,숫자,밑줄 하이픈으로만 구성된 단어로 만들어주는 함수.
from django.utils.text import slugify
from tagging.fields import TagField


# Create your models here.

class Post(models.Model):
    title = models.CharField('TITLE', max_length=50)
    slug = models.SlugField(max_length=255,unique=True)
    # slug = models.SlugField = ('SLUG',unique = True,allow_unicode = True,\
    # help_text='one word for title alias')  # help_text = ('')
    # slug = models.SlugField = (_('slug'),unique=True)
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text')
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    modify_date = models.DateTimeField('Modify_Date', auto_now=True)
    tag = TagField()
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

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

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title, allow_unicode=True)
        super(Post, self).save(*args,**kwargs)
