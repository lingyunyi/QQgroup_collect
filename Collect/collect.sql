/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1
Source Server Version : 50547
Source Host           : localhost:3306
Source Database       : collect

Target Server Type    : MYSQL
Target Server Version : 50547
File Encoding         : 65001

Date: 2021-10-22 20:43:48
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
INSERT INTO `admins_session` VALUES ('0', '123456', '{\'alive_time_s\': 1634911171}');

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
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of alls_notice_activity_list
-- ----------------------------
INSERT INTO `alls_notice_activity_list` VALUES ('7', '成都共青团委社会实践', '各系团委： 2021年是“十四五”开局之年、是中国共产党成立100周年，为深入学习贯彻习近平新时代中国特色社会主义思想，组织引导广大学生了解世情国情、社情民情，感悟党领导人民建设祖国的伟大成就，增强青年的社会责任感，以青春之我、奋斗之我勇担时代使命，谱写青春华章。经学院研究，决定组织学生开展2020-2021学年暑假社会实践活动，现将有关事项通知如下： 一、活动主题 青春向党·奋斗强国 二、活动时间 2021年10月—12月 三、参与对象 2019级、2020级学生 四、活动内容 （一）“弘扬志愿精神·展现青年形象”主题实践活动 鼓励学生聚焦“人人都做志愿者”践行社会主义核心价值观，围绕守望成长、文化传播、敬老爱老、扶弱助困、社区建设等重点领域，通过网络连线西部、连线基层，发挥所知所学，积极开展助学、助医、助农等“微公益”、“云志愿”等活动；参加志愿四川活动通过深入农村、社区、家庭等方式，广泛开展敬老、助残、科普宣传、文化娱乐等志愿服务活动。通过参与活动深入交流与服务活动，感受心得体会，并形成主题实践报告。 （二）大学生“返家乡”社会实践活动 大学生结合自身专业和学科专长，通过对家乡进行实地考察、调研，开展社会调研等方式，了解家乡政治、经济、社会、文化和生态发展变化状况，读懂国情社情民情，记录民族文化和民族风俗，并深入探索背后的文化基因，理清文化传承的深层次原因、传承现状以及发展意义。传承优秀传统文化，树立高度的文化自信，为构建中国特色社会主义文化体系做贡献，并形成主题实践报告。                               成都共青团委员会                                  2021年9月28日  ', '1', '2021-10-22', '2021-12-30', '123456', '0');
INSERT INTO `alls_notice_activity_list` VALUES ('6', '2022年青年志愿者活动', '青年志愿者', '1', '2021-10-21', '2022-10-20', '123456', '0');

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
) ENGINE=MyISAM AUTO_INCREMENT=63 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users_account
-- ----------------------------
INSERT INTO `users_account` VALUES ('1', '123456', 'e10adc3949ba59abbe56e057f20f883e', '1666575515');
INSERT INTO `users_account` VALUES ('2', '1234567', 'e10adc3949ba59abbe56e057f20f883e', '1666575515');
INSERT INTO `users_account` VALUES ('3', '12345678', 'e10adc3949ba59abbe56e057f20f883e', '1666575515');
INSERT INTO `users_account` VALUES ('5', '123456789', 'e10adc3949ba59abbe56e057f20f883e', '1666575515');
INSERT INTO `users_account` VALUES ('6', '12345', 'e10adc3949ba59abbe56e057f20f883e', '1666575515');
INSERT INTO `users_account` VALUES ('7', '11111', 'e10adc3949ba59abbe56e057f20f883e', '1666575515');
INSERT INTO `users_account` VALUES ('8', '22222', 'e10adc3949ba59abbe56e057f20f883e', '1666575515');
INSERT INTO `users_account` VALUES ('9', '33333', 'e10adc3949ba59abbe56e057f20f883e', '1666575515');
INSERT INTO `users_account` VALUES ('10', '55555', 'e10adc3949ba59abbe56e057f20f883e', '1666575515');
INSERT INTO `users_account` VALUES ('11', '66666', 'e10adc3949ba59abbe56e057f20f883e', '1666575515');
INSERT INTO `users_account` VALUES ('12', 'z1', 'e10adc3949ba59abbe56e057f20f883e', '1666453999');
INSERT INTO `users_account` VALUES ('13', 'y1', 'c4ca4238a0b923820dcc509a6f75849b', '1635090867');
INSERT INTO `users_account` VALUES ('14', 'b1', 'c4ca4238a0b923820dcc509a6f75849b', '1666454097');
INSERT INTO `users_account` VALUES ('15', 'y2', 'c4ca4238a0b923820dcc509a6f75849b', '1635004514');
INSERT INTO `users_account` VALUES ('16', 'b2', 'c4ca4238a0b923820dcc509a6f75849b', '1635090934');
INSERT INTO `users_account` VALUES ('17', 'w1', 'c4ca4238a0b923820dcc509a6f75849b', '1650471183');
INSERT INTO `users_account` VALUES ('18', 'w2', 'c4ca4238a0b923820dcc509a6f75849b', '1635092000');
INSERT INTO `users_account` VALUES ('19', 'w3', 'c4ca4238a0b923820dcc509a6f75849b', '1635005618');
INSERT INTO `users_account` VALUES ('20', 'w4', 'c4ca4238a0b923820dcc509a6f75849b', '1666455256');
INSERT INTO `users_account` VALUES ('21', 'w5', 'c4ca4238a0b923820dcc509a6f75849b', '1635524091');
INSERT INTO `users_account` VALUES ('22', 'w6', 'c4ca4238a0b923820dcc509a6f75849b', '1635524116');
INSERT INTO `users_account` VALUES ('23', 'w7', 'c4ca4238a0b923820dcc509a6f75849b', '1666455330');
INSERT INTO `users_account` VALUES ('24', 'w8', 'c4ca4238a0b923820dcc509a6f75849b', '1635524162');
INSERT INTO `users_account` VALUES ('25', 'w9', 'c4ca4238a0b923820dcc509a6f75849b', '1635524180');
INSERT INTO `users_account` VALUES ('26', 'w10', 'c4ca4238a0b923820dcc509a6f75849b', '1635524196');
INSERT INTO `users_account` VALUES ('27', 'b3', 'c4ca4238a0b923820dcc509a6f75849b', '1666457531');
INSERT INTO `users_account` VALUES ('28', 'b4', 'c4ca4238a0b923820dcc509a6f75849b', '1666457544');
INSERT INTO `users_account` VALUES ('29', 'b5', 'c4ca4238a0b923820dcc509a6f75849b', '1666457580');
INSERT INTO `users_account` VALUES ('30', 'b6', 'c4ca4238a0b923820dcc509a6f75849b', '1666457596');
INSERT INTO `users_account` VALUES ('31', 'b7', 'c4ca4238a0b923820dcc509a6f75849b', '1635180810');
INSERT INTO `users_account` VALUES ('32', 'b8', 'c4ca4238a0b923820dcc509a6f75849b', '1635526423');
INSERT INTO `users_account` VALUES ('33', 'b9', 'c4ca4238a0b923820dcc509a6f75849b', '1635526471');
INSERT INTO `users_account` VALUES ('34', 'b10', 'c4ca4238a0b923820dcc509a6f75849b', '1635526502');
INSERT INTO `users_account` VALUES ('35', 'ly1', 'c4ca4238a0b923820dcc509a6f75849b', '1634956673');
INSERT INTO `users_account` VALUES ('36', 'zzq1234', '320fc9f304883c07d3521cea4270f3a0', '1634956706');
INSERT INTO `users_account` VALUES ('37', 'vy1zzq1234', '320fc9f304883c07d3521cea4270f3a0', '1634956735');
INSERT INTO `users_account` VALUES ('38', 'ly2', 'c81e728d9d4c2f636f067f89cc14862c', '1634957014');
INSERT INTO `users_account` VALUES ('39', 'zzq1', '40cce97b4b9ead18e4f6f80e62395df8', '1634957069');
INSERT INTO `users_account` VALUES ('40', 'ly3', 'eccbc87e4b5ce2fe28308fd9f2a7baf3', '1634957116');
INSERT INTO `users_account` VALUES ('41', 'ly4', 'a87ff679a2f3e71d9181a67b7542122c', '1634957149');
INSERT INTO `users_account` VALUES ('42', 'zzq2', '40cce97b4b9ead18e4f6f80e62395df8', '1634957171');
INSERT INTO `users_account` VALUES ('43', 'ly5', 'e4da3b7fbbce2345d7772b0674a318d5', '1634957181');
INSERT INTO `users_account` VALUES ('44', 'ly6', '1679091c5a880faf6fb5e6087eb1b2dc', '1634957216');
INSERT INTO `users_account` VALUES ('45', 'ly7', '8f14e45fceea167a5a36dedd4bea2543', '1634957241');
INSERT INTO `users_account` VALUES ('46', 'ly8', 'c9f0f895fb98ab9159f51fd0297e236d', '1634957270');
INSERT INTO `users_account` VALUES ('47', 'ly9', '45c48cce2e2d7fbdea1afc51c7c6ad26', '1634957296');
INSERT INTO `users_account` VALUES ('48', '112', 'c4ca4238a0b923820dcc509a6f75849b', '1634958940');
INSERT INTO `users_account` VALUES ('49', 'zzq3', 'c4ca4238a0b923820dcc509a6f75849b', '1634967453');
INSERT INTO `users_account` VALUES ('50', 'zzq4', 'c4ca4238a0b923820dcc509a6f75849b', '1634967467');
INSERT INTO `users_account` VALUES ('51', 'zzq', 'c4ca4238a0b923820dcc509a6f75849b', '1634967490');
INSERT INTO `users_account` VALUES ('52', 'zzq6', 'c4ca4238a0b923820dcc509a6f75849b', '1634967505');
INSERT INTO `users_account` VALUES ('53', 'zzq7', 'c4ca4238a0b923820dcc509a6f75849b', '1634967522');
INSERT INTO `users_account` VALUES ('54', 'zzq8', 'c4ca4238a0b923820dcc509a6f75849b', '1634967536');
INSERT INTO `users_account` VALUES ('55', 'zzq9', 'c4ca4238a0b923820dcc509a6f75849b', '1634967550');
INSERT INTO `users_account` VALUES ('56', 'zzq10', 'c4ca4238a0b923820dcc509a6f75849b', '1634967564');
INSERT INTO `users_account` VALUES ('57', 's1', 'c4ca4238a0b923820dcc509a6f75849b', '1634974266');
INSERT INTO `users_account` VALUES ('58', 's2', 'c4ca4238a0b923820dcc509a6f75849b', '1634974278');
INSERT INTO `users_account` VALUES ('59', 's4', 'c4ca4238a0b923820dcc509a6f75849b', '1634974300');
INSERT INTO `users_account` VALUES ('60', 'zzq11', 'c4ca4238a0b923820dcc509a6f75849b', '1634975136');
INSERT INTO `users_account` VALUES ('61', 'zzq12', 'c4ca4238a0b923820dcc509a6f75849b', '1634975151');
INSERT INTO `users_account` VALUES ('62', 'zzq13', 'c4ca4238a0b923820dcc509a6f75849b', '1634975165');

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
  `insert_time` varchar(255) DEFAULT '0000-00-00 00:00',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=732 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users_network_dick
