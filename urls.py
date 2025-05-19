
**Create a `.env` file in the root directory:**

```
DB_NAME=alx_travel
DB_USER=root
DB_PASSWORD=yourpassword
DB_HOST=127.0.0.1
DB_PORT=3306
```

---

**In `alx_travel_app/urls.py`:**

```python
from django.contrib import admin
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="ALX Travel API",
        default_version='v1',
        description="API documentation for travel listings",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
```

---

```bash
git init
echo "venv/" >> .gitignore
echo ".env" >> .gitignore
git add .
git commit -m "Initial project setup with Swagger, MySQL config, and required dependencies"
```
