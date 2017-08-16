
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

    out_table = list()
    out_table.append(["name"              ,job.name])
    out_table.append(["full name"         ,job.get_full_name()])
    out_table.append(["first build number",job.get_first_buildnumber()])
    out_table.append(["last_build_number" ,job.get_last_buildnumber()])

    print(tabulate(out_table))










