# -*- mode: ruby -*-
# vi: set ft=ruby :
# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

$my_install = <<SCRIPT
sudo apt install build-essential git -y
sudo apt install postgresql postgresql-server-dev-9.3 python3-dev libxml2-dev libxslt-dev postgresql-server-dev-9.3 -y
sudo apt install libffi-dev python3.4-venv -y

cd $HOME
pyvenv-3.4 .venv34
. .venv34/bin/activate

cd ~/files/srw.zesar/
pip install Babel
pip install bcrypt
pip install WebOb
pip install pyramid
pip install gunicorn

pip install -r requirements.txt
python setup.py develop

cd ~/files/soapfish-0.6.dev0
pip install -r requirements.txt
python setup.py develop

cp /home/vagrant/files/database.sql /tmp
chmod 644 /tmp/database.sql
sudo su - postgres -c '/usr/bin/psql -Upostgres < /tmp/database.sql'
rm -rf /tmp/database.sql

cd ~/files
zesar-dbinit production.ini

#without create user goes wrong
pip install passlib --upgrade

#changeme
zesar-create-user production.ini --username=srw --password=secret --is-srw

cat > /home/vagrant/run.sh <<'ENDOFMESSAGE'
cd $HOME
#pyvenv-3.4 .venv34
. .venv34/bin/activate
gunicorn --paste ~/files/production.ini
ENDOFMESSAGE

SCRIPT


$my_install_ubu_16 = <<SCRIPT
sudo apt update
sudo apt install build-essential git -y
sudo apt-get install postgresql postgresql-server-dev-9.5 python3-dev libxml2-dev libxslt-dev postgresql-server-dev-9.5 -y
sudo apt-get install libffi-dev python3.5-venv -y

cd $HOME
pyvenv-3.5 .venv35
. .venv35/bin/activate

cd ~/files/srw.zesar/

pip install pip --upgrade
pip install wheel
pip install Babel
pip install bcrypt
pip install WebOb
pip install pyramid
pip install gunicorn

pip install -r requirements.txt
python setup.py develop

cd ~/files/soapfish-0.6.dev0
pip install -r requirements.txt
python setup.py develop

cp /home/vagrant/files/database.sql /tmp
chmod 644 /tmp/database.sql
sudo su - postgres -c '/usr/bin/psql -Upostgres < /tmp/database.sql'
rm -rf /tmp/database.sql

cd ~/files
zesar-dbinit production.ini

#without create user goes wrong
pip install passlib --upgrade

zesar-create-user production.ini --username=srw --password=secret --is-srw

cat > /home/vagrant/run.sh <<'ENDOFMESSAGE'
cd $HOME
#pyvenv-3.5 .venv35
. .venv35/bin/activate
gunicorn --paste ~/files/production.ini

ENDOFMESSAGE

SCRIPT

$my_install_c73 = <<SCRIPT
sudo yum install perl -y
sudo yum install epel-release -y
sudo yum install vim-enhanced -y

sudo yum install -y python-devel glibc-devel zlib-devel xz-devel libxml2-devel libgpg-error-devel libgcrypt-devel libxslt-devel libffi-devel postgresql-devel python34-devel popt-devel rpm-devel keyutils-libs-devel pcre-devel libsepol-devel libselinux-devel libverto-devel libcom_err-devel krb5-devel openssl-devel git

sudo yum install postgresql-server -y

sudo postgresql-setup initdb
sudo perl -pi -e 's#127.0.0.1.*?ident#127.0.0.1\t\tmd5#g' /var/lib/pgsql/data/pg_hba.conf
sudo perl -pi -e 's#::1/128.*?ident#::1/128\t\tmd5#g' /var/lib/pgsql/data/pg_hba.conf
sudo systemctl start postgresql
sudo systemctl restart postgresql
sudo systemctl enable postgresql

cp /home/vagrant/files/database.sql /tmp
chmod 644 /tmp/database.sql
sudo su - postgres -c '/usr/bin/psql -Upostgres < /tmp/database.sql'
rm -rf /tmp/database.sql

