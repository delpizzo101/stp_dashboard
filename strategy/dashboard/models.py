from django.db import models
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    PHASES = (
        ('0', 'Backlog'),
        ('1', 'Ramp-Up'),
        ('2', 'Go_No-Go Decision'),
        ('3', 'Development_Implementation'),
        ('4', 'Stabilization'),
        ('5', 'Project Closing'),
    )

    CATEGORY = (
        ('1', 'Training & Development'),
        ('2', 'Customer Experience'),
        ('3', 'Process Improvement'),
        ('4', 'IT'),
        ('5', 'Management & Controls'),
    )

    STATUS = (
        ('1', 'Not Started'),
        ('2', 'In Progress'),
        ('3', 'Completed'),
        ('4', 'On Hold'),
    )

    project_id = models.BigAutoField(primary_key=True)
    stakeholder = models.CharField(max_length=70)
    project_name = models.CharField(max_length=100)
    project_category = models.CharField(max_length=70, choices=CATEGORY)
    project_details = models.TextField()
    project_phase = models.CharField(max_length=2, choices=PHASES)
    status = models.CharField(max_length=50, choices=STATUS)
    cost_estimate = models.IntegerField()
    actual_cost = models.IntegerField()
    #create_date = models.DateTimeField(default=timezone.now())
    edit_date = models.DateTimeField(blank=True, null=True)
    #resource_id = models.ForeignKey('Resource', on_delete=models.CASCADE,)

 

    def publish(self):
        self.edit_date = timezone.now()
        self.save()

    def __str__(self):
        return self.project_name 

# class Resource(models.Model):
#     resource_id=models.AutoField(primary_key=True)