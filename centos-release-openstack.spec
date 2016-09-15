%global OpenStackVersion mitaka
Summary: OpenStack from the CentOS Cloud SIG repo configs
Name: centos-release-openstack-%{OpenStackVersion}
Version: 1
Release: 5%{?dist}
License: GPL
URL: http://wiki.centos.org/SpecialInterestGroup/Cloud
Source0: CentOS-OpenStack.repo
Source1: RPM-GPG-KEY-CentOS-SIG-Cloud

BuildArch: noarch

Requires: centos-release
Requires: centos-release-ceph-hammer
Requires: centos-release-qemu-ev
Conflicts: centos-release-openstack

%description
yum Configs and basic docs for OpenStack as delivered via the CentOS Cloud SIG.

%prep

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-OpenStack-%{OpenStackVersion}.repo
sed -i -e "s/OPENSTACK_VERSION/%{OpenStackVersion}/g" %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-OpenStack-%{OpenStackVersion}.repo
install -p -d %{buildroot}%{_sysconfdir}/pki/rpm-gpg
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pki/rpm-gpg

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/yum.repos.d/*
%{_sysconfdir}/pki/rpm-gpg

%changelog
* Thu Sep 15 2016 Alan Pevec <apevec AT redhat.com> %{OpenStackVersion}-1-5
- Distribute only RDO Trunk tested repository
- Pin Ceph Hammer for Mitaka

* Fri Apr 22 2016 Alan Pevec <apevec AT redhat.com> %{OpenStackVersion}-1-3
- Add Trunk repositories

* Mon Apr 04 2016 Alan Pevec <apevec AT redhat.com> %{OpenStackVersion}-1-2
- %{OpenStackVersion} release
