-- MariaDB dump 10.19  Distrib 10.11.6-MariaDB, for debian-linux-gnu (aarch64)
--
-- Host: localhost    Database: galaxydb
-- ------------------------------------------------------
-- Server version	10.11.6-MariaDB-0+deb12u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES
('f2fcbabda1ba');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `posts`
--

DROP TABLE IF EXISTS `posts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `posts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` text DEFAULT NULL,
  `body` text DEFAULT NULL,
  `body_html` text DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL,
  `author_id` int(11) DEFAULT NULL,
  `image_url` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `author_id` (`author_id`),
  KEY `ix_posts_timestamp` (`timestamp`),
  CONSTRAINT `posts_ibfk_1` FOREIGN KEY (`author_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `posts`
--

LOCK TABLES `posts` WRITE;
/*!40000 ALTER TABLE `posts` DISABLE KEYS */;
INSERT INTO `posts` VALUES
(3,'The Importance of Clean Spaces for Health and Well-Being','<p>In today&#39;s fast-paced world, maintaining a clean and organized space is more important than ever. Whether at home or in the workplace, cleanliness significantly impacts our health, productivity, and overall well-being. In this blog post, we will explore the benefits of clean spaces and how professional cleaning services can enhance your living and working environments.</p>\r\n\r\n<p>The Health Benefits of a Clean Environment</p>\r\n\r\n<ol>\r\n	<li>\r\n	<p><strong>Reduction of Allergens and Bacteria</strong><br />\r\n	One of the most immediate benefits of a clean space is the reduction of allergens and bacteria. Dust, pollen, pet dander, and mold can accumulate in our homes and offices, leading to respiratory issues and allergies. Regular cleaning eliminates these irritants, promoting better air quality and reducing the risk of illness. Professional cleaning services employ specialized techniques and products that ensure a thorough clean, reaching areas that may often be overlooked.</p>\r\n	</li>\r\n	<li>\r\n	<p><strong>Mental Clarity and Reduced Stress</strong><br />\r\n	A cluttered and dirty environment can contribute to feelings of stress and overwhelm. Research has shown that a clean and organized space can lead to improved focus and mental clarity. When your surroundings are tidy, it becomes easier to concentrate on tasks and make decisions. Hiring a cleaning service allows you to enjoy a pristine environment without the added stress of doing it yourself.</p>\r\n	</li>\r\n	<li>\r\n	<p><strong>Enhanced Productivity</strong><br />\r\n	In a workplace setting, cleanliness directly correlates with productivity. Employees are more likely to be motivated and efficient in a clean environment. Clutter and mess can distract from work, leading to decreased performance. By investing in professional cleaning services, businesses can create a more pleasant and efficient workplace for their employees, ultimately boosting morale and productivity.</p>\r\n	</li>\r\n</ol>\r\n\r\n<p>The Role of Professional Cleaning Services</p>\r\n\r\n<ol>\r\n	<li>\r\n	<p><strong>Expertise and Experience</strong><br />\r\n	Cleaning professionals have the training and experience to handle a variety of cleaning tasks. From deep cleaning carpets to sanitizing restrooms, their expertise ensures that every corner of your space is thoroughly cleaned. They understand the best practices for maintaining cleanliness and can tailor their services to meet your specific needs.</p>\r\n	</li>\r\n	<li>\r\n	<p><strong>Time Savings</strong><br />\r\n	Cleaning can be a time-consuming task, especially for busy families and professionals. By outsourcing cleaning duties to a reliable service, you free up valuable time that can be better spent with family, pursuing hobbies, or focusing on work. Professional cleaners work efficiently, allowing you to enjoy a clean space without dedicating hours to the task.</p>\r\n	</li>\r\n	<li>\r\n	<p><strong>Customized Cleaning Plans</strong><br />\r\n	Every space is unique, and so are the cleaning needs that come with it. Professional cleaning services can create customized cleaning plans that suit your specific requirements. Whether you need daily, weekly, or monthly services, they can accommodate your schedule and preferences. This flexibility ensures that your space remains consistently clean and well-maintained.</p>\r\n	</li>\r\n</ol>\r\n\r\n<p>Maintaining Cleanliness Between Professional Visits</p>\r\n\r\n<p>While professional cleaning services are invaluable, there are several steps you can take to maintain cleanliness between visits:</p>\r\n\r\n<ol>\r\n	<li>\r\n	<p><strong>Establish a Cleaning Routine</strong><br />\r\n	Develop a daily or weekly cleaning routine that includes tasks like dusting, vacuuming, and wiping down surfaces. This routine will help prevent dirt and clutter from building up.</p>\r\n	</li>\r\n	<li>\r\n	<p><strong>Declutter Regularly</strong><br />\r\n	Take time to declutter your space regularly. Donate or discard items you no longer need, making it easier to keep your environment tidy.</p>\r\n	</li>\r\n	<li>\r\n	<p><strong>Involve Everyone</strong><br />\r\n	If you live with family or roommates, involve everyone in the cleaning process. Assign tasks to ensure that everyone contributes to maintaining a clean and organized space.</p>\r\n	</li>\r\n</ol>\r\n\r\n<p>Conclusion</p>\r\n\r\n<p>A clean space is essential for promoting health, productivity, and overall well-being. Whether at home or in the workplace, investing in professional cleaning services can transform your environment into a haven of cleanliness and comfort. By recognizing the benefits of a clean space and taking proactive steps to maintain it, you can enhance your quality of life and create a welcoming atmosphere for yourself and others.</p>\r\n',NULL,'2024-10-10 17:15:00',1,'image_1.png'),
(4,'Why a Deep Cleaning is Essential for Your Home and Office','<p>Maintaining a clean home or office is important, but sometimes regular cleaning isn&rsquo;t enough. A deep cleaning targets areas that accumulate dirt and grime over time, ensuring your space is as hygienic and fresh as possible.</p>\r\n\r\n<p><strong>What is Deep Cleaning?</strong></p>\r\n\r\n<p>Deep cleaning goes beyond surface cleaning to reach those hidden or often-ignored spots. Common tasks include:</p>\r\n\r\n<ul>\r\n	<li>Cleaning behind and under furniture and appliances.</li>\r\n	<li>Washing windows and scrubbing grout.</li>\r\n	<li>Sanitizing high-touch areas like doorknobs and light switches.</li>\r\n	<li>Shampooing carpets and upholstery.</li>\r\n</ul>\r\n\r\n<p><strong>Why is Deep Cleaning Important?</strong></p>\r\n\r\n<ol>\r\n	<li>\r\n	<p><strong>Improves Air Quality</strong><br />\r\n	Dust and allergens accumulate, affecting air quality. Deep cleaning removes these pollutants, promoting healthier environments.</p>\r\n	</li>\r\n	<li>\r\n	<p><strong>Prevents Mold and Bacteria</strong><br />\r\n	Bathrooms and kitchens are prone to moisture, leading to mold and bacteria. Deep cleaning eliminates these health risks.</p>\r\n	</li>\r\n	<li>\r\n	<p><strong>Enhances Appearance</strong><br />\r\n	Deep cleaning restores your home or office, making it look fresh and new, which is important for special events or moving.</p>\r\n	</li>\r\n	<li>\r\n	<p><strong>Prolongs Furniture and Appliance Life</strong><br />\r\n	Removing built-up dirt protects your investments and extends their lifespan.</p>\r\n	</li>\r\n</ol>\r\n\r\n<p><strong>When to Schedule a Deep Clean</strong></p>\r\n\r\n<p>It&rsquo;s ideal to deep clean twice a year&mdash;once in spring and once before the holidays. You may also consider deep cleaning for special events, moving, or changing seasons.</p>\r\n\r\n<p>Why Hire Professional Cleaners?</p>\r\n\r\n<p>Professional cleaners have the tools and expertise to perform thorough, efficient deep cleans, saving you time and effort. They can tailor their services to meet your specific needs, ensuring every corner is spotless.</p>\r\n',NULL,'2024-10-10 18:25:00',1,'deepclean1.png'),
(5,'5 Signs It\'s Time to Hire a Professional Cleaning Service','<p>Keeping your home or office clean is essential for health, productivity, and overall comfort. But with busy schedules and daily responsibilities, it can be hard to keep up with all the cleaning tasks on your own. So, how do you know when it&#39;s time to hire a professional cleaning service? Here are five signs that it might be time to call in the experts.</p>\r\n\r\n<p><strong>1. You&rsquo;re Struggling to Keep Up with the Basics</strong></p>\r\n\r\n<p>Between work, family, and social commitments, it&rsquo;s easy for basic cleaning tasks to fall behind. If you find yourself constantly playing catch-up with vacuuming, dusting, or wiping down surfaces, it might be a sign you need some help. A professional cleaning service can take over these routine tasks, giving you more time to focus on what matters most.</p>\r\n\r\n<p><strong>2. You Have Stubborn Dirt and Stains</strong></p>\r\n\r\n<p>Some cleaning tasks require more than just a quick wipe. Stubborn dirt, stains, or grime on carpets, upholstery, and hard-to-reach areas often need specialized cleaning products and equipment. Professional cleaners have the right tools and experience to tackle these problem areas, leaving your space spotless.</p>\r\n\r\n<p><strong>3. Your Allergies Are Acting Up</strong></p>\r\n\r\n<p>Dust, pet dander, and pollen can build up in your home or office, even with regular cleaning. If you or your family members have allergies and notice that symptoms like sneezing, coughing, or watery eyes are becoming more frequent, it might be time for a thorough cleaning. Professionals use high-quality cleaning products and techniques to remove allergens and improve air quality.</p>\r\n\r\n<p><strong>4. You&rsquo;re Preparing for a Special Event</strong></p>\r\n\r\n<p>Hosting a party, event, or having guests over? First impressions matter, and a clean home or office makes a huge difference. Hiring a professional cleaning service before (or after) a special occasion ensures your space is clean, organized, and ready to impress.</p>\r\n\r\n<p><strong>5. You&rsquo;re Moving In or Out</strong></p>\r\n\r\n<p>Moving is stressful enough without the added pressure of cleaning. Whether you&rsquo;re preparing to move into a new home or leaving your current one, a deep clean is crucial. Professionals can handle everything from scrubbing floors to cleaning out cabinets, helping you make a fresh start or leave the space spotless for the next occupant.</p>\r\n\r\n<p>Why Hiring a Professional Cleaning Service is Worth It</p>\r\n\r\n<p>Professional cleaners offer more than just convenience. They have the experience, tools, and knowledge to deliver a deeper clean, maintain a healthier environment, and keep your space looking its best. You don&rsquo;t have to worry about managing the details&mdash;just enjoy the results of a clean, welcoming space.</p>\r\n',NULL,'2024-10-10 23:23:00',1,'deepclean2.png'),
(6,'Why Professional Cleaning Services Are Worth the Investment','<p>In today&rsquo;s fast-paced world, many people struggle to keep up with the demands of their jobs, families, and personal responsibilities. Maintaining a clean home or office can easily fall to the bottom of the priority list. That&rsquo;s where professional cleaning services come in, providing a vital solution to ensure spaces remain tidy, hygienic, and welcoming.</p>\r\n\r\n<p>At first glance, hiring a professional cleaning company may seem like an unnecessary expense. However, the benefits far outweigh the costs, making it a wise investment for both homes and businesses. Here&#39;s why:</p>\r\n\r\n<h3>1. <strong>Time Savings</strong></h3>\r\n\r\n<p>Time is a precious resource, and cleaning can be incredibly time-consuming, especially for larger spaces or areas that require deep cleaning. When you hire professionals, you free up valuable hours that can be spent on more important things, like family, work, or simply relaxing.</p>\r\n\r\n<h3>2. <strong>Thorough and High-Quality Cleaning</strong></h3>\r\n\r\n<p>Professional cleaners are trained to clean effectively and efficiently. They know how to tackle every nook and cranny, ensuring your space is spotless. Whether it&rsquo;s deep-cleaning carpets, sanitizing bathrooms, or dusting hard-to-reach places, the level of detail and precision offered by experts is hard to match.</p>\r\n\r\n<h3>3. <strong>Healthier Environment</strong></h3>\r\n\r\n<p>A clean space isn&rsquo;t just about appearances; it&rsquo;s also crucial for your health. Dust, allergens, bacteria, and mold can accumulate over time and lead to health problems. Professional cleaners use specialized equipment and products to remove these harmful elements, creating a healthier living or working environment.</p>\r\n\r\n<h3>4. <strong>Custom Cleaning Plans</strong></h3>\r\n\r\n<p>Every space is different, and so are the cleaning needs. A professional service will work with you to create a customized cleaning plan that fits your specific requirements, whether it&rsquo;s a one-time deep clean, regular maintenance, or specialized cleaning for specific areas.</p>\r\n\r\n<h3>5. <strong>Improved Productivity in Workspaces</strong></h3>\r\n\r\n<p>For businesses, maintaining a clean workspace can boost employee morale and productivity. A clutter-free and clean environment allows employees to focus better and reduces the risk of illness, which can lead to fewer sick days.</p>\r\n\r\n<h3><strong>Conclusion</strong></h3>\r\n\r\n<p>Whether for your home or business, professional cleaning services provide peace of mind, ensuring your space is always clean, hygienic, and welcoming. It&rsquo;s an investment that pays off in more ways than one, improving both your health and quality of life.</p>\r\n',NULL,'2024-10-11 16:13:00',1,'image_7.png');
/*!40000 ALTER TABLE `posts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects`
--

DROP TABLE IF EXISTS `projects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `projects` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(150) NOT NULL,
  `introduction` text NOT NULL,
  `category` varchar(150) DEFAULT NULL,
  `client` varchar(50) DEFAULT NULL,
  `start` datetime DEFAULT NULL,
  `ended` datetime DEFAULT NULL,
  `execution_title` varchar(150) NOT NULL,
  `execution_body` text NOT NULL,
  `problems_title` varchar(150) NOT NULL,
  `problems_body` text NOT NULL,
  `solutions_title` varchar(150) NOT NULL,
  `solutions_body` text NOT NULL,
  `total_projects` int(11) DEFAULT NULL,
  `image1_url` varchar(255) DEFAULT NULL,
  `image2_url` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_projects_start` (`start`),
  KEY `ix_projects_ended` (`ended`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects`
--

LOCK TABLES `projects` WRITE;
/*!40000 ALTER TABLE `projects` DISABLE KEYS */;
INSERT INTO `projects` VALUES
(2,'Downtown Office Building Deep Clean and Sanitization','<p>ABC Financial Services Ltd., a leading financial services firm, required a deep cleaning and sanitization of their downtown corporate office building. The building consisted of 15 floors, including executive offices, open workspaces, conference rooms, a cafeteria, and multiple break rooms. Due to ongoing concerns related to health safety and air quality, the client requested a full-scale cleaning, disinfection, and deodorization service, while minimizing disruption to their daily operations.</p>\r\n','Commercial Cleaning','ABC Financial Services Ltd','2023-06-10 08:00:00','2023-06-14 18:00:00','Comprehensive Cleaning and Sanitization of Office Spaces and Facilities','<p>The project started with a thorough assessment of the entire office building, identifying high-priority areas such as executive suites, meeting rooms, and common areas like the cafeteria and restrooms. We deployed a team of 20 highly trained cleaners to carry out the job over a 4-day period.</p>\r\n\r\n<p>For the office spaces, we used eco-friendly cleaning agents to clean all surfaces, including desks, chairs, computer monitors, and windows. Our team dusted and vacuumed carpets and upholstery, while ensuring all electronics were safely wiped and sanitized. We also paid extra attention to disinfecting high-touch surfaces such as doorknobs, light switches, and communal equipment like printers and coffee machines.</p>\r\n\r\n<p>The break rooms and cafeteria required deep cleaning, including degreasing of kitchen equipment, sanitization of eating areas, and proper waste disposal. The team also addressed the indoor air quality by cleaning the HVAC ducts and replacing air filters. This improved the airflow and reduced allergens, which was a key concern for the client.</p>\r\n','Unexpected Mold Growth and Restricted Access to Server Rooms','<p>While cleaning the lower basement level, our team discovered mold growth behind the paneling in the storage room due to a leaky pipe. This required immediate action, as mold presented both health and structural risks. The cleaning process had to be paused in that area to allow for specialized mold removal and restoration services.</p>\r\n\r\n<p>Additionally, we encountered restricted access to the server rooms, which housed sensitive financial data. These areas were highly secured and required special clearance for entry. This delay pushed back the cleaning schedule for the basement floor, as we had to wait for IT staff to supervise the cleaning process.</p>\r\n','Mold Remediation and Coordinated Access to Restricted Areas','<p>Upon discovering the mold issue, we swiftly coordinated with a third-party mold remediation specialist, ensuring the affected areas were properly contained and treated. This included removing and replacing the damaged paneling, dehumidifying the space, and applying antimicrobial solutions to prevent future mold growth.</p>\r\n\r\n<p>To resolve the restricted access issue, we worked closely with the client&rsquo;s IT department to schedule cleaning after working hours, allowing us to clean the server room while ensuring data security protocols were maintained. This cooperation minimized downtime and allowed the project to proceed smoothly without further delays.</p>\r\n',344,'project1.png','project2.png');
/*!40000 ALTER TABLE `projects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subscribers`
--

DROP TABLE IF EXISTS `subscribers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subscribers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subscribers`
--

LOCK TABLES `subscribers` WRITE;
/*!40000 ALTER TABLE `subscribers` DISABLE KEYS */;
INSERT INTO `subscribers` VALUES
(1,'benjaminozor@gmail.com');
/*!40000 ALTER TABLE `subscribers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `team_member`
--

DROP TABLE IF EXISTS `team_member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `team_member` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(65) NOT NULL,
  `last_name` varchar(65) NOT NULL,
  `role` varchar(20) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `address` text NOT NULL,
  `email` varchar(64) DEFAULT NULL,
  `fb_social` varchar(120) DEFAULT NULL,
  `x_social` varchar(120) DEFAULT NULL,
  `lkdn_social` varchar(120) DEFAULT NULL,
  `pin_social` varchar(120) DEFAULT NULL,
  `about_me` text NOT NULL,
  `image_url` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `phone` (`phone`),
  UNIQUE KEY `fb_social` (`fb_social`),
  UNIQUE KEY `x_social` (`x_social`),
  UNIQUE KEY `lkdn_social` (`lkdn_social`),
  UNIQUE KEY `pin_social` (`pin_social`),
  UNIQUE KEY `ix_team_member_email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `team_member`
--

LOCK TABLES `team_member` WRITE;
/*!40000 ALTER TABLE `team_member` DISABLE KEYS */;
/*!40000 ALTER TABLE `team_member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(64) DEFAULT NULL,
  `username` varchar(64) DEFAULT NULL,
  `password_hash` varchar(128) DEFAULT NULL,
  `name` varchar(64) DEFAULT NULL,
  `location` varchar(64) DEFAULT NULL,
  `about_me` text DEFAULT NULL,
  `member_since` datetime DEFAULT NULL,
  `last_seen` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_users_username` (`username`),
  UNIQUE KEY `ix_users_email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES
(1,'support@galaxycleaning.co.uk','Support','pbkdf2:sha256:600000$aB49PJsLoGNFpSnv$b2959641b9716294a0c5f2663b2a97646ce1994fb0825c663a9211b16ac50f6c','Patrick poll','United Kingdom','As a dedicated professional in the cleaning services industry for several years, I have built my career on the commitment to creating clean and welcoming spaces for my clients. My experience has allowed me to hone my skills and develop a reputation for delivering exceptional cleaning services. I focus on quality and customer satisfaction, whether it’s residential cleaning, commercial spaces, or specialized services. My passion for cleanliness drives me to go above and beyond in every task, ensuring that my clients receive the best possible experience.','2024-10-10 16:41:17','2024-10-10 15:41:05');
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

-- Dump completed on 2024-10-22  1:38:46
