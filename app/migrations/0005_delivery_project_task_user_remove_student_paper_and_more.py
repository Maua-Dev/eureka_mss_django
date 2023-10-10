# Generated by Django 4.2.5 on 2023-10-10 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_student_paper'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('delivery_id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('shift', models.CharField(max_length=255)),
                ('stand_number', models.CharField(max_length=255)),
                ('is_entrepreneurship', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('delivery_date', models.DateField()),
                ('responsible', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('role', models.CharField(default='STUDENT', max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='paper',
        ),
        migrations.DeleteModel(
            name='Paper',
        ),
        migrations.DeleteModel(
            name='Professor',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.AddField(
            model_name='project',
            name='professors',
            field=models.ManyToManyField(to='app.user'),
        ),
        migrations.AddField(
            model_name='project',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='students', to='app.user'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.project'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.task'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user'),
        ),
    ]
