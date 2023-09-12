-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 12-09-2023 a las 16:44:14
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `crud-flask_2`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `asignaciones`
--

CREATE TABLE `asignaciones` (
  `Id_asignaciones` int(11) NOT NULL,
  `id` int(11) DEFAULT NULL,
  `id_proceso` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `asignaciones`
--

INSERT INTO `asignaciones` (`Id_asignaciones`, `id`, `id_proceso`) VALUES
(44, 3, 725693814);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `procesos`
--

CREATE TABLE `procesos` (
  `id_proceso` int(11) NOT NULL,
  `Titulo` varchar(60) NOT NULL,
  `Descripcion` longtext DEFAULT NULL,
  `Fecha_creacion` date NOT NULL DEFAULT curdate(),
  `Fecha_terminación` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `procesos`
--

INSERT INTO `procesos` (`id_proceso`, `Titulo`, `Descripcion`, `Fecha_creacion`, `Fecha_terminación`) VALUES
(324761589, 'comer', 'tengo hambre we', '2023-08-24', '2023-08-24'),
(376412985, 'Entrega de suministros', '....', '2023-09-12', '2023-09-21'),
(725693814, 'programar', 'En el contexto de la frase \"I’m the antonymph of the internet\" que mencionaste anteriormente, podemos inferir que la artista vylet pony está utilizando el término \"antonymph\" para expresar que ella representa lo opuesto o contrastante con el mundo de internet.  Dado que la ninfa se asocia con la vitalidad y la belleza de la naturaleza, podemos interpretar que la artista está sugiriendo que ella es una fuerza opuesta a la artificialidad, la inautenticidad o los aspectos negativos que pueden estar presentes en el mundo en línea.  La frase \"Still cleaning up the viruses that you had left\" puede indicar que la artista está asumiendo el papel de limpiar y contrarrestar los efectos negativos dejados por otros en el entorno digital. Podría referirse a la idea de eliminar los aspectos tóxicos, los engaños o los problemas que pueden surgir en el mundo de internet.  En resumen, la frase \"I’m the antonymph of the internet\" en este contexto parece transmitir la idea de que la artista vylet pony se considera a sí misma como', '2023-08-28', '2023-08-28'),
(871436295, 'comer', 'tengo hambre we', '2023-08-24', '2023-08-24');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `NDI` int(20) NOT NULL,
  `password` char(102) NOT NULL,
  `fullname` varchar(50) NOT NULL,
  `Direccion` varchar(30) NOT NULL,
  `Telefono` int(15) NOT NULL,
  `Empresa` varchar(35) NOT NULL,
  `Cargo` varchar(25) NOT NULL,
  `Area_locativa` varchar(30) NOT NULL,
  `Email` varchar(35) NOT NULL,
  `Fecha_nacimiento` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Stores the user''s data.';

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id`, `NDI`, `password`, `fullname`, `Direccion`, `Telefono`, `Empresa`, `Cargo`, `Area_locativa`, `Email`, `Fecha_nacimiento`) VALUES
(1, 21474836, '12345678', 'deivid bautista', 'calle siempre viva109', 31212287, 'Americana de servicios L.T.D.A', 'Aprendiz', 'Oficina', 'debautist15@gmail.com', '2023-05-02'),
(3, 101016642, 'arnulfo', 'hernesto', '', 0, '', '', '', '', NULL),
(6, 10986287, 'owbeuf993', 'armin torres', 'wndnowbdo', 0, '', '', '', '', NULL);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `asignaciones`
--
ALTER TABLE `asignaciones`
  ADD PRIMARY KEY (`Id_asignaciones`),
  ADD KEY `fk_asignaciones_users` (`id`),
  ADD KEY `id_proceso` (`id_proceso`);

--
-- Indices de la tabla `procesos`
--
ALTER TABLE `procesos`
  ADD PRIMARY KEY (`id_proceso`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `asignaciones`
--
ALTER TABLE `asignaciones`
  MODIFY `Id_asignaciones` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;

--
-- AUTO_INCREMENT de la tabla `procesos`
--
ALTER TABLE `procesos`
  MODIFY `id_proceso` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483648;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `asignaciones`
--
ALTER TABLE `asignaciones`
  ADD CONSTRAINT `asignaciones_ibfk_1` FOREIGN KEY (`id_proceso`) REFERENCES `procesos` (`id_proceso`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_asignaciones_users` FOREIGN KEY (`id`) REFERENCES `users` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
