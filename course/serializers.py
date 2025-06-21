from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from .models import Types,UserAccount,Plan,PlanDay,ArticleCategory,PlanExercises,Programs,ProgramDay,Exercises,UserProgrameState,Article,UserPlanState
from django.contrib.auth import get_user_model

User=get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model=User
        fields='__all__'



class TypeSerializers(serializers.ModelSerializer):
    class Meta:
        model=Types
        fields=["id","TypeName","TypeDescription","TypeImage"]
        
        
class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model=Programs
        fields='__all__'
        
class ProgramDaySerializer(serializers.ModelSerializer):
    class Meta:
        model=ProgramDay
        fields='__all__'
        
class ExercisesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Exercises
        fields='__all__'
        
class Exercises1Serializer(serializers.ModelSerializer):
    class Meta:
        model=Exercises
        fields='__all__'
        
class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProgrameState
        fields='__all__'

class SomeArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields='__all__'
        
class CdaysSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProgrameState
        fields=["ComplatedDays"]

class CdaysForPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserPlanState
        fields=["ComplatedDays"]

# class InfoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Articles
#         fields='__all__'

class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["image"]

class GetImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["image"]

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model=Plan
        fields='__all__'

class PlanDaySerializer(serializers.ModelSerializer):
    class Meta:
        model=PlanDay
        fields='__all__'

class PlanExercisesSerializer(serializers.ModelSerializer):
    class Meta:
        model=PlanExercises
        fields='__all__'

class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields='__all__'

class ArticleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=ArticleCategory
        fields='__all__'

class PlanExercises1Serializer(serializers.ModelSerializer):
    class Meta:
        model=PlanExercises
        fields='__all__'

class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['image','name']

# class UserPlanStateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields=['id','goal']



        