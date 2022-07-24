-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema friends_schema
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `friends_schema` ;

-- -----------------------------------------------------
-- Schema friends_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `friends_schema` DEFAULT CHARACTER SET utf8 ;
USE `friends_schema` ;

-- -----------------------------------------------------
-- Table `friends_schema`.`friendships`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `friends_schema`.`friendships` ;

CREATE TABLE IF NOT EXISTS `friends_schema`.`friendships` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `user_id` INT NULL DEFAULT 0,
  `friend_id` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_friendships_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_friendships_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `friends_schema`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `friends_schema`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `friends_schema`.`users` ;

CREATE TABLE IF NOT EXISTS `friends_schema`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(100) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `friendships_id` INT NOT NULL Default 0,
  PRIMARY KEY (`id`),
  INDEX `fk_users_friendships_idx` (`friendships_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_friendships`
    FOREIGN KEY (`friendships_id`)
    REFERENCES `friends_schema`.`friendships` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
SET SQL_SAFE_UPDATES = 0;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


INSERT INTO users (first_name, last_name)
VALUES ("Dolly","Madison"),("Dennis","Rodman"),("George","Clooney"),("Katherine","Heigl"),("Johnny","Depp"),("Amber","Madison");

insert into friendships (friend_id,friendships.user_id)
values(1,2), (2, 5), (3,6), (4,6), (5,3), (6,5);

SELECT users.first_name, users.last_name, users2.first_name as friend_first_name, users2.last_name as friends_last_name
FROM users
JOIN friendships on users.id = friendships.user_id
left join users as users2 on users2.id = friendships.id
order by users.last_name ASC;

select users2.first_name as first_name, users2.last_name as last_name, users.first_name as friends_name
from users
join friendships on users.id = friendships.users_id
left join users as users2 on users2.id = friendships.id
where users.id = 1
order by friendships.id;

select count(*) as friend_num from friendships;

select users.first_name, users.last_name, count(friendships.id) from friendships
left join users on  users.friendships_id = friendships.id
group by users.id
order by users.last_name DESC;
