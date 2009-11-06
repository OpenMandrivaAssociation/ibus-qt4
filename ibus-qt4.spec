%define	version 1.2.0.20091014
%define	release %mkrel 1

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
Requires:	ibus >= 1.2.0

%description
IBus is a next generation input framework.
This package contains qt4 input method plugin.

%prep
%setup -q -n ibus-qt-%{version}-Source
%patch0 -p0

%build
%cmake_qt4 -DLIBDIR="%_libdir"
%make

%install
rm -rf %buildroot
%makeinstall_std -C build

rm -fr %buildroot%_libdir/libibus-qt.so
rm -fr %buildroot%_datadir/doc
rm -fr %buildroot%_includedir/ibus-qt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS README
%{_libdir}/libibus-qt.so.*
%{qt4plugins}/inputmethods/libqtim-ibus.so
