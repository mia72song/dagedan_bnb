-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: dagedan
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('9e7dcbb19330');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `booking`
--

DROP TABLE IF EXISTS `booking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `booking` (
  `date` date NOT NULL,
  `room_no` varchar(64) NOT NULL,
  `order_id` varchar(64) NOT NULL,
  PRIMARY KEY (`date`,`room_no`),
  KEY `order_id` (`order_id`),
  KEY `room_no` (`room_no`),
  CONSTRAINT `booking_ibfk_1` FOREIGN KEY (`date`) REFERENCES `calendar` (`date`),
  CONSTRAINT `booking_ibfk_2` FOREIGN KEY (`order_id`) REFERENCES `orders` (`oid`),
  CONSTRAINT `booking_ibfk_3` FOREIGN KEY (`room_no`) REFERENCES `rooms` (`room_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booking`
--

LOCK TABLES `booking` WRITE;
/*!40000 ALTER TABLE `booking` DISABLE KEYS */;
INSERT INTO `booking` VALUES ('2022-01-25','d002','1643039465');
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
  `day` varchar(3) DEFAULT NULL COMMENT '星期',
  `is_holiday` tinyint(1) DEFAULT '0',
  `note` varchar(128) DEFAULT NULL,
  `is_closed` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `calendar`
--

LOCK TABLES `calendar` WRITE;
/*!40000 ALTER TABLE `calendar` DISABLE KEYS */;
INSERT INTO `calendar` VALUES ('2022-01-01','六',1,'開國紀念日',0),('2022-01-02','日',1,'',0),('2022-01-03','一',0,'',0),('2022-01-04','二',0,'',0),('2022-01-05','三',0,'',0),('2022-01-06','四',0,'',0),('2022-01-07','五',0,'',0),('2022-01-08','六',1,'',0),('2022-01-09','日',1,'',0),('2022-01-10','一',0,'',0),('2022-01-11','二',0,'',0),('2022-01-12','三',0,'',0),('2022-01-13','四',0,'',0),('2022-01-14','五',0,'',0),('2022-01-15','六',1,'',0),('2022-01-16','日',1,'',0),('2022-01-17','一',0,'',0),('2022-01-18','二',0,'',0),('2022-01-19','三',0,'',0),('2022-01-20','四',0,'',0),('2022-01-21','五',0,'',0),('2022-01-22','六',0,'補行上班',0),('2022-01-23','日',1,'',0),('2022-01-24','一',0,'',0),('2022-01-25','二',0,'',0),('2022-01-26','三',0,'',0),('2022-01-27','四',0,'',0),('2022-01-28','五',0,'',0),('2022-01-29','六',1,'',0),('2022-01-30','日',1,'',1),('2022-01-31','一',1,'農曆除夕',1),('2022-02-01','二',1,'春節',1),('2022-02-02','三',1,'春節',1),('2022-02-03','四',1,'春節',0),('2022-02-04','五',1,'調整放假',0),('2022-02-05','六',1,'',0),('2022-02-06','日',1,'',0),('2022-02-07','一',0,'',0),('2022-02-08','二',0,'',0),('2022-02-09','三',0,'',0),('2022-02-10','四',0,'',0),('2022-02-11','五',0,'',0),('2022-02-12','六',1,'',0),('2022-02-13','日',1,'',0),('2022-02-14','一',0,'',0),('2022-02-15','二',0,'',0),('2022-02-16','三',0,'',0),('2022-02-17','四',0,'',0),('2022-02-18','五',0,'',0),('2022-02-19','六',1,'',0),('2022-02-20','日',1,'',0),('2022-02-21','一',0,'',0),('2022-02-22','二',0,'',0),('2022-02-23','三',0,'',0),('2022-02-24','四',0,'',0),('2022-02-25','五',0,'',0),('2022-02-26','六',1,'',0),('2022-02-27','日',1,'',0),('2022-02-28','一',1,'和平紀念日',0),('2022-03-01','二',0,'',0),('2022-03-02','三',0,'',0),('2022-03-03','四',0,'',0),('2022-03-04','五',0,'',0),('2022-03-05','六',1,'',0),('2022-03-06','日',1,'',0),('2022-03-07','一',0,'',0),('2022-03-08','二',0,'',0),('2022-03-09','三',0,'',0),('2022-03-10','四',0,'',0),('2022-03-11','五',0,'',0),('2022-03-12','六',1,'',0),('2022-03-13','日',1,'',0),('2022-03-14','一',0,'',0),('2022-03-15','二',0,'',0),('2022-03-16','三',0,'',0),('2022-03-17','四',0,'',0),('2022-03-18','五',0,'',0),('2022-03-19','六',1,'',0),('2022-03-20','日',1,'',0),('2022-03-21','一',0,'',0),('2022-03-22','二',0,'',0),('2022-03-23','三',0,'',0),('2022-03-24','四',0,'',0),('2022-03-25','五',0,'',0),('2022-03-26','六',1,'',0),('2022-03-27','日',1,'',0),('2022-03-28','一',0,'',0),('2022-03-29','二',0,'',0),('2022-03-30','三',0,'',0),('2022-03-31','四',0,'',0),('2022-04-01','五',0,'',0),('2022-04-02','六',1,'',0),('2022-04-03','日',1,'',0),('2022-04-04','一',1,'兒童節',0),('2022-04-05','二',1,'民族掃墓節',0),('2022-04-06','三',0,'',0),('2022-04-07','四',0,'',0),('2022-04-08','五',0,'',0),('2022-04-09','六',1,'',0),('2022-04-10','日',1,'',0),('2022-04-11','一',0,'',0),('2022-04-12','二',0,'',0),('2022-04-13','三',0,'',0),('2022-04-14','四',0,'',0),('2022-04-15','五',0,'',0),('2022-04-16','六',1,'',0),('2022-04-17','日',1,'',0),('2022-04-18','一',0,'',0),('2022-04-19','二',0,'',0),('2022-04-20','三',0,'',0),('2022-04-21','四',0,'',0),('2022-04-22','五',0,'',0),('2022-04-23','六',1,'',0),('2022-04-24','日',1,'',0),('2022-04-25','一',0,'',0),('2022-04-26','二',0,'',0),('2022-04-27','三',0,'',0),('2022-04-28','四',0,'',0),('2022-04-29','五',0,'',0),('2022-04-30','六',1,'',0),('2022-05-01','日',1,'',0),('2022-05-02','一',0,'',0),('2022-05-03','二',0,'',0),('2022-05-04','三',0,'',0),('2022-05-05','四',0,'',0),('2022-05-06','五',0,'',0),('2022-05-07','六',1,'',0),('2022-05-08','日',1,'',0),('2022-05-09','一',0,'',0),('2022-05-10','二',0,'',0),('2022-05-11','三',0,'',0),('2022-05-12','四',0,'',0),('2022-05-13','五',0,'',0),('2022-05-14','六',1,'',0),('2022-05-15','日',1,'',0),('2022-05-16','一',0,'',0),('2022-05-17','二',0,'',0),('2022-05-18','三',0,'',0),('2022-05-19','四',0,'',0),('2022-05-20','五',0,'',0),('2022-05-21','六',1,'',0),('2022-05-22','日',1,'',0),('2022-05-23','一',0,'',0),('2022-05-24','二',0,'',0),('2022-05-25','三',0,'',0),('2022-05-26','四',0,'',0),('2022-05-27','五',0,'',0),('2022-05-28','六',1,'',0),('2022-05-29','日',1,'',0),('2022-05-30','一',0,'',0),('2022-05-31','二',0,'',0),('2022-06-01','三',0,'',0),('2022-06-02','四',0,'',0),('2022-06-03','五',1,'端午節',0),('2022-06-04','六',1,'',0),('2022-06-05','日',1,'',0),('2022-06-06','一',0,'',0),('2022-06-07','二',0,'',0),('2022-06-08','三',0,'',0),('2022-06-09','四',0,'',0),('2022-06-10','五',0,'',0),('2022-06-11','六',1,'',0),('2022-06-12','日',1,'',0),('2022-06-13','一',0,'',0),('2022-06-14','二',0,'',0),('2022-06-15','三',0,'',0),('2022-06-16','四',0,'',0),('2022-06-17','五',0,'',0),('2022-06-18','六',1,'',0),('2022-06-19','日',1,'',0),('2022-06-20','一',0,'',0),('2022-06-21','二',0,'',0),('2022-06-22','三',0,'',0),('2022-06-23','四',0,'',0),('2022-06-24','五',0,'',0),('2022-06-25','六',1,'',0),('2022-06-26','日',1,'',0),('2022-06-27','一',0,'',0),('2022-06-28','二',0,'',0),('2022-06-29','三',0,'',0),('2022-06-30','四',0,'',0),('2022-07-01','五',0,'',0),('2022-07-02','六',1,'',0),('2022-07-03','日',1,'',0),('2022-07-04','一',0,'',0),('2022-07-05','二',0,'',0),('2022-07-06','三',0,'',0),('2022-07-07','四',0,'',0),('2022-07-08','五',0,'',0),('2022-07-09','六',1,'',0),('2022-07-10','日',1,'',0),('2022-07-11','一',0,'',0),('2022-07-12','二',0,'',0),('2022-07-13','三',0,'',0),('2022-07-14','四',0,'',0),('2022-07-15','五',0,'',0),('2022-07-16','六',1,'',0),('2022-07-17','日',1,'',0),('2022-07-18','一',0,'',0),('2022-07-19','二',0,'',0),('2022-07-20','三',0,'',0),('2022-07-21','四',0,'',0),('2022-07-22','五',0,'',0),('2022-07-23','六',1,'',0),('2022-07-24','日',1,'',0),('2022-07-25','一',0,'',0),('2022-07-26','二',0,'',0),('2022-07-27','三',0,'',0),('2022-07-28','四',0,'',0),('2022-07-29','五',0,'',0),('2022-07-30','六',1,'',0),('2022-07-31','日',1,'',0),('2022-08-01','一',0,'',0),('2022-08-02','二',0,'',0),('2022-08-03','三',0,'',0),('2022-08-04','四',0,'',0),('2022-08-05','五',0,'',0),('2022-08-06','六',1,'',0),('2022-08-07','日',1,'',0),('2022-08-08','一',0,'',0),('2022-08-09','二',0,'',0),('2022-08-10','三',0,'',0),('2022-08-11','四',0,'',0),('2022-08-12','五',0,'',0),('2022-08-13','六',1,'',0),('2022-08-14','日',1,'',0),('2022-08-15','一',0,'',0),('2022-08-16','二',0,'',0),('2022-08-17','三',0,'',0),('2022-08-18','四',0,'',0),('2022-08-19','五',0,'',0),('2022-08-20','六',1,'',0),('2022-08-21','日',1,'',0),('2022-08-22','一',0,'',0),('2022-08-23','二',0,'',0),('2022-08-24','三',0,'',0),('2022-08-25','四',0,'',0),('2022-08-26','五',0,'',0),('2022-08-27','六',1,'',0),('2022-08-28','日',1,'',0),('2022-08-29','一',0,'',0),('2022-08-30','二',0,'',0),('2022-08-31','三',0,'',0),('2022-09-01','四',0,'',0),('2022-09-02','五',0,'',0),('2022-09-03','六',1,'',0),('2022-09-04','日',1,'',0),('2022-09-05','一',0,'',0),('2022-09-06','二',0,'',0),('2022-09-07','三',0,'',0),('2022-09-08','四',0,'',0),('2022-09-09','五',1,'補假',0),('2022-09-10','六',1,'中秋節',0),('2022-09-11','日',1,'',0),('2022-09-12','一',0,'',0),('2022-09-13','二',0,'',0),('2022-09-14','三',0,'',0),('2022-09-15','四',0,'',0),('2022-09-16','五',0,'',0),('2022-09-17','六',1,'',0),('2022-09-18','日',1,'',0),('2022-09-19','一',0,'',0),('2022-09-20','二',0,'',0),('2022-09-21','三',0,'',0),('2022-09-22','四',0,'',0),('2022-09-23','五',0,'',0),('2022-09-24','六',1,'',0),('2022-09-25','日',1,'',0),('2022-09-26','一',0,'',0),('2022-09-27','二',0,'',0),('2022-09-28','三',0,'',0),('2022-09-29','四',0,'',0),('2022-09-30','五',0,'',0),('2022-10-01','六',1,'',0),('2022-10-02','日',1,'',0),('2022-10-03','一',0,'',0),('2022-10-04','二',0,'',0),('2022-10-05','三',0,'',0),('2022-10-06','四',0,'',0),('2022-10-07','五',0,'',0),('2022-10-08','六',1,'',0),('2022-10-09','日',1,'',0),('2022-10-10','一',1,'國慶日',0),('2022-10-11','二',0,'',0),('2022-10-12','三',0,'',0),('2022-10-13','四',0,'',0),('2022-10-14','五',0,'',0),('2022-10-15','六',1,'',0),('2022-10-16','日',1,'',0),('2022-10-17','一',0,'',0),('2022-10-18','二',0,'',0),('2022-10-19','三',0,'',0),('2022-10-20','四',0,'',0),('2022-10-21','五',0,'',0),('2022-10-22','六',1,'',0),('2022-10-23','日',1,'',0),('2022-10-24','一',0,'',0),('2022-10-25','二',0,'',0),('2022-10-26','三',0,'',0),('2022-10-27','四',0,'',0),('2022-10-28','五',0,'',0),('2022-10-29','六',1,'',0),('2022-10-30','日',1,'',0),('2022-10-31','一',0,'',0),('2022-11-01','二',0,'',0),('2022-11-02','三',0,'',0),('2022-11-03','四',0,'',0),('2022-11-04','五',0,'',0),('2022-11-05','六',1,'',0),('2022-11-06','日',1,'',0),('2022-11-07','一',0,'',0),('2022-11-08','二',0,'',0),('2022-11-09','三',0,'',0),('2022-11-10','四',0,'',0),('2022-11-11','五',0,'',0),('2022-11-12','六',1,'',0),('2022-11-13','日',1,'',0),('2022-11-14','一',0,'',0),('2022-11-15','二',0,'',0),('2022-11-16','三',0,'',0),('2022-11-17','四',0,'',0),('2022-11-18','五',0,'',0),('2022-11-19','六',1,'',0),('2022-11-20','日',1,'',0),('2022-11-21','一',0,'',0),('2022-11-22','二',0,'',0),('2022-11-23','三',0,'',0),('2022-11-24','四',0,'',0),('2022-11-25','五',0,'',0),('2022-11-26','六',1,'',0),('2022-11-27','日',1,'',0),('2022-11-28','一',0,'',0),('2022-11-29','二',0,'',0),('2022-11-30','三',0,'',0),('2022-12-01','四',0,'',0),('2022-12-02','五',0,'',0),('2022-12-03','六',1,'',0),('2022-12-04','日',1,'',0),('2022-12-05','一',0,'',0),('2022-12-06','二',0,'',0),('2022-12-07','三',0,'',0),('2022-12-08','四',0,'',0),('2022-12-09','五',0,'',0),('2022-12-10','六',1,'',0),('2022-12-11','日',1,'',0),('2022-12-12','一',0,'',0),('2022-12-13','二',0,'',0),('2022-12-14','三',0,'',0),('2022-12-15','四',0,'',0),('2022-12-16','五',0,'',0),('2022-12-17','六',1,'',0),('2022-12-18','日',1,'',0),('2022-12-19','一',0,'',0),('2022-12-20','二',0,'',0),('2022-12-21','三',0,'',0),('2022-12-22','四',0,'',0),('2022-12-23','五',0,'',0),('2022-12-24','六',1,'',0),('2022-12-25','日',1,'',0),('2022-12-26','一',0,'',0),('2022-12-27','二',0,'',0),('2022-12-28','三',0,'',0),('2022-12-29','四',0,'',0),('2022-12-30','五',0,'',0),('2022-12-31','六',1,'',0);
/*!40000 ALTER TABLE `calendar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `oid` varchar(64) NOT NULL,
  `create_datetime` datetime DEFAULT NULL,
  `check_in_date` date NOT NULL,
  `check_out_date` date NOT NULL,
  `nights` int DEFAULT '1',
  `num_of_guests` int DEFAULT '1',
  `amount` int NOT NULL,
  `booker_name` varchar(128) NOT NULL,
  `booker_gender` varchar(2) DEFAULT 'M',
  `booker_phone` varchar(10) NOT NULL,
  `booker_email` varchar(128) NOT NULL,
  `arrival_datetime` datetime DEFAULT NULL,
  `payment_deadline` date NOT NULL,
  `payment_id` varchar(32) DEFAULT NULL,
  `status` enum('NEW','PENDING','PAID','CANCEL','REFUND') DEFAULT 'NEW',
  `update_datetime` datetime DEFAULT NULL,
  `update_user` varchar(64) DEFAULT NULL,
  `room_type` varchar(128) NOT NULL,
  `room_quantity` int DEFAULT '1',
  PRIMARY KEY (`oid`),
  KEY `room_type` (`room_type`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`room_type`) REFERENCES `room_types` (`type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES ('1643039465','2022-01-24 23:51:06','2022-01-25','2022-01-26',1,1,2112,'Mia Song','M','0950400600','mia721015@gmail.com','2022-01-25 15:00:00','2022-01-25',NULL,'NEW','2022-01-24 23:51:06',NULL,'Double',1);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payment_atm`
--

DROP TABLE IF EXISTS `payment_atm`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payment_atm` (
  `pid` varchar(32) NOT NULL,
  `bank` varchar(128) NOT NULL,
  `account_no` varchar(20) NOT NULL,
  `name` varchar(64) NOT NULL,
  `amount` int NOT NULL,
  `transfer_date` date NOT NULL,
  `update_datetime` datetime DEFAULT NULL,
  `update_user` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment_atm`
--

LOCK TABLES `payment_atm` WRITE;
/*!40000 ALTER TABLE `payment_atm` DISABLE KEYS */;
/*!40000 ALTER TABLE `payment_atm` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `room_types`
--

DROP TABLE IF EXISTS `room_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `room_types` (
  `type` varchar(128) NOT NULL,
  `name` varchar(128) DEFAULT NULL,
  `accommodate` int DEFAULT NULL,
  `rate_weekday` int NOT NULL,
  `rate_holiday` int NOT NULL,
  `single_discount` float DEFAULT NULL,
  `description` text,
  `images` text,
  `is_del` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `room_types`
--

LOCK TABLES `room_types` WRITE;
/*!40000 ALTER TABLE `room_types` DISABLE KEYS */;
INSERT INTO `room_types` VALUES ('Double','海旅雙人套房',2,2400,2900,0.88,'含輕食早餐。本館目前僅四間客房，房型皆同。房間不多，就是為了給您最放鬆、最安靜、不被打擾的美好時光。','https://static.wixstatic.com/media/414e43_5987cbc81a3a4e59bd24c80841b78f1d~mv2.jpg, ',0),('Twin','星空雙人雅房',2,1500,1900,0.88,NULL,'https://static.wixstatic.com/media/414e43_458a78c5c7634ced8f0bbc9cdbc4d520~mv2.jpg, ',0);
/*!40000 ALTER TABLE `room_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rooms`
--

DROP TABLE IF EXISTS `rooms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rooms` (
  `room_no` varchar(64) NOT NULL,
  `room_type` varchar(128) NOT NULL,
  `is_available` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`room_no`),
  KEY `room_type` (`room_type`),
  CONSTRAINT `rooms_ibfk_1` FOREIGN KEY (`room_type`) REFERENCES `room_types` (`type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rooms`
--

LOCK TABLES `rooms` WRITE;
/*!40000 ALTER TABLE `rooms` DISABLE KEYS */;
INSERT INTO `rooms` VALUES ('d001','Double',1),('d002','Double',1),('d003','Double',1),('d004','Double',1),('d005','Double',0),('t001','Twin',1),('t002','Twin',0);
/*!40000 ALTER TABLE `rooms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `uid` int NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `username` varchar(64) NOT NULL,
  `password` varchar(128) NOT NULL,
  `create_datetime` datetime DEFAULT NULL,
  `is_del` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`uid`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'打個蛋總管理者','administer','pbkdf2:sha256:150000$gLUl1gKQ$ffeb5c9d38710ea14bd57c9f5195b44405ff94521f237fe3ae9e0203f6737bbf','2022-01-24 12:47:30',0),(2,'宋小惠工程師','mia72song','pbkdf2:sha256:150000$p9XvDrW4$d03d868b1837d4072b6b8f4574787d4e0d4cbb4be491f3b4409ad119e53c9878','2022-01-24 12:48:04',0);
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

-- Dump completed on 2022-01-25  2:25:51
