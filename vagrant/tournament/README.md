## Tournament Planner PROJECT

## TABLE OF CONTENTS
- [SETUP](#setup)
- [CONTENT](#content)
- [CREATOR](#creator)

## SETUP
- Install [Vagrant](http://vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/)
- Clone the [fullstack-nanodegree-vm repository](https://github.com/wacevedo/fullstack-nanodegree-vm)
- Launch the Vagrant VM (Inside of tournament folder execute the following command $ vagrant up)
- Connect via ssh to the VM (Executing $vagrant ssh)
- Go to tournament folder (cd /vagrant/tournament)
- Run these commands for create initial structure
```
vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ psql
vagrant=> \i tournament.sql
vagrant=> \q
```
- Run the test file `$ python tournament_test.py`

## CONTENT

```
tournament /
|---- README.md
|---- tournament.py
|---- tournament.sql
|---- tournament_test.py
```

## CREATOR

Willson Acevedo
- ![https://www.instagram.com/wilson_acevedo/](https://s3.amazonaws.com/uploads.hipchat.com/603024/4563693/Y3vrs0sC0ZjfVAD/Instagram%20Old-64.png) https://www.instagram.com/wilson_acevedo/
- ![https://www.facebook.com/wilson.acevedosanchez.1](https://s3.amazonaws.com/uploads.hipchat.com/603024/4563693/P82Ho1dhtJgAofV/Facebook-64_thumb.png) https://www.facebook.com/wilson.acevedosanchez.1
- ![https://twitter.com/wilson_acevedo](https://s3.amazonaws.com/uploads.hipchat.com/603024/4563693/IVw4JUBUqdrhOwk/Twitter-64_thumb.png) https://twitter.com/wilson_acevedo