sudo yum install -y python34-pip.noarch python34-setuptool python34 python34-devel
sudo yum install -y gcc rpm-devel

sudo pip3.4 install virtualenv
virtualenv .venv34
. .venv34/bin/activate

cd ~/files/srw.zesar/
pip install Babel
pip install bcrypt
pip install WebOb
pip install pyramid
pip install gunicorn

pip install -r requirements.txt
python setup.py develop

cd ~/files/soapfish-0.6.dev0
pip install -r requirements.txt
python setup.py develop

cd ~/files
zesar-dbinit production.ini

#without create user goes wrong
pip install passlib --upgrade

#changeme
zesar-create-user production.ini --username=srw --password=secret --is-srw

cat > /home/vagrant/run.sh <<'ENDOFMESSAGE'
cd $HOME
. .venv34/bin/activate
gunicorn --paste ~/files/production.ini
ENDOFMESSAGE



SCRIPT


Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.define :ubu1 do |ubu1|
        ubu1.vm.box = "ubuntu/trusty64"
        ubu1.vm.hostname = 'ubu1-14'
        ubu1.vm.network  :private_network, :ip => "192.168.192.51",
        :libvirt__network_name => "default"  # leave it

        ubu1.vm.provider :libvirt do |libvirt|
            libvirt.storage_pool_name = "vagrant"
            #libvirt.storage :file, :size =>'10G', :type => 'qcow2'
            #libvirt.storage :file, :size =>'20G', :type => 'qcow2'
        end
        ubu1.vm.provider :libvirt do |domain|
            domain.cpus = 2
            domain.cpu_mode = 'host-passthrough'
            domain.memory = 2048
            domain.nested = false
            domain.volume_cache = 'none'
        end
        ubu1.vm.synced_folder "./files", "/home/vagrant/files", disabled: false, create: true, owner: "vagrant", group: "vagrant"
        ubu1.vm.provision "shell", inline: $my_install, privileged: false
    end

    config.vm.define :ubu2 do |ubu2|
        ubu2.vm.box = "xenial/libvirt"
        ubu2.vm.box_url = "http://nd-build-01.linux-appliance.net/vagrant/boxes/xenial_libvirt_0.1.0.box"
        ubu2.vm.hostname = 'ubu2-16'
        ubu2.vm.network  :private_network, :ip => "192.168.192.52",
        :libvirt__network_name => "default"  # leave it
        ubu2.vm.provider :libvirt do |libvirt|
            libvirt.storage_pool_name = "vagrant"
            #libvirt.storage :file, :size =>'10G', :type => 'qcow2'
            #libvirt.storage :file, :size =>'20G', :type => 'qcow2'
        end
        ubu2.vm.provider :libvirt do |domain|
            domain.cpus = 2
            domain.cpu_mode = 'host-passthrough'
            domain.memory = 2048
            domain.nested = false
            domain.volume_cache = 'none'
        end
        ubu2.vm.synced_folder "./files", "/home/vagrant/files", disabled: false, create: true, owner: "vagrant", group: "vagrant"
        ubu2.vm.provision "shell", inline: $my_install_ubu_16, privileged: false
    end

    config.vm.define :c73 do |c73|
        c73.vm.box = "centos/7"
        c73.vm.hostname = 'c73-01'
        c73.vm.network  :private_network, :ip => "192.168.192.53",
        :libvirt__network_name => "default"  # leave it
        c73.vm.provider :libvirt do |libvirt|
            libvirt.storage_pool_name = "vagrant"
            #libvirt.storage :file, :size =>'10G', :type => 'qcow2'
            #libvirt.storage :file, :size =>'20G', :type => 'qcow2'
        end
        c73.vm.provider :libvirt do |domain|
            domain.cpus = 2
            domain.cpu_mode = 'host-passthrough'
            domain.memory = 2048
            domain.nested = false
            domain.volume_cache = 'none'
        end
        c73.vm.synced_folder "./files", "/home/vagrant/files", disabled: false, create: true, owner: "vagrant", group: "vagrant"
        c73.vm.provision "shell", inline: $my_install_c73, privileged: false
    end
end


