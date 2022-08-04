-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema dojos_and_ninjas_schema
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `dojos_and_ninjas_schema` ;

-- -----------------------------------------------------
-- Schema dojos_and_ninjas_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dojos_and_ninjas_schema` DEFAULT CHARACTER SET utf8 ;
USE `dojos_and_ninjas_schema` ;

-- -----------------------------------------------------
-- Table `dojos_and_ninjas_schema`.`dojos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dojos_and_ninjas_schema`.`dojos` ;

CREATE TABLE IF NOT EXISTS `dojos_and_ninjas_schema`.`dojos` (
  `dojo_id` INT NOT NULL AUTO_INCREMENT,
  `dojo_name` VARCHAR(100) NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` VARCHAR(45) NULL,
  PRIMARY KEY (`dojo_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dojos_and_ninjas_schema`.`ninjas`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dojos_and_ninjas_schema`.`ninjas` ;

CREATE TABLE IF NOT EXISTS `dojos_and_ninjas_schema`.`ninjas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `age` INT NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `dojo_id` INT NOT NULL,
  PRIMARY KEY (`id`, `dojo_id`),
  INDEX `fk_ninjas_dojos_idx` (`dojo_id` ASC) VISIBLE,
  CONSTRAINT `fk_ninjas_dojos`
    FOREIGN KEY (`dojo_id`)
    REFERENCES `dojos_and_ninjas_schema`.`dojos` (`dojo_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
SET SQL_SAFE_UPDATES = 0;


Insert into dojos(dojo_name)
values ('Shotokan School'),('Dojo Master'),('Dojo Online');

delete from dojos where dojo_name = 'Shotokan School';

Insert into dojos (dojo_name)
values ('Rumble Dojo');

insert into ninjas (first_name, last_name, dojo_id, age)
values ('Rachel', 'Sanchez', '1','28'),('Monty', 'Python', '1', '53'),('James', 'Bond', '1', '37');

insert into ninjas (first_name, last_name, dojo_id, age)
values (4, 'Harry', 'Potter', '28'),(5, 'Hermione', 'Granger','31'),(6, 'Ron', 'Weasley', 2, '30');

insert into ninjas (first_name, last_name, dojo_id, age)
values (7, 'Sabrina', 'Spellman', 3, '16'), (8, 'Kal', 'Drogo', 3, '33'), (9, 'Doctor', 'Strange', 3, '35');

Select * from dojos
left join ninjas on ninjas.id = dojos.dojo_id
where dojo_id = 1;

select first_name, last_name
from ninjas
where dojo_id = 2;

select first_name, last_name
from ninjas
where dojo_id=3;

select id, first_name, last_name
from ninjas
where id = 9;

select * from dojos
left join ninjas on ninjas.id = dojos.dojo_id
	where dojos.dojo_id = (select id from dojos order by id ASC limit 1);


