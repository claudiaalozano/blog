------------------------------------------------------------------
-- Práctica 2
-- Bases de datos
-- Ingeniería Informática, Universidad de Cantabria
------------------------------------------------------------------

-- Crea la base de datos. Si existe, la borra primero
-- Debe ejecutarse desde una conexión a otra base de datos (e.g. "postgres")

-- cierra toda conexión abierta contra la base de datos a borrar
SELECT pg_terminate_backend(pid) 
FROM pg_stat_activity 
WHERE datname = 'blog';

-- elimina la base de datos si ya existe
drop database if exists blog;

-- crea la base de datos
create database blog;
