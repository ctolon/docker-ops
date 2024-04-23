#!/bin/bash

# Script to get the initial password for Jenkins

set -eo pipefail

docker exec -it jenkins-controller bash -c "cat /var/jenkins_home/secrets/initialAdminPassword"