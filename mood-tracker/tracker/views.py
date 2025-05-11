from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import MoodEntryForm, CustomUserCreationForm
from .models import MoodEntry
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

@login_required
def profile_view(request):
    return render(request, 'profile.html')

@csrf_protect
@login_required
def submit_mood(request):
    if request.method == 'POST':
        mood = request.POST.get('mood')
        # Save mood to DB if needed
        print(f"{request.user.username} selected mood: {mood}")
    return redirect('profile')

@login_required
def mood_history(request):
    moods = MoodEntry.objects.filter(user=request.user).order_by('-date')
    return render(request, 'mood_history.html', {'moods': moods})

def home(request):
    return HttpResponse("Welcome to the Mood Tracker App. Go to /submit/ to log your mood.")

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def welcome(request):
    return render(request, 'welcome.html')

@login_required
def profile(request):
    context = {
        'username': request.user.username,
        'date_joined': request.user.date_joined,
        'last_login': request.user.last_login,
    }
    return render(request, 'profile.html', context)

@login_required
def default_profile(request):
    return HttpResponse("This is the default profile page.")

@login_required
def submit_mood(request):
    if request.method == 'POST':
        mood = request.POST.get('mood')
        if mood:
            # Create a new MoodEntry
            mood_entry = MoodEntry(user=request.user, mood=mood)
            mood_entry.save()
            return redirect('mood_history')  # Redirect to history page after submitting the mood
    return redirect('profile')  # Redirect to profile if no mood selected

