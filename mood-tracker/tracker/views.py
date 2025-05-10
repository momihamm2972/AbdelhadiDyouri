from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import MoodEntryForm
from .models import MoodEntry
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def submit_mood(request):
    if request.method == 'POST':
        form = MoodEntryForm(request.POST)
        if form.is_valid():
            mood_entry = form.save(commit=False)
            mood_entry.user = request.user
            mood_entry.save()
            return redirect('mood_history')
    else:
        form = MoodEntryForm()
    return render(request, 'submit_mood.html', {'form': form})

@login_required
def mood_history(request):
    moods = MoodEntry.objects.filter(user=request.user).order_by('-date')
    return render(request, 'mood_history.html', {'moods': moods})

def home(request):
    return HttpResponse("Welcome to the Mood Tracker App. Go to /submit/ to log your mood.")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # after register, go to login
    else:
        form = UserCreationForm()
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

