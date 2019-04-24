#!/bin/sh
BUNDLE_GEMFILE=/opt/metasploit/Gemfile bundle exec ruby /opt/metasploit/.tools/dev/add_pr_fetch.rb "$@"
