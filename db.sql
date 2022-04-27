CREATE TABLE IF NOT EXISTS titles (
                                     id TEXT PRIMARY KEY,
                                     type TEXT NOT NULL,
                                     title TEXT NOT NULL,
                                     release_year INTEGER NOT NULL,
                                     rating TEXT NOT NULL,
                                     duration TEXT NOT NULL,
                                     genre TEXT NOT NULL,
                                     description TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS staffs (
                                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                                     director TEXT,
                                     cast TEXT,
                                     show_id INTEGER NOT NULL,
                                     FOREIGN KEY (show_id) REFERENCES titles(id)
);