OVERALL DESCRIPTION
---------------------------------
Task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

Questions to Answer through Reporting:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

STEPS TO RUN PROGRAM:
-----------------------------------

1. Download VirtualBox and Vagrant software to use Linux based virtual machine. Bring the virtual machine online with "vagrant up" in Git Bash. Then log into it with "vagrant ssh".
2. Download the data provided by Udacity here: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip . 
3. Unzip this file after downloading it. The file inside was called newsdata.sql. 
4. Put this file into the vagrant directory, which is shared with your virtual machine.
5. cd into vagrant directory and use the command "psql -d news -f newsdata.sql" to connect to the database and run sql statements in newsdata.sql
6. Create views to answer Question 3 (statement in below section)
7. Run the Python DB-API code in the file newsdb.py via the command "python newsdb.py"
8. Example output is attached in a text file called example_output_final.txt.

VIEWS CREATED FOR QUESTION 3
------------------------------------

create view error_code_number as
select to_char(time,'YYYY-MM-DD') as date, count (status) as daily_error_number
from log
where status like '%404%'
group by date;

create view status_number as
select to_char(time,'YYYY-MM-DD') as date, count (status) as total_daily_codes
from log
group by date;


