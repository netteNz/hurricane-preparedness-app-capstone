# checklist/views.py
from django.shortcuts import render, redirect
from .models import StaticChecklistItem, StaticChecklistCompletion


def toggle_static_item(request, item_id):
    user = 'anonymous'  # Replace with the actual user logic if necessary
    completion = StaticChecklistCompletion.objects.get(user=user, item_id=item_id)
    completion.completed = not completion.completed
    completion.save()
    return redirect('static_checklist')


def static_checklist(request):
    user = 'anonymous'  # Replace with authenticated user if needed

    # Fetch all static checklist items
    static_items = StaticChecklistItem.objects.all()

    # Fetch or create default completion statuses
    completions = StaticChecklistCompletion.objects.filter(user=user)
    completed_dict = {comp.item.id: comp.completed for comp in completions}
    for item in static_items:
        if item.id not in completed_dict:
            StaticChecklistCompletion.objects.create(item=item, user=user)

    # Refresh the completion status dictionary
    completions = StaticChecklistCompletion.objects.filter(user=user)
    completed_dict = {comp.item.id: comp.completed for comp in completions}

    return render(request, 'checklist/static_checklist.html', {
        'static_items': static_items,
        'completed_dict': completed_dict,  # Pass a mapping directly
    })
