from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from models import Link

def list(request, message = ""): # list all links
  links = Link.objects.all()
  return render_to_response('list.html', {'links': links})

def view(request, id): # show one link
  link = Link.objects.get(id=id)
  return render_to_response('view.html', {'link': link})

def new(request): # show form to new link
  return render_to_response('form.html', {'action': 'add'})

def edit(request, id): # show form to edit a link
  link = Link.objects.get(id=id)
  return render_to_response('form.html', {'link': link, 'action': id + '/update'})

def add(request): # add a new link
  link = Link (
    title = request.POST["title"],
    desc = request.POST["desc"],
    url = request.POST["url"]
  )
  link.save()
  return HttpResponseRedirect("/links")

def update(request, id): # update a link
  link = Link.objects.get(id=id)
  link.title = request.POST["title"]
  link.desc = request.POST["desc"]
  link.url = request.POST["url"]
  link.save()
  return HttpResponseRedirect("/links")

def delete(request, id): # delete a link
  Link.objects.get(id=id).delete()
  return HttpResponseRedirect("/links")