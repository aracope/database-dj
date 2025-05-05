Make sure you download the starter code and run the following:

```sh
  psql < movies.sql
  psql movies_db
```

In markdown, you can place a code block inside of three backticks (```) followed by the syntax highlighting you want, for example

\```sql

SELECT \* FROM users;

\```

Using the `movies_db` database, write the correct SQL queries for each of these tasks:

1.  The title of every movie.
\```sql

SELECT title
FROM movies;

\```

(101 rows)

2.  All information on the G-rated movies.

\```

SELECT *
FROM movies
WHERE rating = 'G';

\```

 id  |        title        | release_year | runtime | rating | studio_id 
-----+---------------------+--------------+---------+--------+-----------
  20 | The Lion King       |         1994 |      89 | G      |         1
  21 | Toy Story 3         |         2010 |     103 | G      |         1
  33 | Finding Nemo        |         2003 |     104 | G      |         1
  86 | Monsters, Inc.      |         2001 |      90 | G      |         1
  95 | Monsters University |         2013 |     107 | G      |         1
 101 | Toy Story 2         |         1999 |      95 | G      |         1
(6 rows)


3.  The title and release year of every movie, ordered with the
    oldest movie first.

\```

SELECT title, release_year
FROM movies
ORDER BY release_year ASC;

\```

                       title                        | release_year 
----------------------------------------------------+--------------
 Star Wars                                          |         1977
 The Empire Strikes Back                            |         1980
 E. T.: The Extra-Terrestrial                       |         1982
 Return of the Jedi                                 |         1983
 Home Alone                                         |         1990
 Jurassic Park                                      |         1993
 The Lion King                                      |         1994
 Forrest Gump                                       |         1994
 Independence Day                                   |         1996
 Titanic                                            |         1997
 The Sixth Sense                                    |         1999
 Star Wars: Episode I - The Phantom Menace          |         1999
 Toy Story 2                                        |         1999
 Harry Potter and the Sorcerer's Stone              |         2001
 Monsters, Inc.                                     |         2001
 The Lord of the Rings: Fellowship of the Ring      |         2001
 Shrek                                              |         2001

...... for space and sanity saving purposes
 Rogue One: A Star Wars Story                       |         2016
 Captain America: Civil War                         |         2016
 Star Wars: The Last Jedi                           |         2017
 Guardians of the Galaxy Vol. 2                     |         2017
 Despicable Me 3                                    |         2017
 Beauty and the Beast                               |         2017
 Spider-Man: Homecoming                             |         2017
 It                                                 |         2017
 Wonder Woman                                       |         2017
 Thor: Ragnarok                                     |         2017
 Jumanji: Welcome to the Jungle                     |         2018
 Black Panther                                      |         2018
(101 rows)

    
4.  All information on the 5 longest movies.

\```

SELECT *
FROM movies
ORDER BY runtime DESC
LIMIT 5;

\```

 id |                     title                     | release_year | runtime | rating | studio_id 
----+-----------------------------------------------+--------------+---------+--------+-----------
 35 | The Lord of the Rings: Return of the King     |         2003 |     200 | PG-13  |         9
  3 | Titanic                                       |         1997 |     194 | PG-13  |         3
 46 | The Lord of the Rings: The Two Towers         |         2002 |     179 | PG-13  |         9
 63 | The Lord of the Rings: Fellowship of the Ring |         2001 |     178 | PG-13  |         9
 67 | Pirates of the Caribbean: At World's End      |         2007 |     168 | PG-13  |         1
(5 rows)

5.  A query that returns the columns of `rating` and `total`, tabulating the
    total number of G, PG, PG-13, and R-rated movies.

\```

SELECT rating, COUNT(*) AS total
FROM movies
WHERE rating IN ('G', 'PG', 'PG-13', 'R')
GROUP BY rating;

\```

rating | total 
--------+-------
 PG-13  |    64
 R      |     6
 G      |     6
 PG     |    25
(4 rows)

6.  A table with columns of `release_year` and `average_runtime`,
    tabulating the average runtime by year for every movie in the database. The data should be in reverse chronological order (i.e. the most recent year should be first).

\```

SELECT release_year, AVG(runtime) AS average_runtime
FROM movies
GROUP BY release_year
ORDER BY release_year DESC;

\```

 release_year |   average_runtime    
--------------+----------------------
         2018 | 129.5000000000000000
         2017 | 130.7500000000000000
         2016 | 118.3000000000000000
         2015 | 122.8571428571428571
         2014 | 125.3333333333333333
         2013 | 117.4285714285714286
         2012 | 144.2857142857142857
         2011 | 130.6666666666666667
         2010 | 126.5000000000000000
         2009 | 129.8333333333333333
         2008 | 132.0000000000000000
         2007 | 136.4000000000000000
         2006 | 151.0000000000000000
         2005 | 143.6666666666666667
         2004 | 115.0000000000000000
         2003 | 144.2500000000000000
         2002 | 148.2500000000000000
         2001 | 127.7500000000000000
         1999 | 111.6666666666666667
         1997 | 194.0000000000000000
         1996 | 153.0000000000000000

7.  The movie title and studio name for every movie in the
    database.

\```

SELECT m.title, s.name AS studio_name
FROM movies m
JOIN studios s ON m.studio_id = s.id;

\```

                  title                        |             studio_name             
----------------------------------------------------+-------------------------------------
 Star Wars: The Force Awakens                       | Walt Disney Studios Motion Pictures
 Marvel's The Avengers                              | Walt Disney Studios Motion Pictures
 Star Wars: The Last Jedi                           | Walt Disney Studios Motion Pictures
 Black Panther                                      | Walt Disney Studios Motion Pictures
 Rogue One: A Star Wars Story                       | Walt Disney Studios Motion Pictures
 Beauty and the Beast                               | Walt Disney Studios Motion Pictures
 Finding Dory                                       | Walt Disney Studios Motion Pictures
 Avengers: Age of Ultron                            | Walt Disney Studios Motion Pictures
 Pirates of the Caribbean: Dead Man's Chest         | Walt Disney Studios Motion Pictures
 The Lion King                                      | Walt Disney Studios Motion Pictures
 Avatar                                             | 20th Century Fox
 Star Wars: Episode I - The Phantom Menace          | 20th Century Fox
 ...... again for space and sanity saving purposes
  Alice in Wonderland                                | Walt Disney Studios Motion Pictures
 Guardians of the Galaxy                            | Walt Disney Studios Motion Pictures
 Thor: Ragnarok                                     | Walt Disney Studios Motion Pictures
 Pirates of the Caribbean: At World's End           | Walt Disney Studios Motion Pictures
 Pirates of the Caribbean: Curse of the Black Pearl | Walt Disney Studios Motion Pictures
 The Sixth Sense                                    | Walt Disney Studios Motion Pictures
 Up                                                 | Walt Disney Studios Motion Pictures
 The Chronicles of Narnia: Lion, Witch & Wardrobe   | Walt Disney Studios Motion Pictures
 Monsters, Inc.                                     | Walt Disney Studios Motion Pictures
 Monsters University                                | Walt Disney Studios Motion Pictures
 The Incredibles                                    | Walt Disney Studios Motion Pictures
 Toy Story 2                                        | Walt Disney Studios Motion Pictures
 Harry Potter and the Goblet of Fire                | Warner Bros.
 The Hangover                                       | Warner Bros.
 Gravity                                            | Warner Bros.
 Harry Potter and the Chamber of Secrets            | Warner Bros.
(101 rows)

8.  The star first name, star last name, and movie title for every
    matching movie and star pair in the database.

\```

SELECT s.first_name, s.last_name, m.title
FROM stars s
JOIN roles r ON s.id = r.star_id
JOIN movies m ON r.movie_id = m.id;

\```

 first_name  |   last_name   |                       title                        
-------------+---------------+----------------------------------------------------
 Frances     | McDormand     | Transformers: Dark of the Moon
 Emma        | Watson        | Beauty and the Beast
 Emma        | Watson        | Harry Potter and the Sorcerer's Stone
 Emma        | Watson        | Harry Potter and the Half-Blood Prince
 Emma        | Watson        | Harry Potter and the Order of the Phoenix
 Emma        | Watson        | Harry Potter and the Goblet of Fire
 Emma        | Watson        | Harry Potter and the Chamber of Secrets
 Emma        | Watson        | Harry Potter and the Deathly Hallows: Part 2
 Emma        | Watson        | Harry Potter and the Deathly Hallows: Part 1
 Daniel      | Radcliffe     | Harry Potter and the Deathly Hallows: Part 2
 Daniel      | Radcliffe     | Harry Potter and the Sorcerer's Stone
 Daniel      | Radcliffe     | Harry Potter and the Half-Blood Prince
...... again for space and sanity saving purposes
 Zoe         | Saldana       | Avatar
 Zoe         | Saldana       | Guardians of the Galaxy Vol. 2
 Zoe         | Saldana       | Guardians of the Galaxy
 Zoe         | Saldana       | Pirates of the Caribbean: Curse of the Black Pearl
 Chris       | Pratt         | Jurassic World
 Chris       | Pratt         | Star Wars
 Chris       | Pratt         | Guardians of the Galaxy Vol. 2
 Chris       | Pratt         | Guardians of the Galaxy
 Anne        | Hathaway      | The Dark Knight Rises
 Anne        | Hathaway      | Alice in Wonderland
 Ellen       | DeGeneres     | Finding Dory
 Ellen       | DeGeneres     | Finding Nemo
 Robert      | Downey Jr.    | Marvel's The Avengers
 Robert      | Downey Jr.    | Avengers: Age of Ultron
 Robert      | Downey Jr.    | Iron Man 3
 Robert      | Downey Jr.    | Captain America: Civil War
 Robert      | Downey Jr.    | Spider-Man: Homecoming
 Robert      | Downey Jr.    | Iron Man
 Robert      | Downey Jr.    | Iron Man 2
(125 rows)

9.  The first and last names of every star who has been in a G-rated movie. The first and last name should appear only once for each star, even if they are in several G-rated movies. *IMPORTANT NOTE*: it's possible that there can be two *different* actors with the same name, so make sure your solution accounts for that.

\```

SELECT DISTINCT s.first_name, s.last_name
FROM stars s
JOIN roles r ON s.id = r.star_id
JOIN movies m ON r.movie_id = m.id
WHERE m.rating = 'G';

\```

 first_name | last_name 
------------+-----------
 Ellen      | DeGeneres
 Michael    | Keaton
 Tom        | Hanks
(3 rows)

10. The first and last names of every star along with the number
    of movies they have been in, in descending order by the number of movies. (Similar to #9, make sure
    that two different actors with the same name are considered separately).

\```

SELECT s.first_name, s.last_name, COUNT(r.movie_id) AS movie_count
FROM stars s
JOIN roles r ON s.id = r.star_id
GROUP BY s.id
ORDER BY movie_count DESC;

\```
 first_name  |   last_name   | movie_count 
-------------+---------------+-------------
 Samuel      | Jackson       |           9
 Emma        | Watson        |           8
 Daniel      | Radcliffe     |           7
 Robert      | Downey Jr.    |           7
 Scarlett    | Johansson     |           6
 Harrison    | Ford          |           5
 Idris       | Elba          |           5
 Helena      | Carter        |           5
 Ian         | McKellen      |           5
 Bradley     | Cooper        |           4
 Jennifer    | Lawrence      |           4
 Keira       | Knightley     |           4
 Zoe         | Saldana       |           4
 Chris       | Pratt         |           4
 Jenny       | Slate         |           3
 Tom         | Hanks         |           3
 Cameron     | Diaz          |           3
 Joseph      | Gordon-Levitt |           3
 Michael     | Keaton        |           3
 Natalie     | Portman       |           3
 Morgan      | Freeman       |           2
 Daniel      | Craig         |           2
 Kristen     | Wiig          |           2
 Anne        | Hathaway      |           2
 Octavia     | Spencer       |           2
 Amy         | Poehler       |           2
 Will        | Smith         |           2
 Chadwick    | Boseman       |           2
 Dwayne      | Johnson       |           2
 Ellen       | DeGeneres     |           2
 Viola       | Davis         |           1
 Kathy       | Bates         |           1
 Kate        | Winslet       |           1
 Emma        | Stone         |           1
 Maya        | Rudolph       |           1
 Danai       | Gurira        |           1
 Keanu       | Reeves        |           1
 Angela      | Bassett       |           1
 Frances     | McDormand     |           1
 Christopher | Plummer       |           1
(40 rows)

### The rest of these are bonuses

11. The title of every movie along with the number of stars in
    that movie, in descending order by the number of stars.

\```

SELECT m.title, COUNT(r.star_id) AS star_count
FROM movies m
JOIN roles r ON m.id = r.movie_id
GROUP BY m.id
ORDER BY star_count DESC;

\```
                     title                        | star_count 
----------------------------------------------------+------------
 Avengers: Age of Ultron                            |          4
 Black Panther                                      |          3
 The Dark Knight Rises                              |          3
 Iron Man 2                                         |          3
 Star Wars: Episode I - The Phantom Menace          |          3
 Captain America: Civil War                         |          3
 Harry Potter and the Half-Blood Prince             |          3
 Harry Potter and the Order of the Phoenix          |          3
 Guardians of the Galaxy Vol. 2                     |          3
 Zootopia                                           |          3
 Harry Potter and the Deathly Hallows: Part 1       |          3
 Marvel's The Avengers                              |          3
 Guardians of the Galaxy                            |          3
 Shrek the Third                                    |          3
 Harry Potter and the Deathly Hallows: Part 2       |          3
 Harry Potter and the Sorcerer's Stone              |          2
...... again for space and sanity saving purposes
 The Matrix Reloaded                                |          1
 Toy Story 2                                        |          1
 Independence Day                                   |          1
 Minions                                            |          1
 Avatar                                             |          1
 Shrek 2                                            |          1
 Indiana Jones & Kingdom of the Crystal Skull       |          1
 The Amazing Spider-Man                             |          1
 Transformers: Dark of the Moon                     |          1
 Inside Out                                         |          1
 The Hunger Games: Mockingjay - Part 2              |          1
 The Lord of the Rings: The Two Towers              |          1
 Furious 7                                          |          1
 The Incredibles                                    |          1
 The Secret Life of Pets                            |          1
 Skyfall                                            |          1
 Spider-Man                                         |          1
 The Hunger Games: Mockingjay - Part 1              |          1
 The Hobbit: An Unexpected Journey                  |          1
 Up                                                 |          1
 Pirates of the Caribbean: Dead Man's Chest         |          1
(76 rows)

12. The first name, last name, and average runtime of the five
    stars whose movies have the longest average.

\```

SELECT s.first_name, s.last_name, AVG(m.runtime) AS avg_runtime
FROM stars s
JOIN roles r ON s.id = r.star_id
JOIN movies m ON r.movie_id = m.id
GROUP BY s.id
ORDER BY avg_runtime DESC
LIMIT 5;

\```

 first_name |   last_name   |     avg_runtime      
------------+---------------+----------------------
 Kate       | Winslet       | 194.0000000000000000
 Kathy      | Bates         | 194.0000000000000000
 Ian        | McKellen      | 170.4000000000000000
 Morgan     | Freeman       | 157.5000000000000000
 Joseph     | Gordon-Levitt | 154.6666666666666667
(5 rows)

13. The first name, last name, and average runtime of the five
    stars whose movies have the longest average, among stars who have more than one movie in the database.

\```

SELECT s.first_name, s.last_name, AVG(m.runtime) AS avg_runtime
FROM stars s
JOIN roles r ON s.id = r.star_id
JOIN movies m ON r.movie_id = m.id
GROUP BY s.id
HAVING COUNT(m.id) > 1
ORDER BY avg_runtime DESC
LIMIT 5;

\```

 first_name |   last_name   |     avg_runtime      
------------+---------------+----------------------
 Ian        | McKellen      | 170.4000000000000000
 Morgan     | Freeman       | 157.5000000000000000
 Joseph     | Gordon-Levitt | 154.6666666666666667
 Daniel     | Radcliffe     | 148.4285714285714286
 Keira      | Knightley     | 146.7500000000000000
(5 rows)

14. The titles of all movies that don't feature any stars in our
    database.

\```

SELECT m.title
FROM movies m
LEFT JOIN roles r ON m.id = r.movie_id
WHERE r.movie_id IS NULL;

\```

                      title                       
--------------------------------------------------
 Rogue One: A Star Wars Story
 The Lion King
 Deadpool
 Home Alone
 Transformers: Revenge of the Fallen
 Transformers
 E. T.: The Extra-Terrestrial
 Meet the Fockers
 Wonder Woman
 Batman v Superman: Dawn of Justice
 It
 Man of Steel
 The Twilight Saga: Breaking Dawn Part 2
 Spider-Man 2
 Spider-Man 3
 The Passion of the Christ
 The Twilight Saga: Eclipse
 The Twilight Saga: New Moon
 The Twilight Saga: Breaking Dawn Part 1
 Frozen
 The Sixth Sense
 The Chronicles of Narnia: Lion, Witch & Wardrobe
 Monsters, Inc.
 Monsters University
 Gravity
(25 rows)

15. The first and last names of all stars that don't appear in any movies in our database.

\```

SELECT s.first_name, s.last_name
FROM stars s
LEFT JOIN roles r ON s.id = r.star_id
WHERE r.movie_id IS NULL;

\```

 first_name | last_name 
------------+-----------
 Wesley     | Snipes
 Sean       | Connery
 Jamie      | Foxx
 Jim        | Carrey
 Angelina   | Jolie
 Mila       | Kunis
 Charles    | Chaplin
 Charlize   | Theron
 Halle      | Berry
 Chris      | Rock
(10 rows)

16. The first names, last names, and titles corresponding to every
    role in the database, along with every movie title that doesn't have a star, and the first and last names of every star not in a movie.
-- 1. Stars in movies
UNION
-- 2. Movies with no stars
UNION
-- 3. Stars not in any movie

\``` sql

SELECT s.first_name, s.last_name, m.title
FROM stars s
JOIN roles r ON s.id = r.star_id
JOIN movies m ON r.movie_id = m.id

UNION

SELECT NULL AS first_name, NULL AS last_name, m.title
FROM movies m
LEFT JOIN roles r ON m.id = r.movie_id
WHERE r.movie_id IS NULL

UNION

SELECT s.first_name, s.last_name, NULL AS title
FROM stars s
LEFT JOIN roles r ON s.id = r.star_id
WHERE r.movie_id IS NULL;

\```

 first_name  |   last_name   |                       title                        
-------------+---------------+----------------------------------------------------
 Tom         | Hanks         | Toy Story 2
 Keira       | Knightley     | Pirates of the Caribbean: At World's End
 Chris       | Rock          | 
 Samuel      | Jackson       | Iron Man
 Harrison    | Ford          | Return of the Jedi
             |               | Spider-Man 2
 Zoe         | Saldana       | Pirates of the Caribbean: Curse of the Black Pearl
 Daniel      | Craig         | Skyfall
             |               | Meet the Fockers
 Helena      | Carter        | Harry Potter and the Order of the Phoenix
 Octavia     | Spencer       | Zootopia
 Natalie     | Portman       | Star Wars: Episode III - Revenge of the Sith
 Chris       | Pratt         | Guardians of the Galaxy Vol. 2
 Ian         | McKellen      | Beauty and the Beast
 Keira       | Knightley     | Star Wars: Episode I - The Phantom Menace
             |               | The Lion King
 Michael     | Keaton        | Toy Story 3
 Daniel      | Radcliffe     | Harry Potter and the Order of the Phoenix
             |               | Spider-Man 3
 Daniel      | Radcliffe     | Harry Potter and the Half-Blood Prince
 Jenny       | Slate         | Zootopia
             |               | Monsters University
 Charles     | Chaplin       | 
 Robert      | Downey Jr.    | Marvel's The Avengers
...... again for space and sanity saving purposes
Ellen       | DeGeneres     | Finding Dory
 Emma        | Watson        | Harry Potter and the Deathly Hallows: Part 2
 Chris       | Pratt         | Jurassic World
             |               | The Twilight Saga: Breaking Dawn Part 2
             |               | Rogue One: A Star Wars Story
 Idris       | Elba          | Thor: Ragnarok
 Wesley      | Snipes        | 
 Robert      | Downey Jr.    | Iron Man 3
 Harrison    | Ford          | Star Wars
 Danai       | Gurira        | Black Panther
 Dwayne      | Johnson       | Jumanji: Welcome to the Jungle
 Samuel      | Jackson       | Marvel's The Avengers
 Cameron     | Diaz          | Shrek
 Halle       | Berry         | 
             |               | The Sixth Sense
 Jenny       | Slate         | Despicable Me 3
 Harrison    | Ford          | Star Wars: The Force Awakens
 Harrison    | Ford          | Indiana Jones & Kingdom of the Crystal Skull
 Jennifer    | Lawrence      | The Hunger Games
 Emma        | Watson        | Harry Potter and the Half-Blood Prince
 Jennifer    | Lawrence      | The Hunger Games: Mockingjay - Part 1
 Chris       | Pratt         | Star Wars
 Viola       | Davis         | Suicide Squad
 Ian         | McKellen      | The Lord of the Rings: Return of the King
 Cameron     | Diaz          | Shrek the Third
 Emma        | Watson        | Harry Potter and the Sorcerer's Stone
             |               | E. T.: The Extra-Terrestrial
(160 rows)
