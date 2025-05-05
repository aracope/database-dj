### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
PostgreSQL is an open-source relational database management system (RDBMS) that uses and extends the SQL (Structured Query Language) language. It is known for its robustness, extensibility, and standards compliance. 

- What is the difference between SQL and PostgreSQL?
SQL is a language used to interact with relational databases, such as querying, updating, and managing data. PostgreSQL is a specific relational database system that implements SQL. While SQL defines the language and syntax for interacting with databases, PostgreSQL is one of the systems (along with MySQL, SQLite, Oracle, etc.) that supports SQL for database management.

- In `psql`, how do you connect to a database?
To connect to a PostgreSQL database using psql, you can run the following command:
  psql -h hostname -U username -d database_name
    -h specifies the host (use localhost if running locally).
    -U specifies the username.
    -d specifies the database you want to connect to.

- What is the difference between `HAVING` and `WHERE`?
HAVING: A clause used to filter records after the GROUP BY operation. It applies to groups of rows and is typically used with aggregate functions (like COUNT, SUM).

WHERE: This clause is used to filter records before grouping them. It is applied to individual rows before any aggregation occurs.

- What is the difference between an `INNER` and `OUTER` join?
INNER JOIN: Returns only the rows where there is a match in both tables. If there is no match, the row is not included in the result.

OUTER JOIN: Returns all rows from one table and the matching rows from the other table. If there is no match, NULL values are returned for the columns from the table that has no match.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
LEFT OUTER JOIN: Returns all rows from the left table and the matching rows from the right table. If there is no match in the right table, NULL values are returned for the right table's columns.

RIGHT OUTER JOIN: Returns all rows from the right table and the matching rows from the left table. If there is no match in the left table, NULL values are returned for the left table's columns.

- What is an ORM? What do they do?
An ORM (Object-Relational Mapping) is a technique that allows developers to interact with a relational database using an object-oriented programming language. ORMs map database tables to classes in code, where each row in the table corresponds to an instance of a class. They abstract away SQL queries and provide a higher-level interface for data manipulation, making it easier to interact with databases in a more intuitive way.

- What are some differences between making HTTP requests using AJAX and from the server side using a library like `requests`?
AJAX: AJAX (Asynchronous JavaScript and XML) is used to make HTTP requests from the client-side (browser). It allows for asynchronous communication with the server; meaning the page doesn’t need to reload to fetch new data. It's typically used for dynamic web applications to fetch data and update parts of the page without a full reload.

`requests` (server-side): The requests library is used to make HTTP requests from the server-side, typically in Python applications. Server-side requests are often used for interacting with external APIs or services, where the request is made in the backend, and the response is processed or passed back to the client.

- What is CSRF? What is the purpose of the CSRF token?
CSRF (Cross-Site Request Forgery) is a type of attack where a malicious user tricks a victim into submitting a request to a web application where the victim is authenticated. This can lead to unintended actions being performed on behalf of the victim.

The CSRF token is a security measure used to prevent CSRF attacks. It is a unique, secret value that is included in each form submitted by a user. The server checks the token to ensure that the request is legitimate and initiated by the user, not an attacker.

- What is the purpose of `form.hidden_tag()`?
`form.hidden_tag()` is a method provided by Flask-WTF (a Flask extension for handling forms) that renders hidden fields within a form. It is typically used to render the CSRF token as a hidden field in a form. This allows the form to be securely submitted while preventing CSRF attacks.
