#!/bin/sh

INAME=f20-xfce-dev
OS=Fedora_64
IDIR=/var/tmp/images
CFG=${IDIR}/${INAME}.ks
IMAGE=${IDIR}/${INAME}.vdi
ORIGKS=fedora-cloud-base.ks
CACHE=/var/cache/appcreator
set -e

# ensure this dependency is already installed
sudo yum install -y appliance-tools

mkdir -p ${IDIR}
cd ${IDIR}
wget https://git.fedorahosted.org/cgit/spin-kickstarts.git/plain/${ORIGKS}

cat > ks-patch.txt <<EOF
--- fedora-cloud-base.ks.orig	2014-06-03 17:37:19.288689158 +0200
+++ fedora-cloud-base.ks	2014-06-03 17:44:29.371312386 +0200
@@ -1,3 +1,6 @@
+#
+# https://git.fedorahosted.org/cgit/spin-kickstarts.git/plain/fedora-cloud-base.ks
+#
 # This is a basic Fedora 21 spin designed to work in OpenStack and other
 # private cloud environments. It's configured with cloud-init so it will
 # take advantage of ec2-compatible metadata services for provisioning ssh
@@ -30,22 +33,34 @@
 
 zerombr
 clearpart --all
-part / --size 3000 --fstype ext4
-
-%include fedora-repo.ks
+part / --size 25000 --fstype ext4
 
+#%include fedora-repo.ks
+repo --name=fedora --mirrorlist=http://mirrors.fedoraproject.org/mirrorlist?repo=fedora-20&arch=x86_64
+repo --name=updates --mirrorlist=http://mirrors.fedoraproject.org/mirrorlist?repo=updates-released-f20&arch=x86_64
+repo --name=rpmfusion-free --baseurl=http://download1.rpmfusion.org/free/fedora/releases/20/Everything/x86_64/os/
+repo --name=rpmfusion-free-updates --baseurl=http://download1.rpmfusion.org/free/fedora/updates/20/x86_64
 
 reboot
 
 # Package list.
 %packages
-kernel-core
 @core
 grubby
+kernel
+@base-x
+@fonts
+@xfce-desktop
+@critical-path-xfce
+shadow-utils
+passwd
+sudo
+vim
+VirtualBox-guest
 
 # cloud-init does magical things with EC2 metadata, including provisioning
 # a user account with ssh keys.
-cloud-init
+# cloud-init
 
 # this is used by openstack's cloud orchestration framework (and it's small)
 heat-cfntools
@@ -57,6 +72,8 @@
 # We need this image to be portable; also, rescue mode isn't useful here.
 dracut-config-generic
 -dracut-config-rescue
+dracut-nohostonly
+dracut-norescue
 
 syslinux-extlinux 
 
@@ -116,9 +133,9 @@
 sed -i 's/^timeout 10/timeout 1/' /boot/extlinux/extlinux.conf
 
 # setup systemd to boot to the right runlevel
-echo -n "Setting default runlevel to multiuser text mode"
+echo -n "Setting default runlevel to multiuser window system mode"
 rm -f /etc/systemd/system/default.target
-ln -s /lib/systemd/system/multi-user.target /etc/systemd/system/default.target
+ln -s /lib/systemd/system/runlevel5.target /etc/systemd/system/default.target
 echo .
 
 # If you want to remove rsyslog and just use journald, remove this!
@@ -183,6 +200,14 @@
 echo "Disabling tmpfs for /tmp."
 systemctl mask tmp.mount
 
+echo -n "Installing rpmfusion-free repo"
+rpm -ivh http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-20.noarch.rpm
+echo .
+
+echo -n "Adding fedora user"
+/sbin/useradd fedora && echo reverse | /bin/passwd fedora --stdin
+echo .
+
 # make sure firstboot doesn't start
 echo "RUN_FIRSTBOOT=NO" > /etc/sysconfig/firstboot
 
@@ -223,11 +248,23 @@
 /usr/sbin/fixfiles -R -a restore
 chattr +i /boot/extlinux/ldlinux.sys
 
-echo "Zeroing out empty space."
-# This forces the filesystem to reclaim space from deleted files
-dd bs=1M if=/dev/zero of=/var/tmp/zeros || :
-rm -f /var/tmp/zeros
-echo "(Don't worry -- that out-of-space error was expected.)"
+if [ ! -e /etc/sysconfig/kernel ]; then
+echo "Creating /etc/sysconfig/kernel."
+cat <<EOF > /etc/sysconfig/kernel
+# UPDATEDEFAULT specifies if new-kernel-pkg should make
+# new kernels the default
+UPDATEDEFAULT=yes
+
+# DEFAULTKERNEL specifies the default kernel package type
+DEFAULTKERNEL=kernel
+EOF
+fi
+
+echo "Adding fedora user to sudoers"
+echo "fedora   ALL=(ALL)       ALL" >> /etc/sudoers
+
+echo "Zeroing out empty space with fstrim"
+/usr/sbin/fstrim /
 
 %end
 
EOF

patch < ks-patch.txt

#ensure that patch created the file we expect
test -f ${ORIGKS}
mv -f ${ORIGKS} ${CFG}

sudo appliance-creator -d -v -t ${IDIR} --config ${CFG} --cache=${CACHE} -o ${IDIR} --name ${INAME} --vmem 512 --vcpu 1 --format raw

sudo chown -R `sudo who am i | cut -d' ' -f1` ${IDIR}

xz -d -c ${IDIR}/${INAME}/${INAME}-sda.raw.xz > ${IDIR}/${INAME}/${INAME}-sda.raw
VBoxManage convertdd ${IDIR}/${INAME}/${INAME}-sda.raw ${IMAGE} --format VDI
VBoxManage createvm --name ${INAME} --ostype ${OS} --register --basefolder /var/tmp/images
VBoxManage modifyvm        ${INAME} --memory 1800 --vram 32 --rtcuseutc on --largepages on
VBoxManage storagectl      ${INAME} --name "scsi-ctrl" --add scsi
VBoxManage storageattach   ${INAME} --storagectl "scsi-ctrl" --port 0 --device 0 --type hdd --medium ${IMAGE}
VBoxManage storagectl      ${INAME} --name "ide-ctrl" --add ide
VBoxManage modifyvm        ${INAME} --boot1 dvd --boot2 disk --boot3 none --boot4 none
VBoxManage modifyvm        ${INAME} --natpf1 "guestssh,tcp,,2222,,22"
# VBoxManage export ${INAME} --manifest -o ${IDIR}/${INAME}.ova
# VirtualBox --startvm ${INAME}
