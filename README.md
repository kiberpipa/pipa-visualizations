Kiberpipine vizualizacije
=========================

Kiberpipa ima bogato zgodovino, ki lahko zgleda precej bolj zanimiva če te podatke spravimo v par vizualizacij.

Zaenkrat imamo
--------------
	* impact-graph, ki prikazuje kje vse po svetu so pristali pipci

Plan/ideje
----------
	* Po navdihu http://www.culture.si/en/Festivals_in_Slovenia_2013, število dogodkov po mesecih
	* Dogodki po času z številom obiskovalcev kot radijem


Nekaj osnovne statistike
========================

Povprečno število obiskovalcev za vse dogodke
---------------------------------------------

    select avg(visitors) from org_event;
             avg
    16.3190519598906108

Povprečno število obiskovalcev ko imamo podatek
-----------------------------------------------

    # select avg(visitors) from org_event where visitors>0;
             avg
    ---------------------
     26.2878120411160059
    (1 row)

Dogodki z več kot 100 obiskovalci
---------------------------------

    # select id, title, visitors from org_event where visitors>100;
      id  |                            title                             | visitors
    ------+--------------------------------------------------------------+----------
      682 | Barcamp, Co-working in prihodnost izmenjave znanj            |      153
     1566 | #200: Slovenska startup scena                                |      103
      818 | Google iz prve roke                                          |      300
     1308 | HAIP 10 klubski večer                                        |      210
     1220 | Hiša Franko: Molekularna kuhinja                             |      230
      849 | MobileCamp Ljubljana                                         |      219
      806 | MoMoSlo S02E03 - Hello Maemo!                                |      117
     1386 | Prišli, videli, zmagali - DoubleRecall v Silciijevi dolini   |      160
     1435 | WebCampLjubljana                                             |      160
     1259 | VIP večer s Petrom Florjančičem                              |      168
     1251 | VIP večer z mag. Alešem Liscem                               |      108
     1434 | VIP z dr. Ichakom Adizesom                                   |      136
     1458 | MoMoSlo: S04E01: HTML5 vs. apps                              |      126
     1491 | VIP večer s Francijem Zavrlom – Bistvo marketinga je zgodba  |      137
     1457 | VIP večer z Milošem Čiričem - Zakaj je treba hoditi na kavo? |      162
    (15 rows)

Število dogodkov z več kot 50 obiskovalci
-----------------------------------------

    # select count(*) from org_event where visitors>50;
     count
    -------
        72
    (1 row)

Število dogodkov po letih
-------------------------

    # select date_trunc('year', org_event.start_date), count(*) from org_event group by date_trunc('year', org_event.start_date);
           date_trunc       | count
    ------------------------+-------
     2009-01-01 00:00:00+01 |   120
     2011-01-01 00:00:00+01 |   205
     2010-01-01 00:00:00+01 |   214
     2012-01-01 00:00:00+01 |   225
     2007-01-01 00:00:00+01 |   207
     2008-01-01 00:00:00+01 |   179
     2013-01-01 00:00:00+01 |   222
     2006-01-01 00:00:00+01 |   172

Število dogodkov po mesecih
---------------------------

    # select date_trunc('month', org_event.start_date), count(*) from org_event group by date_trunc('month', org_event.start_date) order by date_trunc('month', start_date);

            date_trunc       | count
    ------------------------+-------
     2006-02-01 00:00:00+01 |     3
     2006-03-01 00:00:00+01 |    39
     2006-04-01 00:00:00+02 |    14
     2006-05-01 00:00:00+02 |    30
     2006-06-01 00:00:00+02 |    18
     2006-09-01 00:00:00+02 |     3
     2006-10-01 00:00:00+02 |    15
     2006-11-01 00:00:00+01 |    32
     2006-12-01 00:00:00+01 |    18
     2007-01-01 00:00:00+01 |    28
     2007-02-01 00:00:00+01 |    25
     2007-03-01 00:00:00+01 |    20
     2007-04-01 00:00:00+02 |    32
     2007-05-01 00:00:00+02 |    22
     2007-06-01 00:00:00+02 |     8
     2007-09-01 00:00:00+02 |     3
     2007-10-01 00:00:00+02 |    25
     2007-11-01 00:00:00+01 |    18
     2007-12-01 00:00:00+01 |    26
     2008-01-01 00:00:00+01 |    13
     2008-02-01 00:00:00+01 |    13
     2008-03-01 00:00:00+01 |    22
     2008-04-01 00:00:00+02 |    25
     2008-05-01 00:00:00+02 |    27
     2008-06-01 00:00:00+02 |     8
     2008-09-01 00:00:00+02 |     3
     2008-10-01 00:00:00+02 |    19
     2008-11-01 00:00:00+01 |    28
     2008-12-01 00:00:00+01 |    21
     2009-01-01 00:00:00+01 |    12
     2009-02-01 00:00:00+01 |    13
     2009-03-01 00:00:00+01 |    15
     2009-04-01 00:00:00+02 |    16
     2009-05-01 00:00:00+02 |    15
     2009-06-01 00:00:00+02 |     4
     2009-09-01 00:00:00+02 |     4
     2009-10-01 00:00:00+02 |    14
     2009-11-01 00:00:00+01 |    13
     2009-12-01 00:00:00+01 |    14
     2010-01-01 00:00:00+01 |    11
     2010-02-01 00:00:00+01 |    16
     2010-03-01 00:00:00+01 |    17
     2010-04-01 00:00:00+02 |    19
     2010-05-01 00:00:00+02 |    26
     2010-06-01 00:00:00+02 |    15
     2010-08-01 00:00:00+02 |     1
     2010-09-01 00:00:00+02 |    10
     2010-10-01 00:00:00+02 |    31
     2010-11-01 00:00:00+01 |    44
     2010-12-01 00:00:00+01 |    24
     2011-01-01 00:00:00+01 |    23
     2011-02-01 00:00:00+01 |    18
     2011-03-01 00:00:00+01 |    21
     2011-04-01 00:00:00+02 |    26
     2011-05-01 00:00:00+02 |    28
     2011-06-01 00:00:00+02 |     9
     2011-07-01 00:00:00+02 |     6
     2011-08-01 00:00:00+02 |     8
     2011-09-01 00:00:00+02 |    10
     2011-10-01 00:00:00+02 |    20
     2011-11-01 00:00:00+01 |    19
     2011-12-01 00:00:00+01 |    17
     2012-01-01 00:00:00+01 |    15
     2012-02-01 00:00:00+01 |    21
     2012-03-01 00:00:00+01 |    28
     2012-04-01 00:00:00+02 |    16
     2012-05-01 00:00:00+02 |    15
     2012-06-01 00:00:00+02 |    13
     2012-07-01 00:00:00+02 |     2
     2012-08-01 00:00:00+02 |     7
     2012-09-01 00:00:00+02 |    13
     2012-10-01 00:00:00+02 |    31
     2012-11-01 00:00:00+01 |    39
     2012-12-01 00:00:00+01 |    25
     2013-01-01 00:00:00+01 |    23
     2013-02-01 00:00:00+01 |    38
     2013-03-01 00:00:00+01 |    50
     2013-04-01 00:00:00+02 |    45
     2013-05-01 00:00:00+02 |    27
     2013-06-01 00:00:00+02 |    25
     2013-07-01 00:00:00+02 |     5
     2013-10-01 00:00:00+02 |     6
     2013-11-01 00:00:00+01 |     2
     2013-12-01 00:00:00+01 |     1
    (84 rows)


Delavnice
---------

    # select count(*) from org_event where project_id=3;
     count
    -------
        89

