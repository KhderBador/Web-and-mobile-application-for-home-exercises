from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

# Create your models here.
class UserAccountManager(BaseUserManager):
    def create_superuser(self,name, password, **other_fields):

        # other_fields.setdefault('is_staff',True)
         other_fields.setdefault('is_superuser',True)
         other_fields.setdefault('is_active',True)

         #if other_fields.get('is_staff') is not True:
             # raise ValueError('Superuser must be assigned to is_staff=True.')
         if other_fields.get('is_superuser') is not True:
               raise ValueError('Superuser must be assigned to is_superuser=True.')

         return self.create_user(name, password)
    def create_user(self,name,password):
        # if not email :
        #     raise ValueError('user must have an email address')
        # email=self.normalize_email(email)
        user=self.model( name=name)

        user.set_password(password)
        
        user.save()
        return user
   

class UserAccount(AbstractBaseUser,PermissionsMixin):
    name=models.CharField(max_length=15 , null=False ,unique=True)
    # email=models.EmailField(max_length=254  , null=False,unique=True)
    image = models.ImageField(upload_to="images/")
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=True)
   # Password=models.CharField(max_length=20  , null=False)
    #Image=models.ImageField(null=True,blank=True,upload_to="images/")

    objects=UserAccountManager()
    USERNAME_FIELD='name'
    # REQUIRED_FIELDS=['name']
    
    def get_full_name(self) :
        return self.name

    def get_short_name(self) :
        return self.name

    def __str__(self) :
        return self.name
    
class Types (models.Model): 
    TypeName=models.CharField(max_length=15  , null=False)
    TypeDescription=models.CharField(max_length=250)
    TypeImage=models.ImageField(null=False,blank=True,upload_to="images/")
    
    
    def __str__(self) :
        return str(self.TypeName)
    
    
 
class Programs (models.Model):
    
    TypeId=models.ForeignKey(Types,default="",related_name="programs", on_delete=models.CASCADE)
    ProgramName=models.CharField(max_length=30  , null=False)
    ProgramDescription=models.CharField(max_length=500)
    ProgramImage=models.ImageField(null=False,blank=True,upload_to="images/")
    TotalDays=models.IntegerField()
    
    
    
    def __str__(self) :
        return str(self.ProgramName)
    
class UserProgrameState(models.Model):
    UserName=models.ForeignKey(UserAccount,default="", related_name="ups1", on_delete=models.CASCADE)
    UserPrograme=models.ForeignKey(Programs,default="", related_name="ups2",on_delete=models.CASCADE)
    ComplatedDays=models.IntegerField()
    
    def __str__(self) :
        return str(self.UserName)


class ProgramDay (models.Model):
    ProgramId=models.ForeignKey(Programs,default="", related_name="programday", on_delete=models.CASCADE)
    DayName=models.CharField(max_length=20) 
    
    def __str__(self) :
        return str(self.DayName)
    

class CompletedDaysByUser(models.Model):
    UserName=models.ForeignKey(UserAccount,default="", related_name="cdu1", on_delete=models.CASCADE)
    Day=models.ForeignKey(ProgramDay,default="", related_name="cdy2",on_delete=models.CASCADE)
    def __str__(self) :
        return str(self.Day)
    

    
class Exercises (models.Model):   
    DayId=models.ForeignKey(ProgramDay,default="",related_name="exercises", on_delete=models.CASCADE)
    ExerciseName=models.CharField(max_length=30  , null=False)
    ExerciseDescription=models.CharField(max_length=250)
    ExerciseImage=models.ImageField(null=False,blank=True,upload_to="images/")
    ExerciseTime=models.IntegerField()
    def __str__(self) :
        return str(self.ExerciseName)




class Plan(models.Model):
    TotalDays=models.IntegerField()
    TotalExercises=models.IntegerField()

class PlanDay (models.Model):
    PlanId=models.ForeignKey(Plan,default="", related_name="planday", on_delete=models.CASCADE)
    DayName=models.CharField(max_length=20) 

class CompletedDaysByUserForPlan(models.Model):
    UserName=models.ForeignKey(UserAccount,default="", related_name="c1", on_delete=models.CASCADE)
    Day=models.ForeignKey(PlanDay,default="", related_name="c2",on_delete=models.CASCADE)
    def __str__(self) :
        return str(self.Day)

class PlanExercises (models.Model):   
    DayId=models.ForeignKey(PlanDay,default="",related_name="planexercises", on_delete=models.CASCADE)
    ExerciseName=models.CharField(max_length=30  , null=False)
    ExerciseDescription=models.CharField(max_length=250)
    ExerciseImage=models.ImageField(null=False,blank=True,upload_to="images/")
    ExerciseTime=models.IntegerField()
    def __str__(self) :
        return str(self.ExerciseName)

class DataSet (models.Model):
    GOALS=(
      ('muscle building','muscle building'),
      ('weight loss','weight loss'),
      ('fitness','fitness'),

    )

    STATUS=(
        ('3-5 pushs','3-5 pushs'),
        ('5-7 pushs','5-7 pushs'),
        ('7-10 pushs','7-10 pushs'),
    )



    PlanId=models.ForeignKey(Plan,default="", related_name="dataset", on_delete=models.CASCADE)
    
    AveregeWeight=models.IntegerField()
    Age=models.IntegerField()
    AveregeTall=models.IntegerField()
    MainGoal=models.CharField(max_length=30  , null=False,choices=GOALS)
    PhysicalCondation=models.CharField(max_length=30  , null=False,choices=STATUS)


class UserPlanState(models.Model):
    UserName=models.ForeignKey(UserAccount,default="", related_name="upls1", on_delete=models.CASCADE)
    UserPlan=models.ForeignKey(Plan,default="", related_name="upls2",on_delete=models.CASCADE)
    ComplatedDays=models.IntegerField()
    UserGoal=models.CharField(max_length=30  , null=False)
    Gender=models.CharField(max_length=30  , null=False,default='')


class ArticleCategory (models.Model):
    CategoryName=models.CharField(max_length=20  , null=False)
    CategoryImage=models.ImageField(null=False,blank=True,upload_to="images/")


class Article(models.Model):
    CategoryId=models.ForeignKey(ArticleCategory,default="", related_name="article", on_delete=models.CASCADE)
    ArticleName=models.CharField(max_length=50  , null=False)
    ArticleImage=models.ImageField(null=False,blank=True,upload_to="images/")
    ArticleText=models.CharField( null=False)
    ArticleAuthor=models.CharField(max_length=20  , null=False)
    def __str__(self) :
        return str(self.ArticleName)
 

    
#هي مشان بس يجيب نطلب مثلا يوم معين تطلع كل البرامج يلي فيه او اذا طلبنا برنامج معين يطلع كل الايام المتعلقة فيهrelated name 