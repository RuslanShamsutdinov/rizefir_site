from django.urls import path, include


from rizefir.products.views import CategoryView

urlpatterns = [
    path("", CategoryView.as_view(), name='category_index')
]
