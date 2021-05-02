from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import render
from .forms import studentreg 
from .models import user
from django.views.generic.base import TemplateView, RedirectView
from django.views import View



#class based views
class addshowview(TemplateView):
    template_name = 'enroll/addandshow.html'
    def get_context_data(self,*arg,**kwarg):
        context = super().get_context_data(**kwarg)
        fm = studentreg()
        stud = user.objects.all()  
        context = {'std':stud,'form':fm}
        return context

    def post(self,request):
        fm = studentreg(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = user(name=nm,email=em,password=pw)
            reg.save()
            return HttpResponseRedirect('/')

#class based for update
class userview(View):
    def get(self,request,id):
        pi = user.objects.get(pk=id)
        fm = studentreg(instance=pi) 
        return render(request,'enroll/update.html',{'form':fm})

    def post(self,request,id):
        pi = user.objects.get(pk=id)
        fm = studentreg(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')    
        




#update student info
"""def update(request,id):
    if request.method == 'POST':

        pi = user.objects.get(pk=id)
        fm = studentreg(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()     
    else:
        pi = user.objects.get(pk=id)
        fm = studentreg(instance=pi) 
    return render(request,'enroll/update.html',{'form':fm})
"""    
 #delete class based view
class userdelete(RedirectView):


    url = '/'


    def get_redirect_url(self,*args,**kwargs):

        del_id = kwargs['id']
        user.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args,**kwargs)
                    


