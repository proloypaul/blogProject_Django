# Generated by Django 4.2.5 on 2023-11-07 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postblog',
            name='blogImage',
            field=models.ImageField(default='https://d2v9ipibika81v.cloudfront.net/uploads/sites/210/Profile-Icon.png', upload_to='blog_pics'),
        ),
    ]
