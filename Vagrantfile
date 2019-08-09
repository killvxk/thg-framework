# -*- mode: python -*-
# vi: set ft=python :

Vagrant.configure(2) do |config|
  config.ssh.forward_x11 = true
  config.vm.box = "ubuntu/xenial64"
  config.vm.network :forwarded_port, guest: 4444, host: 4444
  config.vm.provider "vmware" do |v|
	  v.memory = 2048
	  v.cpus = 2
  end
  config.vm.provider "virtualbox" do |v|
	  v.memory = 2048
	  v.cpus = 2
  end
  %w(.vimrc .gitconfig).each do |f|
    local = File.expand_path "~/#{f}"
    if File.exist? local
      config.vm.provision "file", source: local, destination: f
    end
  end

  [ #"echo 127.0.1.1 `cat /etc/hostname` >> /etc/hosts", work around a bug in official Ubuntu Xenial cloud images
    "apt-get update",
    "apt-get dist-upgrade -y",
    "apt-get -y install curl build-essential git tig vim john nmap libpq-dev libpcap-dev gnupg2 fortune ",
    "wget -qO - https://www.mongodb.org/static/pgp/server-4.0.asc | sudo apt-key add -",
    "echo 'deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/4.0 multiverse' | sudo tee /etc/apt/sources.list.d/mongodb-org-4.0.list",
    "sudo apt-get update",
    "sudo apt-get install -y mongodb-org",
  ].each do |step|
    config.vm.provision "shell", inline: step
  end

  [ "apt install python3-pip",
  ].each do |step|
    config.vm.provision "shell", privileged: false, inline: step
  end
  config.vm.provision "file", source: "config/database.yml.vagrant", destination: "~/.thg/database.yml"

  config.vm.provision "shell", inline: "sudo -u postgres psql postgres -tAc \"SELECT 1 FROM pg_roles WHERE rolname='vagrant'\" | grep -q 1 || sudo -u postgres createuser -s -e -w vagrant && sudo -u postgres psql -c \"ALTER USER vagrant with ENCRYPTED PASSWORD 'vagrant';\""

  ["thg_dev_db", "thg_test_db"].each do |database|
    config.vm.provision "shell", inline: "sudo -u postgres psql -lqt | awk '{ print $1 }' | grep -w #{database} | wc -l | grep -q 1 || sudo -u postgres createdb --owner vagrant #{database}"
  end
end
