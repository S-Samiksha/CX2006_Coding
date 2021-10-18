profileImgPath-- MySQL Script generated by MySQL Workbench
-- Mon Oct 11 19:23:23 2021
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema cz2006
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema cz2006
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `cz2006` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `cz2006` ;

-- -----------------------------------------------------
-- Table `cz2006`.`accounts`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cz2006`.`accounts` ;

CREATE TABLE IF NOT EXISTS `cz2006`.`accounts` (
  `AccountID` INT NOT NULL AUTO_INCREMENT,
  `Email` VARCHAR(255) NOT NULL,
  `Password` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`AccountID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `cz2006`.`chat_data`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cz2006`.`chat_data` ;

CREATE TABLE IF NOT EXISTS `cz2006`.`chat_data` (
  `RoomateID` INT NOT NULL,
  `ChatHistoryFilePath` VARCHAR(255) NOT NULL,
  `accounts_AccountID` INT NOT NULL,
  PRIMARY KEY (`accounts_AccountID`),
  CONSTRAINT `fk_chat_data_accounts1`
    FOREIGN KEY (`accounts_AccountID`)
    REFERENCES `cz2006`.`accounts` (`AccountID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `cz2006`.`profile`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cz2006`.`profile` ;

CREATE TABLE IF NOT EXISTS `cz2006`.`profile` (
  `Age` INT NULL DEFAULT NULL,
  `Gender` VARCHAR(45) NULL DEFAULT NULL,
  `Occupation` VARCHAR(45) NULL DEFAULT NULL,
  `Ethnicity` VARCHAR(45) NULL DEFAULT NULL,
  `profileImgPath` VARCHAR(255) NULL DEFAULT NULL,
  `Name` VARCHAR(255) NULL DEFAULT NULL,
  `r_Gender` VARCHAR(255) NULL DEFAULT NULL,
  `r_Occupation` VARCHAR(45) NULL DEFAULT NULL,
  `r_Enthnicity` VARCHAR(45) NULL DEFAULT NULL,
  `accounts_AccountID` INT NOT NULL,
  PRIMARY KEY (`accounts_AccountID`),
  INDEX `fk_profile_accounts_idx` (`accounts_AccountID` ASC) VISIBLE,
  CONSTRAINT `fk_profile_accounts`
    FOREIGN KEY (`accounts_AccountID`)
    REFERENCES `cz2006`.`accounts` (`AccountID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `cz2006`.`roommate_language`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cz2006`.`roommate_language` ;

CREATE TABLE IF NOT EXISTS `cz2006`.`roommate_language` (
  `Language` VARCHAR(255) NOT NULL,
  `accounts_AccountID` INT NOT NULL,
  PRIMARY KEY (`accounts_AccountID`),
  CONSTRAINT `fk_roommate_language_accounts1`
    FOREIGN KEY (`accounts_AccountID`)
    REFERENCES `cz2006`.`accounts` (`AccountID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `cz2006`.`user_language`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cz2006`.`user_language` ;

CREATE TABLE IF NOT EXISTS `cz2006`.`user_language` (
  `Language` VARCHAR(255) NOT NULL,
  `accounts_AccountID` INT NOT NULL,
  PRIMARY KEY (`accounts_AccountID`),
  CONSTRAINT `fk_user_language_accounts1`
    FOREIGN KEY (`accounts_AccountID`)
    REFERENCES `cz2006`.`accounts` (`AccountID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;