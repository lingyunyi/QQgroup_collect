/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1
Source Server Version : 50547
Source Host           : localhost:3306
Source Database       : collect

Target Server Type    : MYSQL
Target Server Version : 50547
File Encoding         : 65001

Date: 2021-10-21 16:44:31
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for admins_account
-- ----------------------------
DROP TABLE IF EXISTS `admins_account`;
CREATE TABLE `admins_account` (
  `id` int(11) NOT NULL,
  `admins_account` varchar(255) DEFAULT NULL,
  `admins_passwd` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of admins_account
-- ----------------------------
INSERT INTO `admins_account` VALUES ('0', '123456', 'e10adc3949ba59abbe56e057f20f883e');

-- ----------------------------
-- Table structure for admins_session
-- ----------------------------
DROP TABLE IF EXISTS `admins_session`;
CREATE TABLE `admins_session` (
  `id` int(11) NOT NULL,
  `admins_account` text,
  `admins_session` text,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of admins_session
-- ----------------------------
INSERT INTO `admins_session` VALUES ('0', '123456', '{\'alive_time_s\': 1634810251}');

-- ----------------------------
-- Table structure for alls_notice_activity_list
-- ----------------------------
DROP TABLE IF EXISTS `alls_notice_activity_list`;
CREATE TABLE `alls_notice_activity_list` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `notice_activity_name` text,
  `notice_activity_content` text,
  `notice_activity_type` int(1) DEFAULT NULL,
  `notice_activity_create_time` text,
  `notice_activity_end_time` text,
  `user_name` varchar(255) DEFAULT NULL,
  `is_delete` int(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of alls_notice_activity_list
-- ----------------------------
INSERT INTO `alls_notice_activity_list` VALUES ('4', '这是公告', '这是公告', '0', '2021-10-21', '2021-10-21', '123456', '0');
INSERT INTO `alls_notice_activity_list` VALUES ('5', '这是活动', '这是活动', '1', '2021-10-21', '21-10-22', '123456', '0');

-- ----------------------------
-- Table structure for users_account
-- ----------------------------
DROP TABLE IF EXISTS `users_account`;
CREATE TABLE `users_account` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `users_account` varchar(255) DEFAULT NULL,
  `users_passwd` varchar(255) DEFAULT NULL,
  `users_alives_time_s` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users_account
-- ----------------------------
INSERT INTO `users_account` VALUES ('1', '123456', 'e10adc3949ba59abbe56e057f20f883e', '1666575515');
INSERT INTO `users_account` VALUES ('2', '1234567', 'e10adc3949ba59abbe56e057f20f883e', '1666575515');
INSERT INTO `users_account` VALUES ('3', '12345678', 'e10adc3949ba59abbe56e057f20f883e', '1666575515');
INSERT INTO `users_account` VALUES ('5', '123456789', 'e10adc3949ba59abbe56e057f20f883e', '1666575515');
INSERT INTO `users_account` VALUES ('6', '12345', 'e10adc3949ba59abbe56e057f20f883e', '1666575515');
INSERT INTO `users_account` VALUES ('7', '18172041272', 'e10adc3949ba59abbe56e057f20f883e', '1634890011');

-- ----------------------------
-- Table structure for users_network_dick
-- ----------------------------
DROP TABLE IF EXISTS `users_network_dick`;
CREATE TABLE `users_network_dick` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `qqclass_name` varchar(255) DEFAULT NULL,
  `qqclass_number` varchar(255) DEFAULT NULL,
  `qqclass_from_users_account` varchar(255) DEFAULT NULL,
  `users_is_like` int(1) DEFAULT NULL,
  `groupMemberNum` varchar(255) DEFAULT NULL,
  `is_delete` int(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users_network_dick
-- ----------------------------
INSERT INTO `users_network_dick` VALUES ('2', '『云想』', '7655822', '18172041272', '0', '6', '0');

-- ----------------------------
-- Table structure for users_session
-- ----------------------------
DROP TABLE IF EXISTS `users_session`;
CREATE TABLE `users_session` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `users_account` text,
  `users_session` text,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users_session
-- ----------------------------
INSERT INTO `users_session` VALUES ('1', '18172041272', '{\'alive_time_s\': 1634810724, \'img_path\': \'\\\\Collect\\\\temp\\\\65d4f36a-bd75-47a3-881e-64ab16a83b38.png\', \'scan_status\': \'success\', \'scan_numbers\': \'6-39\'}');
