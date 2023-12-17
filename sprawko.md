# Bazy danych - System zarządzania szkoleniami
Krzysztof Śliwiński
Hubert Kasprzycki
Artur Dwornik


### Funkcje realizowane przez system:
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

### Diagram bazy danych:


![diagram](./diagram.svg)

### Przykładowe dane testowe:
* Tabela `students`:\
`Edward,Harris,EdwardHarris@gmail.com,6130b6ba25b29c18ba24`
* Tabela `lecturers`:\
`Lisa,Sanders,mgr.,LisaSanders@gmail.com,af4acfa79131e063ceac`
* Tabela `employees`:\
`Robert,Williams,1,RobertWilliams@gmail.com,d58e44aff86b392efb18`
* Tabela `roles`:\
`accountant`
* Tabela `lecturers`:\
`Larry,Hooper,dr.,LarryHooper@gmail.com,9888a64ed172993c911a`
* Tabela `lessons`:\
`1,1,analysising lesson,analysising lesson description,2022-01-16,08:25:00,09:55:00,130.69,25,room 8`
* Tabela `materials`:\
`2,societying material,societying material material description,https://TheBestUni.com/materials/societying_material.avi`
* Tabela `attendance`:\
`21,1,1`
* Tabela `courses`:\
`1,howevering course,howevering course description,608.93,15`
* Tabela `studies`:\
`everyoneing study,everyoneing study description,1402.03,15,2023-03-25`
* Tabela `internships`:\
`8,1,Electronic Arts,Internship at Electronic Arts,2022-05-29`
* Tabela `shopping_carts`:\
`16,1`
* Tabela `lesson_items`:\
`1,15`
* Tabela `courses_items`:\
`26,4`
* Tabela `studies_items`:\
`29,1`
* Tabela `payments`:\
`1,2021-12-11,https://PayPal.com/payment/1091940562903259`
* Tabela `lesson_payments`:\
`16,15,1`
* Tabela `course_payments`:\
`1,4,26,1`
* Tabela `study_payments`:\
`4,1,29`

 naprawic 1 do wiele przy payments
 cena przy kursie ktory jest ze studiow - null
 jak kupione to brak mozliwosci edycji koszyka
 komentarz o tym ze zewnetrzna firma daje papier o ukonczeniu studiów
 koszyk to widok
 3 lata danych
 tłumacze

 ### Tabele
Employees
`
CREATE TABLE employees (
   employee_id int  NOT NULL,
   first_name varchar(20)  NOT NULL,
   last_name varchar(20)  NOT NULL,
   role_id int  NOT NULL,
   email varchar(30)  NOT NULL,
   password varchar(20)  NOT NULL,
   CONSTRAINT employees_pk PRIMARY KEY  (employee_id)
);
`
