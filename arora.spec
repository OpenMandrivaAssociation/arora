Name:		arora
Version:	0.3
Release:	%mkrel 1
License:	GPLv2+
URL:		http://code.google.com/p/arora/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-build
BuildRequires:	qt4-devel
Buildrequires:	qt4-linguist
Source:		http://arora.googlecode.com/files/%name-%version.tar.gz
Group:		Networking/WWW
Summary:	Cross Platform WebKit Browser

%description
Arora is a simple cross platform web browser. Currently Arora is a very
basic browser whose feature list includes things like "History" and
"Bookmarks".

%prep
%setup -q

%build
%qmake_qt4 PREFIX=%_prefix QMAKE_CFLAGS="%{optflags}" QMAKE_CXXFLAGS="%{optflags}" QMAKE_LFLAGS="%{?ldflags}"
%make

%install
rm -fr %buildroot
make install INSTALL_ROOT=%{buildroot}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/*
%{_datadir}/pixmaps/*
