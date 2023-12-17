from django.shortcuts import render, get_object_or_404
from main.models import Ring, Club, Expert, Participant
from django.views.generic import DetailView
# Create your views here.
class ParticipantReport(DetailView):
    model = Participant
    template_name = 'main/participantreport.html'
    context_object_name = 'participant'

def clubReport(request, pk):
    club = get_object_or_404(Club, pk=pk)
    club_detail = {'name': club.name}
    club_detail['bronze'] = Participant.objects.filter(medal="Бронза").filter(club_id=club.id).count()
    club_detail['silver'] = Participant.objects.filter(medal="Серебро").filter(club_id=club.id).count()
    club_detail['gold'] = Participant.objects.filter(medal="Золото").filter(club_id=club.id).count()
    breeds_all = Participant.objects.filter(club_id=club.id).distinct('ring_id')
    breeds = []
    for breed in breeds_all:
        breeds.append(breed.ring_id)
    club_detail['breeds'] = breeds
    club_detail['count'] = Participant.objects.filter(club_id=club.id).count()
    club_detail['winners'] = Participant.objects.filter(medal="Золото").filter(club_id=club.id)
    return render(request, 'main/clubreport.html', {'club': club_detail})


def index(request):
    return render(request, 'main/index.html')

def clubs(request):
    clubs_all=Club.objects.all()
    clubs_view=[]
    for club in clubs_all:
        bronze = Participant.objects.filter(medal="Бронза").filter(club_id=club.id).count()
        silver = Participant.objects.filter(medal="Серебро").filter(club_id=club.id).count()
        gold = Participant.objects.filter(medal="Золото").filter(club_id=club.id).count()
        breeds_all=Participant.objects.filter(club_id=club.id).distinct('ring_id')
        breeds=[]
        for breed in breeds_all:
            breeds.append(breed.ring_id)
        clubs_view.append({'name': club.name, 'bronze': bronze, 'silver': silver, 'gold': gold, 'breeds': breeds, 'id': club.id})
    return render(request, 'main/clubs.html', {'clubs': clubs_view})


def participants(request):
    dogs = Participant.objects.all().order_by('id')
    return render(request, 'main/participants.html', {'dogs': dogs})

def rings(request):
    experts_all = Expert.objects.all()
    ring_experts=[]
    for expert in experts_all:
        expert_dict={'ring': expert.ring_id, 'names': [expert.full_name]}
        count=0
        for dict_e in ring_experts:
            if dict_e.get('ring')==expert.ring_id:
                ring_experts[count]['names'].append(expert.full_name)
                break
            count+=1
        else:
            ring_experts.append(expert_dict)
    return render(request, 'main/rings.html', {'experts': ring_experts})

def experts(request):
    experts_all=Expert.objects.all()
    return render(request, 'main/experts.html',{'experts': experts_all})