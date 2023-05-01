from django.http import JsonResponse
from django.views import View
from ads.models import Category

def root(request):
    return JsonResponse({"status": "ok"}, status=200)


class CategoryListView(View):
    def get(self, request):
        all_categories = Category.object.all
        return JsonResponse([{'id': cat.id, 'name': cat.name} for cat in all_categories])
