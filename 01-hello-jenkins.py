
import os
import json

import jenkinsapi

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

    jenkins_keys = j.keys()

    print(json.dumps(jenkins_keys,indent=4))

