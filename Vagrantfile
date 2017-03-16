# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "geerlingguy/ubuntu1604"

  config.vm.box_check_update = false
  
  config.vm.network :forwarded_port, guest: 8080, host: 8080
  config.vm.network :forwarded_port, guest: 8989, host: 8989
  config.vm.network :forwarded_port, guest: 8000, host: 8000

  config.vm.network "private_network", ip: "192.168.33.10"

  config.ssh.forward_agent = true

  config.vm.synced_folder ".", "/jenkins"

  config.vm.provider :virtualbox do |vb|
      vb.customize ["modifyvm", :id, "--memory",  "2048"]
      vb.customize ["modifyvm", :id, "--acpi",    "on"]
      vb.customize ["modifyvm", :id, "--ioapic",  "on"]
      vb.customize ["modifyvm", :id, "--cpus",    "2"]
  end

  config.vm.provision "ansible" do |ansible|
    ansible.host_key_checking = false
    ansible.playbook = "vagrant-jenkins.yml"
    ansible.limit = 'all'
    ansible.inventory_path = "inventory/vagrant-jenkins"
    ansible.verbose = 'vv'
  end
end
