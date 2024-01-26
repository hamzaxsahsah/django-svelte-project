from django.db import models


class Project(models.Model):
    # Basic project details
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    # Status can be active, completed, or paused, etc.
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('paused', 'Paused'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    # Budget and cost
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    cost_to_date = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    # Project Manager or Lead
    project_manager = models.CharField(max_length=100)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
