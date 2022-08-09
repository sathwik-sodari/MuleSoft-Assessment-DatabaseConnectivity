import sqlite3


def insert_movie_data(conn1,query):

    conn1.execute(query)



####Creating a connection object to sqlite3 database if database does not exists and opening it if database exists####
#### our database name is movie.db  #####

conn= sqlite3.connect("movie.db")

print("Database created")

##### creating a table named movie_details #####
 
table_creat = '''create table if not exists movie_details (sno int primary key,
movie_name VARCHAR(40),
actor VARCHAR(40),
actress VARCHAR(40),
director VARCHAR(40),
year_of_release int);'''


#### executing the statement ######  
conn.execute(table_creat)


##### inserting data ######

insert_movie_data(conn,"insert into movie_details values(1,'Pokiri','Mahesh Babu','Ileana','Puri Jagannadh',2006)")
insert_movie_data(conn,"insert into movie_details values(2,'Interstellar','Matthew McConaughey','Anne Hathaway','Christopher Nolan',2014)")
insert_movie_data(conn,"insert into movie_details values(3,'Sulthan','Salman Khan','Kareena Kapoor','Ali Abbas Jaffer',2016)")
insert_movie_data(conn,"insert into movie_details values(4,'Ghajini','Suriya','Asin','A.R. Murugadoss',2008)")
insert_movie_data(conn,"insert into movie_details values(5,'Athadu','Mahesh Babu','Trisha','Trivikram',2005)")
insert_movie_data(conn,"insert into movie_details values(6,'Jalsa','Pawan Kalyan','Ileana','Trivikram',2008)")

conn.commit()


#Querying table


##### Using a Cursor to point to the records in the table ######

curs = conn.execute("select * from movie_details")

print("\n")
print("Favourite Movie Details")
print("\n")

#### pointing to each individual row inside the table ####

for row in curs:
    print("S.no       : " ,row[0])
    print("movie_name : " ,row[1])
    print("actor      : ",row[2])
    print("actress    : ",row[3])
    print("director   : ",row[4])
    print("year_of_release : ",row[5])
    print("\n")


####----querying using actor name----########

print("####----querying using actor name----########")
print("\n")

# print("S.no"+" "+"Movie_name"+" "+"actor"+" "+"actress"+" "+"director"+" "+"year_of_release")

curs = conn.execute("select * from movie_details where actor='Mahesh Babu'")


for row in curs:
    print("S.no       : " ,row[0])
    print("movie_name : " ,row[1])
    print("actor      : ",row[2])
    print("actress    : ",row[3])
    print("director   : ",row[4])
    print("year_of_release : ",row[5])
    print("\n")



####----querying using director name----########
print("####----querying using director name----########")
print("\n")

# print("S.no"+" "+"Movie_name"+" "+"actor"+" "+"actress"+" "+"director"+" "+"year_of_release")

curs = conn.execute("select * from movie_details where director='Trivikram'")


for row in curs:
    print("S.no       : " ,row[0])
    print("movie_name : " ,row[1])
    print("actor      : ",row[2])
    print("actress    : ",row[3])
    print("director   : ",row[4])
    print("year_of_release : ",row[5])
    print("\n")


####----querying using Year of release----########
print("####----querying using Year of release----########")
print("\n")
# print("S.no"+" "+"Movie_name"+" "+"actor"+" "+"actress"+" "+"director"+" "+"year_of_release")

curs = conn.execute("select * from movie_details where year_of_release=2008")


for row in curs:
    print("S.no       : " ,row[0])
    print("movie_name : " ,row[1])
    print("actor      : ",row[2])
    print("actress    : ",row[3])
    print("director   : ",row[4])
    print("year_of_release : ",row[5])
    print("\n")


    









