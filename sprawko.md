# Bazy danych - System zarządzania szkoleniami
Krzysztof Śliwiński
Hubert Kasprzycki
Artur Dwornik


## Funkcje realizowane przez system:
1. Pracownicy zarządzający wydarzeniami:
    * Zarządzanie kursami, webinarami i studiami: 
        * Dodawanie nowych kursów, webinarów i studiów. 
        * Edycja istniejących wydarzeń (w tym harmonogramu). 
        * Usuwanie wydarzeń (zarówno bieżących, jak i archiwizowanych). 
    * Zarządzanie użytkownikami: 
        * Dodawanie nowych użytkowników do systemu. 
        * Edycja danych użytkowników. 
        * Dezaktywacja użytkowników. 
        * Wpisanie użytkownika na listę dłużników. 
    * Generowanie raportów: 
        * Raport ogólny z zapisanych osób na przyszłe wydarzenia. 
        * Raport frekwencji na zakończonych wydarzeniach. 
        * Lista obecności dla każdego szkolenia. 
        * Raport bilokacji – lista osób zapisanych na kolidujące ze sobą wydarzenia. 

2. Pracownicy biurowi: 
    * Generowanie raportów: 
        * Raport finansowy - zestawienie przychodów z poszczególnych wydarzeń. 
        * Lista dłużników - sprawozdanie zalegających z płatnościami użytkowników. 
        * Raport ogólny z zapisanych osób na przyszłe wydarzenia. 
        * Raport frekwencji na zakończonych wydarzeniach. 
        * Lista obecności dla każdego szkolenia. 
        * Raport bilokacji – lista osób zapisanych na kolidujące ze sobą wydarzenia. 
	 
 3. Wykładowca: 
    * Edycja prowadzonych wydarzeń. 
    * Oznaczanie obecności: 
        * Oznaczanie obecności uczestników w trakcie spotkań. 
        * Modyfikowanie listy obecności (oznaczenie odrobienia zajęć w przypadku studiów) 
    * Dodawanie materiałów: 
        * Wykładowca może dodawać materiały do kursów, takie jak prezentacje, pliki do pobrania itp. 
 
4.  Uczestnik: 
    * Przeglądanie oferty: 
        * Przeglądanie dostępnych kursów, webinarów i studiów. 
        * Przeglądanie sylabusów studiów, 
    * Rejestracja i płatności: 
        * Rejestracja na wybrane wydarzenia. 
        * Dodawanie wydarzeń do koszyka. 
        * Generowanie linku do płatności. 
        * Uiszczenie opłat za uczestnictwo w wydarzeniach. 
    * Dostęp do nagrań: 
        * Dostęp do nagrań z różnych wydarzeń online. 
        * Przeglądanie dostępnych nagrań przez okres 30 dni. 
    * Przeglądanie danych: 
        * Uczestnik może przeglądać swoje płatności i historię uczestnictwa. 

## Diagram bazy danych:


![diagram](./diagram.svg)


 naprawic 1 do wiele przy payments
 cena przy kursie ktory jest ze studiow - null
 jak kupione to brak mozliwosci edycji koszyka
 komentarz o tym ze zewnetrzna firma daje papier o ukonczeniu studiów
 koszyk to widok
 3 lata danych
 tłumacze

## Tabele

### Pracownicy
``` sql
CREATE TABLE employees (
   employee_id int  NOT NULL IDENTITY(1, 1),
   first_name varchar(20)  NOT NULL,
   last_name varchar(20)  NOT NULL,
   role_id int  NOT NULL,
   email varchar(30)  NOT NULL,
   password varchar(20)  NOT NULL,
   CONSTRAINT employees_ak_1 UNIQUE (email),
   CONSTRAINT employees_pk PRIMARY KEY  (employee_id)
);

```
### Role pracowników
``` sql
CREATE TABLE roles (
   role_id int  NOT NULL IDENTITY(1,1),
   role_name varchar(20)  NOT NULL,
   CONSTRAINT roles_pk PRIMARY KEY  (role_id)
);
```

### Studenci
``` sql
CREATE TABLE students (
   student_id int  NOT NULL IDENTITY(1, 1),
   first_name varchar(20)  NOT NULL,
   last_name varchar(20)  NOT NULL,
   email varchar(30)  NOT NULL,
   password varchar(20)  NOT NULL,
   CONSTRAINT students_ak_1 UNIQUE (email),
   CONSTRAINT students_pk PRIMARY KEY  (student_id)
);
```

### Lista obecności
``` sql
CREATE TABLE attendance (
   lesson_id int  NOT NULL,
   student_id int  NOT NULL,
   status bit  NOT NULL DEFAULT 0,
   CONSTRAINT attendance_pk PRIMARY KEY  (lesson_id,student_id)
);
```

