from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    synopsis = models.CharField(max_length=312)
    content = models.TextField()
    def __str__(self):
        return self.title
    class Meta:
        db_table = "Articles"
#         permissions = [
#         ('can_downvote_tip', 'Can downvote tip'),  # (codename, description)
# ]

class UserFavouriteArticle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    def __str__(self):
        return self.article.title
    class Meta:
        db_table = "UserFavouriteArticle"
        unique_together = ("user", "article")