#
# TODO: GarminDev - maybe as other package
#	BR check
#
Summary:	Garmin's MapSource clone for Linux
Summary(pl.UTF-8):	Klon MapSource pod Linuksa
Name:		qlandkartegt
Version:	1.8.1
Release:	7
License:	GPL v2
Group:		X11/Applications
Source0:	https://downloads.sourceforge.net/qlandkartegt/%{name}-%{version}.tar.gz
# Source0-md5:	2bfe90aff7e21b19572b7b250d76a540
Patch0:		gcc8.patch
Patch1:		gpsd-3.19.patch
Patch2:		gpsd-3.20.patch
URL:		http://qlandkarte.org/
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	QtCore-devel >= 4.6.0
BuildRequires:	QtDBus-devel >= 4.6.0
BuildRequires:	QtGui-devel >= 4.6.0
BuildRequires:	QtNetwork-devel >= 4.6.0
BuildRequires:	QtOpenGL-devel >= 4.6.0
BuildRequires:	QtSql-devel >= 4.6.0
BuildRequires:	QtWebKit-devel >= 4.6.0
BuildRequires:	QtXml-devel >= 4.6.0
BuildRequires:	cmake >= 2.6.0
BuildRequires:	gdal-devel
BuildRequires:	gpsd-devel >= 3.20
BuildRequires:	libdmtx-devel
BuildRequires:	libexif-devel
BuildRequires:	libjpeg-devel
BuildRequires:	proj-devel
BuildRequires:	qt4-build >= 4.6.0
BuildRequires:	qt4-linguist >= 4.6.0
BuildRequires:	qt4-qmake >= 4.6.0
BuildRequires:	rpmbuild(macros) >= 1.605
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
%patch2 -p1

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

%{__mv} $RPM_BUILD_ROOT%{_datadir}/qlandkartegt/translations/qlandkartegt_{es_ES,es}.qm
%{__mv} $RPM_BUILD_ROOT%{_datadir}/qlandkartegt/translations/qlandkartegt_{it_IT,it}.qm

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc INSTALL changelog.txt
%attr(755,root,root) %{_bindir}/cache2gtiff
%attr(755,root,root) %{_bindir}/map2gcm
%attr(755,root,root) %{_bindir}/map2jnx
%attr(755,root,root) %{_bindir}/map2rmap
%attr(755,root,root) %{_bindir}/map2rmp
%attr(755,root,root) %{_bindir}/qlandkartegt
%dir %{_datadir}/qlandkartegt
%dir %{_datadir}/qlandkartegt/translations
%lang(cs) %{_datadir}/qlandkartegt/translations/qlandkartegt_cs.qm
%lang(de) %{_datadir}/qlandkartegt/translations/qlandkartegt_de.qm
%lang(es) %{_datadir}/qlandkartegt/translations/qlandkartegt_es.qm
%lang(fr) %{_datadir}/qlandkartegt/translations/qlandkartegt_fr.qm
%lang(it) %{_datadir}/qlandkartegt/translations/qlandkartegt_it.qm
%lang(nl) %{_datadir}/qlandkartegt/translations/qlandkartegt_nl.qm
%lang(ru) %{_datadir}/qlandkartegt/translations/qlandkartegt_ru.qm
%attr(755,root,root) %{_libdir}/libSerialPort.so
%attr(755,root,root) %{_libdir}/libqextserialport.so
%attr(755,root,root) %{_libdir}/libqtexthtmlexporter.so
%attr(755,root,root) %{_libdir}/libqtsoap.so
%attr(755,root,root) %{_libdir}/libqzip.so
%attr(755,root,root) %{_libdir}/libtzone.so
%{_desktopdir}/qlandkartegt.desktop
%{_mandir}/man1/qlandkartegt.1*
%{_pixmapsdir}/qlandkartegt.png
