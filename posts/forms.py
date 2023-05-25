from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__( *args, **kwargs)
        self.fields['description'].widget.attrs.update({
            'type':'text',
            'class':'form-control rounded-pill',
            'id':'CreatePost',
            'placeholder':'Some Something',
            'name':'description',
            'required':'',
        })
        self.fields['image'].widget.attrs.update({
            'type':'file',
            'id':'image',
            'name':'image',
        })
    class Meta:
        model = Post
        fields = ['description', 'image']

