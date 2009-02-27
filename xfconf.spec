%define major 2
%define apiver 0
%define libname %mklibname %{name} %{apiver} %{major}
%define develname %mklibname %{name} -d

Summary:	A configuration storage system for Xfce
Name:		xfconf
Version:	4.6.0
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://www.xfce.org
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
BuildRequires:	libxfce4util-devel >= %{version}
BuildRequires:	dbus-glib-devel
BuildRequires:	gtk-doc
BuildRequires:	perl(ExtUtils::Depends)
BuildRequires:	perl(ExtUtils::PkgConfig)
BuildRequires:	perl(Glib)
BuildRequires:	perl-devel
Requires:	%{libname} = %{version}-%{release}
Requires:	dbus-x11
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Xfconf is a hierarchical (tree-like) configuration
system for the Xfce graphical desktop environment.

%package -n %{libname}
Summary:	Main library for xfconf
Group:		System/Libraries
Obsoletes:	%{mklibname %{name} 0} < 4.5.92

%description -n %{libname}
Main library for the xfconf, a configuration
storage system for Xfce.

%package -n %{develname}
Summary:	Development files for xfconf
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n %{develname}
Development files and headers for xfconf.

%package -n perl-%{name}
Summary:	Perl bindings for %{name}
Group:		Development/Perl
Requires:	%{libname} = %{version}-%{release}

%description -n perl-%{name}
Perl bindings for %{name}.

%prep
%setup -q

%build
%configure2_5x	\
	--disable-static \
	--enable-checks \
	--enable-gtk-doc \
	--enable-perl-bindings

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

mkdir -p %{buildroot}%{_mandir}/man3

mv -f %{buildroot}/usr/local/share/man/man3/Xfce4::Xfconf.3pm %{buildroot}%{_mandir}/man3

# dummy
mkdir -p %{buildroot}%{_sysconfdir}/xdg/xfce4/xfconf

%find_lang %{name}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS NEWS ChangeLog
%dir %{_sysconfdir}/xdg/xfce4/xfconf
%{_bindir}/xfconf-query
%{_libdir}/xfconfd
%{_datadir}/dbus-1/services/org.xfce.Xfconf.service
%{_datadir}/gtk-doc/html/xfconf

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*xfconf-%{apiver}.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/xfce4/xfconf-0
%{_libdir}/libxfconf-0.la
%{_libdir}/libxfconf-0.so
%{_libdir}/pkgconfig/libxfconf-0.pc

%files -n perl-%{name}
%defattr(-,root,root)
%dir %{perl_sitearch}/Xfce4
%dir %{perl_sitearch}/Xfce4/Xfconf
%dir %{perl_sitearch}/Xfce4/Xfconf/Install
%dir %{perl_sitearch}/auto/Xfce4/Xfconf
%{perl_sitearch}/Xfce4/*.pm
%{perl_sitearch}/Xfce4/Xfconf/Install/*
%{perl_sitearch}/auto/Xfce4/Xfconf/*.so
%{_mandir}/man3/Xfce4::Xfconf.3pm.*
