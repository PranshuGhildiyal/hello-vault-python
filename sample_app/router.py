from sample_app.viewsets import ProductViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('product', ProductViewset)
