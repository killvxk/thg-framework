#!/bin/sh
BUNDLE_GEMFILE=/opt/metasploit/Gemfile bundle exec ruby /opt/metasploit/.tools/hardware/elm327_relay.rb "$@"