-- ----------------------------
INSERT INTO `users_network_dick` VALUES ('2', '『云想』', '7655822', '18172041272', '0', '6', '0', null);
INSERT INTO `users_network_dick` VALUES ('530', '可爱丸子表情包斗图群', '812106735', 'w3', '0', '2962', '0', null);
INSERT INTO `users_network_dick` VALUES ('529', '拉一人送1000名片赞8', '674168105', 'w4', '0', '942', '0', null);
INSERT INTO `users_network_dick` VALUES ('528', '林沚.、.、Regret&nbsp;.', '607324733', 'w4', '0', '8', '0', null);
INSERT INTO `users_network_dick` VALUES ('527', '优质扩列/交友/处CP/恋', '309409139', 'w4', '0', '885', '0', null);
INSERT INTO `users_network_dick` VALUES ('526', '林沚.、一起看海吗、', '222145959', 'w4', '0', '4', '0', null);
INSERT INTO `users_network_dick` VALUES ('525', '1班.', '961386653', 'b2', '0', '36', '0', null);
INSERT INTO `users_network_dick` VALUES ('524', '2019毕业届', '724498027', 'w3', '0', '51', '0', null);
INSERT INTO `users_network_dick` VALUES ('523', '怡红院', '362836795', 'b3', '0', '36', '0', null);
INSERT INTO `users_network_dick` VALUES ('522', '八一班网络学习群', '850568483', 'b2', '0', '51', '0', null);
INSERT INTO `users_network_dick` VALUES ('521', '关于声音那点事儿', '717856438', 'w3', '0', '8', '0', null);
INSERT INTO `users_network_dick` VALUES ('520', '光遇', '778123964', 'b2', '0', '878', '0', null);
INSERT INTO `users_network_dick` VALUES ('518', '开心唱歌群', '228141526', 'w3', '0', '1410', '0', null);
INSERT INTO `users_network_dick` VALUES ('519', '2019级2班', '438667336', 'w3', '0', '53', '0', null);
INSERT INTO `users_network_dick` VALUES ('517', '北大学生', '777942931', 'b2', '0', '27', '0', null);
INSERT INTO `users_network_dick` VALUES ('516', '2021级电子旅游同学群', '741378584', 'b2', '0', '44', '0', null);
INSERT INTO `users_network_dick` VALUES ('514', '精神病院的扛把子们', '131528037', 'w3', '0', '6', '0', null);
INSERT INTO `users_network_dick` VALUES ('515', '书书在复习（2群）', '736701469', 'b2', '0', '497', '0', null);
INSERT INTO `users_network_dick` VALUES ('513', '?听君一席话', '690778769', 'b2', '0', '28', '0', null);
INSERT INTO `users_network_dick` VALUES ('511', '人间限定宝藏', '610732956', 'b2', '0', '83', '0', null);
INSERT INTO `users_network_dick` VALUES ('512', '侦探小队分公司', '615788084', 'b2', '0', '12', '0', null);
INSERT INTO `users_network_dick` VALUES ('510', '好大一个金元宝①', '487237963', 'b2', '0', '313', '0', null);
INSERT INTO `users_network_dick` VALUES ('509', '哈利波特Arise', '978076909', 'b2', '0', '15', '0', null);
INSERT INTO `users_network_dick` VALUES ('508', '荷塘月色', '716905411', 'b2', '0', '3', '0', null);
INSERT INTO `users_network_dick` VALUES ('507', '真理、南辞、栩白', '206227737', 'b2', '0', '2', '0', null);
INSERT INTO `users_network_dick` VALUES ('506', '开黑', '1074524275', 'w2', '0', '7', '0', null);
INSERT INTO `users_network_dick` VALUES ('505', '19春数控班', '801217495', 'w2', '0', '47', '0', null);
INSERT INTO `users_network_dick` VALUES ('504', '2019数控一班', '791067724', 'w2', '0', '30', '0', null);
INSERT INTO `users_network_dick` VALUES ('503', 'Elite&nbsp;沈一学习交流群1', '1151865774', 'zzq1', '0', '527', '0', null);
INSERT INTO `users_network_dick` VALUES ('502', 'Elite❤低?打字编辑2', '1143967102', 'zzq1', '0', '498', '0', null);
INSERT INTO `users_network_dick` VALUES ('501', '（A）?苏淇传图', '1130968636', 'zzq1', '0', '247', '0', null);
INSERT INTO `users_network_dick` VALUES ('500', '2022届17班历史学习群', '1080890418', 'zzq1', '0', '53', '0', null);
INSERT INTO `users_network_dick` VALUES ('499', '高一&nbsp;17英语群', '1053530793', 'zzq1', '0', '55', '0', null);
INSERT INTO `users_network_dick` VALUES ('498', '（C）?苏淇传图群', '1051972677', 'zzq1', '0', '425', '0', null);
INSERT INTO `users_network_dick` VALUES ('497', '高2022级17班&nbsp;地理群', '1049710379', 'zzq1', '0', '61', '0', null);
INSERT INTO `users_network_dick` VALUES ('496', 'Elite?新人讲课会议3', '1048023026', 'zzq1', '0', '1218', '0', null);
INSERT INTO `users_network_dick` VALUES ('495', '?学习交流群', '1042619475', 'zzq1', '0', '79', '0', null);
INSERT INTO `users_network_dick` VALUES ('493', '22届17班数学群', '936281379', 'zzq1', '0', '61', '0', null);
INSERT INTO `users_network_dick` VALUES ('494', '高三(17)班班群', '956810947', 'zzq1', '0', '77', '0', null);
INSERT INTO `users_network_dick` VALUES ('492', '国家一级奖学金交流群', '931449217', 'zzq1', '0', '57', '0', null);
INSERT INTO `users_network_dick` VALUES ('490', '青青草原', '877856009', 'zzq1', '0', '112', '0', null);
INSERT INTO `users_network_dick` VALUES ('491', '时光瘦了&#039;', '883609920', 'zzq1', '0', '159', '0', null);
INSERT INTO `users_network_dick` VALUES ('489', '线上录入卅', '877829856', 'zzq1', '0', '70', '0', null);
INSERT INTO `users_network_dick` VALUES ('488', '?官方拼多多捡漏28群', '876206869', 'zzq1', '0', '1976', '0', null);
INSERT INTO `users_network_dick` VALUES ('487', '资中粉丝群', '871925012', 'zzq1', '0', '873', '0', null);
INSERT INTO `users_network_dick` VALUES ('486', '高二17班政治群', '819418118', 'zzq1', '0', '56', '0', null);
INSERT INTO `users_network_dick` VALUES ('485', 'Elite?写小说码字群', '817385183', 'zzq1', '0', '1770', '0', null);
INSERT INTO `users_network_dick` VALUES ('483', 'GSY、战阁电竞战队交流', '762373132', 'zzq1', '0', '36', '0', null);
INSERT INTO `users_network_dick` VALUES ('484', '通知24群?主动加你们', '792193309', 'zzq1', '0', '1571', '0', null);
INSERT INTO `users_network_dick` VALUES ('482', '全网优质扩列交友群', '730942335', 'zzq1', '0', '68', '0', null);
INSERT INTO `users_network_dick` VALUES ('481', '??????网拍', '555822458', 'zzq1', '0', '996', '0', null);
INSERT INTO `users_network_dick` VALUES ('480', 'Elite?外宣素材1群', '536989796', 'zzq1', '0', '386', '0', null);
INSERT INTO `users_network_dick` VALUES ('479', 'Elite?&nbsp;购物优惠总群', '366674274', 'zzq1', '0', '2660', '0', null);
INSERT INTO `users_network_dick` VALUES ('477', '红小2016级４班', '317305789', 'zzq1', '0', '56', '0', null);
INSERT INTO `users_network_dick` VALUES ('478', 'Elite&nbsp;?购物总群2群', '333855845', 'zzq1', '0', '2898', '0', null);
INSERT INTO `users_network_dick` VALUES ('475', '资中一中交流群', '113143389', 'zzq1', '0', '1396', '0', null);
INSERT INTO `users_network_dick` VALUES ('476', '资中一中校友群&lt;$ÿĀ&gt;', '113516780', 'zzq1', '0', '1278', '0', null);
INSERT INTO `users_network_dick` VALUES ('474', '20级工造1、2班大班群', '1160043105', 'zzq1234', '0', '104', '0', null);
INSERT INTO `users_network_dick` VALUES ('473', '工造20.2班大家庭', '1101312885', 'zzq1234', '0', '57', '0', null);
INSERT INTO `users_network_dick` VALUES ('398', '软件19.5班大家庭', '744301887', 'ly1', '0', '63', '0', null);
INSERT INTO `users_network_dick` VALUES ('399', '软件19.5、6班公告群', '806671557', 'ly1', '0', '122', '0', null);
INSERT INTO `users_network_dick` VALUES ('400', '奥利给', '839714042', 'ly1', '0', '7', '0', null);
INSERT INTO `users_network_dick` VALUES ('401', '人走茶凉?', '671623106', 'zzq1234', '0', '39', '0', null);
INSERT INTO `users_network_dick` VALUES ('402', '思想微电影1组', '703071044', 'zzq1234', '0', '10', '0', null);
INSERT INTO `users_network_dick` VALUES ('403', '主持团招新群', '319602470', 'zzq1234', '0', '45', '0', null);
INSERT INTO `users_network_dick` VALUES ('404', '机加高三&nbsp;二班', '185184291', 'zzq1234', '0', '56', '0', null);
INSERT INTO `users_network_dick` VALUES ('405', '成都石化工业学校总群', '156495664', 'ly1', '0', '828', '0', null);
INSERT INTO `users_network_dick` VALUES ('406', '129主持', '391628798', 'zzq1234', '0', '3', '0', null);
INSERT INTO `users_network_dick` VALUES ('407', '5班室长群', '165676612', 'ly1', '0', '18', '0', null);
INSERT INTO `users_network_dick` VALUES ('408', '611寝室', '259779729', 'ly1', '0', '14', '0', null);
INSERT INTO `users_network_dick` VALUES ('409', '深夜创业群', '312118100', 'ly1', '0', '3', '0', null);
INSERT INTO `users_network_dick` VALUES ('410', '星星✡️的生日会', '338658831', 'ly1', '0', '8', '0', null);
INSERT INTO `users_network_dick` VALUES ('411', '朵朵奇葩', '483182344', 'ly1', '0', '43', '0', null);
INSERT INTO `users_network_dick` VALUES ('412', '三食堂贡茶（炸鸡，汉', '438055315', 'zzq1234', '0', '1614', '0', null);
INSERT INTO `users_network_dick` VALUES ('413', '机加1701', '487476516', 'zzq1234', '0', '72', '0', null);
INSERT INTO `users_network_dick` VALUES ('414', '十七届挑战杯决赛', '536351680', 'zzq1234', '0', '6', '0', null);
INSERT INTO `users_network_dick` VALUES ('415', '光辉岁月', '607657529', 'zzq1234', '0', '55', '0', null);
INSERT INTO `users_network_dick` VALUES ('416', '川电机2020互助①群', '535669810', 'ly1', '0', '1584', '0', null);
INSERT INTO `users_network_dick` VALUES ('417', '老年人交流大会', '608305829', 'zzq1234', '0', '23', '0', null);
INSERT INTO `users_network_dick` VALUES ('418', '高二（2）班学生群', '587638457', 'ly1', '0', '45', '0', null);
INSERT INTO `users_network_dick` VALUES ('419', '主持人', '615126413', 'zzq1234', '0', '4', '0', null);
INSERT INTO `users_network_dick` VALUES ('397', '拉基鲁', '277056231', 'ly1', '0', '7', '0', null);
INSERT INTO `users_network_dick` VALUES ('396', '小窝??', '1094651752', 'ly1', '0', '4', '0', null);
INSERT INTO `users_network_dick` VALUES ('395', '&lt;$ÿĀ&gt;404&lt;$ÿĀ&gt;', '808701914', 'ly1', '0', '6', '0', null);
INSERT INTO `users_network_dick` VALUES ('394', '彭州小组', '751192682', 'ly1', '0', '3', '0', null);
INSERT INTO `users_network_dick` VALUES ('392', '相亲相爱一家人', '1129262351', 'w1', '0', '27', '0', null);
INSERT INTO `users_network_dick` VALUES ('393', '皓战队', '369391326', 'ly1', '0', '20', '0', null);
INSERT INTO `users_network_dick` VALUES ('390', 'SCHOOOOOL', '860468495', 'w1', '0', '38', '0', null);
INSERT INTO `users_network_dick` VALUES ('391', '虎虎生威', '893814273', 'w1', '0', '6', '0', null);
INSERT INTO `users_network_dick` VALUES ('389', '灾舅子', '855794242', 'w1', '0', '16', '0', null);
INSERT INTO `users_network_dick` VALUES ('388', '职中2019春财会班', '838196345', 'w1', '0', '43', '0', null);
INSERT INTO `users_network_dick` VALUES ('387', '基佬们&nbsp;怕是活在梦里', '794436184', 'w1', '0', '5', '0', null);
INSERT INTO `users_network_dick` VALUES ('386', '英雄联盟手游玩家交流', '793652725', 'w1', '0', '1950', '0', null);
INSERT INTO `users_network_dick` VALUES ('385', '基佬连麦群', '674333699', 'w1', '0', '6', '0', null);
INSERT INTO `users_network_dick` VALUES ('384', '【谨防私信骗钱】OurPla', '293630348', 'w1', '0', '1536', '0', null);
INSERT INTO `users_network_dick` VALUES ('382', '点点滴滴是回忆啊！', '479389017', 'w1', '0', '59', '0', null);
INSERT INTO `users_network_dick` VALUES ('383', '基佬连麦群', '674467416', 'w1', '0', '7', '0', null);
INSERT INTO `users_network_dick` VALUES ('440', '水电费', '823516631', 'ly1', '0', '11', '0', null);
INSERT INTO `users_network_dick` VALUES ('439', '第八组', '813384208', 'ly1', '0', '20', '0', null);
INSERT INTO `users_network_dick` VALUES ('438', '川电机马克思主义理论', '806788335', 'ly1', '0', '159', '0', null);
INSERT INTO `users_network_dick` VALUES ('437', '成都三人行', '781063353', 'ly1', '0', '3', '0', null);
INSERT INTO `users_network_dick` VALUES ('435', '第六届川飞翼轮滑协会', '750486449', 'ly1', '0', '94', '0', null);
INSERT INTO `users_network_dick` VALUES ('436', 'PHP', '767600103', 'ly1', '0', '8', '0', null);
INSERT INTO `users_network_dick` VALUES ('434', '叮当校园【川电机】①', '749854392', 'ly1', '0', '966', '0', null);
INSERT INTO `users_network_dick` VALUES ('433', '我的祖国', '726521140', 'zzq1234', '0', '49', '0', null);
INSERT INTO `users_network_dick` VALUES ('432', '巡逻队', '705318188', 'ly1', '0', '5', '0', null);
INSERT INTO `users_network_dick` VALUES ('431', '大艺节表彰大会领奖人', '718489191', 'zzq1234', '0', '32', '0', null);
INSERT INTO `users_network_dick` VALUES ('430', '车队群', '702164672', 'ly1', '0', '6', '0', null);
INSERT INTO `users_network_dick` VALUES ('429', '红色情景剧工作人员群', '712992017', 'zzq1234', '0', '28', '0', null);
INSERT INTO `users_network_dick` VALUES ('428', '资源学习交流群', '701859175', 'ly1', '0', '95', '0', null);
INSERT INTO `users_network_dick` VALUES ('427', '巡逻队', '705318188', 'zzq1234', '0', '5', '0', null);
INSERT INTO `users_network_dick` VALUES ('425', '健身社新生群（19届）', '659285552', 'ly1', '0', '51', '0', null);
INSERT INTO `users_network_dick` VALUES ('426', '淘宝活动赚外快', '663133816', 'zzq1234', '0', '14', '0', null);
INSERT INTO `users_network_dick` VALUES ('424', '2班评议小组', '655974955', 'zzq1234', '0', '8', '0', null);
INSERT INTO `users_network_dick` VALUES ('420', '电子系文艺委员群', '621439264', 'ly1', '0', '52', '0', null);
INSERT INTO `users_network_dick` VALUES ('421', '2021年成都志愿填报工', '646839493', 'ly1', '0', '57', '0', null);
INSERT INTO `users_network_dick` VALUES ('422', '普通话培训2021春', '625058550', 'zzq1234', '0', '234', '0', null);
INSERT INTO `users_network_dick` VALUES ('423', '班级冠状病毒防疫群', '652266017', 'ly1', '0', '41', '0', null);
INSERT INTO `users_network_dick` VALUES ('465', '主持团候选人', '1021153826', 'zzq1234', '0', '6', '0', null);
INSERT INTO `users_network_dick` VALUES ('466', '朗诵', '1022509362', 'zzq1234', '0', '14', '0', null);
INSERT INTO `users_network_dick` VALUES ('463', '2020秋助学金申请组', '978116066', 'zzq1234', '0', '96', '0', null);
INSERT INTO `users_network_dick` VALUES ('464', '团课节目', '984240325', 'zzq1234', '0', '23', '0', null);
INSERT INTO `users_network_dick` VALUES ('462', '播音主持&nbsp;|&nbsp;新闻中心', '946459643', 'zzq1234', '0', '12', '0', null);
INSERT INTO `users_network_dick` VALUES ('461', '阙月离落泪的队伍', '927333046', 'zzq1234', '0', '16', '0', null);
INSERT INTO `users_network_dick` VALUES ('460', '程雪、tu&nbsp;tu&nbsp;tu、珠穆…', '915290930', 'zzq1234', '0', '3', '0', null);
INSERT INTO `users_network_dick` VALUES ('459', '川电机大学生艺术团', '869240392', 'zzq1234', '0', '11', '0', null);
INSERT INTO `users_network_dick` VALUES ('458', 'HikT。、迃幵、tu&nbsp;tu&nbsp;tu', '852962268', 'zzq1234', '0', '6', '0', null);
INSERT INTO `users_network_dick` VALUES ('457', '讲宪法', '820502153', 'zzq1234', '0', '2', '0', null);
INSERT INTO `users_network_dick` VALUES ('456', '(&#92;赵珞安^@的小队', '805773073', 'zzq1234', '0', '5', '0', null);
INSERT INTO `users_network_dick` VALUES ('455', '美食广场曹氏鸭脖@王', '786923381', 'zzq1234', '0', '1264', '0', null);
INSERT INTO `users_network_dick` VALUES ('441', '演讲与口才协会招新', '871421383', 'ly1', '0', '102', '0', null);
INSERT INTO `users_network_dick` VALUES ('442', '软件19.5班ps', '877154994', 'ly1', '0', '54', '0', null);
INSERT INTO `users_network_dick` VALUES ('443', '4&nbsp;楼室长群', '939927463', 'ly1', '0', '47', '0', null);
INSERT INTO `users_network_dick` VALUES ('444', '成都香酥鸭套饭', '942026931', 'ly1', '0', '79', '0', null);
INSERT INTO `users_network_dick` VALUES ('445', '养老院', '963977083', 'ly1', '0', '18', '0', null);
INSERT INTO `users_network_dick` VALUES ('446', '加丰美食潮味周黑鸭外', '756926097', 'zzq1234', '0', '2162', '0', null);
INSERT INTO `users_network_dick` VALUES ('447', '咳咳', '759362364', 'zzq1234', '0', '4', '0', null);
INSERT INTO `users_network_dick` VALUES ('448', '统招志愿填报咨询群', '971695443', 'ly1', '0', '66', '0', null);
INSERT INTO `users_network_dick` VALUES ('449', '最强王者寝室', '771698801', 'zzq1234', '0', '6', '0', null);
INSERT INTO `users_network_dick` VALUES ('450', '最强团队精英群', '1018978386', 'ly1', '0', '18', '0', null);
INSERT INTO `users_network_dick` VALUES ('451', '王者嘿嘿嘿', '1057163868', 'ly1', '0', '7', '0', null);
INSERT INTO `users_network_dick` VALUES ('452', '老友创建的群', '1090278957', 'ly1', '0', '5', '0', null);
INSERT INTO `users_network_dick` VALUES ('453', '凉屋·元气骑士官方1群', '781989311', 'zzq1234', '0', '1756', '0', null);
INSERT INTO `users_network_dick` VALUES ('454', '韩式炸鸡4店', '781994302', 'zzq1234', '0', '155', '0', null);
INSERT INTO `users_network_dick` VALUES ('472', '大学生艺术团主持团', '1063025768', 'zzq1234', '0', '16', '0', null);
INSERT INTO `users_network_dick` VALUES ('471', '三食堂重庆小面群', '1061528946', 'zzq1234', '0', '1450', '0', null);
INSERT INTO `users_network_dick` VALUES ('469', '廾匸.、乔颜妃.', '1034829346', 'zzq1', '0', '2', '0', null);
INSERT INTO `users_network_dick` VALUES ('470', 'QQ互赞娱乐群', '914614394', 'zzq1', '0', '202', '0', null);
INSERT INTO `users_network_dick` VALUES ('467', '辰光、素素素素素的豆', '1022900638', 'zzq1234', '0', '6', '0', null);
INSERT INTO `users_network_dick` VALUES ('468', '和风和雨和烟起', '689837896', 'zzq1', '0', '15', '0', null);
INSERT INTO `users_network_dick` VALUES ('531', '猪圈', '704331507', 'w4', '0', '6', '0', null);
INSERT INTO `users_network_dick` VALUES ('532', '期末幼儿舞蹈群', '925314158', 'w3', '0', '8', '0', null);
INSERT INTO `users_network_dick` VALUES ('533', '一窝憨憨', '799161479', 'w4', '0', '143', '0', null);
INSERT INTO `users_network_dick` VALUES ('534', '扫黄打黑', '912845914', 'w4', '0', '34', '0', null);
INSERT INTO `users_network_dick` VALUES ('535', '⚡沙雕网友斗图群②', '926177635', 'w3', '0', '363', '0', null);
INSERT INTO `users_network_dick` VALUES ('536', '105寝室', '936402654', 'w3', '0', '7', '0', null);
INSERT INTO `users_network_dick` VALUES ('537', '我们的家（19春幼师1班', '1017524189', 'w3', '0', '69', '0', null);
INSERT INTO `users_network_dick` VALUES ('538', '扫黄打黑', '912845914', 'b4', '0', '34', '0', null);
INSERT INTO `users_network_dick` VALUES ('539', '315养猪场', '622105509', 'b4', '0', '11', '0', null);
INSERT INTO `users_network_dick` VALUES ('540', '初2016级4班', '667578414', 'b4', '0', '48', '0', null);
INSERT INTO `users_network_dick` VALUES ('541', '友好交流', '107559444', 'w5', '0', '2', '0', null);
INSERT INTO `users_network_dick` VALUES ('542', '小学毕业的精神病患者', '971439410', 'b4', '0', '52', '0', null);
INSERT INTO `users_network_dick` VALUES ('543', '扫黄打黑', '912845914', 'b5', '0', '34', '0', null);
INSERT INTO `users_network_dick` VALUES ('544', '315养猪场', '622105509', 'b5', '0', '11', '0', null);
INSERT INTO `users_network_dick` VALUES ('545', '初2016级4班', '667578414', 'b5', '0', '48', '0', null);
INSERT INTO `users_network_dick` VALUES ('546', '小学毕业的精神病患者', '971439410', 'b5', '0', '52', '0', null);
INSERT INTO `users_network_dick` VALUES ('547', '小熊捡漏情报局B3', '791794421', 'w5', '0', '1863', '0', null);
INSERT INTO `users_network_dick` VALUES ('548', '耶斯', '796729994', 'w5', '0', '25', '0', null);
INSERT INTO `users_network_dick` VALUES ('549', '初2019届（1）班♡', '796832440', 'w5', '0', '34', '0', null);
INSERT INTO `users_network_dick` VALUES ('550', '*', '857673745', 'w5', '0', '3', '0', null);
INSERT INTO `users_network_dick` VALUES ('551', '扫黄打黑', '912845914', 'w5', '0', '34', '0', null);
INSERT INTO `users_network_dick` VALUES ('552', '相亲相爱一家人', '965312670', 'w5', '0', '3', '0', null);
INSERT INTO `users_network_dick` VALUES ('553', '旧巷里的猫', '207568187', 'b6', '0', '44', '0', null);
INSERT INTO `users_network_dick` VALUES ('554', '腾讯成长平台', '560019052', 'b6', '0', '143', '0', null);
INSERT INTO `users_network_dick` VALUES ('555', '【嗨聊中】CFM官方福利', '825394766', 'b6', '0', '1627', '0', null);
INSERT INTO `users_network_dick` VALUES ('556', '英雄联盟手游玩家交流', '829015279', 'b6', '0', '1950', '0', null);
INSERT INTO `users_network_dick` VALUES ('557', '新场℡零动力巡山社', '961358245', 'b6', '0', '16', '0', null);
INSERT INTO `users_network_dick` VALUES ('558', '『云想』', '7655822', '123456', '0', '6', '0', null);
INSERT INTO `users_network_dick` VALUES ('559', '百度经验官方群', '254880947', '123456', '0', '1958', '0', null);
INSERT INTO `users_network_dick` VALUES ('560', '广西古董鉴赏群', '319101829', '123456', '0', '395', '0', null);
INSERT INTO `users_network_dick` VALUES ('561', '征程高端古泉拍卖', '591276324', '123456', '0', '211', '0', null);
INSERT INTO `users_network_dick` VALUES ('562', '财院闲置物品交换', '596429135', '123456', '0', '3000', '0', null);
INSERT INTO `users_network_dick` VALUES ('563', '凌云翼云文件共享', '755521126', '123456', '0', '4', '0', null);
INSERT INTO `users_network_dick` VALUES ('564', '相亲相爱一家人', '343475197', 'zzq3', '0', '4', '0', null);
INSERT INTO `users_network_dick` VALUES ('565', '306美女群', '415945206', 'zzq3', '0', '7', '0', null);
INSERT INTO `users_network_dick` VALUES ('566', '炫舞憨憨交流群', '469643741', 'zzq3', '0', '31', '0', null);
INSERT INTO `users_network_dick` VALUES ('567', '水南职中校园群', '631670469', 'zzq3', '0', '341', '0', null);
INSERT INTO `users_network_dick` VALUES ('568', '红浪漫', '649495580', 'zzq3', '0', '36', '0', null);
INSERT INTO `users_network_dick` VALUES ('569', '19魔力班&nbsp;安全教育平台', '703221054', 'zzq3', '0', '39', '0', null);
INSERT INTO `users_network_dick` VALUES ('570', '71无锡工学实习', '717993978', 'zzq3', '0', '133', '0', null);
INSERT INTO `users_network_dick` VALUES ('571', '筱征涨赞②群', '879399677', 'zzq3', '0', '255', '0', null);
INSERT INTO `users_network_dick` VALUES ('572', '王者开黑', '971541555', 'zzq3', '0', '28', '0', null);
INSERT INTO `users_network_dick` VALUES ('573', '?', '218392714', 'zzq4', '0', '5', '0', null);
INSERT INTO `users_network_dick` VALUES ('574', '抖音互关②群', '348971284', 'zzq4', '0', '12', '0', null);
INSERT INTO `users_network_dick` VALUES ('575', '刘俊宏学生群', '526336579', 'zzq4', '0', '143', '0', null);
INSERT INTO `users_network_dick` VALUES ('576', '板栗九二班', '536801987', 'zzq4', '0', '33', '0', null);
INSERT INTO `users_network_dick` VALUES ('577', '优质互赞交友群', '1015032635', 'zzq3', '0', '1839', '0', null);
INSERT INTO `users_network_dick` VALUES ('578', '水南职中校园群', '631670469', 'zzq4', '0', '340', '0', null);
INSERT INTO `users_network_dick` VALUES ('579', '19计2课代表交流群', '659826218', 'zzq4', '0', '8', '0', null);
INSERT INTO `users_network_dick` VALUES ('580', '19计升2劳动组组长群.', '694427672', 'zzq4', '0', '10', '0', null);
INSERT INTO `users_network_dick` VALUES ('581', '19计升1班班务群', '831735086', 'zzq4', '0', '50', '0', null);
INSERT INTO `users_network_dick` VALUES ('582', '筱征涨赞①群', '1137198923', 'zzq3', '0', '826', '0', null);
INSERT INTO `users_network_dick` VALUES ('583', '风牵一袖汉服官方群', '875221922', 'zzq4', '0', '1638', '0', null);
INSERT INTO `users_network_dick` VALUES ('584', '吃鸡姐妹', '887592064', 'zzq4', '0', '5', '0', null);
INSERT INTO `users_network_dick` VALUES ('585', '轰炸憨憨群.', '902010526', 'zzq4', '0', '38', '0', null);
INSERT INTO `users_network_dick` VALUES ('586', '19计升2班英语交流群', '902586126', 'zzq4', '0', '43', '0', null);
INSERT INTO `users_network_dick` VALUES ('587', '王者荣耀-AG秀你一身血', '822257087', 'zzq6', '0', '1', '0', null);
INSERT INTO `users_network_dick` VALUES ('588', 'MD喳喳っ的队伍', '895297374', 'zzq6', '0', '1', '0', null);
INSERT INTO `users_network_dick` VALUES ('589', '青年大学习', '913507617', 'zzq4', '0', '52', '0', null);
INSERT INTO `users_network_dick` VALUES ('590', '19计升4', '1149778718', 'zzq6', '0', '55', '0', null);
INSERT INTO `users_network_dick` VALUES ('591', '数学加油站', '942783345', 'zzq4', '0', '76', '0', null);
INSERT INTO `users_network_dick` VALUES ('592', '二班的狗窝', '219689251', 'zzq6', '0', '39', '0', null);
INSERT INTO `users_network_dick` VALUES ('593', '19计升2班室长群', '1016716985', 'zzq4', '0', '8', '0', null);
INSERT INTO `users_network_dick` VALUES ('594', '信息专业班委干部通知', '370295760', 'zzq6', '0', '54', '0', null);
INSERT INTO `users_network_dick` VALUES ('595', '沙雕二班❤❤❤❤', '546482976', 'zzq6', '0', '35', '0', null);
INSERT INTO `users_network_dick` VALUES ('596', '水南职中19级校园群', '1028345487', 'zzq4', '0', '127', '0', null);
INSERT INTO `users_network_dick` VALUES ('597', '2019级14班同学群', '549989766', 'zzq7', '0', '83', '0', null);
INSERT INTO `users_network_dick` VALUES ('598', '拍照集美', '1053469606', 'zzq4', '0', '6', '0', null);
INSERT INTO `users_network_dick` VALUES ('599', '破产姐妹', '1058094542', 'zzq4', '0', '7', '0', null);
INSERT INTO `users_network_dick` VALUES ('600', '陪伴', '644095118', 'zzq6', '0', '100', '0', null);
INSERT INTO `users_network_dick` VALUES ('601', '王者荣耀-战个爽战队', '645952732', 'zzq6', '0', '5', '0', null);
INSERT INTO `users_network_dick` VALUES ('602', '1中，刘队', '7323760', 'zzq7', '0', '140', '0', null);
INSERT INTO `users_network_dick` VALUES ('603', '懒鬼群', '660529774', 'zzq6', '0', '9', '0', null);
INSERT INTO `users_network_dick` VALUES ('604', '19计升男生八霸', '703537460', 'zzq6', '0', '10', '0', null);
INSERT INTO `users_network_dick` VALUES ('605', '6.3小窝窝', '579018038', 'zzq7', '0', '64', '0', null);
INSERT INTO `users_network_dick` VALUES ('606', '六年二班', '709617316', 'zzq6', '0', '21', '0', null);
INSERT INTO `users_network_dick` VALUES ('607', '仙女仙女??', '619567316', 'zzq7', '0', '5', '0', null);
INSERT INTO `users_network_dick` VALUES ('608', '羊村！', '638834113', 'zzq7', '0', '4', '0', null);
INSERT INTO `users_network_dick` VALUES ('609', '初2016级2班', '815326485', 'zzq6', '0', '46', '0', null);
INSERT INTO `users_network_dick` VALUES ('610', '水南职中。', '1076351881', 'zzq4', '0', '340', '0', null);
INSERT INTO `users_network_dick` VALUES ('611', '19航空班', '717499421', 'zzq7', '0', '41', '0', null);
INSERT INTO `users_network_dick` VALUES ('612', '托儿所', '718925347', 'zzq7', '0', '10', '0', null);
INSERT INTO `users_network_dick` VALUES ('613', '19空乘?', '892135565', 'zzq7', '0', '35', '0', null);
INSERT INTO `users_network_dick` VALUES ('614', '明日之后梅尔医院底里', '821062158', 'zzq6', '0', '225', '0', null);
INSERT INTO `users_network_dick` VALUES ('615', '。。。', '959547691', 'zzq7', '0', '12', '0', null);
INSERT INTO `users_network_dick` VALUES ('616', '《202》', '936161190', 'zzq6', '0', '10', '0', null);
INSERT INTO `users_network_dick` VALUES ('617', '子子之家?', '1011811277', 'zzq7', '0', '8', '0', null);
INSERT INTO `users_network_dick` VALUES ('618', '19计服升', '974372429', 'zzq6', '0', '76', '0', null);
INSERT INTO `users_network_dick` VALUES ('619', 'LO、A7、澈', '1036311583', 'zzq6', '0', '5', '0', null);
INSERT INTO `users_network_dick` VALUES ('620', '水南职中。', '1076351881', 'zzq7', '0', '340', '0', null);
INSERT INTO `users_network_dick` VALUES ('621', '拉屎小分队?', '893642535', 'zzq8', '0', '2', '0', null);
INSERT INTO `users_network_dick` VALUES ('622', '水南F3', '1132257938', 'zzq8', '0', '5', '0', null);
INSERT INTO `users_network_dick` VALUES ('623', '411的美女', '264547245', 'zzq8', '0', '6', '0', null);
INSERT INTO `users_network_dick` VALUES ('624', '资中职校水南校区19电', '589424811', 'zzq8', '0', '59', '0', null);
INSERT INTO `users_network_dick` VALUES ('625', '水南职中校园群', '631670469', 'zzq8', '0', '340', '0', null);
INSERT INTO `users_network_dick` VALUES ('626', '玉带初2019届二班', '668756640', 'zzq8', '0', '62', '0', null);
INSERT INTO `users_network_dick` VALUES ('627', '19化工班学生学习群', '244614145', 'ly4', '0', '52', '0', null);
INSERT INTO `users_network_dick` VALUES ('628', '19化工青年学习团', '336026526', 'ly4', '0', '51', '0', null);
INSERT INTO `users_network_dick` VALUES ('629', '9.2八卦阵', '457353488', 'ly4', '0', '47', '0', null);
INSERT INTO `users_network_dick` VALUES ('630', '3年时光，永不催散', '527103512', 'ly4', '0', '45', '0', null);
INSERT INTO `users_network_dick` VALUES ('631', '老赵头的圈子', '625949074', 'ly4', '0', '10', '0', null);
INSERT INTO `users_network_dick` VALUES ('632', '水南职中校园群', '631670469', 'ly4', '0', '340', '0', null);
INSERT INTO `users_network_dick` VALUES ('633', '爱芯、罗斯、.&#039;财&#039;.', '780078486', 'ly4', '0', '5', '0', null);
INSERT INTO `users_network_dick` VALUES ('634', '安全教育平台', '955985801', 'ly4', '0', '29', '0', null);
INSERT INTO `users_network_dick` VALUES ('635', '还记得那时的我们吗小', '966935738', 'ly4', '0', '22', '0', null);
INSERT INTO `users_network_dick` VALUES ('636', '水南职中19级校园群', '1028345487', 'ly4', '0', '127', '0', null);
INSERT INTO `users_network_dick` VALUES ('637', '一堆憨憨排排坐', '1041671074', 'ly4', '0', '10', '0', null);
INSERT INTO `users_network_dick` VALUES ('638', '刘俊宏学生群', '526336579', 'zzq10', '0', '143', '0', null);
INSERT INTO `users_network_dick` VALUES ('639', '2022届高考交流群②', '658195874', 'zzq10', '0', '1977', '0', null);
INSERT INTO `users_network_dick` VALUES ('640', '全网聊天处cp交友群', '734025556', 'zzq10', '0', '336', '0', null);
INSERT INTO `users_network_dick` VALUES ('641', '19本科班', '1145850572', 'zzq10', '0', '53', '0', null);
INSERT INTO `users_network_dick` VALUES ('642', '清华烂账们', '610299020', 'w10', '0', '4', '0', null);
INSERT INTO `users_network_dick` VALUES ('643', '。', '907935263', 'w10', '0', '9', '0', null);
INSERT INTO `users_network_dick` VALUES ('644', 'M8', '948198237', 'w10', '0', '16', '0', null);
INSERT INTO `users_network_dick` VALUES ('645', '巴啦啦小魔仙呜咔啦咔', '820298979', 'w10', '0', '7', '0', null);
INSERT INTO `users_network_dick` VALUES ('646', 'F4', '913174922', 'w10', '0', '4', '0', null);
INSERT INTO `users_network_dick` VALUES ('647', '基建首选人群', '1035685961', 'w10', '0', '76', '0', null);
INSERT INTO `users_network_dick` VALUES ('648', '5-2', '114539536', 'w10', '0', '6', '0', null);
INSERT INTO `users_network_dick` VALUES ('649', '颜值最高的2018届6班', '512736053', 'w10', '0', '38', '0', null);
INSERT INTO `users_network_dick` VALUES ('650', 'c.、欲。、ゞ&nbsp;正在缓…', '956804437', 'b1', '0', '3', '0', null);
INSERT INTO `users_network_dick` VALUES ('651', 'game', '1065512665', 'b1', '0', '15', '0', null);
INSERT INTO `users_network_dick` VALUES ('652', '高三2班级群', '281375422', 'b2', '0', '70', '0', null);
INSERT INTO `users_network_dick` VALUES ('653', '二班学习交流群', '744716168', 'b2', '0', '7', '0', null);
INSERT INTO `users_network_dick` VALUES ('654', '励志用腿毛思考玩赢狼', '938702056', 'b2', '0', '5', '0', null);
INSERT INTO `users_network_dick` VALUES ('655', '小兴土匪集团', '1037253078', 'b2', '0', '14', '0', null);
INSERT INTO `users_network_dick` VALUES ('656', '有手就行', '1061491363', 'b2', '0', '3', '0', null);
INSERT INTO `users_network_dick` VALUES ('657', '孤寡孤寡', '1071848024', 'b2', '0', '3', '0', null);
INSERT INTO `users_network_dick` VALUES ('658', '呉彧的队伍', '860933225', 'w3', '0', '1', '0', null);
INSERT INTO `users_network_dick` VALUES ('659', '2—7大家庭', '615457734', 'w3', '0', '5', '0', null);
INSERT INTO `users_network_dick` VALUES ('660', '2019级1班各科学习群', '221340675', 'w3', '0', '26', '0', null);
INSERT INTO `users_network_dick` VALUES ('661', '?', '280857726', 'w3', '0', '11', '0', null);
INSERT INTO `users_network_dick` VALUES ('662', '八班王者班赛群', '613317784', 'w3', '0', '22', '0', null);
INSERT INTO `users_network_dick` VALUES ('663', '四川——交流⑧', '644044395', 'w3', '0', '803', '0', null);
INSERT INTO `users_network_dick` VALUES ('664', '八班', '646346873', 'w3', '0', '58', '0', null);
INSERT INTO `users_network_dick` VALUES ('665', 'y、A、安', '686145589', 'w3', '0', '12', '0', null);
INSERT INTO `users_network_dick` VALUES ('666', '球友！', '711630537', 'w3', '0', '18', '0', null);
INSERT INTO `users_network_dick` VALUES ('667', '我不晓得的哦', '715600176', 'w3', '0', '28', '0', null);
INSERT INTO `users_network_dick` VALUES ('668', '影视TV', '727824510', 'w3', '0', '96', '0', null);
INSERT INTO `users_network_dick` VALUES ('669', '日龙包', '734177015', 'w3', '0', '10', '0', null);
INSERT INTO `users_network_dick` VALUES ('670', '夸灿&nbsp;kcan', '741888057', 'w3', '0', '23', '0', null);
INSERT INTO `users_network_dick` VALUES ('671', 'HM枪王军团', '751237439', 'w3', '0', '36', '0', null);
INSERT INTO `users_network_dick` VALUES ('672', '解冻售后二群', '791878449', 'w3', '0', '116', '0', null);
INSERT INTO `users_network_dick` VALUES ('673', '全民赛车场', '823438082', 'w3', '0', '14', '0', null);
INSERT INTO `users_network_dick` VALUES ('674', '怡红院', '833780062', 'w3', '0', '27', '0', null);
INSERT INTO `users_network_dick` VALUES ('675', '最不一般的八班', '908115791', 'w3', '0', '56', '0', null);
INSERT INTO `users_network_dick` VALUES ('676', '2019届一班', '933250965', 'w3', '0', '42', '0', null);
INSERT INTO `users_network_dick` VALUES ('677', 'A-兴欣实货铺?', '937236281', 'w3', '0', '296', '0', null);
INSERT INTO `users_network_dick` VALUES ('678', '狗子大队', '949252939', 'w3', '0', '33', '0', null);
INSERT INTO `users_network_dick` VALUES ('679', '(≧ω≦)/', '976929625', 'w3', '0', '7', '0', null);
INSERT INTO `users_network_dick` VALUES ('680', '一和', '468848504', 'w4', '0', '20', '0', null);
INSERT INTO `users_network_dick` VALUES ('681', '自信小伙.??', '686663778', 'w4', '0', '19', '0', null);
INSERT INTO `users_network_dick` VALUES ('682', '未来明星', '314970662', 'w4', '0', '30', '0', null);
INSERT INTO `users_network_dick` VALUES ('683', '高二四班班群', '461265674', 'w4', '0', '58', '0', null);
INSERT INTO `users_network_dick` VALUES ('684', '龙会中学校友群', '1085876364', 'w3', '0', '979', '0', null);
INSERT INTO `users_network_dick` VALUES ('685', '自强高2024届群', '484501965', 'w4', '0', '134', '0', null);
INSERT INTO `users_network_dick` VALUES ('686', '@、失意.、…………', '1142620432', 'w3', '0', '4', '0', null);
INSERT INTO `users_network_dick` VALUES ('687', '天道', '574535345', 'w4', '0', '17', '0', null);
INSERT INTO `users_network_dick` VALUES ('688', 'y、A、安', '686145589', 'w4', '0', '12', '0', null);
INSERT INTO `users_network_dick` VALUES ('689', '快乐就好', '695975447', 'w4', '0', '15', '0', null);
INSERT INTO `users_network_dick` VALUES ('690', '自强大分队', '724295078', 'w4', '0', '11', '0', null);
INSERT INTO `users_network_dick` VALUES ('691', '自强3V3', '822711662', 'w4', '0', '25', '0', null);
INSERT INTO `users_network_dick` VALUES ('692', 'h、......、為難', '876861804', 'w4', '0', '6', '0', null);
INSERT INTO `users_network_dick` VALUES ('693', '河东街烂卡学校2022届', '907557045', 'w4', '0', '67', '0', null);
INSERT INTO `users_network_dick` VALUES ('694', '小怡.、纯欲、小玉.', '927537725', 'w4', '0', '36', '0', null);
INSERT INTO `users_network_dick` VALUES ('695', '4班球队', '933261739', 'w4', '0', '14', '0', null);
INSERT INTO `users_network_dick` VALUES ('696', '哦哦', '361915553', 'b3', '0', '2', '0', null);
INSERT INTO `users_network_dick` VALUES ('697', '第五人格语音群', '577206942', 'b3', '0', '9', '0', null);
INSERT INTO `users_network_dick` VALUES ('698', 'Furry王者快乐群', '701734458', 'b3', '0', '20', '0', null);
INSERT INTO `users_network_dick` VALUES ('699', '第五语音群', '827202295', 'b3', '0', '7', '0', null);
INSERT INTO `users_network_dick` VALUES ('700', '李白创建的群', '173965305', 'b3', '0', '5', '0', null);
INSERT INTO `users_network_dick` VALUES ('701', '一堆lsp', '365173650', 'b3', '0', '4', '0', null);
INSERT INTO `users_network_dick` VALUES ('702', '刘海洋是&nbsp;猪蹄', '687709011', 'b3', '0', '10', '0', null);
INSERT INTO `users_network_dick` VALUES ('703', '阿梦的小窝', '810649221', 'b3', '0', '42', '0', null);
INSERT INTO `users_network_dick` VALUES ('704', '熊猴的小窝?', '317560277', 'b3', '0', '714', '0', null);
INSERT INTO `users_network_dick` VALUES ('705', '?可以在群里找对象', '477633364', 'b3', '0', '90', '0', null);
INSERT INTO `users_network_dick` VALUES ('706', '王者荣耀-星辰天之城', '544927529', 'b3', '0', '4', '0', null);
INSERT INTO `users_network_dick` VALUES ('707', '糖糖折纸鸢?、宅浩', '591166835', 'b3', '0', '3', '0', null);
INSERT INTO `users_network_dick` VALUES ('708', '19届1班友谊群', '593878659', 'b3', '0', '39', '0', null);
INSERT INTO `users_network_dick` VALUES ('709', '鸠魃交友群', '761212237', 'b3', '0', '10', '0', null);
INSERT INTO `users_network_dick` VALUES ('710', '搬砖大队', '795382311', 'w5', '0', '11', '0', null);
INSERT INTO `users_network_dick` VALUES ('711', '昂昂的熊窝?', '766188402', 'b3', '0', '170', '0', null);
INSERT INTO `users_network_dick` VALUES ('712', '刘小弟求带的队伍', '794290968', 'b3', '0', '5', '0', null);
INSERT INTO `users_network_dick` VALUES ('713', '自强2019届学生群', '926724233', 'w5', '0', '71', '0', null);
INSERT INTO `users_network_dick` VALUES ('714', '智障三人组♡', '1060685749', 'w5', '0', '3', '0', null);
INSERT INTO `users_network_dick` VALUES ('715', '自强2022届6班学生群', '879186550', 'b3', '0', '64', '0', null);
INSERT INTO `users_network_dick` VALUES ('716', '??大家', '981070667', 'b3', '0', '10', '0', null);
INSERT INTO `users_network_dick` VALUES ('717', '自强初三的小阔耐们', '651606868', 'w5', '0', '33', '0', null);
INSERT INTO `users_network_dick` VALUES ('718', '作业交流群', '1025058856', 'b3', '0', '4', '0', null);
INSERT INTO `users_network_dick` VALUES ('719', '19级大家庭', '715206893', 'w5', '0', '75', '0', null);
INSERT INTO `users_network_dick` VALUES ('720', '王牌战队?', '1038793392', 'b3', '0', '64', '0', null);
INSERT INTO `users_network_dick` VALUES ('721', '自强2022届交友群', '280193942', 'w5', '0', '242', '0', null);
INSERT INTO `users_network_dick` VALUES ('722', '奥特曼警队(永团2016届)', '463115109', 'w5', '0', '35', '0', null);
INSERT INTO `users_network_dick` VALUES ('723', '2019级初中毕业级', '1021747106', 'w5', '0', '44', '0', null);
INSERT INTO `users_network_dick` VALUES ('724', '高一三班', '1057193172', 'w5', '0', '73', '0', null);
INSERT INTO `users_network_dick` VALUES ('725', '自强中学校友群', '1136673410', 'w5', '0', '553', '0', null);
INSERT INTO `users_network_dick` VALUES ('726', '打王者', '967453449', 'b5', '0', '1', '0', null);
INSERT INTO `users_network_dick` VALUES ('727', '初2019.10班', '700428537', 'b5', '0', '47', '0', null);
INSERT INTO `users_network_dick` VALUES ('728', '勇士团队', '737563208', 'b5', '0', '64', '0', null);
INSERT INTO `users_network_dick` VALUES ('729', '7班', '755564655', 'b5', '0', '61', '0', null);
INSERT INTO `users_network_dick` VALUES ('730', '吹牛批集团—战队群', '834597479', 'b5', '0', '32', '0', null);
INSERT INTO `users_network_dick` VALUES ('731', '自强中学校友群', '1136673410', 'b5', '0', '553', '0', null);

