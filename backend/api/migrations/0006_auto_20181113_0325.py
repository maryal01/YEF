# Generated by Django 2.1.1 on 2018-11-13 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20181113_0259'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='JudgePoints',
            new_name='JudgePoint',
        ),
        migrations.RenameModel(
            old_name='MemberPoints',
            new_name='MemberPoint',
        ),
        migrations.RemoveField(
            model_name='round',
            name='chair',
        ),
        migrations.RemoveField(
            model_name='round',
            name='decision',
        ),
        migrations.RemoveField(
            model_name='round',
            name='win',
        ),
        migrations.AddField(
            model_name='matchup',
            name='decision',
            field=models.CharField(choices=[('Split', 'Split'), ('Unaminous', 'Unaminous')], default='Split', max_length=20),
        ),
        migrations.AddField(
            model_name='matchup',
            name='win',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Team'),
        ),
    ]