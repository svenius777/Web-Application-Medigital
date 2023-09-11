"""zdravstveni_sustav URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#iz ove django library importamo vec built in views
#handlea logiku al ne i template
from django.contrib.auth import views as auth_views
from zdravstveni_sustav import settings
from zdravstveni_sustav_app import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('zdravstveni_sustav_app.urls')),
    path('login/', views.login_view, name='login'),
    # path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]

#ako je debug true dodaj media.url u naše urlpatterns
#omogucuje media da radi u browseru
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# auth_views.LoginView.as_view()

# def user_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             login(request, form.get_user())
#             return redirect('success_page')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})