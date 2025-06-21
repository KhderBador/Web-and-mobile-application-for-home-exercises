from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status,permissions
from rest_framework.parsers import MultiPartParser,FormParser

from .models import Types,CompletedDaysByUserForPlan ,CompletedDaysByUser,Programs,ProgramDay,Exercises,UserProgrameState,UserAccount,DataSet,Plan,PlanDay,PlanExercises,UserPlanState,ArticleCategory,Article
from .serializers import TypeSerializers,CdaysForPlanSerializer,ProgramSerializer,ProgramDaySerializer,ExercisesSerializer,Exercises1Serializer,CdaysSerializer,PostImageSerializer,GetImageSerializer,PlanSerializer,PlanDaySerializer,PlanExercisesSerializer,PlanExercises1Serializer,ArticleCategorySerializer,ArticlesSerializer,SomeArticleSerializer,GetUserSerializer
from django.contrib.auth import authenticate,login
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from sklearn.cluster import KMeans
from sklearn import tree
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes
from django.conf import settings
import pickle
import jwt
import os

# from rest_framework.authtoken.models import Token

# # token = Token.objects.get(key='your_token')
# # print(token.user)  # Should print the associated user
# # print(token.user.is_active)  # Should be True

MODEL_PATH=os.path.join(os.path.dirname(__file__),'decision_tree_model.pkl')
with open(MODEL_PATH,'rb') as file:
    model=pickle.load(file)









def queryset_to_dataframe(queryset,newraw):
    data = queryset
    data.append(newraw)  # Convert the queryset to a list of dictionaries
    df = pd.DataFrame(data) 
    len=data.__len__()
    # Create a Pandas DataFrame from the list of dictionaries
    return df,len


# Create your views here.
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def Type_Ex(request):
    print(request.user.id)
    
    
    if request.method == "GET":
        type = Types.objects.all()
        serializer=TypeSerializers(type,many=True)
        return Response(serializer.data)
    
    
   #fk




@api_view(["POST"])
@permission_classes([IsAuthenticated])
def get_plan(request):
    if request.method == "POST":
        
        #1.this is user information which we will use tp predict the perfict plan
        user_data=request.data
        print(user_data)
        User_Weight=user_data.get('User_Weight') 
        User_Tall=user_data.get('User_Tall')
        Age=user_data.get('Age') 
        Physical_Condation=user_data.get('Physical_Condation')
        Main_Goal=user_data.get('Main_Goal')
        Gender=user_data.get('gender')
        print("level is :",Physical_Condation)
        print("goal is :",Main_Goal)
        if Main_Goal==1 :
            goal='weight loss'
        elif Main_Goal==2:
            goal='fitness'
        else :
            goal='muscle building'
        

        #this is a test data

        # Averege_Weight=76
        # Averege_Tall=177
        # Physical_Condation='3-5 pushs'
        # Main_Goal='muscle building'

       #age: 18->32 32->46 46->60
        if Age>=18 and Age<=32 :
            Age=1
        elif Age>32 and Age<=46 :
            Age=2
        else:
            Age=3
        #tall: 150->166.6 166.6->183.2 183.2->200
        if User_Tall>=150 and User_Tall<=166.6 :
            User_Tall=1
        elif User_Tall>166.6 and User_Tall<=183.2 :
            User_Tall=2
        else:
            User_Tall=3
       
        #weight:50->73.3 73.3->96.6 96.6->120
        if User_Weight>=50 and User_Weight<=73.3 :
            User_Weight=1
        elif User_Weight>73.3 and User_Weight<=96.6 :
            User_Weight=2
        else:
            User_Weight=3

        #user_input=pd.DataFrame({"age":Age,"tall":User_Tall,"weight":User_Weight,"main_goal":Main_Goal,"physical level":Physical_Condation}, index=[0])

        UserPlanId=model.predict([[Age,User_Tall,User_Weight,Main_Goal,Physical_Condation]])
        print("this is plan id :",UserPlanId[0])
        
        
        #14.here we use id plan to get total days and total exersises for this plan from plan table
        UserPlan=Plan.objects.all().filter(id=UserPlanId[0]).first()
        print("total days of user plan is :",UserPlan.TotalDays)
        print("total exersises of user plan is :",UserPlan.TotalExercises)
        serializerplan=PlanSerializer(UserPlan)

        print("the user plan is :",serializerplan.data)
        user=UserPlanState()
        user.ComplatedDays= 0
        user.UserName=UserAccount.objects.get(id=request.user.id)
        user.UserPlan=Plan.objects.get(id=UserPlanId[0])
        user.UserGoal=goal
        user.Gender=Gender
        user.save()

        
        return Response(serializerplan.data,status=status.HTTP_200_OK)
    

