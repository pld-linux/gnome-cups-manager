Summary:	GNOME manager for CUPS printers
Name:		gnome-cups-manager
Version:	0.16
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.16/%{name}-%{version}.tar.bz2
# Source0-md5:	745bcd136ba9e13433303462e9ad6a1e
URL:		http://www.gnome.org
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	libgnomecups-devel >= 0.1.4
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libgnomeprint-devel
BuildRequires:	libbonobo-devel >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME manager for CUPS printers.

%package devel
Summary:	Devel files for gnome-cups-manager (libgnomecupsui)
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Devel files for gnome-cups-manager (libgnomecupsui).

%package static
Summary:	gnome-cups-manager (libgnomecupsui) static library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
gnome-cups-manager (libgnomecupsui) static library.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/gnome-cups-add
%attr(755,root,root) %{_bindir}/gnome-cups-manager
%attr(755,root,root) %{_sbindir}/gnome-cups-switch
%attr(755,root,root) %{_libdir}/libgnomecupsui*.so.*.*.*
%{_libdir}/bonobo/servers/Gnome_CupsManager.server
%{_datadir}/%{name}
%{_datadir}/icons/gnome/48x48/devices/*.png
%{_datadir}/icons/gnome/48x48/emblems/*.png
%{_pixmapsdir}/%{name}

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%defattr(644,root,root,755)
%{_libdir}/libgnomecupsui*.la
%{_libdir}/libgnomecupsui*.so
%{_includedir}/libgnomecups-1/libgnomecups/*.h
%{_pkgconfigdir}/libgnomecupsui*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnomecupsui*.a
