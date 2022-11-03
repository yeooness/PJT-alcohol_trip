from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "title",
            "content",
            "grade",
            "image",
        ]
        labels = {
            "title": "리뷰 제목",
            "content": "리뷰 내용",
            "grade": "평점",
            "image": "이미지",
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content",
        ]
        labels = {
            "content": "댓글을 작성해주세요.",
        }