@api_view(["GET"])
def Program_EX(request,pk):
   
    prog=Programs.objects.filter(TypeId=pk)
   # prog=Programs.objects.get(TypeId=pk)
 
     
    if request.method == 'GET':
       serializer=ProgramSerializer(prog,many=True)
       return Response(serializer.data)
   
   
@api_view(["GET"])
def Program_only(request,pk):
    prog1=get_object_or_404(Programs,id=pk)
    if request.method == 'GET':
       serializer=ProgramSerializer(prog1)
       return Response(serializer.data)
    

#fk
@api_view(["GET"])
def Day_only(request,pk):
    
    
    day=ProgramDay.objects.all().filter(ProgramId=pk)
    if request.method == 'GET':
       serializer=ProgramDaySerializer(day ,many=True)
       return Response(serializer.data)
    


 #fk  

@api_view(["GET"])
def Day_Ex(request,pk):
    exc=Exercises.objects.all().filter(DayId=pk).order_by('id')
    
    if request.method == 'GET':
       serializer=ExercisesSerializer(exc,many=True)
       return Response(serializer.data)
    

@api_view(["GET"])
def Plan_Day_Ex(request,pk):
    ExsOfDayPlan=PlanExercises.objects.all().filter(DayId=pk).order_by('id')
    
    if request.method == 'GET':
       serializer=PlanExercisesSerializer(ExsOfDayPlan,many=True)
       print(serializer.data)
       return Response(serializer.data)

@api_view(["GET"])
def Exercise(request,pk):
    exc1=get_object_or_404(Exercises,id=pk)
    if request.method == 'GET':
       serializer=Exercises1Serializer(exc1)
       
       return Response(serializer.data)
    
@api_view(["GET"])
def Plan_Exercise(request,pk):
    exc1=get_object_or_404(PlanExercises,id=pk)
    if request.method == 'GET':
       serializer=PlanExercises1Serializer(exc1)
       return Response(serializer.data)
   
   
@api_view(["GET"])
def Cday(request,name):
    UserProIdd=UserAccount.objects.all().filter(UserName=name)
    UserProId=Programs.objects.all().filter(UserId__in=UserProIdd)
    UserProId1=UserProgrameState.objects.all().filter(UserName__in=UserProIdd)
    if request.method == 'GET':
       serializer=CdaysSerializer(UserProId1,many=True)
       return Response(serializer.data)

#@api_view(["GET","POST"])
#def UserInfo(request,name):
   # U#serProIdd=UserAcc.objects.all().filter(UserName=name)
    #if request.method == 'GET':
     #  serializer=UserSerializer(UserProIdd,many=True)
    #   return Response(serializer.data)
  
   #fk

@api_view(["GET"])
def ProgInfo(request):
   # UserProIdd=UserAcc.objects.all().filter(UserName=name)
    #UserProId=Programs.objects.all().filter(UserId__in=UserProIdd)
   # UserProId1=UserProgrameState.objects.prefetch_related('UserPrograme').values('UserPrograme__ProgramName','ComplatedDays')
  # UserProId=Programs.objects.all()
 #   UserProId1=UserPrograme.userprogramestate__set.all()
    UserProId1 = Programs.objects.prefetch_related('userprogramestate_set')

    if request.method == 'GET':
       serializer=InfoSerializer(UserProId1,many=True)
       return Response(serializer.data)

