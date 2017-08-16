import os
import json
from tabulate import tabulate

from jenkinsapi.jenkins import Jenkins

def read_config():
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '00-config.json')
    config_fd = open(config_path, 'r')
    config = json.load(config_fd)

    return config


if __name__ == "__main__":

    config = read_config()
    jenkins_url = config["jenkins_url"]
    print("Connecting to Jenkins at %s" % jenkins_url )
    j = Jenkins(jenkins_url)
    print("Jenkins version is %s" % j.version)

    job = j.get_job(config['jenkins_job'])

    last_build_number = job.get_last_buildnumber()
    last_build_meta= job.get_build_metadata(last_build_number)

    last_build = job.get_build(last_build_number)

    last_build_console = last_build.get_console()

    print(last_build_console)



