import json
from timeit import timeit
import importlib

LIBS = (
    "json",
    "orjson",
    "cysimdjson",
    "nujson",
    "simdjson",
    "yapic.json",
    "simplejson",
    "ujson",
    "rapidjson",
)


def load_data_file(path):
    with open(path, "r", encoding="utf8") as f:
        return f.read()


def load_libs():
    libs_to_test = {}

    for lib in LIBS:
        try:
            libs_to_test[lib] = importlib.import_module(lib)
        except ModuleNotFoundError:
            print(f"Failed to import {lib}. Skipping.")

    return libs_to_test


def run_benchmarks(benchmarks, n):
    results = {}

    for benchmark_name, bench_func in benchmarks:
        for lib_name, lib in libs_to_test.items():
            print(f'Running benchmark "{benchmark_name}" with {lib_name}.')

            try:
                t = timeit(lambda: bench_func(lib), number=n)
                results[(benchmark_name, lib_name)] = t
            except Exception as e:
                print(f"Library {lib_name} failed to run this bench ({e}).")

    return results


libs_to_test = load_libs()
print(f"Benchmarking {len(libs_to_test)} libraries:", libs_to_test.keys())

if "cysimdjson" in libs_to_test:
    _cysimdjson = libs_to_test["cysimdjson"].JSONParser()
    cysimdjson = type(
        "MockCysimdjson", (), {"loads": lambda i: _cysimdjson.parse_string(i).export()}
    )
    libs_to_test["cysimdjson"] = cysimdjson

canada_str = load_data_file("canada.json")
citm_catalog_str = load_data_file("citm_catalog.json")
github_str = load_data_file("github.json")
twitter_str = load_data_file("twitter.json")

benchmarks = (
    ("dumps_canada", lambda lib: lib.dumps(canada_str)),
    ("dumps_citm_catalog", lambda lib: lib.dumps(citm_catalog_str)),
    ("dumps_github", lambda lib: lib.dumps(github_str)),
    ("dumps_twitter", lambda lib: lib.dumps(twitter_str)),
    ("loads_canada", lambda lib: lib.loads(canada_str)),
    ("loads_citm_catalog", lambda lib: lib.loads(citm_catalog_str)),
    ("loads_github", lambda lib: lib.loads(github_str)),
    ("loads_twitter", lambda lib: lib.loads(twitter_str)),
)

print("\nRunning benchmarks (n=1, to warm-up)...\n")
run_benchmarks(benchmarks, n=1)

print("\nRunning benchmarks...\n")
results = run_benchmarks(benchmarks, n=300)
print(results)

with open("results.json", "w") as f:
    results = {repr(key): value for key, value in results.items()}
    serialized = json.dump(results, f)

print('Saved results to "results.json"!')