@api_view(["POST"])
def UserImage(request, format=all):
        serializer = PostImageSerializer(data=request.data)
        parser=( MultiPartParser,FormParser)
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def GetUserAvatar(request):
   user=request.user
   if request.method == 'GET':
       serializer=GetImageSerializer(user)
       print("the image is :",serializer.data)
       return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def GetUserInformation(request):
   user=request.user
   if request.method == 'GET':
       serializer=GetUserSerializer(user)
       print("the image is :",serializer.data['image'])
       print("the name is :",serializer.data['name'])

       return Response(serializer.data)

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def IncreaseCDays(request):
        user_id=request.user.id
        print("this user id from token:",request.user.id)
        # user_id = request.data.get('user_id')
        prog_id = request.data.get('prog_id')
        day_id=request.data.get('day_id')
        if CompletedDaysByUser.objects.all().filter(UserName=UserAccount.objects.get(id=user_id),Day=ProgramDay.objects.get(id=day_id)):
            return Response({'message': 'exersises of that day have finished already'}, status=status.HTTP_200_OK)
        
        user = UserProgrameState.objects.all().filter(UserName=UserAccount.objects.get(id=user_id),UserPrograme=Programs.objects.get(id=prog_id)).first()
        if user!=None:
         user.ComplatedDays += 1
         user.save()
         userday=CompletedDaysByUser()
         userday.UserName=UserAccount.objects.get(id=user_id)
         userday.Day=ProgramDay.objects.get(id=day_id)
         userday.save()
         return Response({'message': 'finish day'}, status=status.HTTP_200_OK)
        else:
          user=UserProgrameState()
          userday=CompletedDaysByUser()
          user.ComplatedDays= 1
          user.UserName=UserAccount.objects.get(id=user_id)
          user.UserPrograme=Programs.objects.get(id=prog_id)
          user.save()
          userday.UserName=UserAccount.objects.get(id=user_id)
          userday.Day=ProgramDay.objects.get(id=day_id)
          userday.save()
          return Response( status=status.HTTP_200_OK)
        

@api_view(["PUT"])
@permission_classes([IsAuthenticated]) 
def IncreaseCDaysForPlan(request):
    
        user_id=request.user.id
        day_id=request.data.get('day_id')
        user_goal=request.data.get('user_goal')
        print("this user id from token:",request.user.id)
        plan_id = request.data.get('plan_id')
        if CompletedDaysByUserForPlan.objects.all().filter(UserName=UserAccount.objects.get(id=user_id),Day=PlanDay.objects.get(id=day_id)):
            return Response({'message': 'exersises of that day have finished already'}, status=status.HTTP_200_OK)
        
        user = UserPlanState.objects.all().filter(UserName=UserAccount.objects.get(id=user_id),UserPlan=Plan.objects.get(id=plan_id)).first()
        if user!=None:
         user.ComplatedDays += 1
         user.save()
         userday=CompletedDaysByUserForPlan()
         userday.UserName=UserAccount.objects.get(id=user_id)
         userday.Day=PlanDay.objects.get(id=day_id)
         userday.save()
         return Response({'message': 'finish day'}, status=status.HTTP_200_OK)
        else:
          
          userday=CompletedDaysByUserForPlan()
          userday.UserName=UserAccount.objects.get(id=user_id)
          userday.Day=PlanDay.objects.get(id=day_id)
          userday.save()
          
          return Response( status=status.HTTP_200_OK)
            
        

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_started_programs(request):
    user_id=request.user.id
    print("this is user id :",user_id)
    programs=[]
    
    
    userprograms= UserProgrameState.objects.filter(UserName=UserAccount.objects.get(id=user_id)) 
  
    for program in userprograms :
          p=Programs.objects.all().filter(id=program.UserPrograme.id)
    
          serializer=ProgramSerializer(p,many=True)
          programs.append(serializer.data[0])
        #   print(programs)
    return Response(programs)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_started_plans(request):
  
    plans=[]
    user_id=request.user.id
    print("this is userplan id :",user_id)
    userplans= UserPlanState.objects.filter(UserName=UserAccount.objects.get(id=user_id)) #pk
  
    for plan in userplans :
          p=Plan.objects.all().filter(id=plan.UserPlan.id)
    
          serializer=PlanSerializer(p,many=True)
          serializer.data[0]["goal"]=plan.UserGoal
          serializer.data[0]["gender"]=plan.Gender
          
          plans.append(serializer.data[0])
          print(plans)
    return Response(plans)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_completed_day_for_program(request,prog_id):
      user_id=request.user.id
      print(user_id)
      print(prog_id)
      user = UserProgrameState.objects.filter(UserName=UserAccount.objects.get(id=user_id),UserPrograme=Programs.objects.get(id=prog_id)).first()
      if user :
        print("user is :"+user.UserName.name)
        print("program is :"+user.UserPrograme.ProgramName)
        serializer=CdaysSerializer(user)
        print(serializer.data)
        return Response(serializer.data,status=status.HTTP_200_OK)
      else :
          return Response({'ComplatedDays':0},status=status.HTTP_200_OK)
      

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_completed_day_for_plan(request,plan_id):
      user_id=request.user.id
      print(user_id)
      print(plan_id)
      user = UserPlanState.objects.filter(UserName=UserAccount.objects.get(id=user_id),UserPlan=Plan.objects.get(id=plan_id)).first()
      if user :
        print("user is :"+user.UserName.name) 
        # print("program is :"+user.UserPlan.ProgramName)
        serializer=CdaysForPlanSerializer(user)
        print(serializer.data)
        return Response(serializer.data,status=status.HTTP_200_OK)
      else :
          return Response({'ComplatedDays':0},status=status.HTTP_200_OK)

