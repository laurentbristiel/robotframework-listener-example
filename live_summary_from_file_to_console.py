import time

LOG_FILE = "/Users/laurentbristiel/Development/robot3/listener_output.log"

def count_results():
    passed = 0
    failed = 0

    try:
        with open(LOG_FILE, "r") as f:
            for line in f:
                if "TEST ENDED" in line:
                    if "STATUS: PASS" in line:
                        passed += 1
                    elif "STATUS: FAIL" in line:
                        failed += 1
    except FileNotFoundError:
        print("Waiting for log file...")

    print(f"\n✅ Passed: {passed}  ❌ Failed: {failed}")

if __name__ == "__main__":
    while True:
        count_results()
        time.sleep(1)  # Refresh every second
