# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('Detail_id', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('title', models.CharField(default=b'title', max_length=50)),
                ('section', models.CharField(max_length=3)),
                ('slots', models.PositiveSmallIntegerField(default=30)),
                ('location', models.CharField(max_length=25, blank=True)),
                ('day', models.CharField(default=b'tba', max_length=3, choices=[(b'mth', b'Monday/Thursday'), (b'tfr', b'Tuesday/Friday'), (b'fri', b'Friday'), (b'wed', b'Wednesday'), (b'sat', b'Saturday'), (b'tba', b'To Be Announced')])),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('enrollment_id', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('term', models.CharField(default=b'2015-2016', max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('grade_id', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('grade', models.CharField(blank=True, max_length=10, choices=[(b'100', b'1.00'), (b'125', b'1.25'), (b'150', b'1.50'), (b'175', b'1.75'), (b'200', b'2.00'), (b'225', b'2.25'), (b'250', b'2.50'), (b'275', b'2.75'), (b'300', b'3.00'), (b'400', b'4.00'), (b'500', b'5.00'), (b'INC', b'INCOMPLETE'), (b'DRP', b'DROPPED')])),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('instructor_id', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('first_name', models.CharField(default=b'first', max_length=20)),
                ('last_name', models.CharField(default=b'last', max_length=20)),
                ('middle_name', models.CharField(default=b'middle', max_length=20, blank=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('address', models.TextField(blank=True)),
                ('birthday', models.DateField(default=b'1990-11-01', blank=True)),
                ('gender', models.CharField(blank=True, max_length=6, choices=[(b'male', b'Male'), (b'female', b'Female')])),
            ],
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('lab_id', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('title', models.CharField(default=b'title', max_length=50)),
                ('lab_fee', models.DecimalField(default=0.0, max_digits=5, decimal_places=2)),
                ('Detail_id', models.ManyToManyField(to='student.Detail')),
            ],
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('scholarship_id', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('sts', models.CharField(default=b'nd', max_length=4, choices=[(b'nd', b'No Discount'), (b'pd40', b'Partial Discount (40%)'), (b'pd60', b'Partial Discount (60%)'), (b'pd80', b'Partial Discount (80%)'), (b'fd', b'Full Discount'), (b'fds', b'Full Discount and Stipend')])),
                ('other_scho', models.CharField(max_length=30, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('first_name', models.CharField(default=b'first', max_length=20)),
                ('last_name', models.CharField(default=b'last', max_length=20)),
                ('middle_name', models.CharField(default=b'middle', max_length=20, blank=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('address', models.TextField(blank=True)),
                ('birthday', models.DateField(default=b'1990-11-01', blank=True)),
                ('gender', models.CharField(blank=True, max_length=6, choices=[(b'male', b'Male'), (b'female', b'Female')])),
                ('course', models.CharField(default=b'unkwn', max_length=5, choices=[(b'Sciences', ((b'bscs', b'BS Computer Science'), (b'bsbio', b'BS Biology'), (b'bsmat', b'BS Mathematics'))), (b'Management', ((b'bsmgt', b'BS Management'),)), (b'Social Sciences', ((b'baps', b'BA Political Science'), (b'bspsy', b'BA Psychology'))), (b'Arts and Humanities', ((b'bamc', b'BA  Mass Communication'), (b'bafap', b'BA Fine Arts (Product Design)'), (b'bafas', b'BA Fine Arts (Studio Arts)')))])),
                ('year', models.CharField(default=b'fr', max_length=2, choices=[(b'fr', b'Freshman'), (b'so', b'Sophomore'), (b'ju', b'Junior'), (b'se', b'Senior')])),
                ('term', models.CharField(default=b'2015-2016', max_length=9)),
                ('scholarship_id', models.ForeignKey(default=0, to='student.Scholarship')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_id', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('title', models.CharField(default=b'title', max_length=50)),
                ('code', models.PositiveSmallIntegerField(default=b'00000')),
                ('description', models.TextField(blank=True)),
                ('unit', models.PositiveSmallIntegerField(default=3)),
                ('has_lab', models.BooleanField(default=False)),
                ('is_offered', models.BooleanField(default=True)),
                ('Detail_id', models.ManyToManyField(to='student.Detail')),
                ('lab_id', models.ForeignKey(default=0, to='student.Lab')),
            ],
        ),
        migrations.AddField(
            model_name='grade',
            name='subject_id',
            field=models.ManyToManyField(to='student.Subject'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='grade_id',
            field=models.ForeignKey(default=0, to='student.Grade'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='student_id',
            field=models.ForeignKey(to='student.Student'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='subject_id',
            field=models.ManyToManyField(to='student.Subject'),
        ),
        migrations.AddField(
            model_name='detail',
            name='instructor_id',
            field=models.ForeignKey(default=0, to='student.Instructor'),
        ),
    ]
