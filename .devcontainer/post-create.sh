#!/usr/bin/env bash
set -euo pipefail

if ! command -v python3 >/dev/null 2>&1 || ! command -v ruby >/dev/null 2>&1; then
  sudo apt-get update
  sudo DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-pip python-is-python3 ruby-full
fi

cd /workspaces
if ! command -v aws >/dev/null 2>&1; then
  curl -fsSL "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o awscliv2.zip
  unzip -q awscliv2.zip
  sudo ./aws/install
  rm -f awscliv2.zip
  rm -rf aws
fi
