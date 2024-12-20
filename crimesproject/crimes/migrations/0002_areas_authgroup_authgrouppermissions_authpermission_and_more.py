# Generated by Django 5.1.3 on 2024-12-05 04:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crimes", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Areas",
            fields=[
                (
                    "areaid",
                    models.CharField(
                        db_column="AreaID", primary_key=True, serialize=False
                    ),
                ),
                ("areaname", models.CharField(db_column="AreaName", max_length=255)),
            ],
            options={
                "db_table": "areas",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthGroup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150, unique=True)),
            ],
            options={
                "db_table": "auth_group",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthGroupPermissions",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "auth_group_permissions",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthPermission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("codename", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "auth_permission",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128)),
                ("last_login", models.DateTimeField(blank=True, null=True)),
                ("is_superuser", models.BooleanField()),
                ("username", models.CharField(max_length=150, unique=True)),
                ("first_name", models.CharField(max_length=150)),
                ("last_name", models.CharField(max_length=150)),
                ("email", models.CharField(max_length=254)),
                ("is_staff", models.BooleanField()),
                ("is_active", models.BooleanField()),
                ("date_joined", models.DateTimeField()),
            ],
            options={
                "db_table": "auth_user",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthUserGroups",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "auth_user_groups",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthUserUserPermissions",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "auth_user_user_permissions",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="CrimeData",
            fields=[
                ("drno", models.AutoField(primary_key=True, serialize=False)),
                ("datereported", models.DateField(blank=True, null=True)),
                ("dateoccured", models.DateField(blank=True, null=True)),
                ("timeoccured", models.IntegerField(blank=True, null=True)),
                ("areaid", models.IntegerField(blank=True, null=True)),
                ("areaname", models.CharField(blank=True, max_length=255, null=True)),
                ("reporteddistrictcode", models.IntegerField(blank=True, null=True)),
                ("crimecode", models.CharField(blank=True, max_length=10, null=True)),
                ("crimecodedescription", models.TextField(blank=True, null=True)),
                ("mocodes", models.TextField(blank=True, null=True)),
                ("victimage", models.IntegerField(blank=True, null=True)),
                ("victimsex", models.CharField(blank=True, max_length=10, null=True)),
                (
                    "victimdescent",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("premisescode", models.IntegerField(blank=True, null=True)),
                ("premisesdescription", models.TextField(blank=True, null=True)),
                ("weaponusedcode", models.IntegerField(blank=True, null=True)),
                ("weaponusedfull", models.TextField(blank=True, null=True)),
                ("statuscode", models.CharField(blank=True, max_length=50, null=True)),
                ("statusdescription", models.TextField(blank=True, null=True)),
                ("crimecode1", models.IntegerField(blank=True, null=True)),
                ("crimecode2", models.IntegerField(blank=True, null=True)),
                ("crimecode3", models.IntegerField(blank=True, null=True)),
                ("crimecode4", models.IntegerField(blank=True, null=True)),
                ("location", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "crossstreet",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("latitude", models.FloatField(blank=True, null=True)),
                ("longitude", models.FloatField(blank=True, null=True)),
            ],
            options={
                "db_table": "crime_data",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="CrimesCrimelookup",
            fields=[
                (
                    "crimecode",
                    models.IntegerField(
                        db_column="CrimeCode", primary_key=True, serialize=False
                    ),
                ),
                (
                    "crimecodedescription",
                    models.CharField(db_column="CrimeCodeDescription", max_length=255),
                ),
            ],
            options={
                "db_table": "crimes_crimelookup",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DescentLookup",
            fields=[
                (
                    "descentid",
                    models.CharField(
                        db_column="DescentID",
                        max_length=255,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "descentfull",
                    models.CharField(
                        blank=True, db_column="DescentFull", max_length=255, null=True
                    ),
                ),
            ],
            options={
                "db_table": "descent_lookup",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DistrictLookup",
            fields=[
                (
                    "reporteddistrictcode",
                    models.IntegerField(
                        db_column="ReportedDistrictCode",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("prec", models.CharField(blank=True, db_column="PREC", null=True)),
                ("aprec", models.CharField(blank=True, db_column="APREC", null=True)),
                ("bureau", models.CharField(blank=True, db_column="BUREAU", null=True)),
                (
                    "basiccar",
                    models.CharField(blank=True, db_column="BASICCAR", null=True),
                ),
                ("agency", models.CharField(blank=True, db_column="AGENCY", null=True)),
                ("name", models.CharField(blank=True, db_column="NAME", null=True)),
                (
                    "shape_leng",
                    models.FloatField(blank=True, db_column="SHAPE_LENG", null=True),
                ),
                (
                    "abbrev_apr",
                    models.CharField(blank=True, db_column="ABBREV_APR", null=True),
                ),
                (
                    "shape_area",
                    models.FloatField(blank=True, db_column="Shape__Area", null=True),
                ),
                (
                    "shape_length",
                    models.FloatField(blank=True, db_column="Shape__Length", null=True),
                ),
            ],
            options={
                "db_table": "district_lookup",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoAdminLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("action_time", models.DateTimeField()),
                ("object_id", models.TextField(blank=True, null=True)),
                ("object_repr", models.CharField(max_length=200)),
                ("action_flag", models.SmallIntegerField()),
                ("change_message", models.TextField()),
            ],
            options={
                "db_table": "django_admin_log",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoContentType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("app_label", models.CharField(max_length=100)),
                ("model", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "django_content_type",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoMigrations",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("app", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=255)),
                ("applied", models.DateTimeField()),
            ],
            options={
                "db_table": "django_migrations",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoSession",
            fields=[
                (
                    "session_key",
                    models.CharField(max_length=40, primary_key=True, serialize=False),
                ),
                ("session_data", models.TextField()),
                ("expire_date", models.DateTimeField()),
            ],
            options={
                "db_table": "django_session",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Locations",
            fields=[
                (
                    "drno",
                    models.IntegerField(
                        db_column="DRNO", primary_key=True, serialize=False
                    ),
                ),
                (
                    "location",
                    models.CharField(
                        blank=True, db_column="Location", max_length=255, null=True
                    ),
                ),
                (
                    "crossstreet",
                    models.CharField(
                        blank=True, db_column="CrossStreet", max_length=255, null=True
                    ),
                ),
                (
                    "latitude",
                    models.DecimalField(
                        blank=True,
                        db_column="Latitude",
                        decimal_places=6,
                        max_digits=9,
                        null=True,
                    ),
                ),
                (
                    "longitude",
                    models.DecimalField(
                        blank=True,
                        db_column="Longitude",
                        decimal_places=6,
                        max_digits=9,
                        null=True,
                    ),
                ),
            ],
            options={
                "db_table": "locations",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Victims",
            fields=[
                (
                    "drno",
                    models.IntegerField(
                        db_column="DRNO", primary_key=True, serialize=False
                    ),
                ),
                (
                    "victimage",
                    models.IntegerField(blank=True, db_column="VictimAge", null=True),
                ),
                (
                    "victimsex",
                    models.CharField(
                        blank=True, db_column="VictimSex", max_length=255, null=True
                    ),
                ),
            ],
            options={
                "db_table": "victims",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Mocodes",
            fields=[
                (
                    "drno",
                    models.IntegerField(
                        db_column="DRNO", primary_key=True, serialize=False
                    ),
                ),
                ("mocode", models.IntegerField(db_column="Mocode")),
            ],
            options={
                "db_table": "mocodes",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="PremisesLookup",
            fields=[
                (
                    "premisescode",
                    models.IntegerField(
                        db_column="PremisesCode", primary_key=True, serialize=False
                    ),
                ),
                (
                    "premisesdescription",
                    models.TextField(db_column="PremisesDescription"),
                ),
            ],
            options={
                "db_table": "premises_lookup",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="StatusLookup",
            fields=[
                (
                    "statuscode",
                    models.CharField(
                        db_column="StatusCode", primary_key=True, serialize=False
                    ),
                ),
                (
                    "statusdescription",
                    models.CharField(db_column="StatusDescription", max_length=255),
                ),
            ],
            options={
                "db_table": "status_lookup",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="WeaponLookup",
            fields=[
                (
                    "weaponusedcode",
                    models.IntegerField(
                        db_column="WeaponUsedCode", primary_key=True, serialize=False
                    ),
                ),
                (
                    "weaponusedfull",
                    models.CharField(db_column="WeaponUsedFull", max_length=255),
                ),
            ],
            options={
                "db_table": "weapon_lookup",
                "managed": False,
            },
        ),
        migrations.AlterModelOptions(
            name="crimelookup",
            options={"managed": False},
        ),
        migrations.CreateModel(
            name="Main",
            fields=[
                (
                    "drno",
                    models.OneToOneField(
                        db_column="DRNO",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="crimes.victims",
                    ),
                ),
                (
                    "datereported",
                    models.DateField(blank=True, db_column="DateReported", null=True),
                ),
                (
                    "dateoccured",
                    models.DateField(blank=True, db_column="DateOccured", null=True),
                ),
                (
                    "timeoccured",
                    models.IntegerField(blank=True, db_column="TimeOccured", null=True),
                ),
                (
                    "reporteddistrictcode",
                    models.IntegerField(
                        blank=True, db_column="ReportedDistrictCode", null=True
                    ),
                ),
                (
                    "crimecode1",
                    models.IntegerField(blank=True, db_column="CrimeCode1", null=True),
                ),
                (
                    "crimecode2",
                    models.IntegerField(blank=True, db_column="CrimeCode2", null=True),
                ),
                (
                    "crimecode3",
                    models.IntegerField(blank=True, db_column="CrimeCode3", null=True),
                ),
                (
                    "crimecode4",
                    models.IntegerField(blank=True, db_column="CrimeCode4", null=True),
                ),
                (
                    "premisescode",
                    models.IntegerField(
                        blank=True, db_column="PremisesCode", null=True
                    ),
                ),
            ],
            options={
                "db_table": "main",
                "managed": False,
            },
        ),
    ]
