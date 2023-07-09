from django.core.management.base import BaseCommand
#import Course
from ...models import Course
from ...models import Teacher
import csv
import os

class Command(BaseCommand):
    help = 'Seeds the database with initial data'

    def handle(self, *args, **options):
        # Define your seed data
        file_path = os.path.join(os.path.dirname(__file__), 'data.csv')
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                name = row[0]
                description = row[1]
                initials = row[2]
                teacher_names = row[3].replace('[', '').replace(']', '').replace("'","").split(';')

                # Create the course
                course, _ = Course.objects.update_or_create(name=name, description=description, initials=initials)

                # Add the teachers
                for teacher_name in teacher_names:
                    teacher, _ = Teacher.objects.get_or_create(name=teacher_name, ratingOrganized=0, ratingCommunication=0, ratingMaterial=0)
                    course.teachers.add(teacher)

        last_teacher = Teacher.objects.order_by('-addedDate').last()
        for teacher in Teacher.objects.all():
            print(f'teacher {teacher.course_set.all()}')
        success = last_teacher.course_set.all()
        print(f'success {success}')
        self.stdout.write(self.style.SUCCESS('Seed data successfully populated'))
        last_teacher = Teacher.objects.order_by('-addedDate').first()
        success = last_teacher.course_set.all()
        self.stdout.write(self.style.SUCCESS(success))

