    select 
        l.lesson_id,
        l.[date],
        s.first_name,
        s.last_name,
        (
            CASE
                WHEN a.status=0 THEN 'ABSENT'
                ELSE 'PRESENT'
            END
        ) as "status"
    from lessons l
    join attendance a on l.lesson_id=a.lesson_id
    join students s on a.student_id=s.student_id
