# Generated by Django 5.0.6 on 2024-07-17 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_enrollment_selectmembershipplan_trainer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SelectMembershipPlan',
            new_name='MembershipPlan',
        ),
    ]
