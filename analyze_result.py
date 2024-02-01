import json
import matplotlib.pyplot as plt


def analyze_results(file_path, name_prefix, py_name):
    with open(file_path, "r", encoding="u8") as f:
        data = json.load(f)

    parsed_data = {eval(k): v for k, v in data.items()}

    aggregated_data = {}
    for (test, library), time in parsed_data.items():
        if library not in aggregated_data:
            aggregated_data[library] = {"total_time": 0, "count": 0}
        aggregated_data[library]["total_time"] += time
        aggregated_data[library]["count"] += 1

    for library, data in aggregated_data.items():
        data["average_time"] = data["total_time"] / data["count"]

    sorted_libraries = sorted(
        aggregated_data.items(), key=lambda x: x[1]["average_time"]
    )

    fastest_libraries = sorted_libraries[:3]
    slowest_libraries = list(reversed((sorted_libraries[-3:])))

    print("\n\n\n")
    print("=" * 30)
    print(f"Version {py_name}")

    print("Top 3 fastest libraries:")
    for library, data in fastest_libraries:
        print(f"{library}: {data['average_time']}")

    print("\nTop 3 slowest libraries:")
    for library, data in slowest_libraries:
        print(f"{library}: {data['average_time']}")

    libraries = [library for library, _ in sorted_libraries]
    average_times = [data["average_time"] for _, data in sorted_libraries]

    plt.figure(figsize=(10, 5))
    plt.bar(libraries, average_times, color="skyblue", edgecolor="black")
    plt.xlabel("Library")
    plt.ylabel("Average Time in seconds (less is better)")
    plt.title(f"Average Time for Each Library ({py_name})")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.savefig(f"imgs/All libraries (Average Time) ({name_prefix}).png")

    tests = set(test for test, _ in parsed_data.keys())
    for test in tests:
        libraries = []
        times = []

        av_data = list(parsed_data.items())
        av_data.sort(key=lambda i: i[1])

        for (t, library), time in av_data:
            if t == test:
                libraries.append(library)
                times.append(time)

        plt.figure(figsize=(10, 5))
        plt.bar(libraries, times, color="skyblue", edgecolor="black")
        plt.xlabel("Library")
        plt.ylabel("Time in seconds (less is better)")
        plt.title(f"Time for Each Library ({test}) {py_name}")
        plt.grid(axis="y", linestyle="--", alpha=0.4)
        plt.tight_layout()
        plt.savefig(f"imgs/Time for Each Library {test} ({name_prefix}).png")

    total_average = 0
    for library, data in aggregated_data.items():
        total_average += data["average_time"]

    if "orjson" in aggregated_data:
        print("Orjson:", aggregated_data["orjson"]["average_time"])


analyze_results("results/results3_8.json", "py3_8", "Py3.8")
analyze_results("results/results3_9.json", "py3_9", "py3.9")
analyze_results("results/results3_10.json", "py3_10", "py3.10")
analyze_results("results/results3_11.json", "py3_11", "py3.11")
analyze_results("results/results3_12.json", "py3_12", "py3.12")
analyze_results("results/results3_13.json", "py3_13", "py3.13")

# copied manually, from the "Orjson:" print in analyze_results
version_data = [
    ("Py3.8", 0.6685440625000036),
    ("Py3.9", 0.6504194375000032),
    ("Py3.10", 0.5858595124998374),
    ("Py3.11", 0.6099488249999467),
    ("Py3.12", 0.6505188500000259),
]

x = [item[0] for item in version_data]
y = [item[1] for item in version_data]

plt.figure(figsize=(10, 6))
plt.bar(x, y, color="skyblue", edgecolor="black")
plt.xlabel("Python Version (orjson)")
plt.ylabel("Benchmark Time (seconds, less is better)")
plt.title("Benchmark Results for Different Python Versions")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("imgs/orjson for Python versions.png")
