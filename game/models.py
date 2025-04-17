from django.db import models

CHOICES = [
    ('rock', 'Rock'),
    ('paper', 'Paper'),
    ('scissors', 'Scissors')
]

RESULTS = [
    ('win', 'Win'),
    ('lose', 'Lose'),
    ('draw', 'Draw')
]

class GameResult(models.Model):
    player_choice = models.CharField(max_length=10, choices=CHOICES)
    computer_choice = models.CharField(max_length=10, choices=CHOICES)
    result = models.CharField(max_length=10, choices=RESULTS)
    played_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player_choice} vs {self.computer_choice} => {self.result}"
