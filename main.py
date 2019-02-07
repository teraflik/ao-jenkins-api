'''
This script calls the Jenkins API on the specified ENDPOINT to list all active jobs, with status of the last succesful build of a specified job.
The client API library used is [jenkinsapi](https://github.com/pycontribs/jenkinsapi).
Installation: pip install jenkinsapi
Documentation: https://jenkinsapi.readthedocs.io/en/latest/
'''

from jenkinsapi.jenkins import Jenkins

TOKEN = '113941e94f1f89c7153d965cfab80d6c70'
ENDPOINT = 'http://localhost:8080'
JOBNAME = 'ao-raghav-test'

J = Jenkins(ENDPOINT, username='teraflik', password=TOKEN)

print ("===== ALL JOBS =====")
for index, job in enumerate(J.get_jobs()):
    print ("{:d}-".format(index+1))
    print ('Name: %s' %job[1].name)
    print ('Description: %s' %job[1].get_description())
    print ('Running: %s' %job[1].is_running())
    print ('Enabled: %s' %job[1].is_enabled())

test_job = J[JOBNAME]
lgb = test_job.get_last_good_build()
print("\nLast good build for job '{}': {}".format(JOBNAME, lgb))
