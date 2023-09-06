NoSQL

##Resources
Read or watch:

NoSQL Databases Explained
What is NoSQL ?
MongoDB with Python Crash Course - Tutorial for Beginners
MongoDB Tutorial 2 : Insert, Update, Remove, Query
Aggregation
Introduction to MongoDB and Python
mongo Shell Methods
The mongo Shell

##Learning Objectives
What NoSQL means
What is difference between SQL and NoSQL
What is ACID
What is a document storage
What are NoSQL types
What are benefits of a NoSQL database
How to query information from a NoSQL database
How to insert/update/delete information from a NoSQL database
How to use MongoDB

##Requirements
MongoDB Command File
All your files will be interpreted/compiled on Ubuntu 18.04 LTS using MongoDB (version 4.2)
All your files should end with a new line
The first line of all your files should be a comment: // my comment
A README.md file, at the root of the folder of the project, is mandatory
The length of your files will be tested using wc
Python Scripts
All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7) and PyMongo (version 3.10)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/env python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle style (version 2.5.*)
The length of your files will be tested using wc
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)'
Your code should not be executed when imported (by using if __name__ == "__main__":)
## More Info
Install MongoDB 4.2 in Ubuntu 18.04

$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
...
$  sudo service mongod status
mongod start/running, process 3627
$ mongo --version
MongoDB shell version v4.2.8
git version: 43d25964249164d76d5e04dd6cf38f6111e21f5f
OpenSSL version: OpenSSL 1.1.1  11 Sep 2018
allocator: tcmalloc
modules: none
build environment:
    distmod: ubuntu1804
    distarch: x86_64
    target_arch: x86_64
$  
$ pip3 install pymongo
$ python3
>>> import pymongo
>>> pymongo.__version__
'3.10.1'

##Files

0-list_databases | script that lists all databases in MongoDB.
1-use_or_create_database | script that creates or uses the database my_db
2-insert | script that inserts a document in the collection school
3-all | script that lists all documents in the collection school
4-match | script that lists all documents with name="Holberton school" in the collection school
5-count | script that displays the number of documents in the collection school
6-update | script that adds a new attribute to a document in the collection school
7-delete | script that deletes all documents with name="Holberton school" in the collection school
8-all.py | Python function that lists all documents in a collection
9-insert_school.py |  Python function that inserts a new document in a collection based on kwargs
10-update_topics.py | Python function that changes all topics of a school document based on the name
11-schools_by_topic.py |  Python function that returns the list of school having a specific topic
12-log_stats.py | Python script that provides some stats about Nginx logs stored in MongoDB

##Holberton Student
Tania Hillock
Github @TaniaHillock