from django.shortcuts import render
from .models import MyModel

def home(request):

    all_instances = MyModel.objects.all()

    for instance in all_instances:
        instance.entries = f"{instance.entries} ({instance.id})"
        instance.save(update_fields=['entries'])

    return render(request, 'home.html', {'model': all_instances})