# from sys import setprofile
# from django.contrib.auth import get_user_model
# from django.db import models
# from accounts.models import User, UserProfile, PlacesProfile


# def image_post_user(instance,filename):
#     imgename , extension = filename.split(".")
#     return "image_post_user/%s.%s"%(instance.id, extension)

# class Post_User(models.Model):
#     PostUser = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="posts")
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     image = models.ImageField(upload_to=image_post_user)

#     def __str__(self):
#         return f"Post {self.id}"

# class Comment_Post_User(models.Model):
#     post = models.ForeignKey(Post_User, on_delete=models.CASCADE, related_name="comments")
#     UserProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="posts")
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Comment {self.id}"


# class Like_Post_User(models.Model):
#     post = models.ForeignKey(Post_User, on_delete=models.CASCADE, related_name="comments")
#     UserProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="posts")
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Like {self.id}"

# ################################

# # def image_post_places(instance,filename):
# #     imgename , extension = filename.split(".")
# #     return "image_post_user/%s.%s"%(instance.id, extension)

# # class Post_Places(models.Model):
# #     PostPlaces = models.ForeignKey(PlacesProfile, on_delete=models.CASCADE, related_name="comments")
# #     content = models.TextField()
# #     created_at = models.DateTimeField(auto_now_add=True)
# #     image = models.ImageField(upload_to=image_post_places)

# #     def __str__(self):
# #         return f"Post {self.id}"

# # class Comment_Post_Places(models.Model):
# #     post = models.ForeignKey(Post_Places, on_delete=models.CASCADE, related_name="comments")
# #     PostPlaces = models.ForeignKey(PlacesProfile, on_delete=models.CASCADE, related_name="comments")
# #     content = models.TextField()
# #     created_at = models.DateTimeField(auto_now_add=True)

# #     def __str__(self):
# #         return f"Comment {self.id}"

# # class Like_Post_Places(models.Model):
# #     post = models.ForeignKey(Post_Places, on_delete=models.CASCADE, related_name="comments")
# #     PostPlaces = models.ForeignKey(PlacesProfile, on_delete=models.CASCADE, related_name="comments")
# #     created_at = models.DateTimeField(auto_now_add=True)

# #     def __str__(self):
# #         return f"Like {self.id}"
