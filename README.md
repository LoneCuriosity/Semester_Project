# Spring 2023 Semester Project
Date: 5/2023

**note**: Currently looking for a raspberry pi python script. The server and client code is available expect the raspberry pi python code.

## Screenshots
![App Screenshot](http://ramongarciajr.tech/Semester_Project.png)

## Lessons Learned

Throughout this project, I acquired several valuable lessons. Firstly, I learned how to effectively utilize Beeware, which proved to be a user-friendly and straightforward software/library. Beeware facilitated quick and seamless prototyping using Python and enabled deployment across various platforms. However, it should be noted that Beeware's community support is still in its early stages, resulting in limited tutorials and examples beyond the information provided on their official website.

Another important lesson was setting up an SQLite server. Having prior experience with SQLite, I appreciated its usefulness as a lightweight SQL server. It offered the advantage of easy installation without the added bulk of a typical SQL server while still allowing for the usage of SQL syntax.

Overall, this project provided me with valuable insights into different programming languages and how to effectively leverage them. It allowed me to expand my knowledge and skills, particularly in working with Beeware for rapid prototyping and SQLite for efficient data management.


## Optimizations

In terms of optimizations, one consideration I have is transitioning from Beeware to a more native solution. While Beeware serves as a convenient middleman between platforms, it introduces some bloatware that can increase the overall size of the application. By shifting to a native language like Java, we can eliminate much of this excess and improve the performance of the app, resulting in faster load times. However, one drawback to this change would be sacrificing the cross-platform compatibility that Beeware provides.

## Prerequisites
- Next.js app
- Beeware preconfigured on system.

## Run Locally

Clone the project

```bash
git clone https://github.com/LoneCuriosity/Semester_Project
```

Create a migration folder and copy 001-SemesterProject.sql into it.

```bash
Project Root > migration > 001-SemesterProject.sql
```

Copy Pins.js into the API directory within the project.

```bash
Project Root > pages > api > Pins.js
```

Copy mydb.sqlite and db-test.js into the project root directory.

```bash
Project Root > mydb.sqlite
Project Root > db-test.js
```

Install Sqlite and Sqlite3

```bash
npm i sqlite sqlite3
```

Run db-test.js to initialize sqlite database

```bash
node .\db-test.js
```

Copy semesterproject folder into Beeware directory.


## 🛠 Skills
Javascript, JSON, SQL


## Tech Stack

- JSON
- SQL
- Javascript
- Python

## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ramongarciajr.tech/)


## Authors

- [@LoneCursioty](https://www.github.com/LoneCursioty)

