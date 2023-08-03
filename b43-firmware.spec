Name:		b43-firmware
Version:	6.30.163.46
Release:	12%{?dist}
Summary:	Firmware for Broadcom wireless devices
License:	Redistributable, no modification permitted
URL:		http://linuxwireless.sipsolutions.net/en/users/Drivers/b43/#devicefirmware
Source0: 	http://www.lwfinger.com/b43-firmware/broadcom-wl-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	b43-fwcutter


%description
This package contains the V4 firmware required to use the b43 driver
with most wireless cores from Broadcom.

%prep
%setup -q -c

%build
b43-fwcutter broadcom-wl-%{version}.wl_apsta.o

%install
mkdir -p %{buildroot}/lib/firmware/b43
%{__install} -m 644 b43/* %{buildroot}/lib/firmware/b43

%files
%dir /lib/firmware/b43
/lib/firmware/b43/*

%changelog
* Thu Aug 03 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 6.30.163.46-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 6.30.163.46-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Thu Feb 10 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 6.30.163.46-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 6.30.163.46-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 6.30.163.46-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 6.30.163.46-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 6.30.163.46-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 6.30.163.46-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 6.30.163.46-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 6.30.163.46-3
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 6.30.163.46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 16 2018 Nicolas Chauvet <kwizart@gmail.com> - 6.30.163.46-1
- Update to 6.30.163.46

* Mon May 19 2008 kwizart < kwizart at gmail.com > - 351.126-4
- Add patch from Ville Skyttä to repack the needed files.

* Wed Nov 14 2007 John W. Linville <linville@redhat.com> 351.126-3
- remove clarification from COPYING text

* Thu Aug 30 2007 John W. Linville <linville@redhat.com> 351.126-2
- clarify COPYING text

* Mon Aug 27 2007 John W. Linville <linville@redhat.com> 351.126-1
- Initial RPM release.