### Materiały do lekcji online
``` sql
CREATE TABLE materials (
   material_id int  NOT NULL IDENTITY(1, 1),
   lesson_id int  NOT NULL,
   name varchar(20)  NOT NULL,
   description varchar(max)  NOT NULL DEFAULT 'no description found',
   file_url varchar(100)  NOT NULL,
   CONSTRAINT materials_ak_1 UNIQUE (file_url),
   CONSTRAINT materials_pk PRIMARY KEY  (material_id)
);
```

### Wykładowcy
``` sql
CREATE TABLE lecturers (
   lecturer_id int  NOT NULL,
   first_name varchar(20)  NOT NULL,
   last_name varchar(20)  NOT NULL,
   email varchar(30)  NOT NULL,
   password varchar(20)  NOT NULL,
   title varchar(10)  NULL,
   CONSTRAINT lecturers_ak_1 UNIQUE (email),
   CONSTRAINT lecturers_pk PRIMARY KEY  (lecturer_id)
);
```

### Praktyki zawodowe
``` sql
CREATE TABLE internships (
   internship_id int  NOT NULL IDENTITY(1,1),
   student_id int  NOT NULL,
   study_id int  NOT NULL,
   company varchar(50)  NOT NULL,
   description varchar(max)  NOT NULL DEFAULT 'no description found',
   start_date date  NOT NULL,
   CONSTRAINT Internships_pk PRIMARY KEY  (internship_id)
);
```

### Lekcje (z kursów i studiów) i webinary
``` sql
CREATE TABLE lessons (
   lesson_id int  NOT NULL IDENTITY(1, 1),
   course_id int  NULL,
   lecturer_id int  NOT NULL,
   name varchar(30)  NOT NULL,
   description varchar(max)  NOT NULL DEFAULT 'no description found',
   date date  NOT NULL,
   start_time time  NOT NULL,
   end_time time  NOT NULL,
   price smallmoney  NULL,
   students_limit int  NULL,
   classroom varchar(10)  NOT NULL,
   translator_id int  NULL,
   CONSTRAINT data CHECK (start_time < end_time),
   CONSTRAINT students_limit CHECK (students_limit > 0),
   CONSTRAINT price CHECK (price > 0),
   CONSTRAINT lessons_pk PRIMARY KEY  (lesson_id)
);
```

### Kursy
``` sql
CREATE TABLE courses (
   course_id int  NOT NULL IDENTITY(1, 1),
   study_id int  NULL,
   name varchar(30)  NOT NULL,
   description varchar(max)  NOT NULL DEFAULT 'no description found',
   entry_price smallmoney  NULL,
   full_price smallmoney  NULL,
   students_limit int  NULL,
   CONSTRAINT entry_price CHECK (entry_price > 0),
   CONSTRAINT full_price CHECK (full_price > 0),
   CONSTRAINT students_limit CHECK (students_limit > 0),
   CONSTRAINT courses_pk PRIMARY KEY  (course_id)
);
```

### Studia
``` sql
CREATE TABLE studies (
   study_id int  NOT NULL IDENTITY(1, 1),
   name varchar(30)  NOT NULL,
   description varchar(max)  NOT NULL DEFAULT 'no description found',
   entry_fee int  NOT NULL,
   students_limit int  NOT NULL,
   exam_date datetime  NULL,
   employee_id int  NOT NULL,
   CONSTRAINT entry_fee CHECK (entry_fee > 0),
   CONSTRAINT students_limit CHECK (students_limit > 0),
   CONSTRAINT studies_pk PRIMARY KEY  (study_id)
);
```

### Płatności
``` sql
CREATE TABLE payments (
   payment_id int  NOT NULL IDENTITY(1,1),
   status bit  NOT NULL DEFAULT 0,
   date date  NOT NULL,
   payment_url varchar(100)  NOT NULL,
   CONSTRAINT payments_pk PRIMARY KEY  (payment_id)
);
```

### Płatności za lekcje
``` sql
CREATE TABLE lesson_payments (
   student_id int  NOT NULL,
   lesson_id int  NOT NULL,
   payment_id int  NOT NULL,
   CONSTRAINT lesson_payments_pk PRIMARY KEY  (student_id,lesson_id)
);
```

### Płatności za kursy
``` sql
CREATE TABLE course_payments (
   student_id int  NOT NULL,
   course_id int  NOT NULL,
   payment_id int  NOT NULL,
   is_full_price bit  NOT NULL DEFAULT 0,
   CONSTRAINT course_payments_pk PRIMARY KEY  (student_id,course_id)
);
```

### Płatności za studia
``` sql
CREATE TABLE study_payments (
   student_id int  NOT NULL,
   study_id int  NOT NULL,
   payment_id int  NOT NULL,
   CONSTRAINT study_payments_pk PRIMARY KEY  (student_id,study_id)
);
```
