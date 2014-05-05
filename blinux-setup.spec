#-
# Copyright 2013-2014 Emmanuel Vadot <elbarto@bocal.org>
# All rights reserved
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted providing that the following conditions 
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

Name:		blinux-setup
Version:	2.1
Release:	0
License:        BSD-2-Clause
Summary:	Blinux setup
Requires(post):	systemd
Requires(preun):	systemd
BuildArch:      noarch
Source0:        %{name}-%{version}.tgz
Vendor:		Bocal
Url:            http://www.bocal.org
Group:          System Environment/Daemons
Packager:       Emmanuel Vadot <elbarto@bocal.org>
Requires:	python-gtk, setxkbmap

%description
bocal-setup script opensuse bocal

%prep
%setup

%build

%install
rm -fr %{buildroot}
mkdir -p %{buildroot}/%{_sbindir}
mkdir -p %{buildroot}/usr/lib/systemd/system
cp %{name} %{buildroot}/%{_sbindir}
cp %{name}_step1 %{buildroot}/%{_sbindir}
cp %{name}.service %{buildroot}/usr/lib/systemd/system;

%post
/usr/bin/systemctl enable blinux-setup.service
mkdir /var/lib/blinux-setup/
touch /var/lib/blinux-setup/runme

%postun
case "$*" in
  0)  
  /usr/bin/systemctl disable blinux-update.service
  ;;
  esac

%files
%attr(755,root,root) %{_sbindir}/%{name}
%attr(755,root,root) %{_sbindir}/%{name}_step1
%attr(644,root,root) /usr/lib/systemd/system/%{name}.service

%changelog
* Sun May 04 2014 Emmanuel Vadot <elbarto@bocal.org> - 2.1-0
- Bump to version 2.1

* Sat May 03 2014 Emmanuel Vadot <elbarto@bocal.org> - 2.0-0
- Bump to version 2.0

* Sun Mar 02 2014 Emmanuel Vadot <elbarto@bocal.org> - 1.1-0
- Bump to version 1.1

* Sun Mar 02 2014 Emmanuel Vadot <elbarto@bocal.org> - 1.0-0
- Package creation
