from django.db import models
from datetime import datetime,date,timedelta
from django.dispatch import receiver
from django.db.models.signals import pre_save,post_save



class Librarian(models.Model):
    library_ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Library(models.Model):
    library_id = models.AutoField(primary_key=True)
    library_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    librarian = models.ForeignKey(Librarian, null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.library_name

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=200)
    book_price = models.IntegerField(default=0)
    ISBN = models.IntegerField()
    available = models.BooleanField(default=False)
    author = models.CharField(max_length=100, null=True,blank=True)
    total_no_books = models.IntegerField(default=0)
    stock = models.IntegerField(default=1)

    def __str__(self):
        return self.book_name


class Member(models.Model):
    member_ID = models.AutoField(primary_key=True)
    member_name = models.CharField(max_length=100)
    member_email = models.CharField(max_length=100)
    member_phone = models.IntegerField()

    def __str__(self):
        return self.member_name

class Record(models.Model):
    record_id = models.AutoField(primary_key=True)
    issued_librarian = models.ForeignKey(Librarian, null=True, on_delete=models.CASCADE)
    book_borrowed = models.ForeignKey(Book, null=True, on_delete=models.CASCADE)
    issued_to_member = models.ForeignKey(Member, null=True, on_delete=models.CASCADE)
    borrow_date = models.DateField()
    return_date = models.DateField()
    returned = models.BooleanField(default=False)
    actual_return = models.DateField()
    # pay_fine = models.IntegerField(default=0)


    @property
    def is_due(self):
        if  self.returned is not None:
            difference = self.actual_return - self.return_date
            if difference.days > 0:
                return difference.days * 10
        else:
            return 0
            # self.pay_fine = (self.borrow_date - self.return_date).days * 10
            # return self.pay_fine

    # def return_date_calculation(self):
    #     if self.returned:
    #         return self.return_date
    #     else:
    #         return 'Not returned'
    #
    # return_date_calculation.short_description = 'Returned date'


# @receiver(pre_save, sender=Record)
# def is_borrowed(sender, instance, **kwargs):
#     book_borrowed = instance.book_borrowed
#     if instance.returned == True:
#         book_borrowed.stock += 1
#         book_borrowed.save()


@receiver(post_save, sender=Record)
def is_returned(sender, instance, created, **kwargs):
    book_borrowed = instance.book_borrowed
    if instance.returned:
        book_borrowed.stock = book_borrowed.stock + 1
        book_borrowed.save()
    else:
        if book_borrowed.stock > 0:
            book_borrowed.stock = book_borrowed.stock - 1
            book_borrowed.save()
# if created:
#     if book_borrowed.available == True:
#          book_borrowed.stock -= 1
#     if book_borrowed.stock == 0:
#         book_borrowed.available = False
#     book_borrowed.save()


