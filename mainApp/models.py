from django.db import models

gender = (
    ("Erkak", "Erkak"),
    ("Ayol", "Ayol")
)


class Major(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField()

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=255)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    main = models.BooleanField()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=6, choices=gender)
    age = models.PositiveSmallIntegerField()
    level = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
