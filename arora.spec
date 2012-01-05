Name:		arora
Version:	0.11.0
Release:	%mkrel 1
License:	GPLv2+
URL:		http://code.google.com/p/arora/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-build
BuildRequires:	qt4-devel >= 3:4.4
Buildrequires:	qt4-linguist
Source:		http://arora.googlecode.com/files/%name-%version.tar.gz
Patch:		0001-fix-the-problem-in-the-downloadmanager-when-the-dele.patch
Patch1:		0002-Show-the-number-of-downloads-in-the-download-manager.patch
Patch2:		0003-Change-the-AutoFillManager-to-not-use-hard-coded-off.patch
Patch3:		0004-Fixed-ssl-certificate-problem-with-sites-like-https-.patch
Patch4:		0005-Autofill-webforms-in-Preferences-was-always-checked.patch
Patch5:		0006-Autofill-manager-was-always-storing-forms.patch
Patch6:		0007-Support-persistent-data-storage-HTML5-localStorage.patch
Patch7:		0008-Fix-start-page-not-being-valid-XML-but-claiming-to-b.patch
Group:		Networking/WWW
Provides:	webclient
Summary:	Cross Platform WebKit Browser

%description
Arora is a simple cross platform web browser. Currently Arora is a very
basic browser whose feature list includes things like "History" and
"Bookmarks".

%prep
%setup -q
%patch -p1 -b .dlm~
%patch1 -p1 -b .dls~
%patch2 -p1 -b .afm~
%patch3 -p1 -b .ssl~
%patch4 -p1 -b .autofill1~
%patch5 -p1 -b .autofill2~
%patch6 -p1 -b .localStorage~
%patch7 -p1 -b .startPage~

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
