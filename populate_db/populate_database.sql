-- Description: Script to populate the database with some data for testing purposes

INSERT INTO app_user (user_id, name, email, role) VALUES
(1, 'VITOR GUIRAO SOLLER', '21.01444-2@maua.br', 'STUDENT'),
(2, 'JOAO VITOR CHOUERI BRANCO', '21.01075-7@maua.br', 'STUDENT'),
(3, 'BRUNO VILARDI BUENO', '19.00331-5@maua.br', 'STUDENT'),
(4, 'CARLOS EDUARDO DANTAS DE MENEZES', 'carlos.menezes@maua.br', 'PROFESSOR'), -- Advisor
(5, 'ANA PAULA GONCALVES SERRA', 'ana.serra@maua.br', 'PROFESSOR'), -- Responsible
(6, 'SILVIO SANTOS', 'silvio.santos@sbt.br', 'STUDENT'),
(7, 'JOSE MARIA', 'jose.maria@sbt.br', 'PROFESSOR'), -- Responsible
(8, 'VANDERLEI CUNHA PARRO', 'vcp@maua.br', 'PROFESSOR'), -- Advisor
(9, 'RODRIGO MORALES MILES', 'rodrigo.miles@maua.br', 'STUDENT'), -- Student without project
(10, 'FERNANDO ANDRADE RODRIGUES', 'fernando.rodrigues@maua.br', 'ADMIN');

INSERT INTO app_project (project_id, title, qualification, code, shift, stand_number, is_entrepreneurship) VALUES
(1, 'Teste', 'Engenharia da Computação', 'ECOM000', 'DIRUNO', '1', FALSE),
(2, 'Teste 2', 'Design', 'DSGN123', 'NOTURNO', '2', FALSE),
(3, 'Teste 3', 'Administração', 'ADM123', 'DIURNO', '1', FALSE);

-- Associar advisors
INSERT INTO app_project_advisors (project_id, user_id) VALUES
(1, 4),
(2, 4),
(2, 8),
(3, 4),
(3, 8);

-- Associar responsibles
INSERT INTO app_project_responsibles (project_id, user_id) VALUES
(1, 5),
(2, 7),
(3, 5);

-- Associar students
INSERT INTO app_project_students (project_id, user_id) VALUES
(1, 1),
(1, 2),
(2, 3),
(3, 6);

INSERT INTO app_task (task_id, title, delivery_date, responsible) VALUES
(1, 'Dados do trabalho', '2023-05-15', 'STUDENT'),
(2, 'Dados do trabalho', '2023-05-22', 'ADVISOR'),
(3, 'Dados do trabalho', '2023-09-14', 'RESPONSIBLE'),
(4, 'Pôster Técnico (PDF)', '2023-10-01', 'STUDENT'),
(5, 'Pôster Técnico (PDF)', '2023-10-03', 'ADVISOR'),
(6, 'Pôster Imagem', '2023-09-17', 'STUDENT'),
(7, 'Pôster Imagem', '2023-09-20', 'ADVISOR'),
(8, 'Tirar usuário do sistema', '2023-10-10', 'ADMIN');
