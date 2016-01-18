-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Servidor: localhost
-- Tempo de Geração: 18/01/2016 às 20:57
-- Versão do servidor: 5.5.46-0ubuntu0.14.04.2
-- Versão do PHP: 5.5.9-1ubuntu4.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Banco de dados: `biblioteca`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `livro`
--

CREATE TABLE IF NOT EXISTS `livro` (
  `id_livro` int(11) NOT NULL AUTO_INCREMENT,
  `titulo_livro` varchar(255) NOT NULL,
  `categoria_livro` varchar(80) NOT NULL,
  `autor_livro` varchar(80) NOT NULL,
  `editora_livro` varchar(80) NOT NULL,
  PRIMARY KEY (`id_livro`),
  UNIQUE KEY `id_livro` (`id_livro`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=15 ;

--
-- Fazendo dump de dados para tabela `livro`
--

INSERT INTO `livro` (`id_livro`, `titulo_livro`, `categoria_livro`, `autor_livro`, `editora_livro`) VALUES
(5, 'Python', 'ProgramaÃ§Ã£o', 'Luiz', 'EdiÃ§Ã£o do autor'),
(7, 'Python para desenvolvedores', 'Tecnologia', 'Luiz Eduardo Borges', 'EdiÃ§Ã£o do Autor'),
(8, 'Java Web', 'programaÃ§Ã£o', 'gabriel', 'novatec'),
(9, 'Teste de Sofware', 'teste', 'desconhecido', 'teste'),
(11, 'Django Essencial', 'ProgramaÃ§Ã£o', 'Juliana Elman e Mark Lavin', 'Novatec'),
(12, 'ProgramaÃ§Ã£o Java', 'ProgramaÃ§Ã£o', 'Gabriel', 'Novatec'),
(14, 'Black Hat Python', 'SeguranÃ§a', 'Justin Seitz', 'Novatec');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
