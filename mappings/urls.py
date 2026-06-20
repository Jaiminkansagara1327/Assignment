from django.urls import path
from .views import MappingListCreateView, MappingByPatientView, MappingDeleteView

urlpatterns = [
    # POST (assign) and GET (all mappings)
    path('', MappingListCreateView.as_view(), name='mapping-list-create'),

    # GET all doctors for a specific patient
    path('<int:patient_id>/', MappingByPatientView.as_view(), name='mapping-by-patient'),

    # DELETE a specific mapping by its ID
    path('delete/<int:pk>/', MappingDeleteView.as_view(), name='mapping-delete'),
]
