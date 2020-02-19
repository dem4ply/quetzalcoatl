from rest_framework_nested import routers
from . import views

router = routers.SimpleRouter()

router.register( r'catalog', views.Catalog, basename='catalog' )


urlpatterns = router.urls
