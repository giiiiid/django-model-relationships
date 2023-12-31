# Generated by Django 4.2.2 on 2023-11-08 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postget', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField(null=True)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('delivery', models.CharField(choices=[('Pick up', 'Pick up'), ('Delivery', 'Delivery')], max_length=150, null=True)),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('Bantama', 'Bantama'), ('Santasi', 'Santasi'), ('Abrepo', 'Abrepo'), ('North', 'North'), ('South', 'South')], max_length=150, null=True)),
                ('invoice', models.CharField(max_length=150, null=True)),
                ('customer_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='postget.customer')),
                ('food', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='postget.food')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Room',
        ),
        migrations.AddField(
            model_name='food',
            name='tag',
            field=models.ManyToManyField(to='postget.tag'),
        ),
    ]
