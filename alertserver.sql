-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost
-- Généré le : jeu. 18 juin 2026 à 00:48
-- Version du serveur : 10.4.32-MariaDB
-- Version de PHP : 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `alertserver`
--

-- --------------------------------------------------------

--
-- Structure de la table `idtestServer`
--

CREATE TABLE `idtestServer` (
  `id` int(11) NOT NULL,
  `serveur` varchar(255) NOT NULL,
  `etat` varchar(255) NOT NULL,
  `date` varchar(255) NOT NULL,
  `taux_reussite` varchar(255) NOT NULL,
  `temps_moyen` varchar(255) NOT NULL,
  `host` varchar(255) NOT NULL,
  `cpu` varchar(255) NOT NULL,
  `ram` varchar(255) NOT NULL,
  `disk` varchar(255) NOT NULL,
  `temperature` varchar(255) NOT NULL,
  `resume` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `idtestServer`
--

INSERT INTO `idtestServer` (`id`, `serveur`, `etat`, `date`, `taux_reussite`, `temps_moyen`, `host`, `cpu`, `ram`, `disk`, `temperature`, `resume`) VALUES
(1, 'http://localhost/page_serve/', 'Serveur faible', '2026-05-27T13:59:47.613Z', '0%', '0.0036025643348693848s', 'debian', '3.4', '19.1', '24.3', '48', 'SUCCESS 0 / FAIL 20'),
(2, 'http://localhost/page_serve/', 'Serveur faible', '2026-05-27T14:15:09.377Z', '0%', '0.0028415918350219727s', 'debian', '6.7', '24.8', '24.3', '53', 'SUCCESS 0 / FAIL 20'),
(3, 'http://localhost/page_serve/', 'Serveur faible', '2026-05-27T14:15:29.202Z', '0%', '0.003139317035675049s', 'debian', '1.6', '24.9', '24.3', '50', 'SUCCESS 0 / FAIL 20'),
(4, 'http://localhost/page_serve/', 'Serveur faible', '2026-05-27T14:15:48.082Z', '0%', '0.0036541104316711428s', 'debian', '0.4', '24.7', '24.3', '49', 'SUCCESS 0 / FAIL 20'),
(5, 'http://localhost/page_serve/', 'Serveur faible', '2026-05-27T14:16:07.480Z', '0%', '0.0031141042709350586s', 'debian', '0.7', '24.8', '24.3', '47', 'SUCCESS 0 / FAIL 20'),
(6, 'http://localhost/page_serve/', 'Serveur faible', '2026-05-27T14:16:25.965Z', '0%', '0.0037096023559570314s', 'debian', '3.7', '24.9', '24.3', '45', 'SUCCESS 0 / FAIL 20'),
(7, 'http://localhost/page_serve/', 'Serveur faible', '2026-05-27T14:16:45.208Z', '0%', '0.003867185115814209s', 'debian', '3.4', '24.9', '24.3', '48', 'SUCCESS 0 / FAIL 20'),
(8, 'http://localhost/page_serve/', 'Serveur faible', '2026-05-27T14:17:03.948Z', '0%', '0.0032903552055358887s', 'debian', '4.2', '25.3', '24.3', '49', 'SUCCESS 0 / FAIL 20'),
(9, 'http://localhost/page_serve/', 'Serveur faible', '2026-05-27T14:17:22.913Z', '0%', '0.0037376046180725097s', 'debian', '3.8', '25.1', '24.3', '49', 'SUCCESS 0 / FAIL 20'),
(10, 'http://localhost/page_serve/', 'Serveur faible', '2026-05-27T14:17:41.118Z', '0%', '0.0034711360931396484s', 'debian', '4.6', '25.6', '24.3', '48', 'SUCCESS 0 / FAIL 20'),
(11, 'http://localhost/page_serve/', 'Serveur faible', '2026-05-27T14:18:00.214Z', '0%', '0.00395592451095581s', 'debian', '5.9', '25.4', '24.3', '51', 'SUCCESS 0 / FAIL 20'),
(12, 'http://localhost/page_serve/', 'Serveur faible', '2026-05-27T14:18:18.401Z', '0%', '0.003395819664001465s', 'debian', '2.6', '25.6', '24.3', '52', 'SUCCESS 0 / FAIL 20'),
(13, 'http://localhost/page_serve/', 'Serveur faible', '2026-05-27T14:18:37.528Z', '0%', '0.003915369510650635s', 'debian', '4', '27.3', '24.3', '73', 'SUCCESS 0 / FAIL 20'),
(14, 'http://localhost/page_serve/', 'Serveur faible', '2026-05-27T14:18:56.677Z', '0%', '0.0033283591270446776s', 'debian', '5.1', '27.2', '24.3', '63', 'SUCCESS 0 / FAIL 20'),
(15, 'http://localhost/page_serve/', 'Serveur faible', '2026-05-27T14:19:15.303Z', '0%', '0.003620433807373047s', 'debian', '4.2', '27.6', '24.3', '56', 'SUCCESS 0 / FAIL 20'),
(16, 'http://localhost/page_server/', 'Très stable', '2026-06-05T21:40:07.611Z', '100%', '0.004035627841949463s', 'debian', '17.5', '18.8', '27.4', '90', 'SUCCESS 20 / FAIL 0'),
(17, 'http://localhost/page_server', 'Très stable', '2026-06-05T21:40:46.849Z', '100%', '0.006079530715942383s', 'debian', '6.1', '18.4', '27.4', '69', 'SUCCESS 20 / FAIL 0'),
(18, 'http://localhost/page_server', 'Très stable', '2026-06-05T21:41:05.235Z', '100%', '0.006104612350463867s', 'debian', '1.6', '18.7', '27.4', '65', 'SUCCESS 20 / FAIL 0'),
(19, 'http://localhost/page_servr', 'Serveur faible', '2026-06-06T10:28:07.027Z', '0%', '0.01319352388381958s', 'debian', '5', '21.1', '26.8', '41', 'SUCCESS 0 / FAIL 20');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `idtestServer`
--
ALTER TABLE `idtestServer`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `idtestServer`
--
ALTER TABLE `idtestServer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
