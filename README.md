# zesar-vagrant

This is for testing zesar in conjunction with libvirt and vagrant

## Prequisites

You need the following

* storage pool vagrant
* vagrant and libvirt running
* change Vagrantfile and add static ip address for

`vm.vm.network  :private_network, :ip => "192.168.192.52",..`

* fire `vagrant up`
* fire `vagrant status`
* run the start script for unicorn in `/home/vagrant/run.sh`


## get the base box

* xenial unbuntu 16

- `vagrant box add https://atlas.hashicorp.com/ubuntu/xenial64`
- `vagrant mutate ubuntu/xenial64 libvirt`

---

