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
  `created_at` DATETIME NOT NULL,
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


Insert into dojos(dojo_id, dojo_name, created_at)
values ('1', 'Shotokan School', current_timestamp()),('2', 'Shotokan School', current_timestamp()),('3','Shotokan School', current_timestamp());

delete from dojos where dojo_name = 'Shotokan School';

Insert into dojos (dojo_id, dojo_name, created_at)
values ('1', 'Rumble Dojo', current_timestamp()), ('2','Rumble Dojo', current_timestamp()), ('3', 'Rumble Dojo',current_timestamp());

insert into ninjas (id, first_name, last_name, dojo_id, age)
values 
	(1, 'Rachel', 'Sanchez', '1','28'),
	(2, 'Monty', 'Python', '1', '53'),
    (3, 'James', 'Bond', '1', '37');

Select first_name, last_name
from ninjas
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




