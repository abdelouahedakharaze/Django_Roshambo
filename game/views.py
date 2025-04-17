import random
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import GameResult

CHOICES = ['rock', 'paper', 'scissors']

def determine_winner(player, computer):
    if player == computer:
        return 'draw'
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        return 'win'
    else:
        return 'lose'

def play_game(request):
    result_data = None

    if request.method == 'POST':
        player_choice = request.POST.get('choice')
        if player_choice in CHOICES:
            computer_choice = random.choice(CHOICES)
            result = determine_winner(player_choice, computer_choice)

            # Save to DB
            GameResult.objects.create(
                player_choice=player_choice,
                computer_choice=computer_choice,
                result=result
            )

            # Save result to session for display after redirect
            request.session['result'] = {
                'player_choice': player_choice,
                'computer_choice': computer_choice,
                'result': result
            }

            return redirect(reverse('play_game'))

    # After redirect, get and clear result from session
    result_data = request.session.pop('result', None)

    history = GameResult.objects.all().order_by('-played_at')[:10]

    return render(request, 'game/index.html', {
        'result': result_data['result'] if result_data else None,
        'player_choice': result_data['player_choice'] if result_data else None,
        'computer_choice': result_data['computer_choice'] if result_data else None,
        'history': history,
        'choices': CHOICES
    })
