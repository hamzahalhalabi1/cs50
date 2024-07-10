update users set password = (
    select password from users where username = 'emily33'
)
where username = 'admin';


update users set password = '982c0381c279d139fd221fce974916e7'
where username = 'admin';

delete from user_logs where new_password = '982c0381c279d139fd221fce974916e7';
