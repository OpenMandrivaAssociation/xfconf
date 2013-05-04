%define url_ver %(echo %{version} | cut -d. -f1,2)
%define major 2
%define apiver 0
%define libname %mklibname %{name} %{apiver} %{major}
%define develname %mklibname %{name} -d

Summary:	A configuration storage system for Xfce
Name:		xfconf
Version:	4.10.0
Release:	4
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/xfce/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	libxfce4util-devel >= 4.10.0
BuildRequires:	glib2-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	perl(ExtUtils::Depends)
BuildRequires:	perl(ExtUtils::PkgConfig)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Glib::MakeHelper)
BuildRequires:	perl(Glib)
BuildRequires:	perl-devel
BuildRequires:	gettext
Requires:	dbus-x11
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Xfconf is a hierarchical (tree-like) configuration
system for the Xfce graphical desktop environment.

%package -n %{libname}
Summary:	Main library for xfconf
Group:		System/Libraries
Requires:	%{name} = %{version}-%{release}
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
Requires:	dbus-glib-devel
Requires:	dbus-devel
Requires:	glib2-devel

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
	--disable-checks \
	--disable-gtk-doc \
	--enable-perl-bindings

%make

%install

%makeinstall_std

mkdir -p %{buildroot}%{_mandir}/man3

mv -f %{buildroot}/usr/local/share/man/man3/Xfce4::Xfconf.3pm %{buildroot}%{_mandir}/man3

# dummy
mkdir -p %{buildroot}%{_sysconfdir}/xdg/xfce4/xfconf


%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS NEWS ChangeLog
%dir %{_sysconfdir}/xdg/xfce4/xfconf
%{_bindir}/xfconf-query
%{_libdir}/xfce4/%{name}/xfconfd
%{_datadir}/dbus-1/services/org.xfce.Xfconf.service
%{_datadir}/gtk-doc/html/xfconf

%files -n %{libname}
%{_libdir}/*xfconf-%{apiver}.so.%{major}*

%files -n %{develname}
%{_includedir}/xfce4/xfconf-%{apiver}
%{_libdir}/libxfconf-%{apiver}.so
%{_libdir}/pkgconfig/libxfconf-%{apiver}.pc

%files -n perl-%{name}
%dir %{perl_sitearch}/Xfce4
%dir %{perl_sitearch}/Xfce4/Xfconf
%dir %{perl_sitearch}/Xfce4/Xfconf/Install
%dir %{perl_sitearch}/auto/Xfce4/Xfconf
%{perl_sitearch}/Xfce4/*.pm
%{perl_sitearch}/Xfce4/Xfconf/Install/*
%{perl_sitearch}/auto/Xfce4/Xfconf/*.so
%{_mandir}/man3/Xfce4::Xfconf.3pm.*

%changelog
* Mon Apr 30 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.10.0-1
+ Revision: 794638
- update to new version 4.10.0

* Sun Apr 15 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.9.1-1
+ Revision: 791113
- disable gtk docs
- update to new version 4.9.1

* Mon Apr 02 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.9.0-1
+ Revision: 788881
- update to new version 4.9.0
- drop old stuff from spec file

* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 4.8.1-2
+ Revision: 768358
- mass rebuild of perl extensions against perl 5.14.2

* Tue Dec 27 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.1-1
+ Revision: 745802
- drop la files
- provide better url parsing in url_ver definition (this should go to the global rpm macros, maybe someday who knows :)
- update to new version 4.8.1
- fix file list

* Wed Jan 19 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.0-1
+ Revision: 631655
- update to new version 4.8.0

* Thu Jan 06 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.5-1mdv2011.0
+ Revision: 629099
- update to new version 4.7.5

* Sat Dec 04 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.4-1mdv2011.0
+ Revision: 609296
- update to new version 4.7.4

* Fri Sep 17 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.3-1mdv2011.0
+ Revision: 579276
- update to new version 4.7.3
- fix file list
- handle new url for Source0

* Thu Jul 22 2010 Jérôme Quelin <jquelin@mandriva.org> 4.6.2-2mdv2011.0
+ Revision: 556783
- perl 5.12 rebuild

* Thu Jul 15 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.2-1mdv2011.0
+ Revision: 553659
- update to new version 4.6.2

* Mon Mar 01 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.1-4mdv2010.1
+ Revision: 513125
- disable checks for non existing settings

* Thu Feb 25 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.1-3mdv2010.1
+ Revision: 511087
- add missing requires and buildrequires

* Sat Jan 02 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.1-2mdv2010.1
+ Revision: 484913
- library should require binaries

* Tue Apr 21 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.1-1mdv2010.0
+ Revision: 368570
- update to new version 4.6.1

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.0-2mdv2009.1
+ Revision: 349233
- rebuild whole xfce

* Fri Feb 27 2009 Jérôme Soyer <saispo@mandriva.org> 4.6.0-1mdv2009.1
+ Revision: 345642
- New upstream release

* Mon Jan 26 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.99.1-1mdv2009.1
+ Revision: 333867
- update to new version 4.5.99.1

* Wed Jan 14 2009 Jérôme Soyer <saispo@mandriva.org> 4.5.93-1mdv2009.1
+ Revision: 329529
- New upstream release
- New upstream release

* Wed Dec 10 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.92-3mdv2009.1
+ Revision: 312380
- requires dbus-x11

* Mon Nov 24 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.92-2mdv2009.1
+ Revision: 306418
- own /etc/xdg/xfce4/xfconf dir
- add full path for the Source0

* Sat Nov 15 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.92-1mdv2009.1
+ Revision: 303482
- introduce perl-xfconf subpackage
- bump major
- obsolete old library
- update to new version 4.5.92 (Xfce 4.6 Beta 2 Hopper)
- enable perl bindings
- own missing directory

* Thu Oct 16 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.91-1mdv2009.1
+ Revision: 294440
- Xfce4.6 beta1 is landing on cooker
- add source and spec files
- Created package structure for xfconf.

