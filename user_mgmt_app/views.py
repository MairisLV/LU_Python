from django.shortcuts import render
from user_mgmt_app.models import Registered_users
from django.http import HttpResponse
# Create your views here.


def index(request):
    
    registered_users = Registered_users.objects.all()

    context = {
        
        'registered_user': registered_users,

    }

    return render(
        template_name='index.html',
        request=request,
        context=context,
    )

def add_user(request):
    if request.method == 'POST':

        register_user = Registered_users(
            username=request.POST["username"],
            email=request.POST["email"],
        )

        register_user.save()

        context = {
            'user_id': register_user.id,
            'username': register_user.username,
            'email': register_user.email,
            'action': 'added',
            
        }

        return render(
            template_name='details_page.html',
            request=request,
            context=context,
        )

    return render(
        template_name='add_user.html',
        request=request,
        context={},
    )

def get_user(request, user_id=0):
    
    if user_id != 0:
        entry = {'entry': Registered_users.objects.get(pk=user_id)}
        
        return render(
            template_name='get_user.html',
            request=request,
            context=entry
        )

    return HttpResponse('<h2>Please fill in the user ID in the url to see information about the user!</h2>')

def edit_user(request, user_id=0):
    if user_id != 0:
        if request.method == 'POST':
            entry = Registered_users.objects.get(pk=user_id)
            
            if request.POST['username'] != '': entry.username = request.POST['username']
            if request.POST['email'] != '': entry.email = request.POST['email']

            entry.save()

            context = {
            'user_id': entry.id,
            'username': entry.username,
            'email': entry.email,
            'action': 'edited',
                }

            return render(
            template_name = 'details_page.html',
            request = request,
            context = context, 
             )

        return render(
            template_name='edit_user.html',
            request=request,
            )

    return HttpResponse('<h2>Please fill in the user ID in the url to edit the information about the user!</h2>')

def delete_user(request, user_id=0):
    if user_id != 0:
        
        entry = Registered_users.objects.get(pk=user_id)

        context = { 
            'user_id': user_id,
            'action': 'DELETED',
                }

        entry.delete()
    
        return render(
            template_name='delete_user.html',
            request=request,
            context=context
        )

    return HttpResponse('<h2>Please fill in the user ID in the url to DELETE the user!</h2>')
