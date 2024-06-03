from ninja import Router
from core.api.v1.intensives.handlers import router as intensives_router


router = Router(tags=["v1"])
router.add_router('intensives/', intensives_router)
