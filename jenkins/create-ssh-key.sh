#!/bin/bash

# Script to create an SSH key for Jenkins Agent

set -eo pipefail

ssh-keygen -t ed25519 -f jenkins.id_ed25519 -C jenkins.