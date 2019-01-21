from jenkinsapi.jenkins import Jenkins

TOKEN = '113941e94f1f89c7153d965cfab80d6c70'
ENDPOINT = 'http://localhost:8080'
JOBNAME = 'ao-raghav-test'

J = Jenkins(ENDPOINT, username='teraflik', password=TOKEN)

job = J[JOBNAME]
lgb = job.get_last_good_build()

for j in J.get_jobs():
    job = J[JOBNAME]
    print ('Job Name:%s' %(job_instance.name))
    print ('Job Description:%s' %(job_instance.get_description()))
    print ('Is Job running:%s' %(job_instance.is_running()))
    print ('Is Job enabled:%s' %(job_instance.is_enabled()))

print("Last good job: {}".format(lgb))
print("Successful: {}".format(lgb.is_good()))