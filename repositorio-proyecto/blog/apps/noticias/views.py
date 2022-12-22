from django.shortcuts import render, redirect

from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required

from .models import Noticia, Categoria, Comentario

from django.core.paginator import (Paginator,EmptyPage,PageNotAnInteger)




# Create your views here.

@login_required
def Listar_Noticias(request):
	contexto = {}

	id_categoria = request.GET.get('id', None)

	if id_categoria:
		n = Noticia.objects.filter(categoria_noticia = id_categoria).order_by('-fecha')
	else:
		n = Noticia.objects.all().order_by('-fecha')

	contexto['noticia'] = n

	page = request.GET.get('page', 1)

	paginator = Paginator(n, 6)

	try:
		items_page = paginator.page(page)
	except PageNotAnInteger:
			items_page = paginator.page(1)
	except EmptyPage:
			items_page = paginator.page(paginator.num_pages)


	contexto['pagi'] = items_page

	cat = Categoria.objects.all().order_by('categoria')
	contexto['categorias'] = cat
	return render(request, 'noticias/listar.html', contexto)




@login_required
def Detalle_Noticias(request, pk):
	contexto = {}

	n = Noticia.objects.get(pk = pk) #RETORNA SOLO UN OBEJTO
	contexto['noticia'] = n


	c = Comentario.objects.filter(noticia = n)
	contexto['comentarios'] = c

	return render(request, 'noticias/detalle.html',contexto)




@login_required
def Comentar_Noticia(request):

	com = request.POST.get('comentario',None)
	usu = request.user
	noti = request.POST.get('id_noticia', None)# OBTENGO LA PK
	noticia = Noticia.objects.get(pk = noti) #BUSCO LA NOTICIA CON ESA PK
	coment = Comentario.objects.create(usuario = usu, noticia = noticia, texto = com)
	
	return redirect(reverse_lazy('noticias:detalle', kwargs={'pk': noti}))



@login_required
def Delete(request, com_id):
	borrar = Comentario.objects.get(id = com_id)
	borrar.delete()
	
	return redirect('noticias:listar')
