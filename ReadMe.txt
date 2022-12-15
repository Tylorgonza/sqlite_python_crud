Tylor Gonzalez
20542734
CSCI 4333

IN ORDER FOR THIS TO RUN THE PYTHON SCRIPTS MUST BE RUN IN THIS ORDER
---------------------------
1)task.py
2)summary.py
3)update.py
----------------------------
The task.py can be run as the following:

	python3 task.py

#NOTE: after running task.py a .db file will be made so that "summary.py" and "update.py" can work with the db
---------------------------
The summary.py can be run as the following:

	python3 summary.py
----------------------------
The update.py script allows the user to add or delete records from a table in the CSCI4333.db

The user must fill in the following paramaters:
1) --add or --delete
2) table_name
3) record

The user must specify one of the following tables as exactly written below:
1)instrument
2)album
3)musician
4)musicianToalbum
5)albumToinstrument

IF YOU DO NOT USE THE SPECIFIED TABLES THE PROGRAM WILL EXECUTE BUT NO ACTION WILL BE MADE ON DB
--------------------------------------------------------------------------------------------------
The general usage is as follows:

	python3 update.py --add/delete --table table_name --record "record"

Here is an example of deleting a record:

	python3 update.py --delete --table instrument --record "12,guitar,B"
	
		Output:
			SQLite version:
			2.6.0
			---------------
			delete: True
			this is our table name: instrument
			this is our record: ['12', 'guitar', 'B']

Here is an example of adding a record:

	python3 update.py --add --table instrument --record "12,guitar,B"

		Output:
			SQLite version:
			2.6.0
			---------------
			add: True      
			this is our table name: instrument
			this is our record: ['12', 'guitar', 'B']

TO SEE THESE CHANGES HAVE BEEN MADE WE CAN RUN "summary.py" AGAIN TO SEE WHETHER A RECORD WAS DELETED OR ADDED

Currently the program does not check if there is a match between relations and does not creat them. For example:

If an album record is created and a musician record is created, they will not be added to the musicianToalbum table.
This will need to manually done.