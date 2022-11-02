from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        labels = {
            "title": "리뷰 제목",
            "content": "리뷰 내용",
            "grade": "평점",
        }
        exclude = ["user", "restaurant"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content",
        ]
