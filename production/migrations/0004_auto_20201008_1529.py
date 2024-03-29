# Generated by Django 3.1.2 on 2020-10-08 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0003_auto_20201008_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production',
            name='year',
            field=models.IntegerField(choices=[(198485, '1984/85'), (198586, '1985/86'), (198687, '1986/87'), (198788, '1987/88'), (198889, '1988/89'), (198990, '1989/90'), (199091, '1990/91'), (199192, '1991/92'), (199293, '1992/93'), (199394, '1993/94'), (199495, '1994/95'), (199596, '1995/96'), (199697, '1996/97'), (199798, '1997/98'), (199899, '1998/99'), (199900, '1999/00'), (200001, '2000/01'), (200102, '2001/02'), (200203, '2002/03'), (200304, '2003/04'), (200405, '2004/05'), (200506, '2005/06'), (200607, '2006/07'), (200708, '2007/08'), (200809, '2008/09'), (200910, '2009/10'), (201011, '2010/11'), (201112, '2011/12'), (201213, '2012/13'), (201314, '2013/14'), (201415, '2014/15'), (201516, '2015/16'), (201617, '2016/17'), (201718, '2017/18'), (201819, '2018/19'), (201920, '2019/20'), (202021, '2020/21')]),
        ),
    ]
