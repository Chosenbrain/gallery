# Generated by Django 3.0.6 on 2020-05-21 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlockPaving',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_title', models.CharField(max_length=50)),
                ('b_num_pic', models.IntegerField()),
                ('b_label', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Fencing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_title', models.CharField(max_length=50)),
                ('f_pic', models.IntegerField()),
                ('f_label', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Patios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_title', models.CharField(max_length=50)),
                ('p_pic', models.IntegerField()),
                ('p_label', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Resins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_title', models.CharField(max_length=50)),
                ('r_pic', models.IntegerField()),
                ('r_label', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Tarmac',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_title', models.CharField(max_length=50)),
                ('t_pic', models.IntegerField()),
                ('t_label', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Tarmacimage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_images', models.FileField(upload_to='images/')),
                ('tarmac', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='website.Tarmac')),
            ],
        ),
        migrations.CreateModel(
            name='Resinsimage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_images', models.FileField(upload_to='images/')),
                ('resins', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='website.Resins')),
            ],
        ),
        migrations.CreateModel(
            name='Patiosimage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_images', models.FileField(upload_to='images/')),
                ('patios', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='website.Patios')),
            ],
        ),
        migrations.CreateModel(
            name='Fencingimage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_images', models.FileField(upload_to='images/')),
                ('fencing', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='website.Fencing')),
            ],
        ),
        migrations.CreateModel(
            name='BlockPavingimage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='images/')),
                ('blockpaving', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='website.BlockPaving')),
            ],
        ),
    ]