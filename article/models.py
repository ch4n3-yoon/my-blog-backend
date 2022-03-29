from django.db import models


class Article(models.Model):
    title = models.CharField("제목", max_length=256, default="")
    content = models.TextField("본문", default="", blank=True)
    view_count = models.IntegerField("조회수", default=None, null=True, blank=True)
    like_count = models.IntegerField("추천수", default=None, null=True, blank=True)
    is_deleted = models.BooleanField("게시글 삭제 여부", default=False)

    def __str__(self) -> str:
        return f"{self.title}"


class Comment(models.Model):
    article = models.ForeignKey(Article, verbose_name="게시글", on_delete=models.CASCADE, null=False)
    nickname = models.CharField("닉네임", max_length=64, blank=False)
    password = models.CharField("비밀번호", max_length=64, blank=False)
    content = models.TextField("댓글 내용", default="", blank=False)
    is_deleted = models.BooleanField("댓글 삭제 여부", default=False)

    def __str__(self) -> str:
        return self.content.replace("\n", " ")

