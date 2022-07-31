-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema users_schema
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `users_schema` ;

-- -----------------------------------------------------
-- Schema users_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `users_schema` DEFAULT CHARACTER SET utf8 ;
USE `users_schema` ;

-- -----------------------------------------------------
-- Table `users_schema`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `users_schema`.`users` ;

CREATE TABLE IF NOT EXISTS `users_schema`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `users_schema`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `users_schema`.`users` ;

CREATE TABLE IF NOT EXISTS `users_schema`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

insert into users (first_name, last_name, email)
values ('Monty', 'Python', 'monty.python@gmail.com'), ('Harry','Potter', 'hpotter@gmail.com'), ('Hermione', 'Granger', 'hgranger@hotmail.com');

select *
from users;

select * from users
where email='hgranger@hotmail.com';

select * from users
where id = 3;

update users set last_name = 'Pancakes'
where users.id=3;

delete from users
where user.id=2;

select * from users
order by first_name ASC;

select * 
from users
order by first_name DESC;