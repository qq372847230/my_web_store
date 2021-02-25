DROP DATABASE IF EXISTS my_web_store ;
CREATE DATABASE my_web_store CHARACTER SET UTF8 ;
USE my_web_store ;

-- 创建用户表
CREATE TABLE user(
    uid     VARCHAR(100)  ,
    password    VARCHAR(32) ,
    name    VARCHAR(20),
    gender      VARCHAR(10) ,
    birthday    DATE,
    photo       VARCHAR(50) ,
    note        TEXT,
    admin       INT,
    CONSTRAINT pk_uid PRIMARY KEY(uid)
)engine=innodb ;

INSERT INTO user(uid, password, name, gender, photo, note, admin) VALUES ('admin', '4800ac7363f11c0e1fbd63d04a642b32', '炎黄', '男', 'user-nophoto.png', '管理员', 1) ;

-- 创建数据表
CREATE TABLE item(
	iid			BIGINT AUTO_INCREMENT ,
	title		VARCHAR(50) ,
	CONSTRAINT pk_iid PRIMARY KEY(iid)
)engine=innodb ;
-- 测试数据
INSERT INTO item(title) VALUES ('图书音像') ;
INSERT INTO item(title) VALUES ('电脑办公') ;
INSERT INTO item(title) VALUES ('手机数码') ;
INSERT INTO item(title) VALUES ('家居生活') ;
INSERT INTO item(title) VALUES ('汽车用品') ;
INSERT INTO item(title) VALUES ('家用电器') ;

CREATE TABLE goods (
	gid			BIGINT AUTO_INCREMENT ,
	name		VARCHAR(50) ,
	price		double ,
	photo		VARCHAR(100) ,
	content     TEXT ,
	dflag		BIGINT ,
	iid			BIGINT ,
	CONSTRAINT pk_gid10 PRIMARY KEY(gid) ,
	CONSTRAINT fk_iid FOREIGN KEY(iid) REFERENCES item(iid)
)engine=innodb ;
-- 商品信息
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('java从入门到项目实战',99.8,'book_1_000004.png','沐言优拓：www.yootk.com',0,1) ;
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('Android开发实战经典',88.6,'book_1_000001.png','沐言优拓：www.yootk.com',0,1) ;
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('JavaWeb开发实战经典',68.9,'book_1_000002.png','沐言优拓：www.yootk.com',0,1) ;
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('JavaWeb开发实战宝典',128.9,'book_1_000003.png','沐言优拓：www.yootk.com',0,1) ;
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('Java核心技术精讲',57.9,'book_1_000005.png','沐言优拓：www.yootk.com',0,1) ;
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('Java开发实战经典',69.8,'book_1_000006.png','沐言优拓：www.yootk.com',0,1) ;
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('Java开发实战经典（第二版）',89.8,'book_1_000007.png','沐言优拓：www.yootk.com',0,1) ;
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('Java微服务架构实战',69.8,'book_1_000008.png','沐言优拓：www.yootk.com',0,1) ;
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('Oracle开发实战经典',87.8,'book_1_000009.png','沐言优拓：www.yootk.com',0,1) ;
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('第一行代码java',86.7,'book_1_000010.png','沐言优拓：www.yootk.com',0,1) ;
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('Python从入门到项目实战',96.7,'book_1_000011.png','沐言优拓：www.yootk.com',0,1) ;
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('GO程序设计',93.2,'book_1_000012.png','沐言优拓：www.yootk.com',0,1) ;
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('Spring开发框架',97.2,'book_1_000013.png','沐言优拓：www.yootk.com',0,1) ;
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('沐言优拓-Java编程',97.2,'other_6_000001.png','沐言优拓：www.yootk.com',0,1) ;
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('沐言优拓-Python编程',97.2,'other_6_000002.png','沐言优拓：www.yootk.com',0,1) ;
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('沐言优拓',97.2,'goods-nophoto.png','沐言优拓：www.yootk.com',0,1) ;

INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('Java工程师',5980.2,'office_2_000001.png','沐言优拓：www.yootk.com',0,2) ;
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('CSV数据存储',80.2,'office_2_000002.png','沐言优拓：www.yootk.com',0,2) ;
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('DevOPS',1980.2,'office_2_000003.png','沐言优拓：www.yootk.com',0,2) ;
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('GitLab私服',280.0,'office_2_000004.png','沐言优拓：www.yootk.com',0,2) ;
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('GIT版本控制工具',98.0,'office_2_000005.png','沐言优拓：www.yootk.com',0,2) ;
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('gunicorn',8.9,'office_2_000006.png','沐言优拓：www.yootk.com',0,2) ;
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('Python数据分析',896.8,'office_2_000007.png','沐言优拓：www.yootk.com',0,2) ;
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('IDEA开发工具',66.8,'office_2_000008.png','沐言优拓：www.yootk.com',0,2) ;

INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('Java架构师',8900.0,'data_3_000001.png','沐言优拓：www.yootk.com',0,3) ;
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('jQuery开发框架',90.0,'data_3_000002.png','沐言优拓：www.yootk.com',0,3) ;
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('JSON数据传输',69.0,'data_3_000003.png','沐言优拓：www.yootk.com',0,3) ;
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('Kafka消息组件',569.0,'data_3_000004.png','沐言优拓：www.yootk.com',0,3) ;
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('MySQL数据库',19.0,'data_3_000005.png','沐言优拓：www.yootk.com',0,3) ;
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('Netty开发框架',680.0,'data_3_000006.png','沐言优拓：www.yootk.com',0,3) ;
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('OAuth统一认证',980.0,'data_3_000007.png','沐言优拓：www.yootk.com',0,3) ;

INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('Jinja2模版技术',6.0,'live_4_000001.png','沐言优拓：www.yootk.com',0,4) ;
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('RabbitMQ消息组件',280.0,'live_4_000002.png','沐言优拓：www.yootk.com',0,4) ;
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('UBuntu操作系统',1.0,'live_4_000003.png','沐言优拓：www.yootk.com',0,4) ;
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('WebLogic中间件',1678.0,'live_4_000004.png','沐言优拓：www.yootk.com',0,4) ;
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('Django工程师',278.0,'live_4_000005.png','沐言优拓：www.yootk.com',0,4) ;
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('Flask工程师',278.0,'live_4_000006.png','沐言优拓：www.yootk.com',0,4) ;

INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('Java架构师',8900.0,'car_5_000001.png','沐言优拓：www.yootk.com',0,5) ;
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('大数据工程师',9900.0,'car_5_000002.png','沐言优拓：www.yootk.com',0,5) ;
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('软件系统架构',6600.0,'car_5_000004.png','沐言优拓：www.yootk.com',0,5) ;
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('分布式接口设计',2300.0,'car_5_000003.png','沐言优拓：www.yootk.com',0,5) ;
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('软件项目管理',5300.0,'car_5_000005.png','沐言优拓：www.yootk.com',0,5) ;
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('软件需求分析',3300.0,'car_5_000006.png','沐言优拓：www.yootk.com',0,5) ;
INSERT INTO goods (name,price,photo,content,dflag,iid) VALUES ('云服务架构',3300.0,'car_5_000007.png','沐言优拓：www.yootk.com',0,5) ;


-- 提交事务
COMMIT ;

