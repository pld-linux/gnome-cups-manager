Summary:	GNOME manager for CUPS printers
Summary(pl.UTF-8):	Zarządca drukarek CUPS dla GNOME
Name:		gnome-cups-manager
Version:	0.31
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-cups-manager/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	4144b2cf05e381e89fed066793e3b249
Source1:	%{name}-cc.desktop
Patch0:		%{name}-version.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gnome-keyring-devel
BuildRequires:	gtk+2-devel >= 2:2.6.3
BuildRequires:	intltool >= 0.20
BuildRequires:	libbonobo-devel >= 2.0.0
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libgnomecups-devel >= 0.2.0
BuildRequires:	libgnomeprint-devel >= 2.10.0
BuildRequires:	libgnomeui-devel >= 2.10.0-2
BuildRequires:	libsmbclient-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	cups-devel >= 1.1.23
Requires:	gnome-icon-theme
Requires:	gnomesu >= 0.3
Obsoletes:	gnome-cups-manager-cc-applet <= 0.17-3
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME manager for CUPS printers.

%description -l pl.UTF-8
Zarządca drukarek CUPS dla GNOME.

%package devel
Summary:	Devel files for gnome-cups-manager (libgnomecupsui)
Summary(pl.UTF-8):	Pliki nagłówkowe dla gnome-cups-manager (libgnomecupsui)
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.6.3
Requires:	libgnomecups-devel >= 0.1.14

%description devel
Devel files for gnome-cups-manager (libgnomecupsui).

%description devel -l pl.UTF-8
Pliki nagłówkowe dla gnome-cups-manager (libgnomecupsui).

%package static
Summary:	gnome-cups-manager (libgnomecupsui) static library
Summary(pl.UTF-8):	Statyczna biblioteka gnome-cups-manager (libgnomecupsui)
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
gnome-cups-manager (libgnomecupsui) static library.

%description static -l pl.UTF-8
Statyczna biblioteka gnome-cups-manager (libgnomecupsui).

%prep
%setup -q
%patch0 -p0

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no
[ -d $RPM_BUILD_ROOT%{_datadir}/locale/sr@latin ] || \
	mv -f $RPM_BUILD_ROOT%{_datadir}/locale/sr@{Latn,latin}
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
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/48x48/devices/*.png
%{_iconsdir}/hicolor/48x48/stock/data/*.png
%{_libdir}/bonobo/servers/Gnome_CupsManager.server
%{_pixmapsdir}/%{name}

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/libgnomecupsui*.so
%{_includedir}/libgnomecups-1/libgnomecups/*.h
%{_libdir}/libgnomecupsui*.la
%{_pkgconfigdir}/libgnomecupsui*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnomecupsui*.a
