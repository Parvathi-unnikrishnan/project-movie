from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect
from app1.models import Movie

from app1.forms import MovieForm
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView


# Create your views here.
# def home(request):
#     k=Movie.objects.all()
#     return render(request,'home.html',{'movie':k})

class Home(ListView):
    model = Movie
    template_name = "home.html"
    context_object_name = "movie"
    # def get_queryset(self):
    #     qs=super().get_queryset()
    #     # queryset=qs.filter(title="kathal")
    #     queryset=qs.filter(title__icontains="s")
    #
    #     return queryset

    def get_context_data(self):
        context=super().get_context_data()
        context['title']="Paru"
        return context








# def add(request):
#     if(request.method=="POST"):
#         t=request.POST['t']
#         d = request.POST['d']
#         y = request.POST['y']
#         i = request.FILES['i']
#         l = request.POST['l']
#         m=Movie.objects.create(title=t,description=d,year=y,language=l,image=i)
#         m.save()
#         return home(request)
#     return render(request,'add.html')
#


# def addmovie1(request):                                #builtin form
#     if(request.method=="POST"):                        #after form submission
#         form=MovieForm(request.POST,request.FILES)     #creates a form object using values that are passed through the request.POST
#         if form.is_valid():                            #is_valid() built in functiom to check the values of form fields
#             form.save()                                #save the form object in Db table
#             return redirect('/')                    #redirect home page
#     form=MovieForm()                                   #empty form object is created
#     context={'form':form}
#     return render(request,'add1.html',context)

class Addmovie(CreateView):
    model = Movie
    fields = ['title','description','year','language','image']
    template_name = "add.html"
    success_url = reverse_lazy('app1:home')   #redirect page name


# def details(request,i):
#     k=Movie.objects.get(id=i)
#     return render(request,'details.html',{'movie':k})
class Detail(DetailView):
    model = Movie
    template_name = "details.html"
    context_object_name = "movie"

class Update(UpdateView):
    model = Movie
    fields = ['title', 'description', 'year', 'language', 'image']
    template_name = "edit.html"
    success_url = reverse_lazy('app1:details')




# def delete(request,i):
#     k=Movie.objects.get(id=i)
#     k.delete()
#     return home(request)

class Delete(DeleteView):
    template_name = "delete.html"
    model = Movie
    success_url = reverse_lazy('app1:home')






# def edit(request,i):
#     k=Movie.objects.get(id=i)
#     if(request.method=="POST"):
#         k.title=request.POST['t']
#         k.description=request.POST['d']
#         k.year=request.POST['y']
#         k.language=request.POST['l']
#         if(request.FILES.get('i')==None):
#             k.save()
#         else:
#             k.image=request.FILES.get('i')
#         k.save()
#         return home(request)
#
#     return render(request,'edit.html',{'movie':k})
#
