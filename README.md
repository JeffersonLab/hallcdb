# Hall C RCDB

## Setting up
All HallC run condition databases are updated with schema v2 and can now use the rcdb python library (https://pypi.org/project/rcdb/)
1) Install rcdb if not done already
  ```
  pip install rcdb
  ```
2) Set environment variable for connection strings
  ```
  setenv RCDB_CONNECTION mysql://rcdb@hallcdb.jlab.org/<database name> (csh, tcsh)
  export RCDB_CONNECTION=mysql://rcdb@hallcdb.jlab.org/<database name> (bash, zsh)
  ```
  If using SQLite databases, valid SQLite URL forms are:
  ```
  sqlite:///:memory: (or, sqlite://)
  sqlite:///relative/path/to/file.db
  sqlite:////absolute/path/to/file.db
  ```
3) Check if things are set properly using the command line tools. For example,
  ```
  rcdb 
  ```
  This will print out a summary about the database contents. For more information on the CLI, see https://jeffersonlab.github.io/rcdb/#/rcdb-cli

## Setting up from scratch (with old schema v1)
1) Clone this repository
  ```
  git clone https://github.com/JeffersonLab/hallcdb
  ```
2) Set environment variables. Modify setup.csh script as needed. You will most likely need to update the first two variables to adjust the path.
  Once it's done, 
  ```
  > cd hallcdb
  > source setup.csh
  ```
3) Check if things are set properly. For example, type:
  ```
  > rcnd
  ```
  This should show the list of condition types. </br>
  More information on the commandline tool can be found from: https://github.com/JeffersonLab/rcdb/wiki/rcnd
  
-----------------------------

## Notes:
### RCDB submodule
  - rcdb package (https://github.com/JeffersonLab/rcdb) is added as submodule with a specific tag. This release version is a rather old one, but for now keep it as it is. 
### Connection string:
  - For updating DB entries: Master DB should be only used when making DB entries by start/end run scripts from cdaq machines. On cdaq computers, RCDB environment is set when login, and the connection string is set to the master database.
  - Please use the read-only copy otherwise:
    ```
    setenv RCDB_CONNECTION mysql://rcdb@hallcdb.jlab.org/c-rcdb
    ```
## Useful information: 
### DB GUI for users
  #### RCDB EDIT
  rcdb_edit.py: this gui allows one to update run type, comment and flag the run.
