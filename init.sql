-- Création de la table Etudiant --
CREATE TABLE Etudiant (
    id_etud SERIAL PRIMARY KEY, -- Identifiant unique de l'étudiant
    nom VARCHAR(50) NOT NULL, -- Nom de l'étudiant
    prenom VARCHAR(50) NOT NULL, -- Prénom de l'étudiant
    email VARCHAR(100) UNIQUE NOT NULL, -- Email de l'étudiant (unique)
    date_inscription DATE DEFAULT CURRENT_DATE, -- Date d'inscription
    solde_amende NUMERIC(5,2) DEFAULT 0 CHECK (solde_amende >= 0) -- Solde des amendes
);

-- Création de la table Livre --
CREATE TABLE Livre (
    isbn CHAR(13) PRIMARY KEY, -- ISBN unique du livre
    titre VARCHAR(200) NOT NULL, -- Titre du livre
    editeur VARCHAR(100), -- Éditeur du livre
    annee INT CHECK (annee > 1900 AND annee < 2027), -- Année de publication
    exemplaires_dispo INT DEFAULT 1 CHECK (exemplaires_dispo >= 0) -- Nombre d'exemplaires disponibles
);

-- Création de la table Emprunt --
CREATE TABLE Emprunt (
    id_emprunt SERIAL PRIMARY KEY, -- Identifiant unique de l'emprunt
    id_etud INT NOT NULL, -- Référence à l'étudiant
    isbn CHAR(13) NOT NULL, -- Référence au livre
    date_emprunt DATE NOT NULL, -- Date de l'emprunt
    date_retour DATE, -- Date de retour (peut être NULL si pas encore retourné)
    amende NUMERIC(5,2) DEFAULT 0, -- Amende associée à l'emprunt
    CONSTRAINT fk_etud FOREIGN KEY (id_etud) 
        REFERENCES Etudiant(id_etud) ON DELETE RESTRICT, -- Contrainte de clé étrangère vers Etudiant
    CONSTRAINT fk_livre FOREIGN KEY (isbn)
        REFERENCES Livre(isbn) ON DELETE RESTRICT -- Contrainte de clé étrangère vers Livre
);

-- Indexation des colonnes Etudiant.nom et Emprunt.date_emprunt --
CREATE INDEX idx_nom ON Etudiant(nom); -- Index sur le nom de l'étudiant
CREATE INDEX idx_date_emprunt ON Emprunt(date_emprunt); -- Index sur la date d'emprunt

-- Insertion des étudiants --
INSERT INTO Etudiant (nom, prenom, email, solde_amende) VALUES
('Dupont', 'Jean', 'jean.dupont@example.com', 2.50),
('Martin', 'Sophie', 'sophie.martin@example.com', 0.00),
('Bernard', 'Luc', 'luc.bernard@example.com', 1.00),
('Durand', 'Claire', 'claire.durand@example.com', 0.00),
('Leroy', 'Paul', 'paul.leroy@example.com', 0.75);

-- Insertion des livres --
INSERT INTO Livre (isbn, titre, editeur, annee, exemplaires_dispo) VALUES
('9782070368228', 'L''Étranger', 'Gallimard', 1942, 2),
('9782070409181', '1984', 'Gallimard', 1949, 0),
('9782253004226', 'Le Seigneur des Anneaux', 'Pocket', 1954, 3),
('9782253006329', 'Fondation', 'Pocket', 1951, 1),
('9782070413119', 'Fahrenheit 451', 'Gallimard', 1953, 0),
('9782266286260', 'Harry Potter à l''école des sorciers', 'Bloomsbury', 1997, 4),
('9782266286277', 'Harry Potter et la Chambre des secrets', 'Bloomsbury', 1998, 1),
('9782070451562', 'Dune', 'Robert Laffont', 1965, 2),
('9782290320899', 'The Witcher : Le Dernier Vœu', 'Bragelonne', 1993, 5),
('9782366291779', 'Metro 2033', 'L''Atalante', 2005, 1),
('9780132350884', 'Clean Code', 'Prentice Hall', 2008, 2),
('9780134494166', 'Clean Architecture', 'Prentice Hall', 2017, 1),
('9781491950357', 'Designing Data-Intensive Applications', 'O''Reilly', 2017, 0),
('9780201633610', 'Design Patterns', 'Addison-Wesley', 1994, 1),
('9781617294136', 'Spring in Action', 'Manning', 2018, 2),
('9784041029806', 'Death Note Vol.1', 'Shueisha', 2004, 3),
('9782723498729', 'Watchmen', 'DC Comics', 1987, 1),
('9782365773467', 'Akira Vol.1', 'Kodansha', 1982, 2),
('9782376862857', 'Cyberpunk 2077 : No Coincidence', 'Orbit', 2023, 1),
('9782380170312', 'The Art of Game Design', 'CRC Press', 2015, 2);

-- Insertion des emprunts --
INSERT INTO Emprunt (id_etud, isbn, date_emprunt, date_retour, amende) VALUES
(1, '9782070368228', '2025-01-05', '2025-01-15', 0),
(2, '9782253004226', '2025-01-10', '2025-01-20', 0),
(3, '9782266286260', '2025-01-12', '2025-01-22', 0),
(4, '9782070451562', '2025-01-15', '2025-01-25', 0),
(5, '9780132350884', '2025-01-18', '2025-01-28', 0);

-- Emprunts en cours (date_retour NULL) --
INSERT INTO Emprunt (id_etud, isbn, date_emprunt, date_retour, amende) VALUES
(1, '9782070451562', '2025-12-01', NULL, 0),
(3, '9782266286260', '2025-12-03', NULL, 0),
(5, '9780132350884', '2025-12-05', NULL, 0);

-- Emprunts en retard --
INSERT INTO Emprunt (id_etud, isbn, date_emprunt, date_retour, amende) VALUES
(2, '9782070409181', '2025-11-01', '2025-11-21', 3.00),
(4, '9782070413119', '2025-11-05', '2025-11-29', 5.00);