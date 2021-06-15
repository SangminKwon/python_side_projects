-- --------------------------------------------------------
-- 호스트:                          127.0.0.1
-- 서버 버전:                        10.5.10-MariaDB - mariadb.org binary distribution
-- 서버 OS:                        Win64
-- HeidiSQL 버전:                  11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- python_db 데이터베이스 구조 내보내기
CREATE DATABASE IF NOT EXISTS `python_db` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `python_db`;

-- 테이블 python_db.users_tbl 구조 내보내기
CREATE TABLE IF NOT EXISTS `users_tbl` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '내부 관리 id',
  `uid` varchar(64) NOT NULL COMMENT '회원 ID',
  `upw` varchar(64) NOT NULL COMMENT '회원 PW',
  `name` varchar(32) NOT NULL COMMENT '회원 이름',
  `regdate` timestamp NOT NULL DEFAULT current_timestamp() COMMENT '가입일',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uid` (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- 테이블 데이터 python_db.users_tbl:~2 rows (대략적) 내보내기
/*!40000 ALTER TABLE `users_tbl` DISABLE KEYS */;
INSERT INTO `users_tbl` (`id`, `uid`, `upw`, `name`, `regdate`) VALUES
	(1, 'guest', '123', '게스트', '2021-06-10 10:23:16'),
	(2, 'admin', '456', '관리자', '2021-06-10 10:28:10');
/*!40000 ALTER TABLE `users_tbl` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
