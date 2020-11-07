from .settings import *

CURRENT_INSTANCE = env('CURRENT_INSTANCE', default='prod')

if CURRENT_INSTANCE == 'prod':
    from .prod import *
else:
    from .dev import *
