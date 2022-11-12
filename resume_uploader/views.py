from django.shortcuts import redirect, render
from myapp.models import Resume
def home(request):
    if request.method == 'POST':
        nm = request.POST.get('name')
        dob = request.POST.get('dob')
        gen = request.POST.get('gen')
        locality = request.POST.get('locality')
        city = request.POST.get('city')
        code = request.POST.get('code')
        state = request.POST.get('state')
        mob = request.POST.get('mob')
        email = request.POST.get('email')
        jobloc = request.POST.get('jobloc')
        img = request.FILES['img']
        doc = request.FILES['doc']
        var = Resume(name=nm,dob=dob,gen=gen,locality=locality,city=city,code=code,state=state,mob=mob,email=email,jobloc=jobloc,img=img,doc=doc)
        var.save()
        return redirect('/')
    else:
        img = ''
        doc = ''
        data = Resume.objects.all()
        return render(request,'home.html',{'data':data})

def resume(request,id):
    data = Resume.objects.filter(pk=id)
    return render(request,'resume.html',{'data':data})