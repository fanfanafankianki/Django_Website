"""
URL configuration for GymWebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from Website_training_objects.views import (
    return_user_profile,
    create_user_profile,
    edit_user_profile,
    delete_user_profile,

    return_exercises,
    create_exercises,
    edit_exercises,
    delete_exercises,

    return_testing,
    create_testing,
    edit_testing,
    delete_testing,

    return_training,
    create_training,
    edit_training,
    delete_training,

    return_training_with_exercises,
    create_training_with_exercises,
    edit_training_with_exercises,
    delete_training_with_exercises,

    return_training_history,
    create_training_history,
    edit_training_history,
    delete_training_history,

    return_training_details,
    create_training_details,
    edit_training_details,
    delete_training_details,

    return_all_exercises,
    return_all_trainings,
    return_all_training_with_exercises,
    return_all_training_history,
    return_all_training_details
)
from Website_diet_objects.views import (
    return_all_products,
    return_all_product_consumptions,
    return_all_nutritional_info,

    return_product,
    create_product,
    edit_product,
    delete_product,

    return_nutritional_info,
    create_nutritional_info,
    edit_nutritional_info,
    delete_nutritional_info,

    return_product_consumptions,
    create_product_consumptions,
    edit_product_consumptions,
    delete_product_consumptions
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),    
    path('profile_info/<int:id>/', return_user_profile, name='user_profiles'),

    path('exercises/', return_all_exercises, name='exercises'),
    path('trainings/', return_all_trainings, name='trainings'),
    path('training_with_exercises/', return_all_training_with_exercises, name='trainings_with_exercises'),
    path('training_histories/', return_all_training_history, name='training_history'),
    path('training_details/', return_all_training_details, name='training_details'),

    path('products/', return_all_products, name='products'),
    path('consumptions/', return_all_product_consumptions, name='consumptions'),
    path('nutritional_info/', return_all_nutritional_info, name='nutritional_info'),

    path('new_profile/', create_user_profile, name='new_profile'),
    path('edit_profile/<int:id>/', edit_user_profile, name='edit_profile'),
    path('delete_profile/<int:id>/', delete_user_profile, name='delete_profile'),

    path('exercise_info/<int:id>/', return_exercises, name='exercise_info'),
    path('new_exercise/', create_exercises, name='new_exercise'),
    path('edit_exercise/<int:id>/', edit_exercises, name='edit_exercise'),
    path('delete_exercise/<int:id>/', delete_exercises, name='delete_exercise'),

    path('testing_info/<int:id>/', return_testing, name='return_testing'),
    path('new_testing/', create_testing, name='create_testing'),
    path('edit_testing/<int:id>/', edit_testing, name='edit_testing'),
    path('delete_testing/<int:id>/', delete_testing, name='delete_testing'),

    path('training_info/<int:id>/', return_training, name='return_training'),
    path('new_training/', create_training, name='create_training'),
    path('edit_training/<int:id>/', edit_training, name='edit_training'),
    path('delete_training/<int:id>/', delete_training, name='delete_training'),

    path('training_with_exercises_info/<int:id>/', return_training_with_exercises, name='return_training_with_exercises'),
    path('new_training_with_exercises/', create_training_with_exercises, name='create_training_with_exercises'),
    path('edit_training_with_exercises/<int:id>/', edit_training_with_exercises, name='edit_training_with_exercises'),
    path('delete_training_with_exercises/<int:id>/', delete_training_with_exercises, name='delete_training_with_exercises'),

    path('training_history_info/<int:id>/', return_training_history, name='return_training_history'),
    path('new_training_history/', create_training_history, name='create_training_history'),
    path('edit_training_history/<int:id>/', edit_training_history, name='edit_training_history'),
    path('delete_training_history/<int:id>/', delete_training_history, name='delete_training_history'),

    path('training_details_info/<int:id>/', return_training_details, name='return_training_details'),
    path('new_training_details/', create_training_details, name='create_training_details'),
    path('edit_training_details/<int:id>/', edit_training_details, name='edit_training_details'),
    path('delete_training_details/<int:id>/', delete_training_details, name='delete_training_details'),

    path('product/<int:id>/', return_product, name='return_product'),
    path('new_product/', create_product, name='create_product'),
    path('edit_product/<int:id>/', edit_product, name='edit_product'),
    path('delete_product/<int:id>/', delete_product, name='delete_product'),

    path('nutritional_info/<int:id>/', return_nutritional_info, name='return_training_details'),
    path('new_nutritional_info/', create_nutritional_info, name='create_nutritional_info'),
    path('edit_nutritional_info/<int:id>/', edit_nutritional_info, name='edit_nutritional_info'),
    path('delete_nutritional_info/<int:id>/', delete_nutritional_info, name='delete_nutritional_info'),

    path('product_consumptions/<int:id>/', return_product_consumptions, name='return_product_consumptions'),
    path('new_product_consumptions/', create_product_consumptions, name='create_product_consumptions'),
    path('edit_product_consumptions/<int:id>/', edit_product_consumptions, name='edit_product_consumptions'),
    path('delete_product_consumptions/<int:id>/', delete_product_consumptions, name='delete_product_consumptions'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)