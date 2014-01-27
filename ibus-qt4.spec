%define major 1
%define libname %mklibname ibus-qt %{major}
%define devname %mklibname ibus-qt -d

Summary:	ibus qt4 input method plugin
Name:		ibus-qt4
Version:	1.3.2
Release:	1
License:	GPLv2+
Group:		System/Internationalization
Url:		http://code.google.com/p/ibus/
Source0:	http://ibus.googlecode.com/files/ibus-qt-%{version}-Source.tar.gz
BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	icu-devel
BuildRequires:	qt4-devel >= 4.4
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(ibus-1.0)
Requires:	ibus >= 1.3.0

%description
IBus is a next generation input framework. This package contains qt4 input
method plugin.

%files
%doc AUTHORS README
%{qt4plugins}/inputmethods/libqtim-ibus.so

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared library for ibus-qt
Group:		System/Libraries
Conflicts:	%{name} < 1.3.2

%description -n %{libname}
Shared library for ibus-qt.

%files -n %{libname}
%{_libdir}/libibus-qt.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for ibus-qt
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Conflicts:	%{name}-devel < 1.3.2
Obsoletes:	%{name}-devel < 1.3.2
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This package contains development files for ibus-qt.

%files -n %{devname}
%{_includedir}/ibus-qt
%{_libdir}/*.so

#----------------------------------------------------------------------------

%prep
%setup -q -n ibus-qt-%{version}-Source

%build
%cmake_qt4 -DLIBDIR="%{_libdir}"
%make

%install
%makeinstall_std -C build

rm -fr %{buildroot}%{_datadir}/doc

