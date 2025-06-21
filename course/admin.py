from django.contrib import admin

# Register your models here.
# from .models import UserAccount
# admin.site.register(UserAccount)

from .models import Types

admin.site.register(Types)

from .models import Programs
admin.site.register(Programs)

from .models import ProgramDay
admin.site.register(ProgramDay)

from .models import Exercises
admin.site.register(Exercises)

from .models import UserProgrameState
admin.site.register(UserProgrameState)

from .models import Plan
admin.site.register(Plan)

from .models import PlanDay
admin.site.register(PlanDay)


from .models import PlanExercises
admin.site.register(PlanExercises)

from .models import DataSet
admin.site.register(DataSet)

from .models import UserPlanState
admin.site.register(UserPlanState)

from .models import Article
admin.site.register(Article)

from .models import ArticleCategory
admin.site.register(ArticleCategory)

from .models import CompletedDaysByUser
admin.site.register(CompletedDaysByUser)


from .models import CompletedDaysByUserForPlan
admin.site.register(CompletedDaysByUserForPlan)

