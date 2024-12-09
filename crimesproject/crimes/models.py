from django.db import models
from django.core.exceptions import PermissionDenied

class Areas(models.Model):
    areaid = models.CharField(db_column='AreaID', primary_key=True)  # Field name made lowercase.
    areaname = models.CharField(db_column='AreaName', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'areas'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CrimeData(models.Model):
    drno = models.AutoField(primary_key=True)
    datereported = models.DateField(blank=True, null=True)
    dateoccured = models.DateField(blank=True, null=True)
    timeoccured = models.IntegerField(blank=True, null=True)
    areaid = models.IntegerField(blank=True, null=True)
    areaname = models.CharField(max_length=255, blank=True, null=True)
    reporteddistrictcode = models.IntegerField(blank=True, null=True)
    crimecode = models.CharField(max_length=10, blank=True, null=True)
    crimecodedescription = models.TextField(blank=True, null=True)
    mocodes = models.TextField(blank=True, null=True)
    victimage = models.IntegerField(blank=True, null=True)
    victimsex = models.CharField(max_length=10, blank=True, null=True)
    victimdescent = models.CharField(max_length=50, blank=True, null=True)
    premisescode = models.IntegerField(blank=True, null=True)
    premisesdescription = models.TextField(blank=True, null=True)
    weaponusedcode = models.IntegerField(blank=True, null=True)
    weaponusedfull = models.TextField(blank=True, null=True)
    statuscode = models.CharField(max_length=50, blank=True, null=True)
    statusdescription = models.TextField(blank=True, null=True)
    crimecode1 = models.IntegerField(blank=True, null=True)
    crimecode2 = models.IntegerField(blank=True, null=True)
    crimecode3 = models.IntegerField(blank=True, null=True)
    crimecode4 = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    crossstreet = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crime_data'


class CrimeLookup(models.Model):
    crimecode = models.IntegerField(db_column='CrimeCode', primary_key=True)  # Field name made lowercase.
    crimecodedescription = models.CharField(db_column='CrimeCodeDescription', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crime_lookup'


class CrimesCrimelookup(models.Model):
    crimecode = models.IntegerField(db_column='CrimeCode', primary_key=True)  # Field name made lowercase.
    crimecodedescription = models.CharField(db_column='CrimeCodeDescription', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crimes_crimelookup'


class DescentLookup(models.Model):
    descentid = models.CharField(db_column='DescentID', primary_key=True, max_length=255)  # Field name made lowercase.
    descentfull = models.CharField(db_column='DescentFull', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'descent_lookup'


class DistrictLookup(models.Model):
    reporteddistrictcode = models.IntegerField(db_column='ReportedDistrictCode', primary_key=True)  # Field name made lowercase.
    prec = models.CharField(db_column='PREC', blank=True, null=True)  # Field name made lowercase.
    aprec = models.CharField(db_column='APREC', blank=True, null=True)  # Field name made lowercase.
    bureau = models.CharField(db_column='BUREAU', blank=True, null=True)  # Field name made lowercase.
    basiccar = models.CharField(db_column='BASICCAR', blank=True, null=True)  # Field name made lowercase.
    agency = models.CharField(db_column='AGENCY', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', blank=True, null=True)  # Field name made lowercase.
    shape_leng = models.FloatField(db_column='SHAPE_LENG', blank=True, null=True)  # Field name made lowercase.
    abbrev_apr = models.CharField(db_column='ABBREV_APR', blank=True, null=True)  # Field name made lowercase.
    shape_area = models.FloatField(db_column='Shape__Area', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    shape_length = models.FloatField(db_column='Shape__Length', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.

    class Meta:
        managed = False
        db_table = 'district_lookup'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Locations(models.Model):
    drno = models.IntegerField(db_column='DRNO', primary_key=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=255, blank=True, null=True)  # Field name made lowercase.
    crossstreet = models.CharField(db_column='CrossStreet', max_length=255, blank=True, null=True)  # Field name made lowercase.
    latitude = models.DecimalField(db_column='Latitude', max_digits=9, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    longitude = models.DecimalField(db_column='Longitude', max_digits=9, decimal_places=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'locations'

    def save(self, *args, **kwargs):
        if self.pk:  
            raise PermissionDenied("Updates are not allowed on this table.")
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        raise PermissionDenied("Deletions are not allowed on this table.")


class Main(models.Model):
    drno = models.OneToOneField('Victims', models.DO_NOTHING, db_column='DRNO', primary_key=True)  # Field name made lowercase.
    datereported = models.DateField(db_column='DateReported', blank=True, null=True)  # Field name made lowercase.
    dateoccured = models.DateField(db_column='DateOccured', blank=True, null=True)  # Field name made lowercase.
    timeoccured = models.IntegerField(db_column='TimeOccured', blank=True, null=True)  # Field name made lowercase.
    reporteddistrictcode = models.IntegerField(db_column='ReportedDistrictCode', blank=True, null=True)  # Field name made lowercase.
    crimecode = models.ForeignKey(CrimeLookup, models.DO_NOTHING, db_column='CrimeCode', blank=True, null=True)  # Field name made lowercase.
    crimecode1 = models.IntegerField(db_column='CrimeCode1', blank=True, null=True)  # Field name made lowercase.
    crimecode2 = models.IntegerField(db_column='CrimeCode2', blank=True, null=True)  # Field name made lowercase.
    crimecode3 = models.IntegerField(db_column='CrimeCode3', blank=True, null=True)  # Field name made lowercase.
    crimecode4 = models.IntegerField(db_column='CrimeCode4', blank=True, null=True)  # Field name made lowercase.
    areaid = models.ForeignKey(Areas, models.DO_NOTHING, db_column='AreaID', blank=True, null=True)  # Field name made lowercase.
    premisescode = models.IntegerField(db_column='PremisesCode', blank=True, null=True)  # Field name made lowercase.
    weaponusedcode = models.ForeignKey('WeaponLookup', models.DO_NOTHING, db_column='WeaponUsedCode', blank=True, null=True)  # Field name made lowercase.
    statuscode = models.ForeignKey('StatusLookup', models.DO_NOTHING, db_column='StatusCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'main'

    def save(self, *args, **kwargs):
        if self.pk:  
            raise PermissionDenied("Updates are not allowed on this table.")
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        raise PermissionDenied("Deletions are not allowed on this table.")

class Mocodes(models.Model):
    drno = models.IntegerField(db_column='DRNO', primary_key=True)  # Field name made lowercase. The composite primary key (DRNO, Mocode) found, that is not supported. The first column is selected.
    mocode = models.IntegerField(db_column='Mocode')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'mocodes'
        unique_together = (('drno', 'mocode'),)
    def save(self, *args, **kwargs):
        if self.pk:  
            raise PermissionDenied("Updates are not allowed on this table.")
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        raise PermissionDenied("Deletions are not allowed on this table.")


class PremisesLookup(models.Model):
    premisescode = models.IntegerField(db_column='PremisesCode', primary_key=True)  # Field name made lowercase.
    premisesdescription = models.TextField(db_column='PremisesDescription')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'premises_lookup'


class StatusLookup(models.Model):
    statuscode = models.CharField(db_column='StatusCode', primary_key=True)  # Field name made lowercase.
    statusdescription = models.CharField(db_column='StatusDescription', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'status_lookup'


class Victims(models.Model):
    drno = models.IntegerField(db_column='DRNO', primary_key=True)  # Field name made lowercase.
    victimage = models.IntegerField(db_column='VictimAge', blank=True, null=True)  # Field name made lowercase.
    victimsex = models.CharField(db_column='VictimSex', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'victims'

    def save(self, *args, **kwargs):
        if self.pk:  
            raise PermissionDenied("Updates are not allowed on this table.")
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        raise PermissionDenied("Deletions are not allowed on this table.")


class WeaponLookup(models.Model):
    weaponusedcode = models.IntegerField(db_column='WeaponUsedCode', primary_key=True)  # Field name made lowercase.
    weaponusedfull = models.CharField(db_column='WeaponUsedFull', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'weapon_lookup'
