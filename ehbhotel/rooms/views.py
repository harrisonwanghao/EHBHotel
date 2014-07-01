from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from rooms.forms import RoomAddForm
from rooms.models import Room


def RoomAdd(request):
    if request.user.is_authenticated and request.user.ad:
        if request.method == 'POST':
            form = RoomAddForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/rooms/')
            else:
                return render_to_response('addroom.html', {'form': form}, context_instance=RequestContext(request))

        else:
            form = RoomAddForm()
            context = {'form': form}
            return render_to_response('addroom.html', context, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')


def RoomList(request):
    if request.user.is_authenticated and request.user.ad:
        return render_to_response('rooms.html', {'rooms': Room.objects.all()}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')