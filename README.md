# Jenkins API

Script to call the Jenkins API on the specified ENDPOINT to list all active jobs, with status of the last successful build of a specified job.

The client API library used is [jenkinsapi](https://github.com/pycontribs/jenkinsapi).

## Installation
```
pip install jenkinsapi
```

## Execution
Specify your `TOKEN`, `ENDPOINT` and `JOBNAME` inside the script.
```python
TOKEN = 'abcdef'
ENDPOINT = 'http://localhost:8080'
JOBNAME = 'test-job'
```
Then open console and run
```sh
python3 main.py
```

## References
https://jenkinsapi.readthedocs.io/en/latest/