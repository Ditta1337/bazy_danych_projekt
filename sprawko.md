# Bazy danych - System zarządzania szkoleniami
Krzysztof Śliwiński
Hubert Kasprzycki
Artur Dwornik


### 1. Funkcje realizowane przez system:
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

### 2. Diagram bazy danych:


![diagram](./diagram.svg)


nieuchwycone rzeczy:
* kilku prowadzacych moga prowadzic kusy,
* roznica w prica za miejsce dla osob ktore sa 'z zewnatrz'
* koszyk ogarniecie identyfikator platnosci i potwierdzenie platnosci
* lista dloznikow != odroczona platnosc
* kurs to set webinarow, studia to set kursów itd...

