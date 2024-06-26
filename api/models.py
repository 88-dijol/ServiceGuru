from django.db import models

from django.db.models import Sum

from django.contrib.auth.models import User



class Customer(models.Model):

    name=models.CharField(max_length=200)

    email=models.CharField(max_length=200)

    phone=models.CharField(max_length=200)

    vehicle_number=models.CharField(max_length=200)

    running_km=models.PositiveIntegerField()

    technician=models.ForeignKey(User,on_delete=models.CASCADE)

    options=(

        ("pending","pending"),

        ("in-progress","in-progress"),

        ("completed","completed")
    )

    status=models.CharField(max_length=200,choices=options,default="pending")

    created_date=models.DateTimeField(auto_now_add=True)

    update_date=models.DateTimeField(auto_now=True)

    is_active=models.BooleanField(default=True)

    # custom method  ---to get count of work
    @property     # customerinte oru property aayit edukan decorator koduka
    def work_count(self):           #self is customer Object,for pointing an instance(customer obj it can be dijol,dinoy etc for taking that we are using self)

        # return self.Work_set.all().count() or
        return Work.objects.filter(customer=self).count()
    

    @property
    def work_total(self):

        return Work.objects.filter(customer=self).values('amount').aggregate(total=Sum('amount'))['total']
    

    # when we are taking a customer we need to return the customer work also for that we are using this method:
    @property
    def works(self):

        return Work.objects.filter(customer=self)

    def __str__(self) -> str:

        return self.name


class Work(models.Model):

    title=models.CharField(max_length=200)

    description=models.TextField()

    amount=models.PositiveIntegerField()

    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)

    created_date=models.DateTimeField(auto_now_add=True)

    update_date=models.DateTimeField(auto_now=True)

    is_active=models.BooleanField(default=True)

    def __str__(self) -> str:

        return self.title



