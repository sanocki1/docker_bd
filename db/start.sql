USE wydarzenia;

CREATE TABLE zapisy (
    id INT AUTO_INCREMENT PRIMARY KEY,
    imie VARCHAR(100),
    wydarzenie VARCHAR(100)
);

CREATE TABLE audit_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    operation_type VARCHAR(50),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    processed BOOLEAN DEFAULT FALSE
);

DELIMITER $$

CREATE TRIGGER registration_after_insert
AFTER INSERT ON zapisy
FOR EACH ROW
BEGIN

    INSERT INTO audit_logs(operation_type, description)
    VALUES(
        'INSERT',
        CONCAT(
            'Dodano uzytkownika ',
            NEW.imie,
            ' na wydarzenie ',
            NEW.wydarzenie
        )
    );

END$$

DELIMITER ;