## Catnotfoundnear's code for "Benchmarking all JSON libraries on all Python versions"

Welcome to the README for the code related to the Catnotfoundnear's blog article "Benchmarking all JSON libraries on all Python versions". This code is designed to accompany the blog article, which can be found at [Catnotfoundnear's Blog](https://catnotfoundnear.github.io/).

**This benchmark tests out the following JSON libraries:**
1. orjson
2. nujson
3. pysimdjson
4. yapic.json
5. simplejson
6. ujson
7. python-rapidjson
8. cysimdjson

**Testing System:**
The code was tested on a Windows 10 system with an Intel i5-8365U processor and 8GB of RAM. It's important to note that the availability of libraries may vary across different Python versions due to compatibility issues. As a result, subsequent Python versions may have fewer libraries available for testing. This is often due to certain libraries not supporting newer Python versions or encountering build issues on the testing system.

**Code Description:**
The code provided in this repository is specifically tailored for benchmarking JSON libraries across various Python versions. It aims to provide insights into the performance of these libraries under different Python environments. The results and analysis of this benchmarking process are detailed in the associated blog article.

**How to Use:**
To utilize this code for benchmarking JSON libraries on different Python versions, follow these steps:
1. Clone or download the repository from the provided link.
2. Ensure that the required Python versions are installed on your system (run "py --list" to check)
3. Run "setup_envs.bat" - this will setup envs, install libraries, and copy the benchmarking script and data to each env.
4. Run "run_all_benchs.bat" - this will run benchmarks for each env, sequentially. Then, collect the results and analyze them, finally, generating some charts in the "imgs" dir.

**Contributions:**
Contributions and feedback on the code and benchmarking results are welcome. Feel free to submit issues or pull requests to enhance the functionality and accuracy of the benchmarking process. (the code is messy as hell, thank you, I am aware of this, okay?)

For a detailed analysis and findings, please visit [Catnotfoundnear's Blog](https://catnotfoundnear.github.io/).

If you have any questions or need further assistance, feel free to reach out (catnotfoundnear AT proton.me).

Happy benchmarking!
