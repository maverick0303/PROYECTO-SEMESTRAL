# Generated by Django 4.2.1 on 2023-05-26 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id_comuna', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id_pregunta', models.AutoField(primary_key=True, serialize=False)),
                ('respuesta', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id_region', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id_rol', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('rut', models.CharField(max_length=13)),
                ('correo', models.CharField(max_length=30)),
                ('clave', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=13)),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiendita.pregunta')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiendita.rol')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.AutoField(primary_key=True, serialize=False)),
                ('f_venta', models.DateField()),
                ('f_despacho', models.DateField()),
                ('f_entrega', models.DateField()),
                ('total', models.IntegerField()),
                ('carrito', models.BooleanField(verbose_name='para saber si el usuario tiene objetos en el carrito')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiendita.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('cod_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
                ('descripcion', models.CharField(max_length=60)),
                ('stock', models.IntegerField()),
                ('foto', models.ImageField(upload_to='tiendita')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiendita.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id_direccion', models.AutoField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=30)),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiendita.comuna')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiendita.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiendita.region'),
        ),
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id_boleta', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('subtotal', models.IntegerField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiendita.producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiendita.venta')),
            ],
        ),
    ]
