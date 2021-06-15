from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from .models import Document


# Create your views here.


def hello(request):
	return HttpResponse("hello world")

def htmlfile(request):
	docid = int (request.GET.get('docid',0))
	documents = Document.objects.all()

	if request.method == 'POST':
		docid=int(request.POST.get('docid', 0))
		title=request.POST.get('title')
		content=request.POST.get('content','')

		if docid>0:
			document=Document.objects.get(pk=docid)
			document.title=title
			document.content=content
			document.save()

			return redirect('/?docid=%i' %docid)
		else:
			document=Document.objects.create(title=title, content=content)
			return redirect ('/?docid=%i' % document.id)

	if docid>0:
		document=Document.objects.get(pk=docid)

	else:
		document=''

	context = {
		'docid':docid,
		'documents': documents,
		'document' : document
	}
	return render(request,'index.html',context )

def delete_note(request, docid):
	document=Document.objects.get(pk=docid)
	document.delete()
	
	return redirect('/?docid=0')
