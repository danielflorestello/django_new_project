# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Despacho(models.Model):
    iddespacho = models.AutoField(db_column='idDespacho', primary_key=True)  # Field name made lowercase.
    idpersonal = models.ForeignKey('Personal', models.DO_NOTHING, db_column='idPersonal')  # Field name made lowercase.
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='idUsuario')  # Field name made lowercase.
    fechadespacho = models.DateField(db_column='fechaDespacho')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'despacho'


class DetalleDespacho(models.Model):
    iddetalledespacho = models.AutoField(db_column='idDetalleDespacho', primary_key=True)  # Field name made lowercase.
    iddespacho = models.ForeignKey(Despacho, models.DO_NOTHING, db_column='idDespacho')  # Field name made lowercase.
    idequipo = models.ForeignKey('Equipos', models.DO_NOTHING, db_column='idEquipo')  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detalle_despacho'


class Equipos(models.Model):
    idequipo = models.AutoField(db_column='idEquipo', primary_key=True)  # Field name made lowercase.
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='idUsuario')  # Field name made lowercase.
    codigo_sap = models.IntegerField(db_column='codigo_SAP')  # Field name made lowercase.
    serie = models.CharField(db_column='Serie', max_length=20)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=30)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad')  # Field name made lowercase.
    precio = models.FloatField(db_column='Precio')  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'equipos'


class Personal(models.Model):
    idpersonal = models.AutoField(db_column='idPersonal', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=10)  # Field name made lowercase.
    cargo = models.CharField(db_column='Cargo', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'personal'


class Rol(models.Model):
    idrol = models.IntegerField(db_column='idRol', primary_key=True)  # Field name made lowercase.
    nombrerol = models.CharField(db_column='NombreRol', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rol'


class Usuario(models.Model):
    idusuario = models.AutoField(db_column='idUsuario', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=20)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=30)  # Field name made lowercase.
    dni = models.IntegerField(db_column='DNI')  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=20)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=20)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=20)  # Field name made lowercase.
    idrol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='idRol')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario'
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Despacho(models.Model):
    iddespacho = models.AutoField(db_column='idDespacho', primary_key=True)  # Field name made lowercase.
    idpersonal = models.ForeignKey('Personal', models.DO_NOTHING, db_column='idPersonal')  # Field name made lowercase.
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='idUsuario')  # Field name made lowercase.
    fechadespacho = models.DateField(db_column='fechaDespacho')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'despacho'


class DetalleDespacho(models.Model):
    iddetalledespacho = models.AutoField(db_column='idDetalleDespacho', primary_key=True)  # Field name made lowercase.
    iddespacho = models.ForeignKey(Despacho, models.DO_NOTHING, db_column='idDespacho')  # Field name made lowercase.
    idequipo = models.ForeignKey('Equipos', models.DO_NOTHING, db_column='idEquipo')  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detalle_despacho'


class Equipos(models.Model):
    idequipo = models.AutoField(db_column='idEquipo', primary_key=True)  # Field name made lowercase.
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='idUsuario')  # Field name made lowercase.
    codigo_sap = models.IntegerField(db_column='codigo_SAP')  # Field name made lowercase.
    serie = models.CharField(db_column='Serie', max_length=20)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=30)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad')  # Field name made lowercase.
    precio = models.FloatField(db_column='Precio')  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'equipos'


class Personal(models.Model):
    idpersonal = models.AutoField(db_column='idPersonal', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=10)  # Field name made lowercase.
    cargo = models.CharField(db_column='Cargo', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'personal'


class Rol(models.Model):
    idrol = models.IntegerField(db_column='idRol', primary_key=True)  # Field name made lowercase.
    nombrerol = models.CharField(db_column='NombreRol', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rol'


class Usuario(models.Model):
    idusuario = models.AutoField(db_column='idUsuario', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=20)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=30)  # Field name made lowercase.
    dni = models.IntegerField(db_column='DNI')  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=20)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=20)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=20)  # Field name made lowercase.
    idrol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='idRol')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario'
