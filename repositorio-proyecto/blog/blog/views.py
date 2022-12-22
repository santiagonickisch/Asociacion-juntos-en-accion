from django.shortcuts import render

from apps.noticias.models import Noticia




def Noticias_base(request):
	
	contexto ={}

	n = Noticia.objects.all().order_by('-fecha')[:3] # Esto es para mostrar los...
	#ultimos tres por fecha.
	contexto['notiFecha'] = n

	return render(request, 't_home.html', contexto) 


    

def Nosotros(request):
    return render(request, 't_nosotros.html')

