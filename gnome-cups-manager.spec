Summary:	GNOME manager for CUPS printers
Summary(pl):	Zarz±dca drukarek CUPS dla GNOME
Name:		gnome-cups-manager
Version:	0.18
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.18/%{name}-%{version}.tar.bz2
# Source0-md5:	d8508654ed956de73fa62a72b4358a1a
Source1:	%{name}-cc.desktop
Patch0:		%{name}-gcc34.patch
Patch1:		%{name}-locale-names.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gnome-common >= 2.4.0
BuildRequires:	gtk+2-devel >= 2.3.1
BuildRequires:	libbonobo-devel >= 2.0.0
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libgnomecups-devel >= 0.1.5
BuildRequires:	libgnomeprint-devel >= 2.5.0
BuildRequires:	libgnomeui-devel >= 2.3.3.1-2
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
Requires:	gnome-icon-theme
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
Requires:	%{name} = %{version}-%{release}
Requires:	libgnomecups-devel >= 0.1.4

%description devel
Devel files for gnome-cups-manager (libgnomecupsui).

%description devel -l pl
Pliki nag³ówkowe dla gnome-cups-manager (libgnomecupsui).

%package static
Summary:	gnome-cups-manager (libgnomecupsui) static library
Summary(pl):	Statyczna biblioteka gnome-cups-manager (libgnomecupsui)
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
gnome-cups-manager (libgnomecupsui) static library.

%description static -l pl
Statyczna biblioteka gnome-cups-manager (libgnomecupsui).

%prep
%setup -q
%patch0 -p1
%patch1 -p1

mv po/{no,nb}.po

%build
%{__libtoolize}
%{__aclocal} -I %{_aclocaldir}/gnome2-macros
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/gnome/capplets

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/gnome/capplets

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
%{_iconsdir}/hicolor/48x48/devices/*.png
%{_iconsdir}/hicolor/48x48/emblems/*.png
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
