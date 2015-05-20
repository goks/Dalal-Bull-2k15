-- phpMyAdmin SQL Dump
-- version 4.2.11
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 20, 2015 at 04:54 PM
-- Server version: 5.6.21
-- PHP Version: 5.5.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `dalalbull_2k15`
--

-- --------------------------------------------------------

--
-- Table structure for table `history`
--

CREATE TABLE IF NOT EXISTS `history` (
  `history_id` int(10) unsigned NOT NULL COMMENT 'Simple identifier',
  `username` varchar(55) NOT NULL COMMENT 'Username from fb',
  `time` datetime NOT NULL COMMENT 'Time of transaction',
  `company` varchar(55) NOT NULL,
  `type` enum('Buy','Sell','Short sell','Short cover') NOT NULL COMMENT 'Type of transaction',
  `quantity` int(10) unsigned NOT NULL COMMENT 'Quantity of shares?',
  `price` float NOT NULL COMMENT 'Price of share'
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='Table to store history entries';

-- --------------------------------------------------------

--
-- Table structure for table `pending`
--

CREATE TABLE IF NOT EXISTS `pending` (
`pend_id` int(11) NOT NULL COMMENT 'Simple identifier',
  `username` varchar(55) NOT NULL COMMENT 'Username from fb',
  `symbol` varchar(55) NOT NULL COMMENT 'Symbol of stock',
  `type` enum('Buy','Short sell','Sell','Short cover') NOT NULL COMMENT 'Buy/Shortsell/Sell/Shortcover',
  `quantity` int(11) unsigned NOT NULL COMMENT 'Quantity of stock',
  `price` float NOT NULL COMMENT 'price of stock',
  `time` datetime NOT NULL COMMENT 'Time of transaction'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `portfolio`
--

CREATE TABLE IF NOT EXISTS `portfolio` (
  `user` varchar(55) NOT NULL COMMENT 'Username from fb same as in usertable',
  `cash_bal` double NOT NULL COMMENT 'Cash balance of user',
  `net_worth` double NOT NULL COMMENT 'Net worth of user',
  `margin` double NOT NULL COMMENT 'Margin=networth-cash bal',
  `no_trans` int(11) unsigned NOT NULL DEFAULT '0' COMMENT 'Number of transactions made'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `transactions`
--

CREATE TABLE IF NOT EXISTS `transactions` (
`trans_id` int(11) NOT NULL COMMENT 'Simple identifier',
  `username` varchar(55) NOT NULL COMMENT 'Username from fb',
  `symbol` varchar(55) NOT NULL COMMENT 'Symbol of stock ',
  `buy_ss` enum('Buy','Short sell') NOT NULL COMMENT 'Buy/Shortsell',
  `quantity` int(11) unsigned NOT NULL COMMENT 'Quantity of stock',
  `value` float NOT NULL COMMENT 'Value of Stock',
  `time` datetime NOT NULL COMMENT 'Time of transaction'
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='This table stores transaction details';

-- --------------------------------------------------------

--
-- Table structure for table `usertable`
--

CREATE TABLE IF NOT EXISTS `usertable` (
  `username` varchar(55) NOT NULL COMMENT 'uid from FB',
  `firstname` varchar(55) NOT NULL COMMENT 'FirstName from fb',
  `lastname` varchar(55) NOT NULL COMMENT 'LastName from fb',
  `email` varchar(55) NOT NULL COMMENT 'emailid from fb'
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='This table stores user information provided from FB.Used for login purposes only';

--
-- Indexes for dumped tables
--

--
-- Indexes for table `history`
--
ALTER TABLE `history`
 ADD UNIQUE KEY `history_id` (`history_id`);

--
-- Indexes for table `pending`
--
ALTER TABLE `pending`
 ADD PRIMARY KEY (`pend_id`), ADD UNIQUE KEY `pend_id` (`pend_id`);

--
-- Indexes for table `portfolio`
--
ALTER TABLE `portfolio`
 ADD PRIMARY KEY (`user`);

--
-- Indexes for table `transactions`
--
ALTER TABLE `transactions`
 ADD PRIMARY KEY (`trans_id`), ADD UNIQUE KEY `trans_id` (`trans_id`);

--
-- Indexes for table `usertable`
--
ALTER TABLE `usertable`
 ADD PRIMARY KEY (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `pending`
--
ALTER TABLE `pending`
MODIFY `pend_id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Simple identifier';
--
-- AUTO_INCREMENT for table `transactions`
--
ALTER TABLE `transactions`
MODIFY `trans_id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Simple identifier';
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
