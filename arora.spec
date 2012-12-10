Name:		arora
Version:	0.11.0
Release:	%mkrel 3
License:	GPLv2+
URL:		http://code.google.com/p/arora/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-build
BuildRequires:	qt4-devel >= 3:4.4
Buildrequires:	qt4-linguist
#Source:		http://arora.googlecode.com/files/%name-%version.tar.gz
Source:		arora-20120617.tar.xz
Group:		Networking/WWW
Provides:	webclient
Summary:	Cross Platform WebKit Browser

%description
Arora is a simple cross platform web browser. Currently Arora is a very
basic browser whose feature list includes things like "History" and
"Bookmarks".

%prep
%setup -q -n %name

%build
%qmake_qt4 PREFIX=%_prefix 
%make

%install
rm -fr %buildroot
make install INSTALL_ROOT=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_bindir}/arora-cacheinfo
%{_bindir}/arora-placesimport
%{_bindir}/htmlToXBel
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/*
%{_datadir}/pixmaps/*


%changelog
* Sun Jun 17 2012 Bernhard Rosenkraenzer <bero@bero.eu> 0.11.0-3mdv2012.0
+ Revision: 806028
- Add fixes from git

* Thu Jan 05 2012 Bernhard Rosenkraenzer <bero@bero.eu> 0.11.0-2
+ Revision: 757927
- Add some bugfixes and HTML5 localStorage support from upstream git

* Fri Oct 01 2010 Funda Wang <fwang@mandriva.org> 0.11.0-1mdv2011.0
+ Revision: 582216
- update to new version 0.11.0

* Thu Dec 10 2009 Funda Wang <fwang@mandriva.org> 0.10.2-1mdv2010.1
+ Revision: 476118
- new version 0.10.2

* Tue Oct 06 2009 Stéphane Téletchéa <steletch@mandriva.org> 0.10.1-1mdv2010.0
+ Revision: 454633
- New version 0.10.1

* Mon Aug 31 2009 Frederik Himpe <fhimpe@mandriva.org> 0.9.0-1mdv2010.0
+ Revision: 423035
- update to new version 0.9.0
- update to new version 0.8.0

* Wed Jun 24 2009 Funda Wang <fwang@mandriva.org> 0.7.1-2mdv2010.0
+ Revision: 388837
- bump arora as qt4.5 goes 2009.0

* Wed Jun 03 2009 Funda Wang <fwang@mandriva.org> 0.7.1-1mdv2010.0
+ Revision: 382397
- New version 0.7.1

* Fri May 08 2009 Funda Wang <fwang@mandriva.org> 0.6.1-1mdv2010.0
+ Revision: 373464
- New version 0.6.1
- cacheinfo only builds with qt4.5

* Sat Apr 18 2009 Funda Wang <fwang@mandriva.org> 0.6-1mdv2009.1
+ Revision: 368005
- New version 0.6

* Sat Feb 21 2009 Funda Wang <fwang@mandriva.org> 0.5-1mdv2009.1
+ Revision: 343745
- New version 0.5

* Sat Oct 11 2008 Funda Wang <fwang@mandriva.org> 0.4-1mdv2009.1
+ Revision: 291876
- New version 0.4

* Tue Aug 05 2008 Funda Wang <fwang@mandriva.org> 0.3-1mdv2009.0
+ Revision: 263695
- BR lrelease
- import arora


