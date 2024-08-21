CREATE DATABASE IF NOT EXISTS `appdb` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
GO
USE `appdb`;
GO
CREATE TABLE `tasks` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL DEFAULT '',
  `color` varchar(30) NOT NULL,
  `status` int(11) NOT NULL,
  `category` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
GO
ALTER TABLE `tasks`
  ADD PRIMARY KEY (`id`);
GO
ALTER TABLE `tasks`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;