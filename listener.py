# Listener implemented as a module using the listener API version 3.

def start_suite(data, result):
    print(f"Suite '{data.name}' starting.")

def end_test(data, result):
    print(f"Test '{result.name}' ended with status {result.status}.")

