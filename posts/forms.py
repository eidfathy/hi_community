# from django import forms
# from .models import Post_User, Comment_Post_User

# class CreatePostForm(forms.ModelForm):
#     class Meta:
#         model = Post_User
#         fields = ['content', 'image']

# class CreateCommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment_Post_User
#         fields = ['content']


from django import forms
from .models import Post_User

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post_User
        fields = ['content_text', 'image']

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post_User
        fields = ['content_text', 'image']

class LikePostForm(forms.Form):
    pass

class UnlikePostForm(forms.Form):
    pass

