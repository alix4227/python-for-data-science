from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


class Articles(models.Model):
    title = models.CharField(_("titre"), max_length=64)
    author = models.ForeignKey(User, verbose_name=_("auteur"), on_delete=models.CASCADE)
    created = models.DateTimeField(_("créé le"), auto_now_add=True)
    synopsis = models.CharField(_("synopsis"), max_length=312)
    content = models.TextField(_("contenu"))
    def __str__(self):
        return self.title
    class Meta:
        db_table = "Articles"

class UserFavouriteArticle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    def __str__(self):
        return self.article.title
    class Meta:
        db_table = "UserFavouriteArticle"
        unique_together = ("user", "article")