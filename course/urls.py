from django.urls import path,include
from . import views




urlpatterns = [
    path("types", views.Type_Ex),
    path("programmsOfSomeType/<int:pk>", views.Program_EX),
    path("someProgram/<int:pk>", views.Program_only),
    path("daysOfSomePrograms/<int:pk>", views.Day_only),
    path("exercisesOfSomeDay/<int:pk>", views.Day_Ex),
    path("exercisesOfSomePlanDay/<int:pk>", views.Plan_Day_Ex),
    path("someExercises/<int:pk>", views. Exercise),
    path("somePlanExercises/<int:pk>", views.Plan_Exercise),
    path("cdays/<str:name>", views. Cday),
    path("info", views. ProgInfo),
    path("uploadimage", views. UserImage),
    
    path("increase", views. IncreaseCDays),
    path("increasePlan", views. IncreaseCDaysForPlan),
    path("programStartedByUser", views.user_started_programs),
    path("planStartedByUser", views.user_started_plans),
    path("getCompletedDayForProgram/<int:prog_id>", views.get_completed_day_for_program),
    path("getCompletedDayForPlan/<int:plan_id>", views.get_completed_day_for_plan),
    path("getmyplan", views.get_plan),
    path("daysOfSomePlan/<int:pk>", views.Days_of_plan),
    path("getArticleCategorires", views.get_article_categories),
    path("getArticlesOfCategory/<int:pk>", views.get_articles_of_category),
    path("getArticlesInformation/<int:pk>", views.get_article_information),
    path("uplodeAvatar", views.avatar_upload_view),
    path("getAvatar", views.GetUserAvatar),
    path("getPersonalInformation", views.GetUserInformation),
    path("deleteSomePlan/<int:pk>", views.DeleteSomePlan),
    path("deleteSomeProgram/<int:pk>", views.DeleteSomeProgram),
    path("deleteDaysOfPlan/<int:pk>", views.DeleteDaysOfPlan),
    path("deleteDaysOfProgram/<int:pk>", views.DeleteDaysOfProgram),


    ]
