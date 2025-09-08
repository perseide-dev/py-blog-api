from .models import Post 

def create_post(author, title, content):
    post = Post.objects.create(author=author, title=title, content=content)
    return post
def update_post(instance: Post, title=title, content=content)
    instance.title = title
    instance.content = content 
    instance.save()
    return instance 