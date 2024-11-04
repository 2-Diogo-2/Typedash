# Generated by Django 5.1.1 on 2024-10-24 13:32

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0004_delete_dica_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicoteste',
            old_name='data_teste',
            new_name='data',
        ),
        migrations.RemoveField(
            model_name='historicoteste',
            name='erros_total',
        ),
        migrations.RemoveField(
            model_name='historicoteste',
            name='frases',
        ),
        migrations.RemoveField(
            model_name='resultadosteste',
            name='acertos',
        ),
        migrations.RemoveField(
            model_name='resultadosteste',
            name='data',
        ),
        migrations.RemoveField(
            model_name='resultadosteste',
            name='tempo',
        ),
        migrations.RemoveField(
            model_name='resultadosteste',
            name='usuario',
        ),
        migrations.AddField(
            model_name='historicoteste',
            name='erros',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='historicoteste',
            name='palavras_por_minuto',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='resultadosteste',
            name='frase',
            field=models.CharField(default='Digite aqui a sua frase', max_length=255),
        ),
        migrations.AddField(
            model_name='resultadosteste',
            name='tempo_gasto',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
        migrations.AddField(
            model_name='resultadosteste',
            name='teste',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.historicoteste'),
        ),
        migrations.AlterField(
            model_name='historicoteste',
            name='tempo_total',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('groups', models.ManyToManyField(blank=True, related_name='customuser_set', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='customuser_set', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='historicoteste',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.customuser'),
        ),
    ]