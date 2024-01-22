#!/bin/sh

certbot certonly --manual --dry-run --preferred-challenges dns-01 -d "*.a4barros.com,a4barros.com" --manual-auth-hook "python3 linode-post-txt.py" --manual-cleanup-hook "python3 linode-delete-txt.py"
