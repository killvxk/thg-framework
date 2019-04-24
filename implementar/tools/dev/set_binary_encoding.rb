#!/bin/sh
BUNDLE_GEMFILE=/opt/metasploit/Gemfile bundle exec ruby /opt/metasploit/.tools/dev/set_binary_encoding.rb "$@"
