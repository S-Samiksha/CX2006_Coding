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
-- Table structure for table `accounts`
--

DROP TABLE IF EXISTS `accounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts` (
  `AccountID` int NOT NULL AUTO_INCREMENT,
  `Email` varchar(255) NOT NULL,
  `Password` varchar(255) NOT NULL,
  PRIMARY KEY (`AccountID`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts`
--

LOCK TABLES `accounts` WRITE;
/*!40000 ALTER TABLE `accounts` DISABLE KEYS */;
INSERT INTO `accounts` VALUES (1,'davidlee@gmail.com','password123'),(2,'JervisTan@gmail.com','Wat4ermelon'),(3,'YapZiYi98@yahoo.com','Sg2021!!'),(4,'DingYongZu34@hotmail.com','dingygzu@123'),(5,'FongYi.Ming_2021@yahoo.com','YhqD@Sc'),(6,'AngDeKang65@reddit.com','AngDepassword!'),(7,'Cheong_Seng_Hee98@gmail.com','187@passwordsg'),(8,'Woo-ChengHa@yahoo.com','ChengChengHa_901'),(9,'nicky456@outlook.com','lOSOc'),(10,'FungFungMingDe@gmail.com','America@54'),(11,'Chong12KaiMing@gmail.com','KaiMingSingapore!'),(12,'Leong_JunRui71@hotmail.com','YoloCarpeDiem@'),(13,'kyla.howell@gmail.com','BMUI$!'),(14,'JonathanJunYi@yahoo.com','0Qdj@delhi'),(15,'kling.rylan@gmail.com','pascode#76'),(16,'jferry@yahoo.com','Ferry53!'),(17,'gopal_190@gmail.com','doggos@qw'),(18,'LiJunDe12@outlook.com','%mangos123'),(19,'ChangJiaDe2309@gmail.com','Qwerty67'),(20,'FangJiaJian39sg@gmail.com','Roomiepasscode3'),(21,'TeohZhiEn46@yahoo.com','Hiiamteoh'),(22,'23KohRuiLin@gmail.com','Kilmanoh'),(23,'Zeng-ZhiEn2021@yahoo.com','34NNC'),(24,'ChiaKaiLing-90@outlook.com','Chia783'),(25,'ZhongKaiWen123@hotmail.com','Wen1234'),(26,'Shen_Jia_Min908@hotmail.com','Min890pass'),(27,'LiuJia-Qi123@yahoo.com','NUI90736'),(28,'Daisy_JiaWen901@gmail.com','GLKE@890'),(29,'TangXinEn123@gmail.com','MgMf@6727'),(30,'carol.kub@hotmail.com','MKUBcarol@77');
/*!40000 ALTER TABLE `accounts` ENABLE KEYS */;
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
