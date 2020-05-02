from django.shortcuts import render,get_object_or_404

from .models import Post
from  .forms import NewComment

# Create your views here.




def home(request):

    context = {
        'title': 'الصفحة الرئيسية',
        'posts':Post.objects.all(),
        
    }
    return render(request, 'index.html', context)



    # about
def about(request):

    return render(request, 'about.html', {'title': 'من أنا'})


# post details or contents:
def post_detail(request,post_id):
    post= get_object_or_404(Post,pk=post_id)
    comments = post.comments.filter(active=True)
    comment_form=NewComment()
    context={

        'title':post,
        'post':post,
        'comments': comments,
        'comment_form':comment_form,
    }
    return render(request,'detail.html',context)