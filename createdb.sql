-- creates clean database for weerstation
DROP DATABASE IF EXISTS `alert`;
CREATE DATABASE `alert`;
USE `alert`;
CREATE TABLE `message` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `prio` VARCHAR(45),
  `datetime` VARCHAR(45),
  `message` VARCHAR(45),
  `vehicle` VARCHAR(45),
  PRIMARY KEY (`id`)
); 
