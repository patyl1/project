from django.contrib import admin
from .models import Category, Course
# Register your models here.


admin.site.site_header = "Hello Admin"
admin.site.site_title = "Courses Project"
admin.site.index_title = "Admin"


class CoursesInline(admin.TabularInline):
    model = Course
    exclude = ['created_at']
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price')


class CaytegoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Dates', {
            'fields': ['created_at'],
            'classes': ['collapse']
        })
    ]
    inlines = [CoursesInline]


admin.site.register(Category, CaytegoryAdmin)
admin.site.register(Course, CourseAdmin)
