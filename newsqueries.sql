--select TRIM (path,'/article/') from log limit 5;
--select substring (path,10,len(path)) from log limit 5;
--select STRING_SPLIT (path,'/article/') from log limit 5;

/*select articles.title, count(log.path) as views
from articles left join log
on articles.slug=substring(log.path,10)
group by articles.title
order by views desc
limit 3;*/

--select articles.title, count(log.path) as views from articles left join log on articles.slug=trim(log.path,'/article/') group by articles.title order by views desc limit 3;

/*select authors.name, article_views.articles.title
from authors join
(select title, count(log.path) as views
    from articles left join log
    on articles.slug=trim(log.path,'/article/')
    group by title
    order by views desc) as article_views
on articles.author=authors.id;*/

/*select articles.title, authors.name
from authors, articles
where authors.id=articles.author;*/

/*select authors.name, count(log.path) as views
from articles 
left join log on articles.slug=trim(log.path,'/article/')
join authors on authors.id=articles.author
group by authors.name
order by views desc;*/

--Creating Views for Question 3
create view error_code_number as
select to_char(time,'YYYY-MM-DD') as date, count (status) as daily_error_number
from log
where status like '%404%'
group by date;

--select * from error_code_number;

create view status_number as
select to_char(time,'YYYY-MM-DD') as date, count (status) as total_daily_codes
from log
group by date;


select error_code_number.date, round(100.0*daily_error_number/total_daily_codes,2) as percent
from error_code_number, status_number
where error_code_number.date=status_number.date
and daily_error_number > total_daily_codes/100;



--select * from status_number;

/*create view error_table as
select error_code_number.date, daily_error_number, total_daily_codes
from error_code_number,status_number
where error_code_number.date=status_number.date
group by error_code_number.date,daily_error_number, total_daily_codes;


select date, round((daily_error_number/total_daily_codes),4) as error_percent
from error_table
--group by date, error_percent
order by error_percent desc;

select date, to_number(daily_error_number/total_daily_codes) as error_percent
from error_table
order by error_percent desc;*/


