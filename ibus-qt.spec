Summary:	Qt IBus library and Qt input method plugin
Name:		ibus-qt
Version:	1.3.1
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://ibus.googlecode.com/files/%{name}-%{version}-Source.tar.gz
# Source0-md5:	769e8872ca8a59327b2073ce2f142589
Patch0:		%{name}-HEAD.patch
URL:		http://code.google.com/p/ibus/
BuildRequires:	cmake
BuildRequires:	dbus-devel >= 1.2
BuildRequires:	doxygen >= 1.6
BuildRequires:	ibus-devel >= 1.3.9
BuildRequires:	libicu-devel >= 4.0
BuildRequires:	qt4-build >= 4.5
Requires:	ibus >= 1.3.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qt IBus library and Qt input method plugin.

%package devel
Summary:	Development tools for ibus qt
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The ibus-qt-devel package contains the header files for ibus qt
library.

%prep
%setup -q -n %{name}-%{version}-Source
%patch0 -p1

%build
%cmake -DLIBDIR=%{_libdir}

%{__make} \
	VERBOSE=1

%{__make} docs \
	VERBOSE=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_libdir}/libibus-qt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libibus-qt.so.[0-9]
%attr(755,root,root) %{_libdir}/qt4/plugins/inputmethods/libqtim-ibus.so

%files devel
%defattr(644,root,root,755)
%doc docs/html/*
%{_includedir}/*
%attr(755,root,root) %{_libdir}/libibus-qt.so
