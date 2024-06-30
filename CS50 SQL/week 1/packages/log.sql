
-- *** The Lost Letter ***
select * from addresses where id in (
select address_id from scans where package_id =(
    select id from packages where from_address_id = (
        select id from addresses where address = '900 Somerville Avenue'
))); -- this query will give us from and to address with address id and type of address


-- *** The Devious Delivery ***
select type from addresses where id = (
select to_address_id from packages where from_address_id is NULL);

select * from packages where from_address_id is NULL; -- to find content of package 
-- *** The Forgotten Gift ***

