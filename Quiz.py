from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from datetime import date
from reportlab.pdfgen import canvas
from flask import send_file
import io
from flask import Flask, render_template,request, redirect, url_for,session,flash
app = Flask(__name__)
app.secret_key = "quizsecret"

@app.route('/', methods=['GET','POST'])
def home():
  if request.method == "POST":
    password = request.form.get("pass")
    user = request.form.get("user")
    if password == "123":
        session["user"] = user
        session["score"] = 0
        session["qindex"] = 0
        return redirect("/test")
    else:
      flash("Wrong Password" , "Try Again")
  return render_template("home.html")



@app.route('/test', methods=['GET','POST'])
def ques():
  questions = [
      {
          "id": 1,
          "question": "Which MySQL command is used to retrieve data from a table?",
          "options": ["GET", "SELECT", "FETCH", "OPEN"],
          "answer": "SELECT"
      },
      {
          "id": 2,
          "question": "Which clause is used to filter rows in MySQL?",
          "options": ["WHERE", "ORDER BY", "GROUP BY", "FILTER"],
          "answer": "WHERE"
      },
      {
          "id": 3,
          "question": "Which command is used to add new data into a table?",
          "options": ["INSERT", "ADD", "PUT", "NEW"],
          "answer": "INSERT"
      },
      {
          "id": 4,
          "question": "Which statement removes a table permanently?",
          "options": ["DELETE", "REMOVE", "DROP", "CLEAR"],
          "answer": "DROP"
      },
      {
          "id": 5,
          "question": "Which clause sorts query results?",
          "options": ["SORT", "ORDER BY", "GROUP BY", "ARRANGE"],
          "answer": "ORDER BY"
      },
      {
          "id": 6,
          "question": "Which function counts rows in MySQL?",
          "options": ["COUNT()", "SUM()", "TOTAL()", "ADD()"],
          "answer": "COUNT()"
      },
      {
          "id": 7,
          "question": "Which command modifies existing data?",
          "options": ["CHANGE", "UPDATE", "ALTER", "SET"],
          "answer": "UPDATE"
      },
      {
          "id": 8,
          "question": "Which command removes specific rows from a table?",
          "options": ["DELETE", "DROP", "REMOVE", "CUT"],
          "answer": "DELETE"
      },
      {
          "id": 9,
          "question": "Which keyword combines rows from multiple tables?",
          "options": ["MERGE", "JOIN", "CONNECT", "MATCH"],
          "answer": "JOIN"
      },
      {
          "id": 10,
          "question": "Which join returns only matching rows?",
          "options": ["LEFT JOIN", "RIGHT JOIN", "INNER JOIN", "FULL JOIN"],
          "answer": "INNER JOIN"
      },

      {
          "id": 11,
          "question": "Which join returns all rows from the left table?",
          "options": ["LEFT JOIN", "RIGHT JOIN", "FULL JOIN", "INNER JOIN"],
          "answer": "LEFT JOIN"
      },
      {
          "id": 12,
          "question": "Which join returns all rows from the right table?",
          "options": ["RIGHT JOIN", "LEFT JOIN", "INNER JOIN", "CROSS JOIN"],
          "answer": "RIGHT JOIN"
      },
      {
          "id": 13,
          "question": "Which clause groups rows with same values?",
          "options": ["GROUP BY", "ORDER BY", "WHERE", "SORT"],
          "answer": "GROUP BY"
      },
      {
          "id": 14,
          "question": "Which clause filters grouped data?",
          "options": ["HAVING", "WHERE", "FILTER", "CHECK"],
          "answer": "HAVING"
      },
      {
          "id": 15,
          "question": "Which keyword removes duplicate records?",
          "options": ["DISTINCT", "UNIQUE", "REMOVE", "FILTER"],
          "answer": "DISTINCT"
      },
      {
          "id": 16,
          "question": "Which function returns average value?",
          "options": ["AVG()", "MEAN()", "CENTER()", "MID()"],
          "answer": "AVG()"
      },
      {
          "id": 17,
          "question": "Which function returns maximum value?",
          "options": ["MAX()", "TOP()", "HIGH()", "UP()"],
          "answer": "MAX()"
      },
      {
          "id": 18,
          "question": "Which function returns minimum value?",
          "options": ["MIN()", "LOW()", "SMALL()", "BOTTOM()"],
          "answer": "MIN()"
      },
      {
          "id": 19,
          "question": "Which function calculates total?",
          "options": ["SUM()", "TOTAL()", "ADD()", "PLUS()"],
          "answer": "SUM()"
      },
      {
          "id": 20,
          "question": "Which operator checks NULL values?",
          "options": ["IS NULL", "== NULL", "= NULL", "NULL"],
          "answer": "IS NULL"
      },

      {
          "id": 21,
          "question": "Which command creates a table?",
          "options": ["MAKE TABLE", "CREATE TABLE", "NEW TABLE", "BUILD"],
          "answer": "CREATE TABLE"
      },
      {
          "id": 22,
          "question": "Which command deletes a database?",
          "options": ["DROP DATABASE", "DELETE DATABASE", "REMOVE DB", "CLEAR DB"],
          "answer": "DROP DATABASE"
      },
      {
          "id": 23,
          "question": "Which keyword limits returned rows?",
          "options": ["LIMIT", "STOP", "BOUND", "TOP"],
          "answer": "LIMIT"
      },
      {
          "id": 24,
          "question": "Which wildcard represents many characters?",
          "options": ["%", "_", "*", "#"],
          "answer": "%"
      },
      {
          "id": 25,
          "question": "Which wildcard represents one character?",
          "options": ["_", "%", "*", "#"],
          "answer": "_"
      },
      {
          "id": 26,
          "question": "Which clause is used with LIKE?",
          "options": ["WHERE", "GROUP BY", "ORDER BY", "HAVING"],
          "answer": "WHERE"
      },
      {
          "id": 27,
          "question": "Which statement modifies table structure?",
          "options": ["ALTER", "UPDATE", "CHANGE", "MODIFY"],
          "answer": "ALTER"
      },
      {
          "id": 28,
          "question": "Which constraint prevents NULL values?",
          "options": ["NOT NULL", "UNIQUE", "PRIMARY", "CHECK"],
          "answer": "NOT NULL"
      },
      {
          "id": 29,
          "question": "Which constraint ensures unique values?",
          "options": ["UNIQUE", "PRIMARY", "INDEX", "KEY"],
          "answer": "UNIQUE"
      },
      {
          "id": 30,
          "question": "Which index improves query speed?",
          "options": ["INDEX", "FAST", "KEY", "SEARCH"],
          "answer": "INDEX"
      },

      {
          "id": 31,
          "question": "Which operator checks range?",
          "options": ["BETWEEN", "IN", "LIMIT", "RANGE"],
          "answer": "BETWEEN"
      },
      {
          "id": 32,
          "question": "Which operator checks list of values?",
          "options": ["IN", "ANY", "ALL", "MATCH"],
          "answer": "IN"
      },
      {
          "id": 33,
          "question": "Which command renames a table?",
          "options": ["RENAME", "CHANGE", "ALTER", "MODIFY"],
          "answer": "RENAME"
      },
      {
          "id": 34,
          "question": "Which function returns current timestamp?",
          "options": ["NOW()", "TODAY()", "DATE()", "TIME()"],
          "answer": "NOW()"
      },
      {
          "id": 35,
          "question": "Which keyword sets default value?",
          "options": ["DEFAULT", "AUTO", "STANDARD", "BASE"],
          "answer": "DEFAULT"
      },
      {
          "id": 36,
          "question": "Which command deletes all rows but keeps table?",
          "options": ["TRUNCATE", "DELETE", "DROP", "CLEAR"],
          "answer": "TRUNCATE"
      },
      {
          "id": 37,
          "question": "Which constraint links two tables?",
          "options": ["FOREIGN KEY", "PRIMARY KEY", "UNIQUE", "INDEX"],
          "answer": "FOREIGN KEY"
      },
      {
          "id": 38,
          "question": "Which statement lists tables?",
          "options": ["SHOW TABLES", "LIST TABLES", "DISPLAY", "VIEW"],
          "answer": "SHOW TABLES"
      },
      {
          "id": 39,
          "question": "Which function converts to uppercase?",
          "options": ["UPPER()", "CAP()", "HIGH()", "BIG()"],
          "answer": "UPPER()"
      },
      {
          "id": 40,
          "question": "Which function converts to lowercase?",
          "options": ["LOWER()", "SMALL()", "DOWN()", "MIN()"],
          "answer": "LOWER()"
      },
      {
          "id": 41,
          "question": "What will be the output of: SELECT 10/3;",
          "options": ["3", "3.33", "3.3333", "Error"],
          "answer": "3.3333"
      },
      {
          "id": 42,
          "question": "What will be the output of: SELECT 10 DIV 3;",
          "options": ["3", "3.33", "4", "Error"],
          "answer": "3"
      },
      {
          "id": 43,
          "question": "What will be the output of: SELECT MOD(10,3);",
          "options": ["0", "1", "2", "3"],
          "answer": "1"
      },
      {
          "id": 44,
          "question": "What will be the output of: SELECT LENGTH('MYSQL');",
          "options": ["4", "5", "6", "Error"],
          "answer": "5"
      },
      {
          "id": 45,
          "question": "What will be the output of: SELECT UPPER('sql');",
          "options": ["sql", "SQL", "Sql", "Error"],
          "answer": "SQL"
      },
      {
          "id": 46,
          "question": "What will be the output of: SELECT LOWER('DATA');",
          "options": ["data", "DATA", "Data", "Error"],
          "answer": "data"
      },
      {
          "id": 47,
          "question": "What will be the output of: SELECT ROUND(7.4);",
          "options": ["7", "8", "7.4", "Error"],
          "answer": "7"
      },
      {
          "id": 48,
          "question": "What will be the output of: SELECT CEIL(7.1);",
          "options": ["7", "8", "7.1", "Error"],
          "answer": "8"
      },
      {
          "id": 49,
          "question": "What will be the output of: SELECT FLOOR(7.9);",
          "options": ["7", "8", "7.9", "Error"],
          "answer": "7"
      },
      {
          "id": 50,
          "question": "What will be the output of: SELECT CONCAT('My','SQL');",
          "options": ["My SQL", "MySQL", "My-SQL", "Error"],
          "answer": "MySQL"
      },

      {
          "id": 51,
          "question": "What will be the output of: SELECT 5 BETWEEN 1 AND 10;",
          "options": ["True", "False", "Error", "NULL"],
          "answer": "True"
      },
      {
          "id": 52,
          "question": "What will be the output of: SELECT 15 BETWEEN 1 AND 10;",
          "options": ["True", "False", "NULL", "Error"],
          "answer": "False"
      },
      {
          "id": 53,
          "question": "What will be the output of: SELECT 'A' LIKE 'A%';",
          "options": ["True", "False", "Error", "NULL"],
          "answer": "True"
      },
      {
          "id": 54,
          "question": "What will be the output of: SELECT 'SQL' LIKE '%L';",
          "options": ["True", "False", "Error", "NULL"],
          "answer": "True"
      },
      {
          "id": 55,
          "question": "What will be the output of: SELECT 5 IN (1,2,3,4,5);",
          "options": ["True", "False", "NULL", "Error"],
          "answer": "True"
      },
      {
          "id": 56,
          "question": "What will be the output of: SELECT 8 IN (1,2,3);",
          "options": ["True", "False", "NULL", "Error"],
          "answer": "False"
      },
      {
          "id": 57,
          "question": "Which MySQL function returns number of characters?",
          "options": ["SIZE()", "COUNT()", "LENGTH()", "CHARCOUNT()"],
          "answer": "LENGTH()"
      },
      {
          "id": 58,
          "question": "Which clause comes after WHERE?",
          "options": ["ORDER BY", "GROUP BY", "LIMIT", "SELECT"],
          "answer": "GROUP BY"
      },
      {
          "id": 59,
          "question": "Which clause executes last?",
          "options": ["WHERE", "ORDER BY", "GROUP BY", "FROM"],
          "answer": "ORDER BY"
      },
      {
          "id": 60,
          "question": "Which clause executes before SELECT?",
          "options": ["FROM", "WHERE", "LIMIT", "ORDER"],
          "answer": "FROM"
      },

      {
          "id": 61,
          "question": "Which index type is default in MySQL?",
          "options": ["HASH", "BTREE", "RTREE", "FULL"],
          "answer": "BTREE"
      },
      {
          "id": 62,
          "question": "Which storage engine supports transactions?",
          "options": ["MyISAM", "InnoDB", "Memory", "CSV"],
          "answer": "InnoDB"
      },
      {
          "id": 63,
          "question": "Which engine does not support foreign keys?",
          "options": ["InnoDB", "MyISAM", "NDB", "Memory"],
          "answer": "MyISAM"
      },
      {
          "id": 64,
          "question": "Which command starts transaction?",
          "options": ["START TRANSACTION", "BEGIN WORK", "OPEN TRANSACTION", "START"],
          "answer": "START TRANSACTION"
      },
      {
          "id": 65,
          "question": "Which command saves transaction permanently?",
          "options": ["SAVE", "COMMIT", "END", "STORE"],
          "answer": "COMMIT"
      },
      {
          "id": 66,
          "question": "Which command cancels transaction?",
          "options": ["STOP", "ROLLBACK", "UNDO", "CANCEL"],
          "answer": "ROLLBACK"
      },
      {
          "id": 67,
          "question": "Which level prevents dirty reads?",
          "options": ["READ UNCOMMITTED", "READ COMMITTED", "REPEATABLE READ", "SERIALIZABLE"],
          "answer": "READ COMMITTED"
      },
      {
          "id": 68,
          "question": "Which level gives highest isolation?",
          "options": ["READ COMMITTED", "SERIALIZABLE", "READ UNCOMMITTED", "REPEATABLE"],
          "answer": "SERIALIZABLE"
      },
      {
          "id": 69,
          "question": "Which normalization removes repeating groups?",
          "options": ["1NF", "2NF", "3NF", "BCNF"],
          "answer": "1NF"
      },
      {
          "id": 70,
          "question": "Which normalization removes partial dependency?",
          "options": ["1NF", "2NF", "3NF", "4NF"],
          "answer": "2NF"
      },

      {
          "id": 71,
          "question": "Which normalization removes transitive dependency?",
          "options": ["1NF", "2NF", "3NF", "BCNF"],
          "answer": "3NF"
      },
      {
          "id": 72,
          "question": "Which command creates index?",
          "options": ["MAKE INDEX", "CREATE INDEX", "ADD INDEX", "BUILD INDEX"],
          "answer": "CREATE INDEX"
      },
      {
          "id": 73,
          "question": "Which command removes index?",
          "options": ["DROP INDEX", "DELETE INDEX", "REMOVE INDEX", "CLEAR INDEX"],
          "answer": "DROP INDEX"
      },
      {
          "id": 74,
          "question": "Which command renames table?",
          "options": ["RENAME TABLE", "ALTER NAME", "CHANGE TABLE", "MODIFY TABLE"],
          "answer": "RENAME TABLE"
      },
      {
          "id": 75,
          "question": "Which function returns system user?",
          "options": ["USER()", "USERNAME()", "CURRENTUSER()", "LOGIN()"],
          "answer": "USER()"
      },
      {
          "id": 76,
          "question": "Which command copies table structure only?",
          "options": ["CREATE TABLE LIKE", "COPY STRUCTURE", "CLONE TABLE", "STRUCT TABLE"],
          "answer": "CREATE TABLE LIKE"
      },
      {
          "id": 77,
          "question": "Which join joins table to itself?",
          "options": ["SELF JOIN", "INNER JOIN", "OUTER JOIN", "SIDE JOIN"],
          "answer": "SELF JOIN"
      },
      {
          "id": 78,
          "question": "Which keyword is used in subquery?",
          "options": ["SELECT", "SUBSELECT", "INNER", "QUERY"],
          "answer": "SELECT"
      },
      {
          "id": 79,
          "question": "Which operator compares subquery result?",
          "options": ["ANY", "ALL", "IN", "All of these"],
          "answer": "All of these"
      },
      {
          "id": 80,
          "question": "Which clause limits grouped results?",
          "options": ["HAVING", "WHERE", "LIMIT", "FILTER"],
          "answer": "HAVING"
      },

      {
          "id": 81,
          "question": "What will be output of: SELECT COUNT(*) FROM (SELECT 1 UNION SELECT 1) A;",
          "options": ["1", "2", "0", "Error"],
          "answer": "1"
      },
      {
          "id": 82,
          "question": "What will be output of: SELECT DISTINCT 5,5;",
          "options": ["One row", "Two rows", "Error", "Null"],
          "answer": "One row"
      },
      {
          "id": 83,
          "question": "What will be output of: SELECT 1+NULL;",
          "options": ["1", "0", "NULL", "Error"],
          "answer": "NULL"
      },
      {
          "id": 84,
          "question": "What will be output of: SELECT IFNULL(NULL,10);",
          "options": ["NULL", "10", "0", "Error"],
          "answer": "10"
      },
      {
          "id": 85,
          "question": "What will be output of: SELECT COALESCE(NULL,NULL,5);",
          "options": ["NULL", "5", "0", "Error"],
          "answer": "5"
      },
      {
          "id": 86,
          "question": "What will be output of: SELECT ABS(-7);",
          "options": ["-7", "7", "0", "Error"],
          "answer": "7"
      },
      {
          "id": 87,
          "question": "What will be output of: SELECT POWER(2,3);",
          "options": ["6", "8", "9", "Error"],
          "answer": "8"
      },
      {
          "id": 88,
          "question": "What will be output of: SELECT SQRT(16);",
          "options": ["2", "4", "8", "16"],
          "answer": "4"
      },
      {
          "id": 89,
          "question": "Which clause is used for pagination?",
          "options": ["LIMIT", "OFFSET", "Both", "None"],
          "answer": "Both"
      },
      {
          "id": 90,
          "question": "Which join returns unmatched rows from both tables?",
          "options": ["FULL OUTER JOIN", "LEFT JOIN", "RIGHT JOIN", "INNER JOIN"],
          "answer": "FULL OUTER JOIN"
      },

      {
          "id": 91,
          "question": "Which statement creates view?",
          "options": ["CREATE VIEW", "MAKE VIEW", "NEW VIEW", "BUILD VIEW"],
          "answer": "CREATE VIEW"
      },
      {
          "id": 92,
          "question": "Which command deletes view?",
          "options": ["DROP VIEW", "DELETE VIEW", "REMOVE VIEW", "CLEAR VIEW"],
          "answer": "DROP VIEW"
      },
      {
          "id": 93,
          "question": "Which command creates stored procedure?",
          "options": ["CREATE PROCEDURE", "MAKE PROCEDURE", "NEW PROCEDURE", "BUILD PROCEDURE"],
          "answer": "CREATE PROCEDURE"
      },
      {
          "id": 94,
          "question": "Which command executes stored procedure?",
          "options": ["RUN", "EXEC", "CALL", "START"],
          "answer": "CALL"
      },
      {
          "id": 95,
          "question": "Which command deletes procedure?",
          "options": ["DROP PROCEDURE", "DELETE PROCEDURE", "REMOVE PROCEDURE", "CLEAR PROCEDURE"],
          "answer": "DROP PROCEDURE"
      },
      {
          "id": 96,
          "question": "Which object runs automatically on event?",
          "options": ["Trigger", "View", "Index", "Cursor"],
          "answer": "Trigger"
      },
      {
          "id": 97,
          "question": "Which command creates trigger?",
          "options": ["CREATE TRIGGER", "MAKE TRIGGER", "NEW TRIGGER", "BUILD TRIGGER"],
          "answer": "CREATE TRIGGER"
      },
      {
          "id": 98,
          "question": "Which command deletes trigger?",
          "options": ["DROP TRIGGER", "DELETE TRIGGER", "REMOVE TRIGGER", "CLEAR TRIGGER"],
          "answer": "DROP TRIGGER"
      },
      {
          "id": 99,
          "question": "Which statement lists databases?",
          "options": ["SHOW DATABASES", "LIST DATABASE", "DISPLAY DB", "VIEW DB"],
          "answer": "SHOW DATABASES"
      },
      {
          "id": 100,
          "question": "Which statement describes table structure?",
          "options": ["DESCRIBE", "STRUCTURE", "INFO", "DETAIL"],
          "answer": "DESCRIBE"
      },

      {
          "id": 101,
          "question": "Which function returns current database?",
          "options": ["DATABASE()", "DBNAME()", "CURRENTDB()", "DB()"],
          "answer": "DATABASE()"
      },
      {
          "id": 102,
          "question": "Which function returns version of MySQL?",
          "options": ["VERSION()", "MYSQLVER()", "VER()", "SYSTEMVERSION()"],
          "answer": "VERSION()"
      },
      {
          "id": 103,
          "question": "Which operator concatenates strings?",
          "options": ["CONCAT()", "MERGE()", "ADD()", "PLUS()"],
          "answer": "CONCAT()"
      },
      {
          "id": 104,
          "question": "Which function trims spaces?",
          "options": ["TRIM()", "CUT()", "STRIP()", "REMOVE()"],
          "answer": "TRIM()"
      },
      {
          "id": 105,
          "question": "Which function returns substring?",
          "options": ["SUBSTRING()", "PART()", "MIDTEXT()", "CUTTEXT()"],
          "answer": "SUBSTRING()"
      },
      {
          "id": 106,
          "question": "Which function returns position of substring?",
          "options": ["LOCATE()", "POSITION()", "FIND()", "Both A and B"],
          "answer": "Both A and B"
      },
      {
          "id": 107,
          "question": "Which function repeats string?",
          "options": ["REPEAT()", "MULTIPLY()", "LOOP()", "COPY()"],
          "answer": "REPEAT()"
      },
      {
          "id": 108,
          "question": "Which function replaces string?",
          "options": ["REPLACE()", "CHANGE()", "ALTERTEXT()", "EDIT()"],
          "answer": "REPLACE()"
      },
      {
          "id": 109,
          "question": "Which clause sorts ascending by default?",
          "options": ["ASC", "DESC", "UP", "TOP"],
          "answer": "ASC"
      },
      {
          "id": 110,
          "question": "Which keyword removes duplicates?",
          "options": ["DISTINCT", "UNIQUE", "FILTER", "GROUP"],
          "answer": "DISTINCT"
      },

      {
          "id": 111,
          "question": "Which command backs up database logically?",
          "options": ["mysqldump", "backupdb", "dbexport", "dumpdb"],
          "answer": "mysqldump"
      },
      {
          "id": 112,
          "question": "Which tool restores MySQL backup?",
          "options": ["mysql", "restoredb", "importdb", "mysqlload"],
          "answer": "mysql"
      },
      {
          "id": 113,
          "question": "Which join is fastest usually?",
          "options": ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL JOIN"],
          "answer": "INNER JOIN"
      },
      {
          "id": 114,
          "question": "Which clause reduces rows before grouping?",
          "options": ["WHERE", "HAVING", "ORDER", "LIMIT"],
          "answer": "WHERE"
      },
      {
          "id": 115,
          "question": "Which clause works after aggregation?",
          "options": ["HAVING", "WHERE", "SELECT", "LIMIT"],
          "answer": "HAVING"
      },
      {
          "id": 116,
          "question": "Which keyword defines alias?",
          "options": ["AS", "NAME", "ALIAS", "DEFINE"],
          "answer": "AS"
      },
      {
          "id": 117,
          "question": "Which keyword sorts multiple columns?",
          "options": ["ORDER BY", "SORT", "GROUP", "ARRANGE"],
          "answer": "ORDER BY"
      },
      {
          "id": 118,
          "question": "Which join is used for hierarchical data?",
          "options": ["SELF JOIN", "INNER JOIN", "LEFT JOIN", "RIGHT JOIN"],
          "answer": "SELF JOIN"
      },
      {
          "id": 119,
          "question": "Which clause limits results after sorting?",
          "options": ["LIMIT", "WHERE", "HAVING", "GROUP"],
          "answer": "LIMIT"
      },
      {
          "id": 120,
          "question": "Which keyword returns first non-null value?",
          "options": ["COALESCE", "IFNULL", "NVL", "FIRST"],
          "answer": "COALESCE"
      },

      {
          "id": 121,
          "question": "Which statement locks table?",
          "options": ["LOCK TABLE", "TABLE LOCK", "LOCK TABLES", "FREEZE TABLE"],
          "answer": "LOCK TABLES"
      },
      {
          "id": 122,
          "question": "Which statement unlocks tables?",
          "options": ["UNLOCK", "UNLOCK TABLES", "FREE TABLE", "RELEASE"],
          "answer": "UNLOCK TABLES"
      },
      {
          "id": 123,
          "question": "Which join is used without condition?",
          "options": ["CROSS JOIN", "INNER JOIN", "LEFT JOIN", "RIGHT JOIN"],
          "answer": "CROSS JOIN"
      },
      {
          "id": 124,
          "question": "Which clause removes duplicate combinations?",
          "options": ["DISTINCT", "UNIQUE", "GROUP", "FILTER"],
          "answer": "DISTINCT"
      },
      {
          "id": 125,
          "question": "Which command analyzes table statistics?",
          "options": ["ANALYZE TABLE", "CHECK TABLE", "SCAN TABLE", "READ TABLE"],
          "answer": "ANALYZE TABLE"
      },
      {
          "id": 126,
          "question": "Which command checks table errors?",
          "options": ["CHECK TABLE", "SCAN TABLE", "TEST TABLE", "VERIFY TABLE"],
          "answer": "CHECK TABLE"
      },
      {
          "id": 127,
          "question": "Which command repairs table?",
          "options": ["REPAIR TABLE", "FIX TABLE", "RECOVER TABLE", "RESTORE TABLE"],
          "answer": "REPAIR TABLE"
      },
      {
          "id": 128,
          "question": "Which clause removes duplicates before aggregation?",
          "options": ["DISTINCT", "GROUP BY", "HAVING", "ORDER"],
          "answer": "DISTINCT"
      },
      {
          "id": 129,
          "question": "Which join combines each row with all rows?",
          "options": ["CROSS JOIN", "INNER JOIN", "LEFT JOIN", "RIGHT JOIN"],
          "answer": "CROSS JOIN"
      },
      {
          "id": 130,
          "question": "Which query shows indexes?",
          "options": ["SHOW INDEX", "DISPLAY INDEX", "LIST INDEX", "VIEW INDEX"],
          "answer": "SHOW INDEX"
      },

      {
          "id": 131,
          "question": "Which keyword defines auto increment column?",
          "options": ["AUTO_INCREMENT", "AUTOKEY", "INCREMENT", "SERIAL"],
          "answer": "AUTO_INCREMENT"
      },
      {
          "id": 132,
          "question": "Which command changes column name?",
          "options": ["ALTER TABLE CHANGE", "MODIFY", "RENAME COLUMN", "Both A and C"],
          "answer": "Both A and C"
      },
      {
          "id": 133,
          "question": "Which query removes duplicate rows using grouping?",
          "options": ["GROUP BY", "HAVING", "ORDER", "LIMIT"],
          "answer": "GROUP BY"
      },
      {
          "id": 134,
          "question": "Which clause filters before SELECT output?",
          "options": ["WHERE", "HAVING", "GROUP", "LIMIT"],
          "answer": "WHERE"
      },
      {
          "id": 135,
          "question": "Which clause executes after SELECT?",
          "options": ["ORDER BY", "FROM", "WHERE", "GROUP"],
          "answer": "ORDER BY"
      },
      {
          "id": 136,
          "question": "Which function returns random number?",
          "options": ["RAND()", "RANDOM()", "GEN()", "NUMBER()"],
          "answer": "RAND()"
      },
      {
          "id": 137,
          "question": "Which function formats date?",
          "options": ["DATE_FORMAT()", "FORMATDATE()", "DATESTYLE()", "STYLEDATE()"],
          "answer": "DATE_FORMAT()"
      },
      {
          "id": 138,
          "question": "Which function extracts year?",
          "options": ["YEAR()", "GETYEAR()", "EXTRACTYEAR()", "YEARNUM()"],
          "answer": "YEAR()"
      },
      {
          "id": 139,
          "question": "Which function extracts month?",
          "options": ["MONTH()", "GETMONTH()", "EXTRACTMONTH()", "MONTHNUM()"],
          "answer": "MONTH()"
      },
      {
          "id": 140,
          "question": "Which function extracts day?",
          "options": ["DAY()", "DATEPART()", "GETDAY()", "DAYNUM()"],
          "answer": "DAY()"
      },

      {
          "id": 141,
          "question": "Which keyword returns limited records with offset?",
          "options": ["LIMIT offset,count", "OFFSET", "BOTH", "NONE"],
          "answer": "LIMIT offset,count"
      },
      {
          "id": 142,
          "question": "Which function returns current timestamp?",
          "options": ["NOW()", "CURRENT_TIMESTAMP", "Both", "None"],
          "answer": "Both"
      },
      {
          "id": 143,
          "question": "Which clause groups identical values?",
          "options": ["GROUP BY", "ORDER BY", "HAVING", "LIMIT"],
          "answer": "GROUP BY"
      },
      {
          "id": 144,
          "question": "Which command removes column?",
          "options": ["ALTER TABLE DROP COLUMN", "DELETE COLUMN", "REMOVE COLUMN", "CLEAR COLUMN"],
          "answer": "ALTER TABLE DROP COLUMN"
      },
      {
          "id": 145,
          "question": "Which query renames database?",
          "options": ["Not directly supported", "RENAME DATABASE", "ALTER DATABASE", "CHANGE DATABASE"],
          "answer": "Not directly supported"
      },
      {
          "id": 146,
          "question": "Which function returns day name?",
          "options": ["DAYNAME()", "DAYTEXT()", "NAMEDAY()", "TEXTDAY()"],
          "answer": "DAYNAME()"
      },
      {
          "id": 147,
          "question": "Which function returns month name?",
          "options": ["MONTHNAME()", "NAMEMONTH()", "TEXTMONTH()", "MONTHWORD()"],
          "answer": "MONTHNAME()"
      },
      {
          "id": 148,
          "question": "Which query checks server status?",
          "options": ["STATUS", "SHOW STATUS", "SERVER STATUS", "CHECK SERVER"],
          "answer": "SHOW STATUS"
      },
      {
          "id": 149,
          "question": "Which query lists processes?",
          "options": ["SHOW PROCESSLIST", "LIST PROCESS", "PROCESS STATUS", "SERVER PROCESS"],
          "answer": "SHOW PROCESSLIST"
      },
      {
          "id": 150,
          "question": "Which keyword stops query execution after limit reached?",
          "options": ["LIMIT", "STOP", "BREAK", "END"],
          "answer": "LIMIT"
      },

      {
          "id": 151,
          "question": "Which clause helps ranking with variables?",
          "options": ["ORDER BY", "GROUP BY", "WHERE", "HAVING"],
          "answer": "ORDER BY"
      },
      {
          "id": 152,
          "question": "Which MySQL feature improves read speed using memory?",
          "options": ["Query Cache", "Buffer Pool", "Temp Table", "Optimizer"],
          "answer": "Query Cache"
      },
      {
          "id": 153,
          "question": "Which engine is fastest for read heavy apps?",
          "options": ["MyISAM", "InnoDB", "Memory", "CSV"],
          "answer": "MyISAM"
      },
      {
          "id": 154,
          "question": "Which engine supports row level locking?",
          "options": ["InnoDB", "MyISAM", "CSV", "Archive"],
          "answer": "InnoDB"
      },
      {
          "id": 155,
          "question": "Which clause is used to paginate results?",
          "options": ["LIMIT", "OFFSET", "Both", "None"],
          "answer": "Both"
      },
      {
          "id": 156,
          "question": "Which command optimizes table?",
          "options": ["OPTIMIZE TABLE", "IMPROVE TABLE", "BOOST TABLE", "FAST TABLE"],
          "answer": "OPTIMIZE TABLE"
      },
      {
          "id": 157,
          "question": "Which function returns connection id?",
          "options": ["CONNECTION_ID()", "SESSIONID()", "USERID()", "LINKID()"],
          "answer": "CONNECTION_ID()"
      },
      {
          "id": 158,
          "question": "Which keyword returns top records after sorting?",
          "options": ["LIMIT", "TOP", "FIRST", "HEAD"],
          "answer": "LIMIT"
      },
      {
          "id": 159,
          "question": "Which statement flushes logs?",
          "options": ["FLUSH LOGS", "CLEAR LOGS", "RESET LOGS", "REMOVE LOGS"],
          "answer": "FLUSH LOGS"
      },
      {
          "id": 160,
          "question": "Which statement reloads privileges?",
          "options": ["FLUSH PRIVILEGES", "REFRESH PRIVILEGES", "RESET USERS", "RELOAD USERS"],
          "answer": "FLUSH PRIVILEGES"
      }
  ]
  if "qindex" not in session:
    return redirect("/")

  qindex = session["qindex"]

  if request.method == "POST":

    user_answer = request.form.get("answer")
    correct = questions[qindex]["answer"]

    if user_answer == correct:
      session["score"] += 2

    session["qindex"] += 1
    qindex = session["qindex"]

    if qindex >= len(questions):
      return redirect("/result")

  question = questions[qindex]

  return render_template("Ques.html", q=question)


