-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: cz2006
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `profile`
--

DROP TABLE IF EXISTS `profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `profile` (
  `Age` int DEFAULT NULL,
  `Gender` varchar(45) DEFAULT NULL,
  `Occupation` varchar(45) DEFAULT NULL,
  `Ethnicity` varchar(45) DEFAULT NULL,
  `profileImgPath` varchar(255) DEFAULT NULL,
  `Name` varchar(255) DEFAULT NULL,
  `r_Gender` varchar(255) DEFAULT NULL,
  `r_Age` int DEFAULT NULL,
  `r_Skip` int DEFAULT NULL,
  `r_Occupation` varchar(45) DEFAULT NULL,
  `r_Enthnicity` varchar(45) DEFAULT NULL,
  `accounts_AccountID` int NOT NULL,
  PRIMARY KEY (`accounts_AccountID`),
  KEY `fk_profile_accounts_idx` (`accounts_AccountID`),
  CONSTRAINT `fk_profile_accounts` FOREIGN KEY (`accounts_AccountID`) REFERENCES `accounts` (`AccountID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profile`
--

LOCK TABLES `profile` WRITE;
/*!40000 ALTER TABLE `profile` DISABLE KEYS */;
INSERT INTO `profile` VALUES (23,'Male','Student','Chinese','../static/images/A1.png','David Lee Hao Wen','Male',23,7,'Student','Chinese',1),(22,'Male','Student','Chinese','../static/images/A2.png','Jervis Tan Jun Hong','Male',22,0,'Any','Any',2),(25,'Female','Accountant','Indian','../static/images/A3.png','Meera','Female',25,0,'Any','Any',3),(26,'Male','Nurse','Chinese','../static/images/A4.png','Zu Ding Yong','Male',26,0,'Any','Any',4),(24,'Male','Student','Chinese','../static/images/A5.png','Fong Yi Ming Jason','Male',24,0,'Student','Chinese',5),(27,'Male','Teacher','Chinese','../static/images/A6.png','Ang De Kang ','Male',27,0,'Any','Chinese',6),(23,'Male','Student','Chinese','../static/images/A7.png','Cheong Seng Hee','Male',23,0,'Student','Any',7),(21,'Male','Student','Chinese','../static/images/A8.png','Woo Cheng Ha','Male',21,0,'Any','Chinese',8),(22,'Male','Student','Chinese','../static/images/A9.png','Guo Yong Hui','Male',22,0,'Student','Any',9),(28,'Male','Sales Associate','European','../static/images/A10.png','Harry John','Male',28,0,'Any','Any',10),(25,'Male','Marketing Manager','Chinese','../static/images/A11.png','Chong Kai Ming','Male',25,0,'Any','Chinese',11),(24,'Male','Student','Chinese','../static/images/A12.png','Leong Jun Rui ','Male',24,0,'Student','Any',12),(22,'Female','Student','British','../static/images/A13.png','Kyla Howell','Female',22,0,'Student','Any',13),(21,'Male','Student','Chinese','../static/images/A14.png','Jonathan Jun Yi','Male',21,0,'Any','Any',14),(24,'Female','Content Creator','British','../static/images/A15.png','Kling Ming Rylan','Female',24,0,'Any','Any',15),(23,'Male','Student','indian','../static/images/A16.png','ramu gopal','Male',22,0,'Student','any',16),(25,'Male','Software Developer','Chinese','../static/images/A17.png','Chang Jia De','Male',26,0,'Any','Chinese',17),(24,'Male','Student','Chinese','../static/images/A18.png','Li Jun De Anthony','Male',25,0,'Student','Chinese',18),(27,'Male','Product Officer','Chinese','../static/images/A19.png','Chang Jia Deng Xavier','Male',26,0,'Any','Any',19),(22,'Male','Student','Chinese','../static/images/A20.png','Fang Jia Jian','Male',22,0,'Any','Any',20),(23,'Male','Student','Chinese','../static/images/A21.png','Teoh Zhi En','Male',23,0,'Student','Any',21),(25,'Female','Biologist','Chinese','../static/images/A22.png','Koh Rui Ling Jessica','Female',25,0,'Any','Chinese',22),(26,'Male','Chemical Engineer','Chinese','../static/images/A23.png','Zeng Zhi En Timothy','Male',26,0,'Any','Chinese',23),(22,'Female','Student','Chinese','../static/images/A24.png','Chia Kai Ling','Female',21,0,'Student','Any',24),(21,'Female','Student','Chinese','../static/images/A25.png','Zhong Kai Wen','Female',20,0,'Student','Chinese',25),(20,'Female','Student','Chinese','../static/images/A26.png','Shen Jia Min','Female',19,0,'Student','Chinese',26),(20,'Female','Student','Chinese','../static/images/A27.png','Liu Jia Qi Rachel','Female',20,0,'Any','Any',27),(24,'Female','Pharmacist','Chinese','../static/images/A28.png','Tan Jia Wen Daisy','Female',24,0,'Any','Chinese',28),(23,'Female','Student','Chinese','../static/images/A29.png','Tang Xin En Jasmine','Female',23,0,'Student','Chinese',29),(22,'Female','Student','Chinese','../static/images/A30.png','Carol Keng Hui Wen','Female',22,13,'Student','Chinese',30);
/*!40000 ALTER TABLE `profile` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-29 13:35:59
