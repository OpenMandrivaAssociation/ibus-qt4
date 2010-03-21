%define	version 1.2.0.20091216
%define	release %mkrel 2

Name:      ibus-qt4
Summary:   ibus qt4 input method plugin
Version:   %{version}
Release:   %{release}
Group:     System/Internationalization
License:   GPLv2+
URL:       http://code.google.com/p/ibus/
Source0:   http://ibus.googlecode.com/files/ibus-qt-%{version}-Source.tar.gz
Patch0:    ibus-qt-1.2.0.20091014-link.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	qt4-devel >= 4.4
BuildRequires:	dbus-devel
BuildRequires:	cmake
BuildRequires:	icu-devel
BuildRequires:	ibus-devel >= 1.2.0
BuildRequires:	doxygen
Requires:	ibus >= 1.2.0

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
%patch0 -p0

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
%doc build/docs/html/*
%{_mandir}/man3/*
%{_includedir}/ibus-qt
%{_libdir}/*.so
