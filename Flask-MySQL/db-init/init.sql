use db;

CREATE TABLE favorite_colors (
  nn VARCHAR(20),
  color VARCHAR(10)
);

INSERT INTO favorite_colors
  (nn, color)
VALUES
  ('Lancelot', 'blue'),
  ('Galahad', 'yellow');