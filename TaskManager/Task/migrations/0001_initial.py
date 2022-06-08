# Generated by Django 4.0.5 on 2022-06-08 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=50)),
                ('title', models.CharField(choices=[('draft', 'draft'), ('active', 'active'), ('done', 'done'), ('achieved', 'achieved')], default='draft', max_length=100)),
            ],
        ),
    ]