

include_recipe "apt"

execute "Update apt repos" do
    command "apt-get update"
end

include_recipe 'build-essential'
include_recipe 'openssl'
include_recipe 'postgresql::server'
include_recipe 'python'

execute "restart postgres" do
    command "sudo /etc/init.d/postgresql restart"
end

# Create the app database
bash "create-database" do
  user 'postgres'
  code <<-EOH
    dropdb -U postgres #{node[:postgresql][:dbname]}
    createdb -U postgres -O postgres #{node[:postgresql][:dbname]}
    #echo "ALTER ROLE postgres ENCRYPTED PASSWORD '#{node[:postgresql][:password][:postgres]}';" | psql
  EOH
  action :run
end

# Install all the dependencies in the virtualenv
bash "prepare-virtual-env" do
  code <<-EOH
    virtualenv /venv_xlarrakoetxeaorg
    source /venv_xlarrakoetxeaorg/bin/activate
    pip install -r /vagrant/requirements.txt
  EOH
  action :run
end