DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS UserPairs;
DROP TABLE IF EXISTS BankFileFormats;
DROP TABLE IF EXISTS UserFileFormatPreferences;
DROP TABLE IF EXISTS Categories;
DROP TABLE IF EXISTS Transactions;
DROP TABLE IF EXISTS TransactionRules;


CREATE TABLE Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE UserPairs (
    user_id INTEGER NOT NULL,
    pair_id INTEGER NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, pair_id),
    FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE,
    FOREIGN KEY (pair_id) REFERENCES Users(id) ON DELETE CASCADE,
    CHECK (user_id < pair_id)
);


CREATE TABLE BankFileFormats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE UserFileFormatPreferences (
    user_id INTEGER NOT NULL,
    format_id INTEGER NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, format_id),
    FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE,
    FOREIGN KEY (format_id) REFERENCES BankFileFormats(id) ON DELETE CASCADE
);


CREATE TABLE Categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,  -- NULL if global
    name TEXT NOT NULL,
    type TEXT NOT NULL CHECK(type IN ('expense','income')),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE SET NULL
);


CREATE TABLE Transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    date DATE NOT NULL,
    amount REAL NOT NULL,
    description TEXT,
    raw_data TEXT,  -- JSON stored as TEXT
    category_id INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES Categories(id) ON DELETE SET NULL
);


CREATE TABLE TransactionRules (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    pattern TEXT NOT NULL,
    category_id INTEGER NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES Categories(id) ON DELETE CASCADE
);


-- For quickly fetching transactions of a user
CREATE INDEX idx_transactions_user_id ON Transactions(user_id);

-- For fetching transactions by category
CREATE INDEX idx_transactions_category_id ON Transactions(category_id);

-- For fetching transactions by date (monthly summaries)
CREATE INDEX idx_transactions_date ON Transactions(date);

-- For quickly fetching all pairs of a user
CREATE INDEX idx_userpairs_user_id ON UserPairs(user_id);

-- For rules lookup per user
CREATE INDEX idx_transactionrules_user_id ON TransactionRules(user_id);

-- Optional: composite index to speed up user + category queries
CREATE INDEX idx_transactions_user_category ON Transactions(user_id, category_id);

