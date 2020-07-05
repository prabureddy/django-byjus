from django.db import models


class Program(models.Model):

    program_text = models.CharField(max_length=30, unique=True, blank=False,
                                    help_text="Check Once everything is written")

    def __str__(self):
        return self.program_text


class Grade(models.Model):

    program = models.OneToOneField(
        Program, on_delete=models.CASCADE)

    grade_text = models.CharField(max_length=10, default="", unique=True, blank=False,
                                  help_text="Write in correct format. for ex: 'class 6'. It is shown in everywhere")

    confirm_grade_text = models.CharField(max_length=10, default="", blank=False,
                                          help_text="Confirm grade")

    def __str__(self):
        return self.grade_text
