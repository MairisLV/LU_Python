from django.shortcuts import render
from django.urls import reverse_lazy
from user_mgmt_app.models import Registered_users
from user_mgmt_app.forms import RegisterForm
from django.http import HttpResponse
from django.views.generic import ListView, View, FormView, DetailView, UpdateView, DeleteView

# Create your views here.

class index_listview(ListView):
    model = Registered_users
    template_name = 'index.html'

class add_user_form(FormView):
    form_class = RegisterForm
    template_name = 'add_user.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()

        return super().form_valid(form)
        
class get_user_DetailView(DetailView):

    model = Registered_users
    template_name = 'get_user.html'
        
class edit_user_UpdateView(UpdateView):
    model = Registered_users
    fields = ['username', 'email']
    template_name = 'edit_user.html'
    success_url = '/'

class delete_user_DeleteView(DeleteView):
    model = Registered_users
    template_name = 'confirm_delete.html'
    success_url = '/'

# def delete_user(request, user_id=0):
#     if user_id != 0:
        
#         entry = Registered_users.objects.get(pk=user_id)

#         context = { 
#             'user_id': user_id,
#             'action': 'DELETED',
#                 }

#         entry.delete()
    
#         return render(
#             template_name='delete_user.html',
#             request=request,
#             context=context
#         )

#     return HttpResponse('<h2>Please fill in the user ID in the url to DELETE the user!</h2>')
