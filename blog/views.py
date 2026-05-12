from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published=True).order_by('created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, published=True)
    return render(request, 'blog/post_detail.html', {'post': post})

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Optional: Send email (configure email settings first)
        # send_mail(
        #     f"Contact Form: {subject}",
        #     f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
        #     email,
        #     ['admin@nexus.com'],
        #     fail_silently=False,
        # )
        
        messages.success(request, 'Thank you for your message! We will get back to you soon.')
        return render(request, 'blog/contact.html')
    
    return render(request, 'blog/contact.html')