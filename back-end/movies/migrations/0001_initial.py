# Generated by Django 3.2.18 on 2023-05-19 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllMovie',
            fields=[
                ('adult', models.BooleanField()),
                ('backdrop_path', models.URLField(null=True)),
                ('movie_id', models.IntegerField(primary_key=True, serialize=False)),
                ('original_language', models.CharField(max_length=10)),
                ('overview', models.TextField()),
                ('popularity', models.DecimalField(decimal_places=4, max_digits=100000)),
                ('poster_path', models.URLField()),
                ('release_date', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=500)),
                ('vote_average', models.DecimalField(decimal_places=3, max_digits=10)),
                ('vote_count', models.IntegerField(default=0)),
                ('eng_title', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='TodayMovie',
            fields=[
                ('adult', models.BooleanField()),
                ('backdrop_path', models.TextField(null=True)),
                ('movie_id', models.IntegerField(primary_key=True, serialize=False)),
                ('original_language', models.CharField(max_length=10)),
                ('overview', models.TextField()),
                ('popularity', models.DecimalField(decimal_places=4, max_digits=100000)),
                ('poster_path', models.URLField()),
                ('release_date', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=500)),
                ('vote_average', models.DecimalField(decimal_places=3, max_digits=10)),
                ('vote_count', models.IntegerField(default=0)),
                ('eng_title', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='TodayMovieCreated',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('today', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TodayRelatedVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.URLField(null=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.todaymovie')),
            ],
        ),
        migrations.CreateModel(
            name='TodayGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_ids', models.CharField(max_length=50)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.todaymovie')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.allmovie')),
            ],
        ),
        migrations.CreateModel(
            name='AllRelatedVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.URLField(null=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.allmovie')),
            ],
        ),
        migrations.CreateModel(
            name='AllGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_ids', models.CharField(max_length=50, null=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.allmovie')),
            ],
        ),
    ]
