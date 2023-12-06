GRANT ALL PRIVILEGES ON *.* TO 'tomo'@'localhost' IDENTIFIED BY 'waw';;

GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'tomo'@'localhost' WITH GRANT OPTION;

sudo systemctl restart mysql