@api_view(["GET"])
def Days_of_plan(request,pk):
    
    day=PlanDay.objects.all().filter(PlanId=pk)
    if request.method == 'GET':
       serializer=PlanDaySerializer(day ,many=True)
       return Response(serializer.data)

    
    # try:
    #     userprograms= UserProgrameState.get_object_or_404(UserName=get_object_or_404(UserAccount,id=user_id))
    #     for program in userprograms :
    #         programs.append(Programs.objects.filter(id=program.UserPrograme))
    #     serializer=ProgramSerializer(programs,many=True)
    #     return Response(serializer.data)
    
    # print(user)
        # started_programs = user.UserPrograme.all()
        # serializer = ProgramSerializer(started_programs, many=True)
        # return Response(serializer.data)
            
    # except :
    #     return Response({"message": "User not found"}, status=404)


@api_view(["GET"])
# @permissions_classes([IsAuthenticated])
def get_article_categories(request):
    if request.method == "GET":
        ArticleCategorys= ArticleCategory.objects.all()
        serializer=ArticleCategorySerializer(ArticleCategorys,many=True)
        return Response(serializer.data)


@api_view(["GET"])
def get_articles_of_category(request,pk):
    articles=Article.objects.filter(CategoryId=pk)
    if request.method == 'GET':
       serializer=ArticlesSerializer(articles,many=True)
       return Response(serializer.data)



@api_view(["GET"])
def get_article_information(request,pk):

    prog1=get_object_or_404(Article,id=pk)
    if request.method == 'GET':
       serializer=SomeArticleSerializer(prog1)
       return Response(serializer.data)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def avatar_upload_view(request, format=None):
    print("this is user :",request.user)
    if 'avatar' in request.FILES:
        avatar = request.FILES['avatar']
        # Save the avatar to the user's profile
        request.user.image= avatar
        request.user.save()
        return Response({'message': 'Avatar uploaded successfully'}, status=status.HTTP_201_CREATED)
    else:
        return Response({'error': 'No avatar found in request'}, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def DeleteSomePlan(request,pk):
    user_id=request.user.id
    userplan=UserPlanState.objects.filter(UserPlan=Plan.objects.get(id=pk), UserName=UserAccount.objects.get(id=user_id)).delete()
    return Response(status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def DeleteSomeProgram(request,pk):
    user_id=request.user.id
    userrogram=UserProgrameState.objects.filter(UserPrograme=Programs.objects.get(id=pk), UserName=UserAccount.objects.get(id=user_id)).delete()
    return Response(status=status.HTTP_200_OK)



@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def DeleteDaysOfPlan(request,pk):
    user_id=request.user.id
    userdays=CompletedDaysByUserForPlan.objects.filter(Day=PlanDay.objects.get(id=pk), UserName=UserAccount.objects.get(id=user_id)).delete()
    return Response(status=status.HTTP_200_OK)



@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def DeleteDaysOfProgram(request,pk):
    user_id=request.user.id
    userdays=CompletedDaysByUser.objects.filter(Day=ProgramDay.objects.get(id=pk), UserName=UserAccount.objects.get(id=user_id)).delete()
    return Response(status=status.HTTP_200_OK)