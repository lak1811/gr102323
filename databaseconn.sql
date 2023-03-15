DROP SCHEMA IF EXISTS gr102023;
CREATE SCHEMA gr102023;

USE gr102023;

CREATE TABLE Locations
(
Location CHAR (50) NOT NULL,
Poststed char(40) NOT NULL,
Dato date NOT NULL,
CONSTRAINT datoPK PRIMARY KEY (Dato,location)
);

CREATE TABLE News
(
Title CHAR (100) NOT NULL,
News MEDIUMTEXT NOT NULL,
url VARCHAR(200) NOT NULL,
dato date NOT NULL,
CONSTRAINT UrlPK PRIMARY KEY (url)
);

CREATE TABLE Contactus
(
Namee CHAR (25) NOT NULL,
Email CHAR(40),
Concern CHAR (10),
DESCR MEDIUMTEXT NOT NULL,
dato date NOT NULL,
ID int(10) NOT NULL,
CONSTRAINT IDPK PRIMARY KEY (ID)
);
CREATE TABLE charity
(
namee CHAR(55) NOT NULL,
Descr mediumtext NOT NULL,
Url varchar(200) NOT NULL,
CONSTRAINT URLPK PRIMARY KEY (Url)
);

INSERT INTO CHARITY VALUES ("COVID-19 Pandemic Response: Vietnam",'Give2Asia is partnering with trusted nonprofit organizations responding to the COVID-19 pandemic. Donate online to support local relief efforts. ','https://give2asia.org/covid-19-pandemic-response-vietnam/');

INSERT INTO Locations VALUES ('Borggata 79','Oslo','2023-05-11');
INSERT INTO Locations VALUES ("Lahellestien 96","Drammen",'2023-05-18');
INSERT INTO Locations VALUES ("Postveien 121","Økerå",'2023-05-22');
INSERT INTO Locations VALUES ("Brubakkveien 152","Fredrikstad",'2023-05-27');
INSERT INTO Locations VALUES ("Vikaveien 128","Halden",'2023-06-04');
INSERT INTO Locations VALUES ("Rolf Wickstrøms gate 182","Gjøvik",'2023-06-06');

INSERT INTO Locations VALUES ("Trippestadlia 148","Oslo",'2023-06-07');
INSERT INTO Locations VALUES ("Anton Kalvaas gate 155","Trondheim",'2023-06-15');
INSERT INTO Locations VALUES ("Lindebergveien 140","Fjordland",'2023-06-19');
INSERT INTO Locations VALUES ("Lia 134","Oslo",'2023-06-22');
INSERT INTO Locations VALUES ("Vårfjoslia 178","Kongsberg",'2023-06-23');

INSERT INTO Locations VALUES ("Huflakvegen 249","Molde",'2023-06-25');
INSERT INTO Locations VALUES ("Industrigaten 249","Tønsberg",'2023-06-27');
INSERT INTO Locations VALUES ("Jakhellns vei 76","Bodø",'2023-07-01');
INSERT INTO Locations VALUES ("Skyttaveien 83","Hagan",'2023-07-11');
INSERT INTO Locations VALUES ("Gabbroveien 182","Kolsås",'2023-07-16');


INSERT INTO contactus VALUES ("Ahmed",'ahmed@live.no','Feedback','Nice work with your stuff. Like everything about it. Keep going!!','20220101',1);
INSERT INTO contactus VALUES ("Mahmed",'mahmed@live.no','Complaint','You have a very bad food selection :-(','20220202',2);
INSERT INTO contactus VALUES ("Dat",'dat@live.no','Other','Where do you have your next stand??','20210303',3);
INSERT INTO contactus VALUES ("Anonymous",'anomymous@live.no','Feedback','Nice work with your stuff. LOVE IT','090101',4);
INSERT INTO contactus VALUES ("Bahmen",'Bahmen@live.no','Feedback','Nice work with your stuff. Interesting!','050303',5);
INSERT INTO contactus VALUES ("Mustafa",'mustafa@live.no','Other','What is the charity of the month?','010101',6);

INSERT INTO news VALUES ('MoF to strengthen the capital market','Besides amending and supplementing the decree on offering and trading private placement corporate bonds in the domestic and foreign markets, the ministry will also review the Law on Securities and the Law on Enterprises.','https://vietnamnews.vn/economy/1442523/mof-to-strengthen-the-capital-market.html','040423');
INSERT INTO news VALUES ('Appeal court reduces sentence of BD chairman','The High-Level People’s Court in Hà Nội decided at the appeal hearing on Wednesday to consider the appeals of four defendants of the case of violations of land management in southern Bình Dương Province, causing losses worth hundreds of billions of đồng to the State budget.','https://vietnamnews.vn/society/1442918/appeal-court-reduces-sentence-of-former-binh-duong-chairman.html','030323');
INSERT INTO news VALUES ('Young Khánh Hoà schoolgirl teaches English for free','Gifted with the ability to learn the language, Võ Anh Thư, a 12-grade student at Lê Quý Đôn Specialised School in Khánh Hoà have participated in many translations and teaching support for English at the Internet.','https://vietnamnews.vn/society/1442493/young-khanh-hoa-schoolgirl-teaches-english-for-free.html','020223');
INSERT INTO news VALUES ('Clean water project donated to remote schools','The five clean water systems worth VNĐ227 million (US$9,800) were set up at Phạm Phú Thứ High school, Lương Thế Vinh Secondary school, Lê Văn Tám Secondary school, Ta B’hing Kindergarten and Zuoich Primary school.','https://vietnamnews.vn/society/1442213/clean-water-project-donated-to-remote-schools.html','010123');
INSERT INTO news VALUES ('Prime Minister visits hospitals on New Years Eve','The Government leader visited and presented gifts to some poor patients who were receiving treatment there as well as doctors, physicians and nurses on duty during the Tết holiday, the biggest traditional festival of Việt Nam.','https://vietnamnews.vn/society/1452961/prime-minister-visits-hospitals-on-new-year-s-eve.html','080423');
INSERT INTO news VALUES ('Overseas Vietnamese around the world celebrate Tết','Vietnamese living abroad across the world have been celebrating the traditional Tết holiday. Local Vietnamese communities held events and festivals in many countries including Australia, Thailand, Belgium and the UK to honour their roots.','https://vietnamnews.vn/society/1451919/overseas-vietnamese-around-the-world-celebrate-tet.html','010223');


CREATE USER IF NOT EXISTS "Admin" IDENTIFIED BY "ADMINPASSWORD";
GRANT ALL PRIVILEGES ON gr102023 TO 'Admin';
GRANT ALL PRIVILEGES ON locations TO 'Admin';
GRANT ALL PRIVILEGES ON contactus TO 'Admin';
GRANT ALL PRIVILEGES ON charity TO 'Admin';
GRANT ALL PRIVILEGES ON news TO 'Admin';
FLUSH PRIVILEGES;



select date_format(dato,'%d''%m''%Y' ) from contactus

select dato from contactus