Summary:	System for layout and rendering of internationalized text - X11 backend
Name:		pangox-compat
Version:	0.0.2
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pangox-compat/0.0/%{name}-%{version}.tar.xz
# Source0-md5:	7bcbd0187f03e1e27af9a81e07249c33
URL:		http://www.pango.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	libtool
BuildRequires:	pango-devel
BuildRequires:	pkg-config
BuildRequires:	xorg-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a compatibility library providing the obsolete pangox library
that is not shipped by Pango itself anymore.

%package devel
Summary:	Development files for pangox library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for pangox library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libpangox-1.0.so.0
%attr(755,root,root) %{_libdir}/libpangox-1.0.so.*.*.*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pango/pangox.aliases

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpangox-1.0.so
%{_libdir}/libpangox-1.0.la
%{_pkgconfigdir}/pangox.pc
%{_includedir}/pango-1.0/pango/pangox.h

