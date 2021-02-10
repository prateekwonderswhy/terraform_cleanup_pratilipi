#!/bin/bash

cd /path/to/terraform_cleanup

terraform apply --auto-approve

terraform output -json > asg_names.json

python3 cleanup.py