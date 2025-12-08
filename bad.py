password = "123456"  # Hardcoded secret (Security Hotspot)

def add(a, b):
    return a + b

# Duplicate function (Code Smell)
def add(a, b):
    return a + b

# Always-true condition (Bug)
if True == "True":
    print("bad logic")

# Unused variable
x = 10
