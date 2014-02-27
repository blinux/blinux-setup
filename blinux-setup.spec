Name:		blinux-setup
Version:	1.0
Release:	1
License:        BSD-2-Clause
Summary:	Blinux setup
BuildRequires:	systemd
BuildArch:      noarch
Vendor:		Bocal
Url:            http://www.bocal.org
Group:          Basic

%description
bocal-setup script opensuse bocal

%prep

%build

%install
rm -fr %{buildroot};
mkdir -p %{buildroot}/usr/sbin;
mkdir -p %{buildroot}/usr/lib/systemd/system;
cd %{_sourcedir}
mv blinux-setup %{buildroot}/usr/sbin;
mv blinux-setup.service %{buildroot}/usr/lib/systemd/system;

%post
/usr/bin/systemctl enable blinux-setup.service

%postrun
/usr/bin/systemctl enable blinux-setup.service

%files
%attr(755,root,root) /usr/sbin/blinux-setup
%attr(644,root,root) /usr/lib/systemd/system/blinux-setup.service
