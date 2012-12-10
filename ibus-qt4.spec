%define	version 1.3.1
%define	release %mkrel 6

Name:      ibus-qt4
Summary:   ibus qt4 input method plugin
Version:   %{version}
Release:   %{release}
Group:     System/Internationalization
License:   GPLv2+
URL:       http://code.google.com/p/ibus/
Source0:   http://ibus.googlecode.com/files/ibus-qt-%{version}-Source.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	qt4-devel >= 4.4
BuildRequires:	dbus-devel
BuildRequires:	cmake
BuildRequires:	icu-devel
BuildRequires:	ibus-devel >= 1.3.0
BuildRequires:	doxygen
Requires:	ibus >= 1.3.0

%description
IBus is a next generation input framework.
This package contains qt4 input method plugin.

%package devel
Group: System/Internationalization
Summary: Development files for ibus-qt
Requires: %name = %version

%description devel
This package contains development files for ibus-qt.

%prep
%setup -q -n ibus-qt-%{version}-Source

%build
%cmake_qt4 -DLIBDIR="%_libdir"
%make

%install
rm -rf %buildroot
%makeinstall_std -C build

rm -fr %buildroot%_datadir/doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS README
%{_libdir}/libibus-qt.so.*
%{qt4plugins}/inputmethods/libqtim-ibus.so

%files devel
%defattr(-,root,root)
%{_includedir}/ibus-qt
%{_libdir}/*.so


%changelog
* Sun Jun 05 2011 Funda Wang <fwang@mandriva.org> 1.3.1-4mdv2011.0
+ Revision: 682809
- rebuild for new icu

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.1-3
+ Revision: 665493
- mass rebuild

* Mon Mar 14 2011 Funda Wang <fwang@mandriva.org> 1.3.1-2
+ Revision: 644572
- rebuild for new icu

* Sun Feb 06 2011 Funda Wang <fwang@mandriva.org> 1.3.1-1
+ Revision: 636395
- new version 1.3.1

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-2mdv2011.0
+ Revision: 611137
- rebuild

* Mon Apr 26 2010 Funda Wang <fwang@mandriva.org> 1.3.0-1mdv2010.1
+ Revision: 538860
- new version 1.3.0

* Sun Mar 21 2010 Funda Wang <fwang@mandriva.org> 1.2.0.20091216-2mdv2010.1
+ Revision: 526140
- rebuild for new icu

* Thu Dec 17 2009 Funda Wang <fwang@mandriva.org> 1.2.0.20091216-1mdv2010.1
+ Revision: 479641
- add devel package
- new version 1.2.0.20091216

* Sun Dec 06 2009 Funda Wang <fwang@mandriva.org> 1.2.0.20091206-1mdv2010.1
+ Revision: 474123
- new version 1.2.0.20091206

* Fri Nov 06 2009 Funda Wang <fwang@mandriva.org> 1.2.0.20091014-1mdv2010.1
+ Revision: 460620
- add back libdir
- fix build
- New version 1.2.0.20091014

* Fri Aug 07 2009 Funda Wang <fwang@mandriva.org> 1.2.0.20090728-3mdv2010.0
+ Revision: 411097
- fix file list
- refresh tarball

* Tue Aug 04 2009 Funda Wang <fwang@mandriva.org> 1.2.0.20090728-2mdv2010.0
+ Revision: 408930
- BR dbus
- import ibus-qt4

