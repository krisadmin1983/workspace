from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MessageForm, CommunityMessageForm
from .models import Message, CommunityMessage
from django.contrib import messages

@login_required
def post_message(request):
    if request.method == 'POST':
        message_form = MessageForm(request.POST)
        community_form = CommunityMessageForm(request.POST)
        if message_form.is_valid() and community_form.is_valid():
            message = message_form.save(commit=False)
            message.user = request.user
            message.save()
            community_message = community_form.save(commit=False)
            community_message.user = request.user
            community_message.save()
            messages.success(request, 'Your messages have been posted.')
            return redirect('p_messages:community_messages')
    else:
        message_form = MessageForm()
        community_form = CommunityMessageForm()
    return render(request, 'p_messages/post_message.html', {'message_form': message_form, 'community_form': community_form})

@login_required
def community_messages(request):
    messages = CommunityMessage.objects.all().order_by('-timestamp')
    return render(request, 'p_messages/community_messages.html', {'messages': messages})
