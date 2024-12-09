predefined_queries = {
        '''SET my.start_date = '2023-01-01';
SET my.start_hour = '1700';
SET my.end_date = '2023-12-31';
SET my.end_hour = '1900';

SELECT cl."CrimeCodeDescription", COUNT(m."DRNO") AS "TotalReports"
FROM "main" m
JOIN "crime_lookup" cl ON m."CrimeCode" = cl."CrimeCode"
WHERE (("DateOccured" = pg_catalog.current_setting('my.start_date')::DATE AND "TimeOccured" > pg_catalog.current_setting('my.start_hour')::INT) OR "DateOccured" > pg_catalog.current_setting('my.start_date')::DATE)
  	AND (("DateOccured" = pg_catalog.current_setting('my.end_date')::DATE AND "TimeOccured" < pg_catalog.current_setting('my.end_hour')::INT) OR "DateOccured" < pg_catalog.current_setting('my.end_date')::DATE)
GROUP BY cl."CrimeCodeDescription"
ORDER BY "TotalReports" DESC;
        ''': '''Find the total number of reports per “Crm Cd” that occurred within a specified time range
and sort them in a descending order''',
        '''SET my.crime_code = '110';
SET my.start_date = '2023-01-01';
SET my.start_hour = '1700';
SET my.end_date = '2023-12-01';
SET my.end_hour = '1900';

SELECT "DateReported", COUNT(*) AS "total_reports"
FROM main
WHERE "CrimeCode" = pg_catalog.current_setting('my.crime_code')::INT
  AND ((("DateOccured" = pg_catalog.current_setting('my.start_date')::DATE AND "TimeOccured" > pg_catalog.current_setting('my.start_hour')::INT) OR "DateOccured" > pg_catalog.current_setting('my.start_date')::DATE)
  	AND (("DateOccured" = pg_catalog.current_setting('my.end_date')::DATE AND "TimeOccured" < pg_catalog.current_setting('my.end_hour')::INT) OR "DateOccured" < pg_catalog.current_setting('my.end_date')::DATE))
GROUP BY "DateReported"
ORDER BY "DateReported";
''': "Find the total number of reports per day for a specific “Crm Cd” and time range.",
       '''SET my.date = '2022-01-03';

SELECT DISTINCT ON (main."AreaID") 
       areas."AreaName", 
       crime_lookup."CrimeCodeDescription", 
       COUNT(*) OVER (PARTITION BY main."AreaID", main."CrimeCode") AS "crime_count"
FROM main
JOIN areas ON areas."AreaID" = main."AreaID"
JOIN crime_lookup ON crime_lookup."CrimeCode" = main."CrimeCode"
WHERE "DateReported" = pg_catalog.current_setting('my.date')::DATE
ORDER BY 
       main."AreaID",
       "crime_count" DESC;''': '''Find the most common crime committed regardless of code 1, 2, 3, and 4, per area for a
specific day.
''',
'''SET my.start_date = '2023-04-03';
SET my.end_date = '2023-08-03';

SELECT 
    FLOOR("TimeOccured" / 100) AS crime_hour, 
    COUNT(*)::FLOAT / (
        SELECT COUNT(DISTINCT "DateOccured") 
        FROM main 
        WHERE "DateOccured" BETWEEN 
            pg_catalog.current_setting('my.start_date')::DATE AND 
            pg_catalog.current_setting('my.end_date')::DATE
    ) AS avg_crimes_per_hour
FROM main
WHERE "DateOccured" BETWEEN 
      pg_catalog.current_setting('my.start_date')::DATE AND 
      pg_catalog.current_setting('my.end_date')::DATE
GROUP BY crime_hour
ORDER BY crime_hour;
''':'''Find the average number of crimes occurred per hour (24 hours) for a specific date range.
''',
'''SET my.date = '2023-04-03';
SET my.lat_min = 34.0000;
SET my.lat_max = 34.1000;
SET my.lon_min = -118.3000;
SET my.lon_max = -118.2000;

SELECT 
    "CrimeCode",
    COUNT(*) AS occurrences
FROM main
JOIN locations ON main."DRNO" = locations."DRNO"
WHERE "DateOccured" = pg_catalog.current_setting('my.date')::DATE
  AND "Latitude" BETWEEN 
      pg_catalog.current_setting('my.lat_min')::FLOAT AND 
      pg_catalog.current_setting('my.lat_max')::FLOAT
  AND "Longitude" BETWEEN 
      pg_catalog.current_setting('my.lon_min')::FLOAT AND 
      pg_catalog.current_setting('my.lon_max')::FLOAT
GROUP BY "CrimeCode"
ORDER BY occurrences DESC
LIMIT 1;
''':'''Find the most common “Crm Cd” in a specified bounding box (as designated by GPS-coordinates)
for a specific day''',
'''SET my.start_date = '2023-04-03';
SET my.end_date = '2023-08-03';

SELECT 
    areas."AreaName",
    COUNT(*) AS total_crimes
FROM main
JOIN areas ON main."AreaID" = areas."AreaID"
WHERE "DateOccured" BETWEEN 
    pg_catalog.current_setting('my.start_date')::DATE AND 
    pg_catalog.current_setting('my.end_date')::DATE
GROUP BY areas."AreaName"
ORDER BY total_crimes DESC
LIMIT 5;
''':'''Find the top-5 Area names with regards to total number of crimes reported per day for a
specific date range.''',
'''SET my.start_date = '2023-04-03';
SET my.end_date = '2023-08-03';

SELECT 
    district_lookup."BUREAU",
    district_lookup."APREC",
    COUNT(*) AS total_crimes
FROM main
JOIN district_lookup 
    ON main."ReportedDistrictCode" = district_lookup."ReportedDistrictCode"
WHERE "DateOccured" BETWEEN 
    pg_catalog.current_setting('my.start_date')::DATE AND 
    pg_catalog.current_setting('my.end_date')::DATE
GROUP BY district_lookup."APREC", district_lookup."BUREAU"
ORDER BY total_crimes DESC
LIMIT 5;
''':'''Find the top-5 Reported Destricts with regards to total number of crimes reported per day for a
specific date range.''',
'''SET my.start_date = '2023-04-03';
SET my.end_date = '2023-08-03';

WITH AreaWithMostCrimes AS (
    SELECT 
        "AreaID",
        COUNT(*) AS total_crimes
    FROM main
    WHERE "DateOccured" BETWEEN 
        pg_catalog.current_setting('my.start_date')::DATE AND 
        pg_catalog.current_setting('my.end_date')::DATE
    GROUP BY "AreaID"
    ORDER BY total_crimes DESC
    LIMIT 1
),
CrimePairs AS (
    SELECT 
        a."AreaID",
        a."DRNO",
        LEAST(crime_a, crime_b) AS crime_code_1,
        GREATEST(crime_a, crime_b) AS crime_code_2
    FROM (
        SELECT 
            UNNEST(ARRAY["CrimeCode1", "CrimeCode2", "CrimeCode3", "CrimeCode4"]) AS crime_a,
            "DRNO",
            "AreaID"
        FROM main
        WHERE "CrimeCode2" IS NOT NULL
    ) AS a
    JOIN (
        SELECT 
            UNNEST(ARRAY["CrimeCode1", "CrimeCode2", "CrimeCode3", "CrimeCode4"]) AS crime_b,
            "DRNO",
            "AreaID"
        FROM main
        WHERE "CrimeCode2" IS NOT NULL
    ) AS b
    ON a."DRNO" = b."DRNO" AND a.crime_a < b.crime_b
    WHERE a."AreaID" = (SELECT "AreaID" FROM AreaWithMostCrimes)
)
SELECT 
    max(areas."AreaID"),
    max("AreaName"),
    crime_code_1,
    max(c1."CrimeCodeDescription") AS CrimeName1,
    crime_code_2,
    max(c2."CrimeCodeDescription") AS CrimeName2,
    COUNT(*) AS pair_count
FROM CrimePairs c
LEFT JOIN crime_lookup c1 ON c1."CrimeCode" = c.crime_code_1
LEFT JOIN crime_lookup c2 ON c2."CrimeCode" = c.crime_code_2
LEFT JOIN areas ON areas."AreaID" = c."AreaID"
GROUP BY crime_code_1, crime_code_2
ORDER BY pair_count DESC
LIMIT 1;

''':'''Find the pair of crimes that has co-occurred the most, in the area with the most reported incidents for
a specific date range.''',
'''SET my.start_date = '2023-04-03';
SET my.end_date = '2023-08-03';
SET my.crime_code = 740;  

WITH CrimePairs AS (
    SELECT 
        a."DRNO",
        LEAST(crime_a, crime_b) AS crime_code_1,
        GREATEST(crime_a, crime_b) AS crime_code_2
    FROM (
        SELECT 
            UNNEST(ARRAY["CrimeCode1", "CrimeCode2", "CrimeCode3", "CrimeCode4"]) AS crime_a,
            "DRNO"
        FROM main
        WHERE "CrimeCode2" IS NOT NULL
    ) AS a
    JOIN (
        SELECT 
            UNNEST(ARRAY["CrimeCode1", "CrimeCode2", "CrimeCode3", "CrimeCode4"]) AS crime_b,
            "DRNO"
        FROM main
        WHERE "CrimeCode2" IS NOT NULL
    ) AS b
    ON a."DRNO" = b."DRNO" AND a.crime_a < b.crime_b
)
SELECT 
    crime_code_1, 
    max(c1."CrimeCodeDescription") AS CrimeName1, 
    crime_code_2, 
    max(c2."CrimeCodeDescription") AS CrimeName2,
    COUNT(*) AS counts 
FROM CrimePairs c
LEFT JOIN crime_lookup c1 ON c1."CrimeCode" = c.crime_code_1
LEFT JOIN crime_lookup c2 ON c2."CrimeCode" = c.crime_code_2
JOIN main ON main."DRNO" = c."DRNO"
WHERE (crime_code_2 = pg_catalog.current_setting('my.crime_code')::INTEGER OR crime_code_2 = pg_catalog.current_setting('my.crime_code')::INTEGER) 
AND "DateOccured" BETWEEN 
    pg_catalog.current_setting('my.start_date')::DATE AND 
    pg_catalog.current_setting('my.end_date')::DATE
GROUP BY crime_code_1, crime_code_2
ORDER BY counts DESC
OFFSET 1 LIMIT 1;
''':'''Find the second most common crime that has co-occurred with a particular crime for a specific date range.''',
'''WITH AgeGroups AS (
    SELECT
        FLOOR("VictimAge" / 5) * 5 AS age_group_start,
        FLOOR("VictimAge" / 5) * 5 + 4 AS age_group_end,
        "WeaponUsedCode",
        COUNT(*) AS weapon_count
    FROM
        victims	
    JOIN main ON main."DRNO" = victims."DRNO"
    WHERE "WeaponUsedCode" IS NOT NULL
    GROUP BY
        age_group_start, age_group_end, "WeaponUsedCode"
)
SELECT DISTINCT ON (age_group_start, age_group_end) 
    age_group_start, 
    age_group_end, 
    "WeaponUsedCode", 
    weapon_count
FROM AgeGroups
ORDER BY age_group_start, age_group_end, weapon_count DESC''':'''Find the most common type of weapon used against victims depending on their group of age.
The age groups are formed by bucketing ages every 5 years, e.g., 0 ≤ x < 5, 5 ≤ x < 10, etc..''',
'''SET my.crime_code = 230;
WITH gaps AS (
SELECT 
    "AreaID",       
    LEAD("DateOccured") OVER (PARTITION BY "AreaID" ORDER BY "DateOccured") - "DateOccured" AS date_diff
FROM main
WHERE "CrimeCode" = pg_catalog.current_setting('my.crime_code')::INT
ORDER BY "AreaID", "DateOccured" ASC)

SELECT areas."AreaName", MAX(date_diff) AS LongestStreakOfCrimeAbsense
FROM gaps
LEFT JOIN areas ON areas."AreaID" = gaps."AreaID"
GROUP BY areas."AreaName"
ORDER BY MAX(date_diff) DESC
LIMIT 1
''':'''Find the area with the longest time range without an occurrence of a specific crime. Include the time range in the results.''',
'''WITH gaps AS (
    SELECT 
        "ReportedDistrictCode",       
        LEAD("DateOccured") OVER (PARTITION BY "ReportedDistrictCode" ORDER BY "DateOccured") - "DateOccured" AS date_diff
    FROM main
    WHERE "CrimeCode" = 230 --Crime
    ORDER BY "ReportedDistrictCode", "DateOccured" ASC
)
SELECT 
    "ReportedDistrictCode", 
    MAX(date_diff) AS LongestStreakOfCrimeAbsense
FROM gaps
WHERE date_diff IS NOT NULL
GROUP BY "ReportedDistrictCode"
ORDER BY MAX(date_diff) DESC
LIMIT 1;
''':'''Find the Reported Destrict Code with the longest time range without an occurrence of a specific crime. Include the time range in the results.''',
'''SET my.crime_code1 = 813;
SET my.crime_code2 = 354;
SELECT 
DISTINCT a."AreaName"
FROM main m
LEFT JOIN areas a ON m."AreaID" = a."AreaID"
WHERE m."CrimeCode" IN (pg_catalog.current_setting('my.crime_code1')::INT, pg_catalog.current_setting('my.crime_code2')::INT) --CrimeCodes
GROUP BY a."AreaName", m."DateOccured"
HAVING 
    COUNT(CASE WHEN m."CrimeCode" = pg_catalog.current_setting('my.crime_code1')::INT THEN 1 END) > 1 AND
    COUNT(CASE WHEN m."CrimeCode" = pg_catalog.current_setting('my.crime_code2')::INT THEN 1 END) > 1
ORDER BY a."AreaName"
''':'''For 2 crimes of your choice, find all areas that have received more than 1 report on each of these 2 crimes on the same day.''',\
'''SET my.start_date = '2023-01-01';
SET my.start_hour = '1700';
SET my.end_date = '2023-12-01';
SET my.end_hour = '1900';
SELECT 
    COUNT(DISTINCT m1."DRNO") AS NumberOfDivisionOfRecords,
    m1."DateOccured",
    m1."WeaponUsedCode"
FROM main m1
JOIN main m2 
    ON m1."DateOccured" = m2."DateOccured"
   AND m1."WeaponUsedCode" = m2."WeaponUsedCode"
   AND m1."AreaID" <> m2."AreaID"
WHERE ((m1."DateOccured" = pg_catalog.current_setting('my.start_date')::DATE AND m1."TimeOccured" > pg_catalog.current_setting('my.start_hour')::INT) OR m1."DateOccured" > pg_catalog.current_setting('my.start_date')::DATE)
  AND ((m1."DateOccured" = pg_catalog.current_setting('my.end_date')::DATE AND m1."TimeOccured" < pg_catalog.current_setting('my.end_hour')::INT) OR m1."DateOccured" < pg_catalog.current_setting('my.end_date')::DATE)
GROUP BY m1."DateOccured", m1."WeaponUsedCode"
ORDER BY m1."WeaponUsedCode", m1."DateOccured"
''':'''Find the number of division of records for crimes reported on the same day in different areas using the same weapon for a specific time range.''',
'''SET my.start_date = '2023-01-01';
SET my.start_hour = '1700';
SET my.end_date = '2023-12-01';
SET my.end_hour = '1900';
SET my.n_value = '12';

WITH relevant_crimes AS (
    SELECT 
        m1."DRNO",
        m1."DateOccured",
        m1."AreaID",
        m1."WeaponUsedCode",
        m1."CrimeCode"
    FROM main m1
    WHERE 
        ((m1."DateOccured" = pg_catalog.current_setting('my.start_date')::DATE 
          AND m1."TimeOccured" > pg_catalog.current_setting('my.start_hour')::INT) 
         OR m1."DateOccured" > pg_catalog.current_setting('my.start_date')::DATE)
        AND 
        ((m1."DateOccured" = pg_catalog.current_setting('my.end_date')::DATE 
          AND m1."TimeOccured" < pg_catalog.current_setting('my.end_hour')::INT) 
         OR m1."DateOccured" < pg_catalog.current_setting('my.end_date')::DATE)
)
SELECT 
    rc."DateOccured",
    a."AreaName",
    cl."CrimeCodeDescription",
    w."WeaponUsedFull",
    COUNT(DISTINCT rc."DRNO") AS NumberOfDivisionOfRecords,
    STRING_AGG(DISTINCT rc."DRNO"::TEXT, ', ') AS ListOfDivisionOfRecords 
FROM relevant_crimes rc
JOIN areas a 
    ON rc."AreaID" = a."AreaID"
JOIN crime_lookup cl 
    ON rc."CrimeCode" = cl."CrimeCode"
JOIN weapon_lookup w 
    ON rc."WeaponUsedCode" = w."WeaponUsedCode"
GROUP BY 
    rc."DateOccured", a."AreaName", cl."CrimeCodeDescription", w."WeaponUsedFull"
HAVING 
    COUNT(DISTINCT rc."DRNO") = pg_catalog.current_setting('my.n_value')::INT
ORDER BY 
    rc."DateOccured", w."WeaponUsedFull";
''':'''Find the crimes that occurred for a given number of times N on the same day, in the same area, using the same weapon, for a specific time range.''',
'''INSERT INTO public.main(
	"DRNO", "DateReported", "DateOccured", "TimeOccured", "ReportedDistrictCode", "CrimeCode", "CrimeCode1", "CrimeCode2", "CrimeCode3", "CrimeCode4", "AreaID", "PremisesCode", "WeaponUsedCode", "StatusCode")
	VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);

INSERT INTO public.mocodes(
	"DRNO", "Mocode")
	VALUES (?, ?);

INSERT INTO public.victims(
	"DRNO", "VictimAge", "VictimSex", "VictimDescent")
	VALUES (?, ?, ?, ?);

INSERT INTO public.locations(
	"DRNO", "Location", "CrossStreet", "Latitude", "Longitude")
	VALUES (?, ?, ?, ?, ?);
''':'''Insert new crime.'''
    }