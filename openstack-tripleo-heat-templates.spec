Name:		openstack-tripleo-heat-templates
Summary:	Heat templates for TripleO
Version:    XXX
Release:    XXX{?dist}
License:	ASL 2.0
Group:		System Environment/Base
URL:		https://wiki.openstack.org/wiki/TripleO
Source0:	http://tarballs.openstack.org/tripleo-heat-templates/tripleo-heat-templates-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python2-devel
BuildRequires:	python-setuptools
BuildRequires:	python-d2to1
BuildRequires:	python-pbr

Requires:	PyYAML

%description
OpenStack TripleO Heat Templates is a collection of templates and tools for
building Heat Templates to do deployments of OpenStack.

%prep
%setup -q -n tripleo-heat-templates-%{upstream_version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root=%{buildroot}
install -d -m 755 %{buildroot}/%{_datadir}/%{name}
cp -ar *.yaml %{buildroot}/%{_datadir}/%{name}
cp -ar puppet %{buildroot}/%{_datadir}/%{name}
cp -ar firstboot %{buildroot}/%{_datadir}/%{name}
cp -ar extraconfig %{buildroot}/%{_datadir}/%{name}
cp -ar environments %{buildroot}/%{_datadir}/%{name}
cp -ar network %{buildroot}/%{_datadir}/%{name}

%files
%doc README.md LICENSE examples
%{python2_sitelib}/tripleo_heat_merge
%{python2_sitelib}/tripleo_heat_templates-*.egg-info
%{_datadir}/%{name}
%{_bindir}/tripleo-heat-merge

%changelog
* Mon Oct 20 2014 James Slagle <jslagle@redhat.com> 0.7.9-5
- Update patches

* Mon Oct 20 2014 James Slagle <jslagle@redhat.com> 0.7.9-4
- Update patches

* Wed Oct 15 2014 James Slagle <jslagle@redhat.com> 0.7.9-3
- Adding SNMP related parameters to storage templates
- Add converted version of block and object storage
- Compute and controller templates without merge.py

* Wed Oct 15 2014 James Slagle <jslagle@redhat.com> 0.7.9-2


* Wed Oct 15 2014 James Slagle <jslagle@redhat.com> 0.7.9-1
- Update to upstream 0.7.9

* Tue Oct 07 2014 James Slagle <jslagle@redhat.com> 0.7.7-3
- Adding SNMP related parameters to storage templates

* Mon Oct 06 2014 James Slagle <jslagle@redhat.com> 0.7.7-2
- Add converted version of block and object storage
- Compute and controller templates without merge.py

* Mon Sep 29 2014 James Slagle <jslagle@redhat.com> 0.7.7-1
- Update to upstream 0.7.7

* Mon Sep 15 2014 James Slagle <jslagle@redhat.com> 0.7.6-1
- Update to upstream 0.7.6

* Thu Jun 26 2014 James Slagle <jslagle@redhat.com> - 0.4.4-3
- Remove patch that swiched to qpid, we are back to rabbit

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 14 2014 James Slagle <jslagle@redhat.com> - 0.4.4-1
- Bump to 0.4.4 and update patches

* Thu Apr 10 2014 James Slagle <jslagle@redhat.com> - 0.4.2-5
- Add patch to use IP address for MySQL connection

* Thu Mar 27 2014 James Slagle <jslagle@redhat.com> - 0.4.2-4
- Update patch 0001-Add-BlockStorageConfig0.patch to include NeutronNetworkType
  parameter.

* Wed Mar 26 2014 James Slagle <jslagle@redhat.com> - 0.4.2-3
- Update patches

* Tue Mar 25 2014 James Slagle <jslagle@redhat.com> - 0.4.2-2
- Add patch 0003-Expose-dnsmasq-options.patch

* Mon Mar 24 2014 James Slagle <jslagle@redhat.com> - 0.4.2-1
- Bump to 0.4.2.

* Fri Mar 21 2014 James Slagle <jslagle@redhat.com> - 0.4.1-1
- Rebase onto 0.4.1.
- Add patch to switch from rabbit to qpid as default message bus

* Wed Mar 12 2014 James Slagle <jslagle@redhat.com> - 0.4.0-2
- Remove python BuildRequires
- Switch __python to __python2 macro
- Switch python_sitelib to python2_sitelib macro
- Use doc macro for README.md, LICENSE, and examples
- Use name macro when copying templates in install

* Mon Feb 17 2014 James Slagle <jslagle@redhat.com> - 0.4.0-1
- Update spec file for Fedora Packaging 

* Thu Sep 19 2013 Ben Nemec <bnemec@redhat.com> - 0.0.1-1
- First build of tripleo-heat-templates
