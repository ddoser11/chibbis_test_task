CREATE_SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT,
    website TEXT,
    address_json TEXT,
    company_json TEXT
);

CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    body TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS comments (
    id INTEGER PRIMARY KEY,
    post_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    body TEXT NOT NULL,
    FOREIGN KEY (post_id) REFERENCES posts(id)
);
"""

UPSERT_USERS_SQL = """
INSERT INTO users (id, name, username, email, phone, website, address_json, company_json)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
ON CONFLICT(id) DO UPDATE SET
    name = excluded.name,
    username = excluded.username,
    email = excluded.email,
    phone = excluded.phone,
    website = excluded.website,
    address_json = excluded.address_json,
    company_json = excluded.company_json;
"""

UPSERT_POSTS_SQL = """
INSERT INTO posts (id, user_id, title, body)
VALUES (?, ?, ?, ?)
ON CONFLICT(id) DO UPDATE SET
    user_id = excluded.user_id,
    title = excluded.title,
    body = excluded.body;
"""

UPSERT_COMMENTS_SQL = """
INSERT INTO comments (id, post_id, name, email, body)
VALUES (?, ?, ?, ?, ?)
ON CONFLICT(id) DO UPDATE SET
    post_id = excluded.post_id,
    name = excluded.name,
    email = excluded.email,
    body = excluded.body;
"""
