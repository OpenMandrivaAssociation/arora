%define debug_package %{nil}

Summary:	Cross Platform WebKit Browser
Name:		arora
Version:	0.11.0
Release:	4
License:	GPLv2+
Group:		Networking/WWW
Url:		http://code.google.com/p/arora/
Source0:	arora-20120617.tar.xz

Buildrequires:	qt4-linguist
BuildRequires:	qt4-devel
Provides:	webclient

%description
Arora is a simple cross platform web browser. Currently Arora is a very
basic browser whose feature list includes things like "History" and
"Bookmarks".

%prep
%setup -qn %{name}

%build
%qmake_qt4 PREFIX=%_prefix 
%make

%install
make install INSTALL_ROOT=%{buildroot}

%files
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

