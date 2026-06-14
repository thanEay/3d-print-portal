from flask import Flask
import sqlite3


conn = sqlite3.connect("prints.db")
cursor = conn.cursor()

