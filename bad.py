# ===========================
# VERY BAD PYTHON CODE FOR SONARQUBE TESTING
# Contains: bugs, vulnerabilities, code smells, hardcoded secrets,
# duplicate code, SQL injection, XSS, infinite loops, unused code...
# ===========================

import os
import subprocess
import sqlite3

# --- BAD PRACTICE: Hardcoded passwords and secrets ---
PASSWORD = "admin123"
SECRET_KEY = "ASD123-ASD123-ASD123"

# --- BAD PRACTICE: Unused variables and functions ---
unused_var1 = 10
unused_var2 = "not used"

def unused_function():
    a = 10
    b = 20
    return a + b

# --- SECURITY VULNERABILITY: SQL Injection ---
def get_user(username):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE name = '{username}';"  # SQL Injection
    cursor.execute(query)
    return cursor.fetchall()

# --- SECURITY VULNERABILITY: OS Command injection ---
def run_system(command):
    os.system(command)  # dangerous

# --- SECURITY VULNERABILITY: Subprocess without sanitizing ---
def run_dangerous(cmd):
    return subprocess.Popen(cmd, shell=True)  # Very dangerous

# --- BAD LOGIC: Always true ---
def compare_values(a, b):
    if a == "True":
        print("This will always run")

# --- BAD: Infinite loop ---
def infinite_loop():
    while True:
        print("This is a bad infinite loop")  # never ends

# --- DUPLICATE CODE (copied 5x) ---
def duplicated_block():
    print("duplicate code")
    x = 10
    y = 20
    z = x + y
    return z

def duplicated_block2():
    print("duplicate code")
    x = 10
    y = 20
    z = x + y
    return z

def duplicated_block3():
    print("duplicate code")
    x = 10
    y = 20
    z = x + y
    return z

def duplicated_block4():
    print("duplicate code")
    x = 10
    y = 20
    z = x + y
    return z

def duplicated_block5():
    print("duplicate code")
    x = 10
    y = 20
    z = x + y
    return z

# --- BAD CODE SMELLS: huge function ---
def huge_function():
    print("starting huge function")
    total = 0
    for i in range(1000):
        for j in range(1000):
            total += i + j
            if i == 10:
                print("magic number detected")  # bad smell
    return total

# --- SECURITY HOTSPOT: Insecure file write ---
def write_sensitive_data():
    with open("passwords.txt", "w") as f:
        f.write("root:1234")  # extremely insecure

# --- BUG: division by zero ---
def buggy_division():
    value = 10 / 0
    return value

# --- BUG: undefined variable ---
def bad_reference():
    print(non_existing_variable)  # crash

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    get_user("admin'; DROP TABLE users; --")
    run_system("rm -rf /")  # SUPER dangerous
    huge_function()
