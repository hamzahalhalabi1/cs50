-- select name from drivers where id in (
--     select id from addresses
--     where type is 'Residential'
-- );

-- select * from addresses
-- join scans on scans.id = addresses.id;

--select id from addresses where address like '2 Finnegan Street';

select address from addresses where id =(
select to_address_id from packages where id =(
    select id from addresses where address = '900 Somerville Avenue'

));