@app.route('/result')
def result():
  score = session.get("score", 0)
  attempted = session.get("qindex", 0)

  correct = score // 2
  incorrect = attempted - correct

  total = score - (incorrect * 0.25)
  status = "PASS" if total >= 192 else "FAIL"

  session["total"] = total

  return render_template(
    "Result.html",
    attempted=attempted,
    correct=correct,
    incorrect=incorrect,
    score=score,
    total = total,
    status = status
  )


@app.route('/pdf')
def pdf():

    if "user" not in session:
        return redirect("/")

    user = session["user"]
    total = session.get("total",0)
    return render_template("PDF.html", user=user,total=total)

@app.route("/download")
def download():

    buffer = io.BytesIO() #to create buffer memory
    p = canvas.Canvas(buffer, pagesize=A4)

    width, height = A4

    user = session.get("user", "Student")
    total = session.get("total", 0)

    # Border
    p.setStrokeColor(HexColor("#0B3D91"))
    p.setLineWidth(6)
    p.rect(30, 30, width-60, height-60) #x left sai distance y bottom sai distance w and rect ki

    # Inner border
    p.setStrokeColor(HexColor("#C9A227"))
    p.setLineWidth(2)
    p.rect(45, 45, width-90, height-90)

    # Title
    p.setFont("Helvetica-Bold", 40)
    p.setFillColor(HexColor("#0B3D91"))
    p.drawCentredString(width/2, 750, "Quiz-iz")

    # Subtitle
    p.setFont("Helvetica-Bold", 16)
    p.setFillColor(HexColor("#000000"))
    p.drawCentredString(width/2, 700, f"This is to certify that the {user} has successfully passed")
    p.drawCentredString(width / 2, 670, f"the Quiz-iz Test scored {total} marks by demonstrating strong")
    p.drawCentredString(width / 2, 640, "knowledge and problem-solving skills. His efforts, dedication,")
    p.drawCentredString(width / 2, 610, "and performance in completing the quiz are truly appreciated.")


    # Statement
    p.setFont("Helvetica", 16)
    p.drawCentredString(width/2, 500, "This certificate is proudly presented to")

    # Name
    p.setFont("Helvetica-Bold", 28)
    p.setFillColor(HexColor("#8B0000"))
    p.drawCentredString(width/2, 400, user)

    # Description
    p.setFont("Helvetica", 16)
    p.setFillColor(HexColor("#000000"))
    p.drawCentredString(width/2, 300, "For successfully completing the")
    p.drawCentredString(width/2, 260, "Quiz-iz Test")



    # Date
    today = date.today().strftime("%d %B %Y")
    p.setFont("Helvetica", 14)
    p.drawString(80, 120, f"Date : {today}")

    # Signature
    p.line(width-200, 150, width-80, 150)
    p.setFont("Helvetica", 14)
    p.drawString(width-210, 110, "Nihal Tiwari")
    p.drawString(width-210, 80, "(Project By Nihal Tiwari)")


    p.save()
    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name="certificate.pdf",
        mimetype="application/pdf"
    )
if __name__ == '__main__':
  app.run(debug=True)