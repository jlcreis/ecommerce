# Generated by Django 3.1.3 on 2021-03-28 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marcador', '0002_auto_20210328_1124'),
        ('blog', '0005_auto_20210228_1636'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post_Marcador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marcador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_marcadors', to='marcador.marcador')),
                ('ppost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
            ],
        ),
    ]
