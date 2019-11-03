#
# TODO: GarminDev - maybe as other package
#	BR check
#
Summary:	Garmin's MapSource clone for Linux
Summary(pl.UTF-8):	Klon MapSource pod Linuksa
Name:		qlandkartegt
Version:	1.8.1
Release:	6
License:	GPLv2
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/qlandkartegt/%{name}-%{version}.tar.gz
# Source0-md5:	2bfe90aff7e21b19572b7b250d76a540
Patch0:		gcc8.patch
Patch1:		gpsd-3.19.patch
URL:		http://qlandkarte.org
BuildRequires:	QtCore-devel >= 4.6.0
BuildRequires:	QtDBus-devel >= 4.6.0
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtOpenGL-devel >= 4.6.0
BuildRequires:	QtSql-devel >= 4.6.0
BuildRequires:	QtWebKit-devel >= 4.6.0
BuildRequires:	QtXml-devel
BuildRequires:	cmake >= 2.6.0
BuildRequires:	gdal-devel
BuildRequires:	libusb-devel
BuildRequires:	proj-devel
BuildRequires:	qt4-build >= 4.6.0
BuildRequires:	qt4-linguist
BuildRequires:	qt4-qmake >= 4.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		filterout	-flto

%description
Garmin's MapSource clone for Linux.

%description -l pl.UTF-8
Klon MapSource pod Linuksa.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
install -d build
cd build
CFLAGS="%{rpmcflags} -DACCEPT_USE_OF_DEPRECATED_PROJ_API_H"
CXXFLAGS="%{rpmcxxflags} -DACCEPT_USE_OF_DEPRECATED_PROJ_API_H"
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_bindir},%{_datadir}/qlandkartegt,%{_libdir}}
cp build/lib/*.so $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL changelog.txt
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/qlandkartegt
%dir %{_datadir}/qlandkartegt/translations
%{_datadir}/qlandkartegt/translations/*.qm
%attr(755,root,root) %{_libdir}/*.so
%{_desktopdir}/qlandkartegt.desktop
%{_mandir}/man1/*.1*
%{_pixmapsdir}/qlandkartegt.png
