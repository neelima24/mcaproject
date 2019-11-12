-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 12, 2019 at 08:01 AM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.1.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sample_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `damaged`
--

CREATE TABLE `damaged` (
  `stock_id` int(50) NOT NULL,
  `stock_type` varchar(50) NOT NULL,
  `damage_desc` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `dept_stock`
--

CREATE TABLE `dept_stock` (
  `stock_id` int(50) NOT NULL,
  `stock_code` varchar(50) NOT NULL,
  `stock_name` varchar(50) NOT NULL,
  `stock_type` varchar(50) NOT NULL,
  `date_time` varchar(200) NOT NULL,
  `dept` varchar(50) NOT NULL,
  `room_no` int(50) NOT NULL,
  `particulars` varchar(100) NOT NULL,
  `bill_no` int(50) NOT NULL,
  `total_amt` int(250) NOT NULL,
  `warranty` varchar(200) NOT NULL,
  `barcodeimage` varchar(1000) NOT NULL,
  `status` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dept_stock`
--

INSERT INTO `dept_stock` (`stock_id`, `stock_code`, `stock_name`, `stock_type`, `date_time`, `dept`, `room_no`, `particulars`, `bill_no`, `total_amt`, `warranty`, `barcodeimage`, `status`) VALUES
(3, '5901234123457', 'stock1', 'lab item', '2019-11-11 21:31:47.049761', 'mca', 101, 'slkfl;skf;sldfk;dsfk;snxm,vnxm,vnxm,', 9878, 9997, '2020-11-20', 'barcodeimage/ean13_barcode.svg', 'working'),
(4, '5901234123457', 'stock1', 'lab item', '2019-11-11 21:31:47.049761', 'mca', 101, 'slkfl;skf;sldfk;dsfk;snxm,vnxm,vnxm,', 9878, 9997, '2020-11-20', 'barcodeimage/ean13_barcode.svg', 'working');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `id` int(11) NOT NULL,
  `username` varchar(300) NOT NULL,
  `password` varchar(300) NOT NULL,
  `usertype` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`id`, `username`, `password`, `usertype`) VALUES
(1, 'abc', 'abc', 'admin'),
(2, 'xyz', 'xyz', 'guest');

-- --------------------------------------------------------

--
-- Table structure for table `login_guest`
--

CREATE TABLE `login_guest` (
  `id` int(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login_guest`
--

INSERT INTO `login_guest` (`id`, `username`, `password`) VALUES
(1, 'aaa', 'aaa'),
(2, 'bbb', 'bbb');

-- --------------------------------------------------------

--
-- Table structure for table `move`
--

CREATE TABLE `move` (
  `stock_id` int(5) NOT NULL,
  `stock_name` varchar(50) NOT NULL,
  `moved_from` varchar(50) NOT NULL,
  `moved_to` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `received_items`
--

CREATE TABLE `received_items` (
  `stock_id` int(50) NOT NULL,
  `stock_name` varchar(50) NOT NULL,
  `stock_type` varchar(50) NOT NULL,
  `no_of_items` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `right_off`
--

CREATE TABLE `right_off` (
  `stock_id` int(50) NOT NULL,
  `stock_name` varchar(50) NOT NULL,
  `stock_type` varchar(50) NOT NULL,
  `no_of_items` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `service`
--

CREATE TABLE `service` (
  `stock_id` int(50) NOT NULL,
  `serviced_company_name` varchar(50) NOT NULL,
  `stock_type` varchar(50) NOT NULL,
  `date&time` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `warranty`
--

CREATE TABLE `warranty` (
  `stock_id` int(50) NOT NULL,
  `warranty_period` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `damaged`
--
ALTER TABLE `damaged`
  ADD PRIMARY KEY (`stock_id`);

--
-- Indexes for table `dept_stock`
--
ALTER TABLE `dept_stock`
  ADD PRIMARY KEY (`stock_id`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `login_guest`
--
ALTER TABLE `login_guest`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `move`
--
ALTER TABLE `move`
  ADD PRIMARY KEY (`stock_id`);

--
-- Indexes for table `received_items`
--
ALTER TABLE `received_items`
  ADD PRIMARY KEY (`stock_id`);

--
-- Indexes for table `right_off`
--
ALTER TABLE `right_off`
  ADD PRIMARY KEY (`stock_id`);

--
-- Indexes for table `service`
--
ALTER TABLE `service`
  ADD PRIMARY KEY (`stock_id`);

--
-- Indexes for table `warranty`
--
ALTER TABLE `warranty`
  ADD PRIMARY KEY (`stock_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `damaged`
--
ALTER TABLE `damaged`
  MODIFY `stock_id` int(50) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `dept_stock`
--
ALTER TABLE `dept_stock`
  MODIFY `stock_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `login_guest`
--
ALTER TABLE `login_guest`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `move`
--
ALTER TABLE `move`
  MODIFY `stock_id` int(5) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `received_items`
--
ALTER TABLE `received_items`
  MODIFY `stock_id` int(50) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `right_off`
--
ALTER TABLE `right_off`
  MODIFY `stock_id` int(50) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `service`
--
ALTER TABLE `service`
  MODIFY `stock_id` int(50) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `warranty`
--
ALTER TABLE `warranty`
  MODIFY `stock_id` int(50) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
