#!/usr/bin/env bash
set -euo pipefail

cd /workspaces
curl -fsSL "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o awscliv2.zip
unzip -q awscliv2.zip
sudo ./aws/install
rm -f awscliv2.zip
rm -rf aws
