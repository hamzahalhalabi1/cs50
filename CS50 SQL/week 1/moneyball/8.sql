select hr from salaries
join teams on teams.id = salaries.team_id
join performances on performances.team_id = teams.id
where performances.year = 2001
order by hr DESC
limit 1;
