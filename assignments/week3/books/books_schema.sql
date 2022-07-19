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
  `book_id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(255) NOT NULL,
  `num_of_pages` INT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`book_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `books_schema`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `books_schema`.`users` ;

CREATE TABLE IF NOT EXISTS `books_schema`.`users` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `updated_at` DATETIME NOT NULL,
  `create_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`));


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
    REFERENCES `books_schema`.`users` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_books_books1`
    FOREIGN KEY (`book_id`)
    REFERENCES `books_schema`.`books` (`book_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

insert into users (user_id,name, updated_at)
values ('1','Jane Amsden', current_timestamp()), ('2','Emily Dixon', current_timestamp()), ('3','Theodore Dostoevsky', current_timestamp()), ('4','William Shapiro', current_timestamp()), ('5','Lao Xiu', current_timestamp());

insert into books (book_id, title)
values ('1','C Sharp'), ('2','Java'), ('3','Python'), ('4','PHP'), ('5','Ruby');

UPDATE books SET title ="C#" WHERE book_id='1';

Update users set name="Bill" where user_id='4';

update favorites set user_id=1 where book_id <=2;

update favorites set user_id=2 where book_id <4;

update favorites set user_id=3 where book_id <5;

update favorites set user_id=4 where book_id <=5;

select user_id
from favorites
where book_id= 3;

delete from favorites
where book_id = 3 and user_id = 1;

insert into favorites (book_id, user_id)
values('2','5');

select book_id
from favorites
where user_id = 3;

select user_id
from favorites
where book_id = 5;