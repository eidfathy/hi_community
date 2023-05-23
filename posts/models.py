from sys import setprofile
from django.contrib.auth import get_user_model
from django.db import models
from accounts.models import User, UserProfile, PlacesProfile


def image_post_user(instance,filename):
    imgename , extension = filename.split(".")
    return "image_post_user/%s.%s"%(instance.id, extension)

class PostUser(models.Model):
    creater = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="posts_created")
    content_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=image_post_user)
    likers = models.ManyToManyField(UserProfile, blank=True, related_name='liked', related_query_name='liked')

    def __str__(self):
        return f"Post {self.id}"


class CommentPostUser(models.Model):
    post = models.ForeignKey(PostUser, on_delete=models.CASCADE, related_name="comments")
    commenter = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="comments_made")
    comment_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post: {self.post} | Commenter: {self.commenter}"

    def serialize(self):
        return {
            "id": self.id,
            "commenter": self.commenter.serialize(),
            "body": self.comment_content,
            "timestamp": self.comment_time.strftime("%b %d %Y, %I:%M %p")
        }


class LikePostUser(models.Model):
    post = models.ForeignKey(PostUser, on_delete=models.CASCADE, related_name="likes")
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="liked_posts", related_query_name='liked_post')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Like {self.id}"

#################################


################################

# def image_post_places(instance,filename):
#     imgename , extension = filename.split(".")
#     return "image_post_user/%s.%s"%(instance.id, extension)

# class Post_Places(models.Model):
#     creater = models.ForeignKey(PlacesProfile, on_delete=models.CASCADE, related_name="comments")
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     image = models.ImageField(upload_to=image_post_places)

#     def __str__(self):
#         return f"Post {self.id}"

# class Comment_Post_Places(models.Model):
#     post = models.ForeignKey(Post_Places, on_delete=models.CASCADE, related_name="comments")
#     commenter = models.ForeignKey(PlacesProfile, on_delete=models.CASCADE, related_name="comments")
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Comment {self.id}"

# class Like_Post_Places(models.Model):
#     post = models.ForeignKey(Post_Places, on_delete=models.CASCADE, related_name="comments")
#     PostPlaces = models.ForeignKey(PlacesProfile, on_delete=models.CASCADE, related_name="comments")
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Like {self.id}"
