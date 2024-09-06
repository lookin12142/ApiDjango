from django.urls import path
from .views import CharacterListView

urlpatterns = [
    path('api/characters/', CharacterListView.as_view(), name='character-list'),
]
