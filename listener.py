# Listener implemented as a module using the listener API version 3.

LOG_FILE = "listener_output.log"

def start_suite(data, result):
    """Logs when a test suite starts"""
    with open(LOG_FILE, "a") as f:
        f.write(f"⚪ SUITE STARTED: {data.name}\n")

def start_test(data, result):
    """Logs when a test starts"""
    with open(LOG_FILE, "a") as f:
        f.write(f"⚪ TEST STARTED: {data.name}\n")

def end_test(data, result):
    """Logs when a test ends"""
    status_symbol = "🟢" if result.status == "PASS" else "🔴"
    with open(LOG_FILE, "a") as f:
        f.write(f"{status_symbol} TEST ENDED: {data.name} - STATUS: {result.status}\n")

def end_suite(data, result):
    """Logs when a test suite ends"""
    status_symbol = "🟢" if result.status == "PASS" else "🔴"
    with open(LOG_FILE, "a") as f:
        f.write(f"{status_symbol} SUITE ENDED: {data.name} - STATUS: {result.status}\n")