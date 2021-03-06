from django.db import migrations, transaction
IMAGES_DIR = 'images'
IMAGE_FILE = 'test_image.jpg'
NEW_IMAGE_FILE = 'new_test_image.jpg'


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
        ('homepage', '0002_user_test_data'),
        ('homepage', '0003_course_test_data'),
        ('homepage', '0005_professor_test_data')
    ]

    def generate_data(apps, schema_editor):
        from homepage.models import AppUser
        from homepage.models import Course
        from homepage.models import Review
        from homepage.models import Professor
        from django.core.files.uploadedfile import SimpleUploadedFile
        from os import path
        from django.conf import settings
        from datetime import datetime
        import pytz

        users = AppUser.objects.all()
        courses = Course.objects.all()
        professors = Professor.objects.all()
        image = ''

        # prevent creating a new image upon every pytest run
        if not path.exists(path.join(settings.MEDIA_ROOT, IMAGES_DIR, NEW_IMAGE_FILE)):
            image_path = path.join(settings.MEDIA_ROOT, IMAGES_DIR, IMAGE_FILE)
            image = SimpleUploadedFile(
                name=NEW_IMAGE_FILE,
                content=open(image_path, 'rb').read(),
                content_type='image/jpeg')
        else:
            image = path.join(IMAGES_DIR, NEW_IMAGE_FILE)

        date1 = datetime(2015, 10, 9, 23, 55, 59, 5, tzinfo=pytz.UTC)
        date2 = datetime(2016, 10, 9, 23, 55, 59, 5, tzinfo=pytz.UTC)
        date3 = datetime(2015, 10, 3, 20, 00, 3, 5, tzinfo=pytz.UTC)
        date4 = datetime(2017, 3, 9, 18, 20, 00, 5, tzinfo=pytz.UTC)
        date5 = datetime(2016, 5, 2, 7, 00, 00, 5, tzinfo=pytz.UTC)
        date6 = datetime(2015, 6, 1, 12, 20, 00, 5, tzinfo=pytz.UTC)

        test_data_review = [
            (1, courses[0].course_id, users[0].user.id, 5, date1,
                "Great course", 3, 10, professors[2].id, image),
            (2, courses[0].course_id, users[0].user.id, 4, date2, "I've learned a lot!", 2, 4),
            (3, courses[1].course_id, users[1].user.id, 4.5, date3,
                "The course was difficult", 5, 0, professors[0].id),
            (4, courses[1].course_id, users[1].user.id, 3.2, date4, "I didn't learn anything new", 3.7),
            (5, courses[2].course_id, users[2].user.id, 4.5, date5,
                "This course helped me to find a job", 2.5),
            (6, courses[2].course_id, users[2].user.id, 3.5, date6, "I didn't understand the material", 4),
        ]

        with transaction.atomic():
            for tdr in test_data_review:
                Review(*tdr).save()

    operations = [
        migrations.RunPython(generate_data),
    ]
