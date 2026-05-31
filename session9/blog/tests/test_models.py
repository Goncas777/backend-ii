import pytest
from django.utils import timezone

from blog.models import BlogPost


@pytest.mark.django_db
def test_blogpost_creation():
    published = timezone.now()
    post = BlogPost.objects.create(
        title="Hello",
        content="Body",
        published_date=published,
    )
    assert post.title == "Hello"
    assert post.content == "Body"
    assert post.published_date == published


@pytest.mark.django_db
def test_blogpost_retrieval():
    published = timezone.now()
    BlogPost.objects.create(
        title="First",
        content="Content",
        published_date=published,
    )
    retrieved = BlogPost.objects.get(title="First")
    assert retrieved.content == "Content"
    assert retrieved.published_date == published
