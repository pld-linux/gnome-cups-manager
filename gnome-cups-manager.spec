Summary:	GNOME manager for CUPS printers
Summary(pl):	Zarz±dca drukarek CUPS dla GNOME
Name:		gnome-cups-manager
Version:	0.17
Release:	4
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.17/%{name}-%{version}.tar.bz2
# Source0-md5:	1aa72f8318a7ccb795cdfd2676d6346c
Source1:	%{name}-cc.desktop
URL:		http://www.gnome.org/
Requires:	gnome-icon-theme
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libbonobo-devel >= 2.0.0
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libgnomecups-devel >= 0.1.5
BuildRequires:	libgnomeprint-devel
BuildRequires:	libgnomeui-devel >= 2.3.3.1-2
BuildRequires:	libstdc++-devel
Obsoletes:	gnome-cups-manager-cc-applet <= 0.17-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME manager for CUPS printers.

%description -l pl
Zarz±dca drukarek CUPS dla GNOME.

%package devel
Summary:	Devel files for gnome-cups-manager (libgnomecupsui)
Summary(pl):	Pliki nag³ówkowe dla gnome-cups-manager (libgnomecupsui)
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	libgnomecups-devel >= 0.1.4

%description devel
Devel files for gnome-cups-manager (libgnomecupsui).

%description devel -l pl
Pliki nag³ówkowe dla gnome-cups-manager (libgnomecupsui).

%package static
Summary:	gnome-cups-manager (libgnomecupsui) static library
Summary(pl):	Statyczna biblioteka gnome-cups-manager (libgnomecupsui)
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
gnome-cups-manager (libgnomecupsui) static library.

%description static -l pl
Statyczna biblioteka gnome-cups-manager (libgnomecupsui).

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/gnome/capplets

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -c %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/gnome/capplets

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/gnome-cups-add
%attr(755,root,root) %{_bindir}/gnome-cups-icon
%attr(755,root,root) %{_bindir}/gnome-cups-manager
%attr(755,root,root) %{_sbindir}/gnome-cups-switch
%attr(755,root,root) %{_libdir}/libgnomecupsui*.so.*.*.*
%{_libdir}/bonobo/servers/Gnome_CupsManager.server
%{_datadir}/%{name}
%{_datadir}/icons/gnome/48x48/devices/*.png
%{_datadir}/icons/gnome/48x48/emblems/*.png
%{_pixmapsdir}/%{name}
%{_datadir}/gnome/capplets/*.desktop

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/libgnomecupsui*.so
%{_libdir}/libgnomecupsui*.la
%{_includedir}/libgnomecups-1/libgnomecups/*.h
%{_pkgconfigdir}/libgnomecupsui*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnomecupsui*.a
