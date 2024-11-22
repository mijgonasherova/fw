# Animal Accounting

Проект "Animal Accounting" предназначен для учета домашних и вьючных животных. 
Приложение позволяет добавлять информацию о животных, просматривать данные и организовывать учет различных пород.

## Функциональность

- **Добавление нового животного**: Пользователь может ввести имя, вид и дату рождения животного.
- **Просмотр информации о животных**: Можно получить информацию о любом животном, добавленном в систему.
- **Управление данными**: Возможна дальнейшая разработка, которая позволит редактировать и удалять записи о животных.

## Установка

1. Клонируйте репозиторий:
  
   git clone https://github.com/VartanShirinyan/animal_accounting.git
   cd animal_accounting


## Диаграмма животных

Для просмотра диаграммы необходимо его скачать и запустить с помощью приложения drawio.

# Работа в MySQL

## Создание базы данных в MySQL
CREATE DATABASE Друзья_человека;
USE Друзья_человека;

## Создание таблиц в БД
CREATE TABLE Домашние_Животные (
    id INT AUTO_INCREMENT PRIMARY KEY,
    имя VARCHAR(255),
    команда VARCHAR(255),
    дата_рождения DATE
);

CREATE TABLE Вьючные_Животные (
    id INT AUTO_INCREMENT PRIMARY KEY,
    имя VARCHAR(255),
    команда VARCHAR(255),
    дата_рождения DATE
);

## Заполнение таблиц данными
INSERT INTO Домашние_Животные (имя, команда, дата_рождения)
VALUES ('Шарик', 'Сидеть', '2021-01-01'),
       ('Мурка', 'Лежать', '2020-05-15');

INSERT INTO Вьючные_Животные (имя, команда, дата_рождения)
VALUES ('Лайма', 'Идти', '2018-03-10'),
       ('Камел', 'Бежать', '2019-06-21');

## Удаление верблюдов из таблицы
DELETE FROM Вьючные_Животные WHERE имя = 'Камилла';

## Создание таблицы "Молодые животные"
CREATE TABLE Молодые_Животные AS
SELECT *, TIMESTAMPDIFF(MONTH, дата_рождения, CURDATE()) AS возраст
FROM (
    SELECT * FROM Домашние_Животные
    UNION ALL
    SELECT * FROM Вьючные_Животные
) AS Все_Животные
WHERE TIMESTAMPDIFF(YEAR, дата_рождения, CURDATE()) > 1
AND TIMESTAMPDIFF(YEAR, дата_рождения, CURDATE()) < 3;

## Объединение всех таблиц
CREATE TABLE Все_Животные AS
SELECT * FROM Домашние_Животные
UNION ALL
SELECT * FROM Вьючные_Животные;