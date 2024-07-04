select year, salary from SALARIES
where player_id = (
    select id from players where first_name is 'Cal' 
    and last_name is 'Ripken'
)
order by year desc;