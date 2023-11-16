/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.7.9 : Database - fuel_station
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`fuel_station` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `fuel_station`;

/*Table structure for table `employees` */

DROP TABLE IF EXISTS `employees`;

CREATE TABLE `employees` (
  `employee_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fuelstation_id` int(11) DEFAULT NULL,
  `emp_name` varchar(50) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `contact` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `employees` */

insert  into `employees`(`employee_id`,`login_id`,`fuelstation_id`,`emp_name`,`address`,`contact`) values (1,4,1,'Employee 1','Abcd Town,\r\nH.no23/476\r\nusnaz tower','6587442256');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `feedback` varchar(500) DEFAULT NULL,
  `reply` varchar(250) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`user_id`,`feedback`,`reply`,`date`) values (1,1,'Good ','Ok','2023-02-28');

/*Table structure for table `fuel` */

DROP TABLE IF EXISTS `fuel`;

CREATE TABLE `fuel` (
  `fuel_id` int(11) NOT NULL AUTO_INCREMENT,
  `fuelstation_id` int(11) DEFAULT NULL,
  `category_id` int(11) DEFAULT NULL,
  `district` varchar(50) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `amount` int(11) DEFAULT NULL,
  `mobile` varchar(50) DEFAULT NULL,
  `available` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`fuel_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `fuel` */

insert  into `fuel`(`fuel_id`,`fuelstation_id`,`category_id`,`district`,`city`,`amount`,`mobile`,`available`) values (1,1,1,'ernakulam','pallimukk',100,'7894561230','yes'),(2,1,2,'alappuzha','Cherthala',120,'8367257990','yes');

/*Table structure for table `fuel_categorys` */

DROP TABLE IF EXISTS `fuel_categorys`;

CREATE TABLE `fuel_categorys` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `categoryname` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `fuel_categorys` */

insert  into `fuel_categorys`(`category_id`,`categoryname`) values (1,'Petrol'),(2,'Diecel');

/*Table structure for table `fuelstations` */

DROP TABLE IF EXISTS `fuelstations`;

CREATE TABLE `fuelstations` (
  `fuelstation_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(50) DEFAULT NULL,
  `licence_no` varchar(50) DEFAULT NULL,
  `district` varchar(50) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `pincode` varchar(50) DEFAULT NULL,
  `mobile` varchar(50) DEFAULT NULL,
  `location` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`fuelstation_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `fuelstations` */

insert  into `fuelstations`(`fuelstation_id`,`login_id`,`fname`,`licence_no`,`district`,`city`,`pincode`,`mobile`,`location`) values (1,1,'fuelstation1','3457658','ernakulam','pallimukk','123456','7894561230','<iframe src=\"https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d15718.718008481845!2d76.2447615!3d9.96060095!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3b086d314f0b178d%3A0xc545233f390db43b!2sFort%20Kochi%2C%20Kochi%2C%20Kerala!5e0!3m2!1sen!2sin!4v1677298604200!5m2!1sen!2sin\" width=\"150\" height=\"100\" style=\"border:0;\" allowfullscreen=\"\" loading=\"lazy\" referrerpolicy=\"no-referrer-when-downgrade\"></iframe>');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `usertype` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`,`status`) values (1,'fs1234@gmail.com','1234','fuelstation','Accept'),(2,'user1@gmail.com','1234','user',NULL),(3,'admin@gmail.com','admin','admin',NULL),(4,'emp1@gmail.com','1234','employee',NULL);

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `request_id` int(11) DEFAULT NULL,
  `card_num` varchar(50) DEFAULT NULL,
  `card_holder` varchar(50) DEFAULT NULL,
  `total` varchar(50) DEFAULT NULL,
  `paytype` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`payment_id`,`user_id`,`request_id`,`card_num`,`card_holder`,`total`,`paytype`) values (1,1,1,'5674839219287826','It is me','500 ','online');

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `request_id` int(11) NOT NULL AUTO_INCREMENT,
  `fuel_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `phn_num` varchar(100) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `req_status` varchar(50) DEFAULT NULL,
  `pay_status` varchar(100) DEFAULT NULL,
  `total` int(11) DEFAULT NULL,
  `employee_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `request` */

insert  into `request`(`request_id`,`fuel_id`,`user_id`,`name`,`phn_num`,`quantity`,`place`,`date`,`req_status`,`pay_status`,`total`,`employee_id`) values (1,1,1,'My name','8746736376',5,'Aluva','2023-02-28','Accepted','Paid',500,1);

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `district` varchar(50) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `street` varchar(50) DEFAULT NULL,
  `pincode` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `users` */

insert  into `users`(`user_id`,`login_id`,`name`,`dob`,`district`,`city`,`street`,`pincode`,`phone`) values (1,2,'First User','2023-02-02','ernakulam','MG Road','Ravipuram','199345','8838464800');

/*Table structure for table `works` */

DROP TABLE IF EXISTS `works`;

CREATE TABLE `works` (
  `work_id` int(11) NOT NULL AUTO_INCREMENT,
  `request_id` int(11) DEFAULT NULL,
  `employee_id` int(11) DEFAULT NULL,
  `work_status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`work_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `works` */

insert  into `works`(`work_id`,`request_id`,`employee_id`,`work_status`) values (1,1,1,'Completed');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
