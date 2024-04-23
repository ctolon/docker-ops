#!/bin/bash

# Script to create Jenkins directories with proper permissions

set -eo pipefail

mkdir -pv {jenkins_backup,jenkins_home}

chmod 775 -R {jenkins_backup,jenkins_home}