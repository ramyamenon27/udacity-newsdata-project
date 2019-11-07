#!/usr/bin/python
import psycopg2
import bleach
import datetime

DBNAME = "news"


def get_popular_articles():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    article_query = """select articles.title, count(log.path) as views
                       from articles left join log
                       on articles.slug=substring(log.path,10)
                       group by articles.title
                       order by views desc limit 3"""
    c.execute(article_query)
    result_one = c.fetchall()
    db.close()
    print("\nWhat are the popular three articles of all time?")
    print("--------------------------------------------------\n")
    for row in range(len(result_one)):
        print("\"" + str(result_one[row][0]) + "\""
              + " --  "+str(result_one[row][1]) + " views")


def get_popular_authors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    author_query = """select authors.name, count(log.path) as views
                      from articles left join log
                      on articles.slug=substring(log.path,10)
                      join authors on authors.id=articles.author
                      group by authors.name order by views desc"""
    c.execute(author_query)
    result_two = c.fetchall()
    db.close()
    print("\nWho are the most popular article authors of all time?")
    print("-----------------------------------------------------\n")
    for row in range(len(result_two)):
        print(str(result_two[row][0])+" -- "+str(result_two[row][1])+" views")


def get_days_of_errors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    error_query = """select error_code_number.date
                     ,round(100.0*daily_error_number/total_daily_codes,2)
                     as percent
                     from error_code_number, status_number
                     where error_code_number.date=status_number.date
                     and daily_error_number > total_daily_codes/100"""
    c.execute(error_query)
    result_three = c.fetchall()
    db.close()
    print("\nOn which days did more than 1% of requests lead to errors?")
    print("----------------------------------------------------------\n")
    for row in range(len(result_three)):
        print(str(result_three[row][0])
              + " -- " + str(result_three[row][1])
              + "% errors")


if __name__ == '__main__':
    get_popular_articles()
    get_popular_authors()
    get_days_of_errors()