-- ----------------------------
-- Table structure for users_session
-- ----------------------------
DROP TABLE IF EXISTS `users_session`;
CREATE TABLE `users_session` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `users_account` text,
  `users_session` text,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=61 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users_session
-- ----------------------------
INSERT INTO `users_session` VALUES ('24', '123456', '{\'alive_time_s\': 1634916048, \'img_path\': \'wait\', \'scan_status\': \'false\', \'scan_numbers\': \'0-0\'}');
INSERT INTO `users_session` VALUES ('25', 'b9', '{\'alive_time_s\': 1634921685, \'img_path\': \'wait\', \'scan_status\': \'wait\', \'scan_numbers\': \'0-0\'}');
INSERT INTO `users_session` VALUES ('26', 'b1', '{\'alive_time_s\': 1634902461, \'img_path\': \'\\\\Collect\\\\temp\\\\f0544c94-30f7-4e62-b5d1-e72ec6f30e74.png\', \'scan_status\': \'finaly-2021-10-22 16:34:21\', \'scan_numbers\': \'2-2\'}');
INSERT INTO `users_session` VALUES ('27', 'w1', '{\'alive_time_s\': 1634893302, \'img_path\': \'\\\\Collect\\\\temp\\\\4ad618b3-d846-496d-a89f-e9ee9af85f06.png\', \'scan_status\': \'false\', \'scan_numbers\': \'0-0\'}');
INSERT INTO `users_session` VALUES ('28', 'ly1', '{\'alive_time_s\': 1634881130, \'img_path\': \'\\\\Collect\\\\temp\\\\c8a02875-82b7-4d0b-892c-a1a94b332bf7.png\', \'scan_status\': \'finaly-2021-10-22 10:38:50\', \'scan_numbers\': \'39-39\'}');
INSERT INTO `users_session` VALUES ('29', 'zzq1234', '{\'alive_time_s\': \'1634968349\', \'img_path\': \'\\\\Collect\\\\temp\\\\cf66a148-87b9-4c9a-a955-3f053b2b6bc0.png\', \'scan_status\': \'wait\', \'scan_numbers\': \'40-40\'}');
INSERT INTO `users_session` VALUES ('30', 'ly2', '{\'alive_time_s\': 1634898843, \'img_path\': \'\\\\Collect\\\\temp\\\\9091098a-d3a6-4ca4-a28e-be8a877e9d05.png\', \'scan_status\': \'false\', \'scan_numbers\': \'0-0\'}');
INSERT INTO `users_session` VALUES ('31', 'zzq1', '{\'alive_time_s\': 1634882695, \'img_path\': \'\\\\Collect\\\\temp\\\\ae8dec0a-5c62-4e90-adeb-29249d7d0802.png\', \'scan_status\': \'finaly-2021-10-22 11:04:55\', \'scan_numbers\': \'32-32\'}');
INSERT INTO `users_session` VALUES ('32', 'ly3', '{\'alive_time_s\': 1634899071, \'img_path\': \'\\\\Collect\\\\temp\\\\5c4dc5ed-5edf-45ce-ba4f-a3eae9bf3728.png\', \'scan_status\': \'success\', \'scan_numbers\': \'0-0\'}');
INSERT INTO `users_session` VALUES ('33', 'ly4', '{\'alive_time_s\': 1634900271, \'img_path\': \'\\\\Collect\\\\temp\\\\98680190-9c4f-4927-823c-6fc534a78a15.png\', \'scan_status\': \'finaly-2021-10-22 15:57:51\', \'scan_numbers\': \'11-11\'}');
INSERT INTO `users_session` VALUES ('34', 'ly5', '{\'alive_time_s\': 1634957191, \'img_path\': \'wait\', \'scan_status\': \'wait\', \'scan_numbers\': \'0-0\'}');
INSERT INTO `users_session` VALUES ('35', 'zzq2', '{\'alive_time_s\': 1634884281, \'img_path\': \'\\\\Collect\\\\temp\\\\1563557c-f69d-44a9-8373-5556b8d26ebc.png\', \'scan_status\': \'false\', \'scan_numbers\': \'0-0\'}');
INSERT INTO `users_session` VALUES ('36', 'ly6', '{\'alive_time_s\': 1634957223, \'img_path\': \'wait\', \'scan_status\': \'wait\', \'scan_numbers\': \'0-0\'}');
INSERT INTO `users_session` VALUES ('37', 'ly7', '{\'alive_time_s\': 1634957249, \'img_path\': \'wait\', \'scan_status\': \'wait\', \'scan_numbers\': \'0-0\'}');
INSERT INTO `users_session` VALUES ('38', 'ly8', '{\'alive_time_s\': 1634957278, \'img_path\': \'wait\', \'scan_status\': \'wait\', \'scan_numbers\': \'0-0\'}');
INSERT INTO `users_session` VALUES ('39', 'ly9', '{\'alive_time_s\': 1634881752, \'img_path\': \'\\\\Collect\\\\temp\\\\68f46d5a-c6ee-4ff0-99e2-a8d963418e2d.png\', \'scan_status\': \'false\', \'scan_numbers\': \'0-0\'}');
INSERT INTO `users_session` VALUES ('55', 'zzq4', '{\'alive_time_s\': 1634898848, \'img_path\': \'\\\\Collect\\\\temp\\\\2a1ae532-bc6d-41c2-af9a-a07b0a88b0b6.png\', \'scan_status\': \'finaly-2021-10-22 15:34:08\', \'scan_numbers\': \'19-19\'}');
INSERT INTO `users_session` VALUES ('40', '112', '{\'alive_time_s\': 1634883670, \'img_path\': \'\\\\Collect\\\\temp\\\\84336b12-05ba-4a01-9fcd-19a031cc483a.png\', \'scan_status\': \'false\', \'scan_numbers\': \'0-0\'}');
INSERT INTO `users_session` VALUES ('41', 'w2', '{\'alive_time_s\': \'1634979956\', \'img_path\': \'\\\\Collect\\\\temp\\\\c451e9ed-0762-4303-9f7c-1fcff8b9a826.png\', \'scan_status\': \'wait\', \'scan_numbers\': \'3-3\'}');
INSERT INTO `users_session` VALUES ('42', 'w3', '{\'alive_time_s\': 1634904202, \'img_path\': \'\\\\Collect\\\\temp\\\\9bcc30df-de38-4ac9-baf8-3e575efec483.png\', \'scan_status\': \'finaly-2021-10-22 17:03:22\', \'scan_numbers\': \'24-24\'}');
INSERT INTO `users_session` VALUES ('43', 'b2', '{\'alive_time_s\': 1634902734, \'img_path\': \'\\\\Collect\\\\temp\\\\694bf536-b226-4f76-92f6-d34401dc4961.png\', \'scan_status\': \'finaly-2021-10-22 16:38:54\', \'scan_numbers\': \'6-6\'}');
INSERT INTO `users_session` VALUES ('44', 'b3', '{\'alive_time_s\': 1634906292, \'img_path\': \'\\\\Collect\\\\temp\\\\b847ec74-68c9-406c-89f1-27c86faa74aa.png\', \'scan_status\': \'finaly-2021-10-22 17:38:12\', \'scan_numbers\': \'20-20\'}');
INSERT INTO `users_session` VALUES ('45', 'w4', '{\'alive_time_s\': 1634904690, \'img_path\': \'\\\\Collect\\\\temp\\\\d5e365bf-fd24-4676-9b6d-eedbee2a784f.png\', \'scan_status\': \'finaly-2021-10-22 17:11:30\', \'scan_numbers\': \'14-14\'}');
INSERT INTO `users_session` VALUES ('46', 'b4', '{\'alive_time_s\': 1634906449, \'img_path\': \'\\\\Collect\\\\temp\\\\76694305-35b2-4087-a08c-e8e9e89dd304.png\', \'scan_status\': \'false\', \'scan_numbers\': \'0-0\'}');
INSERT INTO `users_session` VALUES ('47', 'w5', '{\'alive_time_s\': 1634906559, \'img_path\': \'\\\\Collect\\\\temp\\\\be3ef6c6-9266-48c0-9851-b2efabe89b30.png\', \'scan_status\': \'finaly-2021-10-22 17:42:39\', \'scan_numbers\': \'10-10\'}');
INSERT INTO `users_session` VALUES ('48', 'b5', '{\'alive_time_s\': 1634907074, \'img_path\': \'\\\\Collect\\\\temp\\\\24f3dffd-755e-4bf1-96d8-70afaebcfb91.png\', \'scan_status\': \'finaly-2021-10-22 17:51:14\', \'scan_numbers\': \'6-6\'}');
INSERT INTO `users_session` VALUES ('49', 'w6', '{\'alive_time_s\': 1634964480, \'img_path\': \'wait\', \'scan_status\': \'wait\', \'scan_numbers\': \'0-0\'}');
INSERT INTO `users_session` VALUES ('50', 'b6', '{\'alive_time_s\': 1634907275, \'img_path\': \'\\\\Collect\\\\temp\\\\ab3ca13c-9431-4e70-bb85-e8f27a97867d.png\', \'scan_status\': \'false\', \'scan_numbers\': \'0-0\'}');
INSERT INTO `users_session` VALUES ('51', 'w10', '{\'alive_time_s\': 1634902106, \'img_path\': \'\\\\Collect\\\\temp\\\\075edfb8-978d-419e-8908-6103db8048be.png\', \'scan_status\': \'finaly-2021-10-22 16:28:27\', \'scan_numbers\': \'8-8\'}');
INSERT INTO `users_session` VALUES ('52', 'zzq10', '{\'alive_time_s\': 1634900897, \'img_path\': \'\\\\Collect\\\\temp\\\\bd96b4f4-dc5e-486a-9735-60fa046279f5.png\', \'scan_status\': \'finaly-2021-10-22 16:08:17\', \'scan_numbers\': \'4-4\'}');
INSERT INTO `users_session` VALUES ('53', 'zzq3', '{\'alive_time_s\': 1634898505, \'img_path\': \'\\\\Collect\\\\temp\\\\bcae2f86-386b-405d-b41c-75849fd78fa4.png\', \'scan_status\': \'finaly-2021-10-22 15:28:25\', \'scan_numbers\': \'11-11\'}');
INSERT INTO `users_session` VALUES ('54', '1234567', '{\'alive_time_s\': 1634892996, \'img_path\': \'\\\\Collect\\\\temp\\\\de3e1d80-35b1-4e84-82c3-6a097a64e35d.png\', \'scan_status\': \'false\', \'scan_numbers\': \'0-0\'}');
INSERT INTO `users_session` VALUES ('56', 's1', '{\'alive_time_s\': 1634974346, \'img_path\': \'wait\', \'scan_status\': \'wait\', \'scan_numbers\': \'0-0\'}');
INSERT INTO `users_session` VALUES ('57', 'zzq6', '{\'alive_time_s\': 1634899245, \'img_path\': \'\\\\Collect\\\\temp\\\\ce8301ff-6f20-4b76-9e55-a1ee948fc82c.png\', \'scan_status\': \'finaly-2021-10-22 15:40:45\', \'scan_numbers\': \'16-16\'}');
INSERT INTO `users_session` VALUES ('58', 'zzq7', '{\'alive_time_s\': 1634899306, \'img_path\': \'\\\\Collect\\\\temp\\\\717a6d12-9762-43df-a016-72825d1f4448.png\', \'scan_status\': \'finaly-2021-10-22 15:41:46\', \'scan_numbers\': \'11-11\'}');
INSERT INTO `users_session` VALUES ('59', 'zzq8', '{\'alive_time_s\': 1634899725, \'img_path\': \'\\\\Collect\\\\temp\\\\e654a158-ee20-4f6d-96b4-d704d3c59533.png\', \'scan_status\': \'finaly-2021-10-22 15:48:45\', \'scan_numbers\': \'6-6\'}');
INSERT INTO `users_session` VALUES ('60', 'zzq9', '{\'alive_time_s\': 1634900200, \'img_path\': \'\\\\Collect\\\\temp\\\\e356c99a-6901-4bb3-b9ae-592a244d2797.png\', \'scan_status\': \'false\', \'scan_numbers\': \'0-0\'}');
