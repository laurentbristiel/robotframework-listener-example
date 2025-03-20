import matplotlib.pyplot as plt

LOG_FILE = "/Users/laurentbristiel/Development/robot3/listener_output.log"

def count_results():
    """Count the number of passed and failed tests"""
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
        pass

    return passed, failed

def live_plot():
    """Update the bar chart dynamically"""
    plt.ion()  # Interactive mode ON
    fig, ax = plt.subplots()

    while True:
        passed, failed = count_results()

        ax.clear()
        ax.bar(["Passed", "Failed"], [passed, failed], color=["green", "red"])
        ax.set_ylabel("Number of Tests")
        ax.set_title("Live Test Results")

        plt.pause(1)  # Refresh every second

if __name__ == "__main__":
    live_plot()
