from functools import lru_cache

import punq

from core.apps.users.services import (
    auth,
    codes,
    users,
    senders,
)
from core.apps.intensives.services.intensive import (
    ORMIntensiveService,
    BaseIntensiveService,
)
from core.apps.intensives.services.intensive_session import (
    ORMIntensiveSessionService,
    BaseIntensiveSessionService,
)


@lru_cache(1)
def get_container():
    return _initialize_container()


def _initialize_container():
    container = punq.Container()

    # initialize intensives 
    container.register(BaseIntensiveService, ORMIntensiveService)
    container.register(BaseIntensiveSessionService, ORMIntensiveSessionService)

    # initialize users
    container.register(users.BaseUserService, users.ORMUserService)
    container.register(auth.BaseAuthService, auth.AuthService)
    container.register(codes.BaseCodeService, codes.DjangoCacheCodeService)
    container.register(senders.BaseSenderService, senders.DummySenderService)

    return container
