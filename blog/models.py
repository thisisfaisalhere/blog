import uuid
from django.db import models
from django.utils.translation import gettext as _
from autoslug import AutoSlugField

# Create your models here.
class Article(models.Model):

    draft = 'Draft'
    published = 'Published'

    TYPE = [
        (draft, 'Draft'),
        (published, 'Published'),
    ]


    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(published="Published")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(_("Title"), max_length=200, unique=True)
    thumbnail = models.ImageField(_("Thumbnail"), null=True, blank=True)
    slug = AutoSlugField(populate_from='title')
    excerpt = models.TextField(_("Excerpt"))
    body = models.TextField(_("Body"))
    published = models.CharField(verbose_name="User Type", max_length=10,
                                 choices=TYPE, default="Published")
    author = models.ForeignKey("users.User", verbose_name=_("User"), on_delete=models.CASCADE)
    published_on = models.DateTimeField(_("Published On"), auto_now_add=True)

    objects = models.Manager()
    postobjects = PostObjects()

    class Meta:
        verbose_name = _("article")
        verbose_name_plural = _("articles")

    def __str__(self):
        return self.title


class Comment(models.Model):

    article = models.ForeignKey("blog.Article", verbose_name=_("Article"), on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", verbose_name=_("User"), on_delete=models.CASCADE)
    time = models.DateTimeField(_("Comment Time"),auto_now_add=True)
    comment = models.TextField(_("Comment Text"))

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")