import random
from django.shortcuts import render

def roll_dice(request):
    """Handle GET and POST requests to simulate dice rolling."""
    context = {}
    if request.method == 'POST':
        try:
            number_of_dice = int(request.POST.get('number_of_dice', 1))
            sides_per_die = int(request.POST.get('sides_per_die', 6))

            if number_of_dice <= 0 or sides_per_die <= 0:
                context['error'] = "The number of dice and sides must be positive integers."
            else:
                # Simulate dice rolls
                results = [random.randint(1, sides_per_die) for _ in range(number_of_dice)]
                context['results'] = results

                # Additional features
                context['total'] = sum(results)  # Total of all dice rolls
                context['average'] = round(sum(results) / number_of_dice, 2)  # Average roll
                context['highest_roll'] = max(results)  # Highest roll
                context['lowest_roll'] = min(results)  # Lowest roll
        except ValueError:
            context['error'] = "Invalid input. Please enter positive integers."
    return render(request, 'dice_simulator/roll_dice.html', context)
