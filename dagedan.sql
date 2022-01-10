-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: dagedan
-- ------------------------------------------------------
-- Server version	8.0.22

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
-- Table structure for table `add_on_order_detail`
--

DROP TABLE IF EXISTS `add_on_order_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `add_on_order_detail` (
  `OrderId` int NOT NULL,
  `AddOnServiceId` int NOT NULL,
  `quantity` tinyint NOT NULL,
  `amount` decimal(7,2) NOT NULL,
  KEY `AddOnServiceId` (`AddOnServiceId`),
  KEY `OrderId` (`OrderId`),
  CONSTRAINT `add_on_order_detail_ibfk_2` FOREIGN KEY (`AddOnServiceId`) REFERENCES `add_on_services` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `add_on_order_detail`
--

LOCK TABLES `add_on_order_detail` WRITE;
/*!40000 ALTER TABLE `add_on_order_detail` DISABLE KEYS */;
/*!40000 ALTER TABLE `add_on_order_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `add_on_services`
--

DROP TABLE IF EXISTS `add_on_services`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `add_on_services` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(125) DEFAULT NULL,
  `price` decimal(6,2) DEFAULT NULL,
  `images` text,
  `descriptiont` text,
  `is_available` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `add_on_services`
--

LOCK TABLES `add_on_services` WRITE;
/*!40000 ALTER TABLE `add_on_services` DISABLE KEYS */;
INSERT INTO `add_on_services` VALUES (1,'排灣族風味晚餐 嘎麥小米粽套餐',150.00,NULL,'小米粽+小米酒，供應時間 17:00-19:00',1),(2,'多良部落 芙瀨實驗廚房 無菜單午餐',999.00,NULL,'四季時序料理：包含餐前酒，前菜，主食，副食，甜點，及飲品。\n時段：11:30 - 12:50及13:10 - 14:30。必須準時就位，共食餐桌統一上菜及說菜，也不提供退費及外帶。',1);
/*!40000 ALTER TABLE `add_on_services` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `booking`
--

DROP TABLE IF EXISTS `booking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `booking` (
  `Date` date NOT NULL,
  `RoomNo` varchar(10) NOT NULL,
  `OrderId` int NOT NULL,
  PRIMARY KEY (`Date`,`RoomNo`),
  KEY `OrderId` (`OrderId`),
  CONSTRAINT `booking_ibfk_1` FOREIGN KEY (`Date`) REFERENCES `calendar` (`date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booking`
--

LOCK TABLES `booking` WRITE;
/*!40000 ALTER TABLE `booking` DISABLE KEYS */;
INSERT INTO `booking` VALUES ('2022-01-05','d001',1641219478),('2022-01-06','d001',1641354360),('2022-01-17','d001',1641360258),('2022-01-10','d001',1641660585);
/*!40000 ALTER TABLE `booking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `calendar`
--

DROP TABLE IF EXISTS `calendar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `calendar` (
  `date` date NOT NULL,
  `weekday` varchar(3) NOT NULL,
  `is_holiday` tinyint(1) NOT NULL,
  `note` varchar(125) DEFAULT NULL,
  `is_closed` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `calendar`
--

LOCK TABLES `calendar` WRITE;
/*!40000 ALTER TABLE `calendar` DISABLE KEYS */;
INSERT INTO `calendar` VALUES ('2021-01-01','五',1,'開國紀念日',0),('2021-01-02','六',1,'',0),('2021-01-03','日',1,'',0),('2021-01-04','一',0,'',0),('2021-01-05','二',0,'',0),('2021-01-06','三',0,'',0),('2021-01-07','四',0,'',0),('2021-01-08','五',0,'',0),('2021-01-09','六',1,'',0),('2021-01-10','日',1,'',0),('2021-01-11','一',0,'',0),('2021-01-12','二',0,'',0),('2021-01-13','三',0,'',0),('2021-01-14','四',0,'',0),('2021-01-15','五',0,'',0),('2021-01-16','六',1,'',0),('2021-01-17','日',1,'',0),('2021-01-18','一',0,'',0),('2021-01-19','二',0,'',0),('2021-01-20','三',0,'',0),('2021-01-21','四',0,'',0),('2021-01-22','五',0,'',0),('2021-01-23','六',1,'',0),('2021-01-24','日',1,'',0),('2021-01-25','一',0,'',0),('2021-01-26','二',0,'',0),('2021-01-27','三',0,'',0),('2021-01-28','四',0,'',0),('2021-01-29','五',0,'',0),('2021-01-30','六',1,'',0),('2021-01-31','日',1,'',0),('2021-02-01','一',0,'',0),('2021-02-02','二',0,'',0),('2021-02-03','三',0,'',0),('2021-02-04','四',0,'',0),('2021-02-05','五',0,'',0),('2021-02-06','六',1,'',0),('2021-02-07','日',1,'',0),('2021-02-08','一',0,'',0),('2021-02-09','二',0,'',0),('2021-02-10','三',1,'調整放假',0),('2021-02-11','四',1,'農曆除夕',0),('2021-02-12','五',1,'春節',0),('2021-02-13','六',1,'春節',0),('2021-02-14','日',1,'春節',0),('2021-02-15','一',1,'補假',0),('2021-02-16','二',1,'補假',0),('2021-02-17','三',0,'',0),('2021-02-18','四',0,'',0),('2021-02-19','五',0,'',0),('2021-02-20','六',0,'補行上班',0),('2021-02-21','日',1,'',0),('2021-02-22','一',0,'',0),('2021-02-23','二',0,'',0),('2021-02-24','三',0,'',0),('2021-02-25','四',0,'',0),('2021-02-26','五',0,'',0),('2021-02-27','六',1,'',0),('2021-02-28','日',1,'和平紀念日',0),('2021-03-01','一',1,'補假',0),('2021-03-02','二',0,'',0),('2021-03-03','三',0,'',0),('2021-03-04','四',0,'',0),('2021-03-05','五',0,'',0),('2021-03-06','六',1,'',0),('2021-03-07','日',1,'',0),('2021-03-08','一',0,'',0),('2021-03-09','二',0,'',0),('2021-03-10','三',0,'',0),('2021-03-11','四',0,'',0),('2021-03-12','五',0,'',0),('2021-03-13','六',1,'',0),('2021-03-14','日',1,'',0),('2021-03-15','一',0,'',0),('2021-03-16','二',0,'',0),('2021-03-17','三',0,'',0),('2021-03-18','四',0,'',0),('2021-03-19','五',0,'',0),('2021-03-20','六',1,'',0),('2021-03-21','日',1,'',0),('2021-03-22','一',0,'',0),('2021-03-23','二',0,'',0),('2021-03-24','三',0,'',0),('2021-03-25','四',0,'',0),('2021-03-26','五',0,'',0),('2021-03-27','六',1,'',0),('2021-03-28','日',1,'',0),('2021-03-29','一',0,'',0),('2021-03-30','二',0,'',0),('2021-03-31','三',0,'',0),('2021-04-01','四',0,'',0),('2021-04-02','五',1,'補假',0),('2021-04-03','六',1,'',0),('2021-04-04','日',1,'兒童節及民族掃墓節',0),('2021-04-05','一',1,'補假',0),('2021-04-06','二',0,'',0),('2021-04-07','三',0,'',0),('2021-04-08','四',0,'',0),('2021-04-09','五',0,'',0),('2021-04-10','六',1,'',0),('2021-04-11','日',1,'',0),('2021-04-12','一',0,'',0),('2021-04-13','二',0,'',0),('2021-04-14','三',0,'',0),('2021-04-15','四',0,'',0),('2021-04-16','五',0,'',0),('2021-04-17','六',1,'',0),('2021-04-18','日',1,'',0),('2021-04-19','一',0,'',0),('2021-04-20','二',0,'',0),('2021-04-21','三',0,'',0),('2021-04-22','四',0,'',0),('2021-04-23','五',0,'',0),('2021-04-24','六',1,'',0),('2021-04-25','日',1,'',0),('2021-04-26','一',0,'',0),('2021-04-27','二',0,'',0),('2021-04-28','三',0,'',0),('2021-04-29','四',0,'',0),('2021-04-30','五',0,'',0),('2021-05-01','六',1,'',0),('2021-05-02','日',1,'',0),('2021-05-03','一',0,'',0),('2021-05-04','二',0,'',0),('2021-05-05','三',0,'',0),('2021-05-06','四',0,'',0),('2021-05-07','五',0,'',0),('2021-05-08','六',1,'',0),('2021-05-09','日',1,'',0),('2021-05-10','一',0,'',0),('2021-05-11','二',0,'',0),('2021-05-12','三',0,'',0),('2021-05-13','四',0,'',0),('2021-05-14','五',0,'',0),('2021-05-15','六',1,'',0),('2021-05-16','日',1,'',0),('2021-05-17','一',0,'',0),('2021-05-18','二',0,'',0),('2021-05-19','三',0,'',0),('2021-05-20','四',0,'',0),('2021-05-21','五',0,'',0),('2021-05-22','六',1,'',0),('2021-05-23','日',1,'',0),('2021-05-24','一',0,'',0),('2021-05-25','二',0,'',0),('2021-05-26','三',0,'',0),('2021-05-27','四',0,'',0),('2021-05-28','五',0,'',0),('2021-05-29','六',1,'',0),('2021-05-30','日',1,'',0),('2021-05-31','一',0,'',0),('2021-06-01','二',0,'',0),('2021-06-02','三',0,'',0),('2021-06-03','四',0,'',0),('2021-06-04','五',0,'',0),('2021-06-05','六',1,'',0),('2021-06-06','日',1,'',0),('2021-06-07','一',0,'',0),('2021-06-08','二',0,'',0),('2021-06-09','三',0,'',0),('2021-06-10','四',0,'',0),('2021-06-11','五',0,'',0),('2021-06-12','六',1,'',0),('2021-06-13','日',1,'',0),('2021-06-14','一',1,'端午節',0),('2021-06-15','二',0,'',0),('2021-06-16','三',0,'',0),('2021-06-17','四',0,'',0),('2021-06-18','五',0,'',0),('2021-06-19','六',1,'',0),('2021-06-20','日',1,'',0),('2021-06-21','一',0,'',0),('2021-06-22','二',0,'',0),('2021-06-23','三',0,'',0),('2021-06-24','四',0,'',0),('2021-06-25','五',0,'',0),('2021-06-26','六',1,'',0),('2021-06-27','日',1,'',0),('2021-06-28','一',0,'',0),('2021-06-29','二',0,'',0),('2021-06-30','三',0,'',0),('2021-07-01','四',0,'',0),('2021-07-02','五',0,'',0),('2021-07-03','六',1,'',0),('2021-07-04','日',1,'',0),('2021-07-05','一',0,'',0),('2021-07-06','二',0,'',0),('2021-07-07','三',0,'',0),('2021-07-08','四',0,'',0),('2021-07-09','五',0,'',0),('2021-07-10','六',1,'',0),('2021-07-11','日',1,'',0),('2021-07-12','一',0,'',0),('2021-07-13','二',0,'',0),('2021-07-14','三',0,'',0),('2021-07-15','四',0,'',0),('2021-07-16','五',0,'',0),('2021-07-17','六',1,'',0),('2021-07-18','日',1,'',0),('2021-07-19','一',0,'',0),('2021-07-20','二',0,'',0),('2021-07-21','三',0,'',0),('2021-07-22','四',0,'',0),('2021-07-23','五',0,'',0),('2021-07-24','六',1,'',0),('2021-07-25','日',1,'',0),('2021-07-26','一',0,'',0),('2021-07-27','二',0,'',0),('2021-07-28','三',0,'',0),('2021-07-29','四',0,'',0),('2021-07-30','五',0,'',0),('2021-07-31','六',1,'',0),('2021-08-01','日',1,'',0),('2021-08-02','一',0,'',0),('2021-08-03','二',0,'',0),('2021-08-04','三',0,'',0),('2021-08-05','四',0,'',0),('2021-08-06','五',0,'',0),('2021-08-07','六',1,'',0),('2021-08-08','日',1,'',0),('2021-08-09','一',0,'',0),('2021-08-10','二',0,'',0),('2021-08-11','三',0,'',0),('2021-08-12','四',0,'',0),('2021-08-13','五',0,'',0),('2021-08-14','六',1,'',0),('2021-08-15','日',1,'',0),('2021-08-16','一',0,'',0),('2021-08-17','二',0,'',0),('2021-08-18','三',0,'',0),('2021-08-19','四',0,'',0),('2021-08-20','五',0,'',0),('2021-08-21','六',1,'',0),('2021-08-22','日',1,'',0),('2021-08-23','一',0,'',0),('2021-08-24','二',0,'',0),('2021-08-25','三',0,'',0),('2021-08-26','四',0,'',0),('2021-08-27','五',0,'',0),('2021-08-28','六',1,'',0),('2021-08-29','日',1,'',0),('2021-08-30','一',0,'',0),('2021-08-31','二',0,'',0),('2021-09-01','三',0,'',0),('2021-09-02','四',0,'',0),('2021-09-03','五',0,'',0),('2021-09-04','六',1,'',0),('2021-09-05','日',1,'',0),('2021-09-06','一',0,'',0),('2021-09-07','二',0,'',0),('2021-09-08','三',0,'',0),('2021-09-09','四',0,'',0),('2021-09-10','五',0,'',0),('2021-09-11','六',0,'補行上班',0),('2021-09-12','日',1,'',0),('2021-09-13','一',0,'',0),('2021-09-14','二',0,'',0),('2021-09-15','三',0,'',0),('2021-09-16','四',0,'',0),('2021-09-17','五',0,'',0),('2021-09-18','六',1,'',0),('2021-09-19','日',1,'',0),('2021-09-20','一',1,'調整放假',0),('2021-09-21','二',1,'中秋節',0),('2021-09-22','三',0,'',0),('2021-09-23','四',0,'',0),('2021-09-24','五',0,'',0),('2021-09-25','六',1,'',0),('2021-09-26','日',1,'',0),('2021-09-27','一',0,'',0),('2021-09-28','二',0,'',0),('2021-09-29','三',0,'',0),('2021-09-30','四',0,'',0),('2021-10-01','五',0,'',0),('2021-10-02','六',1,'',0),('2021-10-03','日',1,'',0),('2021-10-04','一',0,'',0),('2021-10-05','二',0,'',0),('2021-10-06','三',0,'',0),('2021-10-07','四',0,'',0),('2021-10-08','五',0,'',0),('2021-10-09','六',1,'',0),('2021-10-10','日',1,'國慶日',0),('2021-10-11','一',1,'補假',0),('2021-10-12','二',0,'',0),('2021-10-13','三',0,'',0),('2021-10-14','四',0,'',0),('2021-10-15','五',0,'',0),('2021-10-16','六',1,'',0),('2021-10-17','日',1,'',0),('2021-10-18','一',0,'',0),('2021-10-19','二',0,'',0),('2021-10-20','三',0,'',0),('2021-10-21','四',0,'',0),('2021-10-22','五',0,'',0),('2021-10-23','六',1,'',0),('2021-10-24','日',1,'',0),('2021-10-25','一',0,'',0),('2021-10-26','二',0,'',0),('2021-10-27','三',0,'',0),('2021-10-28','四',0,'',0),('2021-10-29','五',0,'',0),('2021-10-30','六',1,'',0),('2021-10-31','日',1,'',0),('2021-11-01','一',0,'',0),('2021-11-02','二',0,'',0),('2021-11-03','三',0,'',0),('2021-11-04','四',0,'',0),('2021-11-05','五',0,'',0),('2021-11-06','六',1,'',0),('2021-11-07','日',1,'',0),('2021-11-08','一',0,'',0),('2021-11-09','二',0,'',0),('2021-11-10','三',0,'',0),('2021-11-11','四',0,'',0),('2021-11-12','五',0,'',0),('2021-11-13','六',1,'',0),('2021-11-14','日',1,'',0),('2021-11-15','一',0,'',0),('2021-11-16','二',0,'',0),('2021-11-17','三',0,'',0),('2021-11-18','四',0,'',0),('2021-11-19','五',0,'',0),('2021-11-20','六',1,'',0),('2021-11-21','日',1,'',0),('2021-11-22','一',0,'',0),('2021-11-23','二',0,'',0),('2021-11-24','三',0,'',0),('2021-11-25','四',0,'',0),('2021-11-26','五',0,'',0),('2021-11-27','六',1,'',0),('2021-11-28','日',1,'',0),('2021-11-29','一',0,'',0),('2021-11-30','二',0,'',0),('2021-12-01','三',0,'',0),('2021-12-02','四',0,'',0),('2021-12-03','五',0,'',0),('2021-12-04','六',1,'',0),('2021-12-05','日',1,'',0),('2021-12-06','一',0,'',0),('2021-12-07','二',0,'',0),('2021-12-08','三',0,'',0),('2021-12-09','四',0,'',0),('2021-12-10','五',0,'',0),('2021-12-11','六',1,'',0),('2021-12-12','日',1,'',0),('2021-12-13','一',0,'',0),('2021-12-14','二',0,'',0),('2021-12-15','三',0,'',0),('2021-12-16','四',0,'',0),('2021-12-17','五',0,'',0),('2021-12-18','六',1,'',0),('2021-12-19','日',1,'',0),('2021-12-20','一',0,'',0),('2021-12-21','二',0,'',0),('2021-12-22','三',0,'',0),('2021-12-23','四',0,'',0),('2021-12-24','五',0,'',0),('2021-12-25','六',1,'',0),('2021-12-26','日',1,'',0),('2021-12-27','一',0,'',0),('2021-12-28','二',0,'',0),('2021-12-29','三',0,'',0),('2021-12-30','四',0,'',0),('2021-12-31','五',1,'補假',0),('2022-01-01','六',1,'開國紀念日',0),('2022-01-02','日',1,'',0),('2022-01-03','一',0,'',0),('2022-01-04','二',0,'',1),('2022-01-05','三',0,'',0),('2022-01-06','四',0,'',0),('2022-01-07','五',0,'',0),('2022-01-08','六',1,'',0),('2022-01-09','日',1,'',0),('2022-01-10','一',0,'',0),('2022-01-11','二',0,'',1),('2022-01-12','三',0,'',0),('2022-01-13','四',0,'',0),('2022-01-14','五',0,'',0),('2022-01-15','六',1,'',0),('2022-01-16','日',1,'',0),('2022-01-17','一',0,'',0),('2022-01-18','二',0,'',0),('2022-01-19','三',0,'',0),('2022-01-20','四',0,'',0),('2022-01-21','五',0,'',0),('2022-01-22','六',0,'補行上班',0),('2022-01-23','日',1,'',0),('2022-01-24','一',0,'',0),('2022-01-25','二',0,'',0),('2022-01-26','三',0,'',0),('2022-01-27','四',0,'',0),('2022-01-28','五',0,'',0),('2022-01-29','六',1,'',0),('2022-01-30','日',1,'',1),('2022-01-31','一',1,'農曆除夕',1),('2022-02-01','二',1,'春節',1),('2022-02-02','三',1,'春節',0),('2022-02-03','四',1,'春節',0),('2022-02-04','五',1,'調整放假',0),('2022-02-05','六',1,'',0),('2022-02-06','日',1,'',0),('2022-02-07','一',0,'',0),('2022-02-08','二',0,'',0),('2022-02-09','三',0,'',0),('2022-02-10','四',0,'',0),('2022-02-11','五',0,'',0),('2022-02-12','六',1,'',0),('2022-02-13','日',1,'',0),('2022-02-14','一',0,'',0),('2022-02-15','二',0,'',0),('2022-02-16','三',0,'',0),('2022-02-17','四',0,'',0),('2022-02-18','五',0,'',0),('2022-02-19','六',1,'',0),('2022-02-20','日',1,'',0),('2022-02-21','一',0,'',0),('2022-02-22','二',0,'',0),('2022-02-23','三',0,'',0),('2022-02-24','四',0,'',0),('2022-02-25','五',0,'',0),('2022-02-26','六',1,'',0),('2022-02-27','日',1,'',0),('2022-02-28','一',1,'和平紀念日',0),('2022-03-01','二',0,'',0),('2022-03-02','三',0,'',0),('2022-03-03','四',0,'',0),('2022-03-04','五',0,'',0),('2022-03-05','六',1,'',0),('2022-03-06','日',1,'',0),('2022-03-07','一',0,'',0),('2022-03-08','二',0,'',0),('2022-03-09','三',0,'',0),('2022-03-10','四',0,'',0),('2022-03-11','五',0,'',0),('2022-03-12','六',1,'',0),('2022-03-13','日',1,'',0),('2022-03-14','一',0,'',0),('2022-03-15','二',0,'',0),('2022-03-16','三',0,'',0),('2022-03-17','四',0,'',0),('2022-03-18','五',0,'',0),('2022-03-19','六',1,'',0),('2022-03-20','日',1,'',0),('2022-03-21','一',0,'',0),('2022-03-22','二',0,'',0),('2022-03-23','三',0,'',0),('2022-03-24','四',0,'',0),('2022-03-25','五',0,'',0),('2022-03-26','六',1,'',0),('2022-03-27','日',1,'',0),('2022-03-28','一',0,'',0),('2022-03-29','二',0,'',0),('2022-03-30','三',0,'',0),('2022-03-31','四',0,'',0),('2022-04-01','五',0,'',0),('2022-04-02','六',1,'',0),('2022-04-03','日',1,'',0),('2022-04-04','一',1,'兒童節',0),('2022-04-05','二',1,'民族掃墓節',0),('2022-04-06','三',0,'',0),('2022-04-07','四',0,'',0),('2022-04-08','五',0,'',0),('2022-04-09','六',1,'',0),('2022-04-10','日',1,'',0),('2022-04-11','一',0,'',0),('2022-04-12','二',0,'',0),('2022-04-13','三',0,'',0),('2022-04-14','四',0,'',0),('2022-04-15','五',0,'',0),('2022-04-16','六',1,'',0),('2022-04-17','日',1,'',0),('2022-04-18','一',0,'',0),('2022-04-19','二',0,'',0),('2022-04-20','三',0,'',0),('2022-04-21','四',0,'',0),('2022-04-22','五',0,'',0),('2022-04-23','六',1,'',0),('2022-04-24','日',1,'',0),('2022-04-25','一',0,'',0),('2022-04-26','二',0,'',0),('2022-04-27','三',0,'',0),('2022-04-28','四',0,'',0),('2022-04-29','五',0,'',0),('2022-04-30','六',1,'',0),('2022-05-01','日',1,'',0),('2022-05-02','一',0,'',0),('2022-05-03','二',0,'',0),('2022-05-04','三',0,'',0),('2022-05-05','四',0,'',0),('2022-05-06','五',0,'',0),('2022-05-07','六',1,'',0),('2022-05-08','日',1,'',0),('2022-05-09','一',0,'',0),('2022-05-10','二',0,'',0),('2022-05-11','三',0,'',0),('2022-05-12','四',0,'',0),('2022-05-13','五',0,'',0),('2022-05-14','六',1,'',0),('2022-05-15','日',1,'',0),('2022-05-16','一',0,'',0),('2022-05-17','二',0,'',0),('2022-05-18','三',0,'',0),('2022-05-19','四',0,'',0),('2022-05-20','五',0,'',0),('2022-05-21','六',1,'',0),('2022-05-22','日',1,'',0),('2022-05-23','一',0,'',0),('2022-05-24','二',0,'',0),('2022-05-25','三',0,'',0),('2022-05-26','四',0,'',0),('2022-05-27','五',0,'',0),('2022-05-28','六',1,'',0),('2022-05-29','日',1,'',0),('2022-05-30','一',0,'',0),('2022-05-31','二',0,'',0),('2022-06-01','三',0,'',0),('2022-06-02','四',0,'',0),('2022-06-03','五',1,'端午節',0),('2022-06-04','六',1,'',0),('2022-06-05','日',1,'',0),('2022-06-06','一',0,'',0),('2022-06-07','二',0,'',0),('2022-06-08','三',0,'',0),('2022-06-09','四',0,'',0),('2022-06-10','五',0,'',0),('2022-06-11','六',1,'',0),('2022-06-12','日',1,'',0),('2022-06-13','一',0,'',0),('2022-06-14','二',0,'',0),('2022-06-15','三',0,'',0),('2022-06-16','四',0,'',0),('2022-06-17','五',0,'',0),('2022-06-18','六',1,'',0),('2022-06-19','日',1,'',0),('2022-06-20','一',0,'',0),('2022-06-21','二',0,'',0),('2022-06-22','三',0,'',0),('2022-06-23','四',0,'',0),('2022-06-24','五',0,'',0),('2022-06-25','六',1,'',0),('2022-06-26','日',1,'',0),('2022-06-27','一',0,'',0),('2022-06-28','二',0,'',0),('2022-06-29','三',0,'',0),('2022-06-30','四',0,'',0),('2022-07-01','五',0,'',0),('2022-07-02','六',1,'',0),('2022-07-03','日',1,'',0),('2022-07-04','一',0,'',0),('2022-07-05','二',0,'',0),('2022-07-06','三',0,'',0),('2022-07-07','四',0,'',0),('2022-07-08','五',0,'',0),('2022-07-09','六',1,'',0),('2022-07-10','日',1,'',0),('2022-07-11','一',0,'',0),('2022-07-12','二',0,'',0),('2022-07-13','三',0,'',0),('2022-07-14','四',0,'',0),('2022-07-15','五',0,'',0),('2022-07-16','六',1,'',0),('2022-07-17','日',1,'',0),('2022-07-18','一',0,'',0),('2022-07-19','二',0,'',0),('2022-07-20','三',0,'',0),('2022-07-21','四',0,'',0),('2022-07-22','五',0,'',0),('2022-07-23','六',1,'',0),('2022-07-24','日',1,'',0),('2022-07-25','一',0,'',0),('2022-07-26','二',0,'',0),('2022-07-27','三',0,'',0),('2022-07-28','四',0,'',0),('2022-07-29','五',0,'',0),('2022-07-30','六',1,'',0),('2022-07-31','日',1,'',0),('2022-08-01','一',0,'',0),('2022-08-02','二',0,'',0),('2022-08-03','三',0,'',0),('2022-08-04','四',0,'',0),('2022-08-05','五',0,'',0),('2022-08-06','六',1,'',0),('2022-08-07','日',1,'',0),('2022-08-08','一',0,'',0),('2022-08-09','二',0,'',0),('2022-08-10','三',0,'',0),('2022-08-11','四',0,'',0),('2022-08-12','五',0,'',0),('2022-08-13','六',1,'',0),('2022-08-14','日',1,'',0),('2022-08-15','一',0,'',0),('2022-08-16','二',0,'',0),('2022-08-17','三',0,'',0),('2022-08-18','四',0,'',0),('2022-08-19','五',0,'',0),('2022-08-20','六',1,'',0),('2022-08-21','日',1,'',0),('2022-08-22','一',0,'',0),('2022-08-23','二',0,'',0),('2022-08-24','三',0,'',0),('2022-08-25','四',0,'',0),('2022-08-26','五',0,'',0),('2022-08-27','六',1,'',0),('2022-08-28','日',1,'',0),('2022-08-29','一',0,'',0),('2022-08-30','二',0,'',0),('2022-08-31','三',0,'',0),('2022-09-01','四',0,'',0),('2022-09-02','五',0,'',0),('2022-09-03','六',1,'',0),('2022-09-04','日',1,'',0),('2022-09-05','一',0,'',0),('2022-09-06','二',0,'',0),('2022-09-07','三',0,'',0),('2022-09-08','四',0,'',0),('2022-09-09','五',1,'補假',0),('2022-09-10','六',1,'中秋節',0),('2022-09-11','日',1,'',0),('2022-09-12','一',0,'',0),('2022-09-13','二',0,'',0),('2022-09-14','三',0,'',0),('2022-09-15','四',0,'',0),('2022-09-16','五',0,'',0),('2022-09-17','六',1,'',0),('2022-09-18','日',1,'',0),('2022-09-19','一',0,'',0),('2022-09-20','二',0,'',0),('2022-09-21','三',0,'',0),('2022-09-22','四',0,'',0),('2022-09-23','五',0,'',0),('2022-09-24','六',1,'',0),('2022-09-25','日',1,'',0),('2022-09-26','一',0,'',0),('2022-09-27','二',0,'',0),('2022-09-28','三',0,'',0),('2022-09-29','四',0,'',0),('2022-09-30','五',0,'',0),('2022-10-01','六',1,'',0),('2022-10-02','日',1,'',0),('2022-10-03','一',0,'',0),('2022-10-04','二',0,'',0),('2022-10-05','三',0,'',0),('2022-10-06','四',0,'',0),('2022-10-07','五',0,'',0),('2022-10-08','六',1,'',0),('2022-10-09','日',1,'',0),('2022-10-10','一',1,'國慶日',0),('2022-10-11','二',0,'',0),('2022-10-12','三',0,'',0),('2022-10-13','四',0,'',0),('2022-10-14','五',0,'',0),('2022-10-15','六',1,'',0),('2022-10-16','日',1,'',0),('2022-10-17','一',0,'',0),('2022-10-18','二',0,'',0),('2022-10-19','三',0,'',0),('2022-10-20','四',0,'',0),('2022-10-21','五',0,'',0),('2022-10-22','六',1,'',0),('2022-10-23','日',1,'',0),('2022-10-24','一',0,'',0),('2022-10-25','二',0,'',0),('2022-10-26','三',0,'',0),('2022-10-27','四',0,'',0),('2022-10-28','五',0,'',0),('2022-10-29','六',1,'',0),('2022-10-30','日',1,'',0),('2022-10-31','一',0,'',0),('2022-11-01','二',0,'',0),('2022-11-02','三',0,'',0),('2022-11-03','四',0,'',0),('2022-11-04','五',0,'',0),('2022-11-05','六',1,'',0),('2022-11-06','日',1,'',0),('2022-11-07','一',0,'',0),('2022-11-08','二',0,'',0),('2022-11-09','三',0,'',0),('2022-11-10','四',0,'',0),('2022-11-11','五',0,'',0),('2022-11-12','六',1,'',0),('2022-11-13','日',1,'',0),('2022-11-14','一',0,'',0),('2022-11-15','二',0,'',0),('2022-11-16','三',0,'',0),('2022-11-17','四',0,'',0),('2022-11-18','五',0,'',0),('2022-11-19','六',1,'',0),('2022-11-20','日',1,'',0),('2022-11-21','一',0,'',0),('2022-11-22','二',0,'',0),('2022-11-23','三',0,'',0),('2022-11-24','四',0,'',0),('2022-11-25','五',0,'',0),('2022-11-26','六',1,'',0),('2022-11-27','日',1,'',0),('2022-11-28','一',0,'',0),('2022-11-29','二',0,'',0),('2022-11-30','三',0,'',0),('2022-12-01','四',0,'',0),('2022-12-02','五',0,'',0),('2022-12-03','六',1,'',0),('2022-12-04','日',1,'',0),('2022-12-05','一',0,'',0),('2022-12-06','二',0,'',0),('2022-12-07','三',0,'',0),('2022-12-08','四',0,'',0),('2022-12-09','五',0,'',0),('2022-12-10','六',1,'',0),('2022-12-11','日',1,'',0),('2022-12-12','一',0,'',0),('2022-12-13','二',0,'',0),('2022-12-14','三',0,'',0),('2022-12-15','四',0,'',0),('2022-12-16','五',0,'',0),('2022-12-17','六',1,'',0),('2022-12-18','日',1,'',0),('2022-12-19','一',0,'',0),('2022-12-20','二',0,'',0),('2022-12-21','三',0,'',0),('2022-12-22','四',0,'',0),('2022-12-23','五',0,'',0),('2022-12-24','六',1,'',0),('2022-12-25','日',1,'',0),('2022-12-26','一',0,'',0),('2022-12-27','二',0,'',0),('2022-12-28','三',0,'',0),('2022-12-29','四',0,'',0),('2022-12-30','五',0,'',0),('2022-12-31','六',1,'',0);
/*!40000 ALTER TABLE `calendar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `guests`
--

DROP TABLE IF EXISTS `guests`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `guests` (
  `gid` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `gender` enum('M','F') DEFAULT 'M',
  `phone` varchar(20) NOT NULL,
  `email` varchar(150) NOT NULL,
  `nationality` varchar(150) NOT NULL DEFAULT 'TAIWAN',
  `id_no` varchar(20) DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `address` varchar(200) DEFAULT NULL,
  `lastest_arrival_date` date DEFAULT NULL,
  `note` text,
  `is_del` tinyint(1) DEFAULT '0',
  `update_datetime` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `update_user` varchar(125) DEFAULT NULL,
  PRIMARY KEY (`gid`,`phone`),
  UNIQUE KEY `id_no` (`id_no`),
  KEY `phone_idx` (`phone`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `guests`
--

LOCK TABLES `guests` WRITE;
/*!40000 ALTER TABLE `guests` DISABLE KEYS */;
INSERT INTO `guests` VALUES (1,'宋小惠','F','0950400600','mia72song@gmail.com','TAIWAN',NULL,'1983-10-15',NULL,NULL,NULL,0,'2022-01-01 10:12:24','mia72song'),(2,'王艾旻','F','0987654321','amywang@gmail.com','TAIWAN',NULL,NULL,NULL,NULL,NULL,0,'2022-01-01 10:13:41','mia72song'),(3,'李鷗','M','0912345678','leolee@gmail.com','CHINA',NULL,NULL,NULL,NULL,NULL,0,'2022-01-01 10:17:21','mia72song'),(4,'言午許','F','0911222333','112233@gmail.com','TAIWAN',NULL,NULL,NULL,NULL,NULL,0,'2022-01-01 11:51:02','言午許'),(5,'song','M','0952400600','12@12','TAIWAN',NULL,NULL,NULL,NULL,NULL,0,'2022-01-03 14:17:58','guest');
/*!40000 ALTER TABLE `guests` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `create_datetime` datetime DEFAULT CURRENT_TIMESTAMP,
  `Phone` varchar(20) NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `check_in_date` date NOT NULL,
  `check_out_date` date NOT NULL,
  `nights` tinyint DEFAULT '1',
  `num_of_guests` tinyint DEFAULT '1',
  `note` text,
  `status` enum('NEW','PAID','CANCEL') DEFAULT 'NEW',
  `PaymentId` varchar(20) DEFAULT NULL,
  `update_datetime` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `update_user` varchar(125) NOT NULL,
  `oid` int NOT NULL,
  `arrival_datetime` datetime DEFAULT NULL,
  `payment_deadline` date NOT NULL,
  PRIMARY KEY (`oid`),
  KEY `Phone` (`Phone`),
  KEY `PaymentId` (`PaymentId`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`Phone`) REFERENCES `guests` (`phone`),
  CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`PaymentId`) REFERENCES `payment_atm` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES ('2022-01-02 22:27:16','0950400600',2112.00,'2022-01-03','2022-01-04',1,1,NULL,'CANCEL',NULL,'2022-01-03 11:24:07','guest',1641133636,'2022-01-03 15:00:00','2022-01-03'),('2022-01-02 22:28:12','0950400600',2112.00,'2022-01-03','2022-01-04',1,1,NULL,'CANCEL',NULL,'2022-01-03 11:24:16','guest',1641133692,'2022-01-03 15:00:00','2022-01-03'),('2022-01-02 22:28:58','0987654321',2112.00,'2022-01-03','2022-01-04',1,1,NULL,'CANCEL',NULL,'2022-01-04 05:05:16','guest',1641133738,'2022-01-03 15:00:00','2022-01-03'),('2022-01-02 22:31:41','0950400600',2112.00,'2022-01-10','2022-01-11',1,1,NULL,'CANCEL',NULL,'2022-01-04 05:05:16','guest',1641133901,'2022-01-10 15:00:00','2022-01-03'),('2022-01-02 22:35:15','0950400600',2112.00,'2022-01-10','2022-01-11',1,1,NULL,'CANCEL',NULL,'2022-01-04 05:05:16','guest',1641134115,'2022-01-10 15:00:00','2022-01-03'),('2022-01-02 22:35:35','0950400600',2112.00,'2022-01-10','2022-01-11',1,1,NULL,'CANCEL',NULL,'2022-01-04 05:05:16','guest',1641134135,'2022-01-10 15:00:00','2022-01-03'),('2022-01-02 23:21:04','0950400600',2112.00,'2022-01-17','2022-01-18',1,1,NULL,'CANCEL',NULL,'2022-01-04 05:05:16','guest',1641136864,'2022-01-17 15:00:00','2022-01-03'),('2022-01-03 22:17:58','0952400600',2112.00,'2022-01-05','2022-01-06',1,1,NULL,'PAID','A1641305569','2022-01-04 14:12:49','mia72song',1641219478,'2022-01-05 15:00:00','2022-01-04'),('2022-01-05 11:46:00','0950400600',2112.00,'2022-01-06','2022-01-07',1,1,NULL,'PAID','A1641359912','2022-01-05 05:18:32','mia72song',1641354360,'2022-01-06 15:00:00','2022-01-06'),('2022-01-05 13:24:18','0987654321',2112.00,'2022-01-17','2022-01-18',1,1,NULL,'PAID','A1641360337','2022-01-05 05:25:37','mia72song',1641360258,'2022-01-17 15:00:00','2022-01-06'),('2022-01-09 00:49:45','0950400600',2112.00,'2022-01-10','2022-01-11',1,1,NULL,'NEW',NULL,'2022-01-08 16:49:45','guest',1641660585,'2022-01-10 15:00:00','2022-01-10');
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payment_atm`
--

DROP TABLE IF EXISTS `payment_atm`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payment_atm` (
  `id` varchar(20) NOT NULL,
  `bank` varchar(125) NOT NULL,
  `account_no` varchar(20) NOT NULL,
  `name` varchar(125) NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `update_datetime` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `update_user` varchar(125) NOT NULL,
  `transfer_date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment_atm`
--

LOCK TABLES `payment_atm` WRITE;
/*!40000 ALTER TABLE `payment_atm` DISABLE KEYS */;
INSERT INTO `payment_atm` VALUES ('A1639491788','中國信託','55143','宋小惠',1000.00,'2021-12-15 07:51:37','mia72song','2021-12-10'),('A1639495093','合作金庫','00432','王艾旻',1000.00,'2021-12-16 13:23:12','mia72song','2021-12-11'),('A1639556264','玉山銀行','98765','李鷗',1000.00,'2021-12-15 17:28:02','mia72song','2021-12-15'),('A1641305569','玉山銀行','55400','宋先生',2112.00,'2022-01-05 06:24:51','mia72song','2022-01-04'),('A1641359912','玉山銀行','54321','宋小惠',2112.00,'2022-01-05 05:18:32','mia72song','2022-01-05'),('A1641360337','台新銀行','24680','王艾旻',2112.00,'2022-01-05 05:25:37','mia72song','2022-01-05');
/*!40000 ALTER TABLE `payment_atm` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `room_types`
--

DROP TABLE IF EXISTS `room_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `room_types` (
  `type` varchar(125) NOT NULL,
  `accommodate` tinyint DEFAULT NULL,
  `images` text,
  `description` text,
  `single_discount` float(3,2) DEFAULT NULL,
  `rate_weekday` decimal(8,2) NOT NULL,
  `rate_holiday` decimal(8,2) NOT NULL,
  `is_del` tinyint(1) DEFAULT '0',
  `name` varchar(125) DEFAULT NULL,
  PRIMARY KEY (`type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `room_types`
--

LOCK TABLES `room_types` WRITE;
/*!40000 ALTER TABLE `room_types` DISABLE KEYS */;
INSERT INTO `room_types` VALUES ('Double',2,'https://static.wixstatic.com/media/414e43_c70a15613bf14e828b90f0d51a295d45~mv2.png, https://static.wixstatic.com/media/414e43_dffabff6a474404995697610347644a8~mv2.jpg, https://static.wixstatic.com/media/414e43_1bb96b12be78402cb2233b2c05d45c0d~mv2.png, https://static.wixstatic.com/media/414e43_0887052c444b4dd7841750044fad9fa0~mv2.png, https://static.wixstatic.com/media/414e43_bf21f57bc9144eaabe684e444386c5a1~mv2.png, https://static.wixstatic.com/media/414e43_5987cbc81a3a4e59bd24c80841b78f1d~mv2.jpg','本館目前僅四間客房，房型皆同。含輕食早餐。\n房間不多，就是為了給您最放鬆、最安靜、不被打擾的美好時光。',0.88,2400.00,2900.00,0,'海旅雙人套房'),('Quad',4,NULL,NULL,1.00,5000.00,4200.00,0,'測試四人房'),('Twin',2,NULL,NULL,0.75,1500.00,1800.00,0,'星空雙人雅房');
/*!40000 ALTER TABLE `room_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rooms`
--

DROP TABLE IF EXISTS `rooms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rooms` (
  `room_no` varchar(10) NOT NULL,
  `RoomType` varchar(125) DEFAULT NULL,
  `is_available` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`room_no`),
  KEY `room_type` (`RoomType`),
  CONSTRAINT `rooms_ibfk_1` FOREIGN KEY (`RoomType`) REFERENCES `room_types` (`type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rooms`
--

LOCK TABLES `rooms` WRITE;
/*!40000 ALTER TABLE `rooms` DISABLE KEYS */;
INSERT INTO `rooms` VALUES ('d001','Double',1),('d002','Double',1),('d003','Double',1),('d004','Double',1),('q001','Quad',1),('q002','Quad',1),('t001','Twin',0),('t002','Twin',1);
/*!40000 ALTER TABLE `rooms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `username` varchar(125) NOT NULL,
  `password` varchar(255) NOT NULL,
  `staff_name` varchar(125) NOT NULL,
  `create_datetime` datetime DEFAULT CURRENT_TIMESTAMP,
  `is_del` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('administrator','pbkdf2:sha256:260000$2RmsTcxk7vuhgWxf$ef614d2cfb5394bdc6790b6fd91559c01d059a85f1817f08922b88b5ffa01493','打個蛋總管理者','2021-11-26 20:13:35',0),('mia72song','pbkdf2:sha256:260000$FOgwTH7TAj1gOHuO$51cf672b1b553dd05fd9f9d3de8b81aefd95155cca652de63a5dc7b188f5c2fb','宋小惠工程師','2021-11-26 20:12:48',0);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-10 17:10:15
