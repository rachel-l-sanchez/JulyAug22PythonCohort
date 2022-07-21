-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema books_schema
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `books_schema` ;

-- -----------------------------------------------------
-- Schema books_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `books_schema` DEFAULT CHARACTER SET utf8 ;
USE `books_schema` ;

-- -----------------------------------------------------
-- Table `books_schema`.`books`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `books_schema`.`books` ;

CREATE TABLE IF NOT EXISTS `books_schema`.`books` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(255) NOT NULL,
  `num_of_pages` INT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `books_schema`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `books_schema`.`users` ;

CREATE TABLE IF NOT EXISTS `books_schema`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `updated_at` DATETIME NULL,
  `create_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`));


-- -----------------------------------------------------
-- Table `books_schema`.`favorites`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `books_schema`.`favorites` ;

CREATE TABLE IF NOT EXISTS `books_schema`.`favorites` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `book_id` INT NOT NULL,
  PRIMARY KEY (`user_id`),
  INDEX `fk_users_has_books_books1_idx` (`book_id` ASC) VISIBLE,
  INDEX `fk_users_has_books_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_books_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `books_schema`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_books_books1`
    FOREIGN KEY (`book_id`)
    REFERENCES `books_schema`.`books` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
SET SQL_SAFE_UPDATES = 0;

insert into users (name)
values ('Jane Amsden'), ('Emily Dixon'), ('Theodore Dostoevsky'), ('William Shapiro'), ('Lao Xiu');

insert into books (id, title, user_id)
values (1,'C Sharp', 1), (2,'Java', 3), (3,'Python',2), (4,'PHP',1), (5,'Ruby',5);

INSERT into favorites (user_id, book_id) 
VALUES (1, 1), (1, 2), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3), (3, 4), (4, 1), (4, 2), (4, 3), (4, 4), (4,5);

UPDATE books SET title ="C#" WHERE book_id=1;

Update users set name="Bill" where user_id=4;

update favorites set user_id=1 where book_id <=2;

update favorites set user_id=2 where book_id <4;

update favorites set user_id=3 where book_id <5;

update favorites set user_id=4 where book_id <=5;

select users.name from users
join favorites on users.id = user_id
left join books on favorites.book_id=books.id
where book_id= 3;

delete from favorites
where book_id = 3 and user_id = 1;

insert into favorites (book_id, user_id)
values(2,5);

select books.title from books
join favorites as faves on faves.book_id = books.id
where faves.user_id = 3;

select name from users
join favorites on users.id = favorites.user_id;

select * from books
where books.id = 4;
