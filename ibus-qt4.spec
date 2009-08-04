%define	version 1.2.0.20090728
%define	release %mkrel 2

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
BuildRequires:	cmake
Requires:	ibus >= 1.2.0

%description
IBus is a next generation input framework.
This package contains qt4 input method plugin.

%prep
%setup -q -n ibus-qt-%{version}-Source

%build
%cmake_qt4 -DLIBDIR="%_libdir"
%make

%install
rm -rf %buildroot
%makeinstall_std -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_libdir}/libibus-qt.so
%{qt4plugins}/inputmethods/libqtim-ibus.so
