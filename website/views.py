from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from .models import (Patios,Patiosimage,
Resins,Resinsimage,
Tarmac,Tarmacimage,
Fencing,Fencingimage,
BlockPaving,BlockPavingimage,Walls,Wallsimage,Post,Bio)





def photos_view(request):
    patios = Patios.objects.all()
    resins = Resins.objects.all()
    tarmac = Tarmac.objects.all()
    fencing = Fencing.objects.all()
    blockpaving = BlockPaving.objects.all()
    wall = Walls.objects.all()
    context = {
        'patios':patios,
        'resins':resins,
        'tarmac':tarmac,
        'fencing':fencing,
        'blockpaving':blockpaving,
        'wall':wall

}   
    return render(request, 'photos.html', context)


def pic_detail(request, id):
    patios = get_object_or_404(Patios, id= id)
    photos = Patiosimage.objects.filter(patios=patios)
    return render(request, 'pic_detail.html', {
        'patios':patios,
        'photos':photos
        
})


def res_detail(request, id):
    resins = get_object_or_404(Resins, id= id)
    resins_pic = Resinsimage.objects.filter(resins=resins)
    return render(request, 'res_detail.html', {
        'resins':resins,
        'resins_pic':resins_pic
        
})


def tam_detail(request, id):
    tarmac = get_object_or_404(Tarmac, id= id)
    tarmac_pic = Tarmacimage.objects.filter(tarmac=tarmac)
    return render(request, 'tam_detail.html', {
        'taramc':tarmac,
        'tarmac_pic':tarmac_pic
        
})


def fen_detail(request, id):
    fencing = get_object_or_404(Fencing, id= id)
    fencing_pic = Fencingimage.objects.filter(fencing=fencing)
    return render(request, 'fen_detail.html', {
        'fencing':fencing,
        'fencing_pic':fencing_pic
        
})


def bap_detail(request, id):
    blockpaving = get_object_or_404(BlockPaving, id= id)
    blockpaving_pic = BlockPavingimage.objects.filter(blockpaving=blockpaving)
    return render(request, 'bap_detail.html', {
        'blockpaving':blockpaving,
        'blockpaving_pic':blockpaving_pic
        
})


def wa_detail(request, id):
    wall = get_object_or_404(Walls, id= id)
    wall_pic = Wallsimage.objects.filter(wall=wall)
    return render(request, 'wa_detail.html', {
        'wall':wall,
        'wall_pic':wall_pic
        
})


 
def blog(request):
    post = Post.objects.all()
    return render(request, 'blog.html', {'post':post})



def bio(request):
    bio = Bio.objects.all()
    return render(request, 'bio.html', {'bio':bio})


def quotes(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        message_email = request.POST['message_email']
        service = request.POST['service']
        message = request.POST['message']
        
     
        return render(request, 'quotes.html', {'first_name': first_name})
    else:
        return render(request, 'quotes.html', {})





