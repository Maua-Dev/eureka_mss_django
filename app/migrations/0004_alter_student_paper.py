# Generated by Django 4.2.5 on 2023-09-19 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_assigment_id_paper_paper_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='paper',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.paper'),
        ),
    ]