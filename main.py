import json
import sqlite3
import requests

from sql_queries import (
    CREATE_SCHEMA_SQL,
    UPSERT_COMMENTS_SQL,
    UPSERT_POSTS_SQL,
    UPSERT_USERS_SQL,
)


BASE_URL = "https://jsonplaceholder.typicode.com"
DB_PATH = "jsonplaceholder.db"


def fetch_json(endpoint):
    url = f"{BASE_URL}/{endpoint}"
    response = requests.get(url, timeout=15)
    response.raise_for_status()
    return response.json()


def create_schema(conn):
    conn.executescript(CREATE_SCHEMA_SQL)


def save_users(conn, users):
    conn.executemany(
        UPSERT_USERS_SQL,
        [
            (
                user["id"],
                user["name"],
                user["username"],
                user["email"],
                user.get("phone"),
                user.get("website"),
                json.dumps(user.get("address", {}), ensure_ascii=False),
                json.dumps(user.get("company", {}), ensure_ascii=False),
            )
            for user in users
        ],
    )


def save_posts(conn, posts):
    conn.executemany(
        UPSERT_POSTS_SQL,
        [(post["id"], post["userId"], post["title"], post["body"]) for post in posts],
    )


def save_comments(conn, comments):
    conn.executemany(
        UPSERT_COMMENTS_SQL,
        [
            (
                comment["id"],
                comment["postId"],
                comment["name"],
                comment["email"],
                comment["body"],
            )
            for comment in comments
        ],
    )


def count_rows(conn):
    tables = ("users", "posts", "comments")
    result = {}
    for table in tables:
        result[table] = conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
    return result


def main():
    try:
        users = fetch_json("users")
        posts = fetch_json("posts")
        comments = fetch_json("comments")
    except requests.exceptions.RequestException as error:
        print(f"Ошибка при загрузке данных: {error}")
        return

    with sqlite3.connect(DB_PATH) as conn:
        create_schema(conn)
        save_users(conn, users)
        save_posts(conn, posts)
        save_comments(conn, comments)
        conn.commit()
        totals = count_rows(conn)

    print("Импорт завершен успешно.")
    print(f"users: {totals['users']}")
    print(f"posts: {totals['posts']}")
    print(f"comments: {totals['comments']}")


if __name__ == "__main__":
    main()