# Generated by Django 3.0.3 on 2020-03-09 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website1', '0002_auto_20200306_2307'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_date']},
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='post',
            name='cover2',
            field=models.FileField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='l_heading',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='post',
            name='l_heading_text',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='post',
            name='quote',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='post',
            name='quote_name',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='post',
            name='s_heading',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='post',
            name='s_heading_text',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AddField(
            model_name='post',
            name='tag_1',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='post',
            name='tag_2',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='post',
            name='tag_3',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='post',
            name='text_2',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.FileField(default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
