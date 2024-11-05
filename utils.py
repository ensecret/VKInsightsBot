#utils.py
import os
import logging

def load_sent_posts(filename):
    try:
        with open(filename, "r", encoding='utf-8') as f:
            sent = set(f.read().splitlines())
        return sent
    except FileNotFoundError:
        return set()

def save_sent_post(filename, post_id):
    with open(filename, "a", encoding='utf-8') as f:
        f.write(f"{post_id}\n")