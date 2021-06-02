/*
 Navicat Premium Data Transfer

 Source Server         : 127.0.0.1
 Source Server Type    : MySQL
 Source Server Version : 80021
 Source Host           : localhost:3306
 Source Schema         : badminton

 Target Server Type    : MySQL
 Target Server Version : 80021
 File Encoding         : 65001

 Date: 02/06/2021 22:58:58
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for admin_user
-- ----------------------------
DROP TABLE IF EXISTS `admin_user`;
CREATE TABLE `admin_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of admin_user
-- ----------------------------
BEGIN;
INSERT INTO `admin_user` VALUES (1, '1', '1');
INSERT INTO `admin_user` VALUES (4, '2', '2');
INSERT INTO `admin_user` VALUES (5, '3', '3');
INSERT INTO `admin_user` VALUES (6, 'admin', 'admin');
INSERT INTO `admin_user` VALUES (7, '123', '123');
COMMIT;

-- ----------------------------
-- Table structure for body_param
-- ----------------------------
DROP TABLE IF EXISTS `body_param`;
CREATE TABLE `body_param` (
  `id` int NOT NULL AUTO_INCREMENT,
  `player_id` int DEFAULT NULL,
  `height` double DEFAULT NULL,
  `weight` double DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of body_param
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for match_table
-- ----------------------------
DROP TABLE IF EXISTS `match_table`;
CREATE TABLE `match_table` (
  `match_id` int NOT NULL AUTO_INCREMENT,
  `match_name` varchar(255) DEFAULT NULL,
  `type` int DEFAULT NULL,
  `save_dir` varchar(255) DEFAULT NULL,
  `start_time` varchar(255) DEFAULT NULL,
  `end_time` varchar(255) DEFAULT NULL,
  `create_time` varchar(255) DEFAULT NULL,
  `update_time` varchar(255) DEFAULT NULL,
  `playerA_id` int DEFAULT NULL,
  `playerB_id` int DEFAULT NULL,
  `playerC_id` int DEFAULT NULL,
  `playerD_id` int DEFAULT NULL,
  PRIMARY KEY (`match_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of match_table
-- ----------------------------
BEGIN;
INSERT INTO `match_table` VALUES (1, '3', 4, '4', 'None', NULL, NULL, NULL, 9, NULL, 111, NULL);
INSERT INTO `match_table` VALUES (4, '22', 4, NULL, '3', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `match_table` VALUES (5, '222222', 4, NULL, '3', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `match_table` VALUES (6, '4', 5, NULL, '7', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `match_table` VALUES (8, 'dqqq', 3, NULL, '2323', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
COMMIT;

-- ----------------------------
-- Table structure for player
-- ----------------------------
DROP TABLE IF EXISTS `player`;
CREATE TABLE `player` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '选手id',
  `player_id` int DEFAULT NULL COMMENT '选手编号',
  `player_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '选手名称',
  `sex` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '性别\r',
  `birth_date` datetime DEFAULT NULL COMMENT '出生日期\r',
  `age` int DEFAULT NULL COMMENT '年龄',
  `nationality` varchar(255) DEFAULT NULL COMMENT '国籍',
  `province` varchar(255) DEFAULT NULL COMMENT '省份',
  `body_param_id` varchar(255) DEFAULT NULL COMMENT '身体指标参数id\r',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间\r',
  `update_time` datetime DEFAULT NULL COMMENT '更新时间\r',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of player
-- ----------------------------
BEGIN;
INSERT INTO `player` VALUES (3, 1, '小明', '1', NULL, 11, '3', NULL, NULL, NULL, NULL);
INSERT INTO `player` VALUES (11, 5, 'bb', '5', NULL, 60, '5', NULL, NULL, NULL, NULL);
INSERT INTO `player` VALUES (13, 9, 'dddd', '', NULL, 20, '', NULL, NULL, NULL, NULL);
INSERT INTO `player` VALUES (15, 0, '111', '0', NULL, 20, '0', NULL, NULL, NULL, NULL);
INSERT INTO `player` VALUES (17, 111, '000324', '9', NULL, 22, '9', NULL, NULL, NULL, NULL);
INSERT INTO `player` VALUES (18, 13, '2', '', NULL, 0, '', NULL, NULL, NULL, NULL);
INSERT INTO `player` VALUES (20, 5555, 'bb', '5', NULL, 0, '5', NULL, NULL, NULL, NULL);
COMMIT;

-- ----------------------------
-- Table structure for round_table
-- ----------------------------
DROP TABLE IF EXISTS `round_table`;
CREATE TABLE `round_table` (
  `round_id` int NOT NULL AUTO_INCREMENT,
  `match_id` int DEFAULT NULL,
  `round_name` varchar(255) DEFAULT NULL,
  `start_time` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`round_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of round_table
-- ----------------------------
BEGIN;
INSERT INTO `round_table` VALUES (1, 4, 'aaa', '11');
INSERT INTO `round_table` VALUES (6, 1, '99', '99');
INSERT INTO `round_table` VALUES (7, 1, '999', '888999');
INSERT INTO `round_table` VALUES (9, 5, '第一次世界大战', '2021');
INSERT INTO `round_table` VALUES (11, 8, '999', '999');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
