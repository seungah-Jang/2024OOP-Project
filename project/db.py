from dotenv import load_dotenv
import os
import mysql.connector

# .env 파일 로드
load_dotenv()

def create_connection():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )

def insert_session(session_start_time, total_keystrokes, correct_cnt,elapsed_time,accuracy,wpm):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO TB_SESSION_RESULT (session_start_time, total_keystrokes, correct_cnt,elapsed_time,accuracy,wpm) VALUES (%s, %s, %s,%s, %s,%s, %s)",
        (session_start_time, total_keystrokes, correct_cnt,elapsed_time,accuracy,wpm)
    )
    conn.commit()
    session_id = cursor.lastrowid
    conn.close()
    return session_id

def insert_key_data(session_id, key_value, total_keyvalue, correct_keyvalue, incorrect_keyvalue):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO DB_2 (session_id, key_value, total_keyvalue, correct_keyvalue, incorrect_keyvalue) VALUES (%s, %s, %s, %s, %s)",
        (session_id, key_value, total_keyvalue, correct_keyvalue, incorrect_keyvalue)
    )
    conn.commit()
    conn.close()
