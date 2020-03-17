from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404

from irekua_database.models import Collection


@require_http_methods(["GET"])
def data_collections(request):
    collection_pk = request.GET.get('pk', None)
    collection = get_object_or_404(Collection, pk=collection_pk)

    response = {
        "name": collection.name,
        "description": collection.description
    }
    return JsonResponse(response)
