#-
# Copyright 2013-2015 Emmanuel Vadot <elbarto@bocal.org>
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
Version:	3.0
Release:	4
License:        BSD-2-Clause
Summary:	Blinux setup

BuildRequires:	systemd
Requires(post):	systemd
Requires(preun):	systemd
Requires:	python-gtk, setxkbmap
BuildArch:      noarch

Source0:        blinux-setup
Source1:	blinux-setup_step1
Source2:	blinux-setup.service
Source3:	blinux

Vendor:		Blinux
Url:            http://www.bocal.org
Group:          System Environment/Daemons
Packager:       Emmanuel Vadot <elbarto@bocal.org>


%description
bocal-setup script opensuse bocal

%prep

%build

%install
rm -fr %{buildroot}
mkdir -p %{buildroot}/%{_sbindir}
mkdir -p %{buildroot}/usr/lib/systemd/system
mkdir -p %{buildroot}/usr/lib/X11/displaymanagers/
install -D -p -m 755 %{SOURCE0} %{buildroot}/%{_sbindir}
install -D -p -m 755 %{SOURCE1} %{buildroot}/%{_sbindir}
install -D -p -m 644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system
install -D -p -m 755 %{SOURCE2} %{buildroot}/usr/lib/X11/displaymanagers/

%files
%attr(755,root,root) %{_sbindir}/%{name}
%attr(755,root,root) %{_sbindir}/%{name}_step1
%attr(644,root,root) /usr/lib/systemd/system/%{name}.service
%attr(755,root,root) /usr/lib/X11/displaymanagers/blinux

%changelog
* Fri Oct 02 2015 Emmanuel Vadot <elbarto@bocal.org> - 3.0-4
- Install displaymanager file

* Mon Dec 29 2014 Emmanuel Vadot <elbarto@bocal.org> - 2.1-2
- Handle upgrade

* Sun May 04 2014 Emmanuel Vadot <elbarto@bocal.org> - 2.1-0
- Bump to version 2.1

* Sat May 03 2014 Emmanuel Vadot <elbarto@bocal.org> - 2.0-0
- Bump to version 2.0

* Sun Mar 02 2014 Emmanuel Vadot <elbarto@bocal.org> - 1.1-0
- Bump to version 1.1

* Sun Mar 02 2014 Emmanuel Vadot <elbarto@bocal.org> - 1.0-0
- Package creation
