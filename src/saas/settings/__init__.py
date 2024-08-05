import os

env = os.getenv("DJANGO_ENV", "development")

if env == "production":
    from .production import *
elif env == "development":
    from .development import *
else:
    from .development import *