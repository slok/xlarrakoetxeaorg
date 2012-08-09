# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant::Config.run do |config|

  # Environment
  config.vm.box = "precise32"
  config.vm.box_url = "http://files.vagrantup.com/precise32.box"

  # Forward ports -> guest, host 
  config.vm.forward_port 5000, 5001

  # Recipes to execute
  config.vm.provision :chef_solo do |chef|
    chef.cookbooks_path = "cookbooks"
    # This recipe installs all the other cookbooks
    chef.add_recipe "xlarrakoetxeaorgapp"

  
  # JSON attributes:
  chef.json = { 
    :postgresql => {
      :version => 9.1,
      :dbname => "xlarrakoetxeaorg",
      :password => {
        :postgres => "postgres"
      }
    }
  }
  end
end
