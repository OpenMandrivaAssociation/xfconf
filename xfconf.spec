%define url_ver %(echo %{version} | cut -d. -f1,2)
%define major 2
%define apiver 0
%define libname %mklibname %{name} %{apiver} %{major}
%define develname %mklibname %{name} -d
%define _disable_rebuild_configure 1

Summary:	A configuration storage system for Xfce
Name:		xfconf
Version:	4.12.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/xfce/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
Source1:	xfconf.rpmlintrc
BuildRequires:	pkgconfig(libxfce4util-1.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	perl(ExtUtils::Depends)
BuildRequires:	perl(ExtUtils::PkgConfig)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Glib::MakeHelper)
BuildRequires:	perl(Glib)
BuildRequires:	perl-devel
BuildRequires:	gettext
Requires:	dbus-x11

%description
Xfconf is a hierarchical (tree-like) configuration
system for the Xfce graphical desktop environment.

%files -f %{name}.lang
%doc AUTHORS NEWS ChangeLog
%dir %{_sysconfdir}/xdg/xfce4/xfconf
%{_bindir}/xfconf-query
%{_libdir}/xfce4/%{name}/xfconfd
%{_datadir}/dbus-1/services/org.xfce.Xfconf.service
%{_datadir}/gtk-doc/html/xfconf

#---------------------------------------------------------------------------

%package -n %{libname}
Summary:	Main library for xfconf
Group:		System/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{mklibname %{name} 0} < 4.5.92

%description -n %{libname}
Main library for the xfconf, a configuration
storage system for Xfce.

%files -n %{libname}
%{_libdir}/*xfconf-%{apiver}.so.%{major}*

#---------------------------------------------------------------------------

%package -n %{develname}
Summary:	Development files for xfconf
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n %{develname}
Development files and headers for xfconf.

%files -n %{develname}
%{_includedir}/xfce4/xfconf-%{apiver}
%{_libdir}/libxfconf-%{apiver}.so
%{_libdir}/pkgconfig/libxfconf-%{apiver}.pc

#---------------------------------------------------------------------------

%package -n perl-%{name}
Summary:	Perl bindings for %{name}
Group:		Development/Perl
Requires:	%{libname} = %{version}-%{release}

%description -n perl-%{name}
Perl bindings for %{name}.

%files -n perl-%{name}
%dir %{perl_sitearch}/Xfce4
%dir %{perl_sitearch}/Xfce4/Xfconf
%dir %{perl_sitearch}/Xfce4/Xfconf/Install
%dir %{perl_sitearch}/auto/Xfce4/Xfconf
%{perl_sitearch}/Xfce4/*.pm
%{perl_sitearch}/Xfce4/Xfconf/Install/*
%{perl_sitearch}/auto/Xfce4/Xfconf/*.so
%{_mandir}/man3/Xfce4::Xfconf.3pm.*

#---------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
%xdt_autogen
%configure \
	--enable-perl-bindings \
%make_build

%install
%make_install

install -dm 0755 %{buildroot}%{_mandir}/man3
mv -f %{buildroot}/usr/local/share/man/man3/Xfce4::Xfconf.3pm %{buildroot}%{_mandir}/man3

# dummy
mkdir -p %{buildroot}%{_sysconfdir}/xdg/xfce4/xfconf

# locales
%find_lang %{name} %{name}.lang
