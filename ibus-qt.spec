Summary:	Qt IBus library and Qt input method plugin
Summary(pl.UTF-8):	Biblioteka Qt IBus oraz wtyczka metody wprowadzania znaków dla Qt
Name:		ibus-qt
Version:	1.3.3
Release:	10
License:	GPL v2+
Group:		Libraries
#Source0Download: https://github.com/ibus/ibus-qt/releases
Source0:	https://github.com/ibus/ibus-qt/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	b8f441379b34bd6fca79b63a9e1c7ff5
URL:		https://github.com/ibus/ibus-qt
BuildRequires:	QtCore-devel >= 4.5
BuildRequires:	QtDBus-devel >= 4.5
BuildRequires:	QtGui-devel >= 4.5
BuildRequires:	QtXml-devel >= 4.5
BuildRequires:	cmake >= 2.4
BuildRequires:	dbus-devel >= 1.2
BuildRequires:	doxygen >= 1.6
BuildRequires:	ibus-devel >= 1.3.9
BuildRequires:	libicu-devel >= 4.0
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= 4.5
BuildRequires:	rpmbuild(macros) >= 1.603
BuildRequires:	xorg-lib-libX11-devel
Requires:	ibus-libs >= 1.3.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qt IBus library and Qt input method plugin.

%description -l pl.UTF-8
Biblioteka Qt IBus oraz wtyczka metody wprowadzania znaków dla Qt.

%package devel
Summary:	Development files for IBus Qt library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki IBus Qt
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtCore-devel >= 4.5
Requires:	QtDBus-devel >= 4.5
Requires:	QtXml-devel >= 4.5

%description devel
The ibus-qt-devel package contains the header files for IBus Qt
library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe dla biblioteki IBus Qt.

%prep
%setup -q

%build
%cmake \
	-DLIBDIR=%{_libdir}

%{__make}

%{__make} docs

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_libdir}/libibus-qt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libibus-qt.so.1
%attr(755,root,root) %{_libdir}/qt4/plugins/inputmethods/libqtim-ibus.so

%files devel
%defattr(644,root,root,755)
%doc docs/html/*
%attr(755,root,root) %{_libdir}/libibus-qt.so
%{_includedir}/ibus-qt
