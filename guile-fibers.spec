Summary:	Lighweight concurrency for Guile
Summary(pl.UTF-8):	Lekka współbieżność dla Guile
Name:		guile-fibers
Version:	1.1.1
Release:	1
License:	LGPL v3+ (library), FDL v1.3+ (documentation)
Group:		Libraries
#Source0Download: https://github.com/wingo/fibers/releases
Source0:	https://github.com/wingo/fibers/archive/v%{version}/fibers-%{version}.tar.gz
# Source0-md5:	061d9f677f676142ad79a21c2cad9443
Patch0:		fibers-info.patch
URL:		https://github.com/wingo/fibers
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	guile-devel >= 5:2.2
BuildRequires:	libtool
BuildRequires:	texinfo
Requires:	guile >= 5:2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautostrip	.*\.go

%description
Fibers is a facility that provides Go-like concurrency for Guile
Scheme, in the tradition of Concurrent ML.

%description -l pl.UTF-8
Fibers to biblioteka dostarczająca współbieżność w stylu Go dla
języka Guile Scheme, utrzymaną w tradycji Concurrent ML.

%prep
%setup -q -n fibers-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/guile/*.*/extensions/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md TODO.md
%attr(755,root,root) %{_libdir}/guile/*.*/extensions/epoll.so*
%{_libdir}/guile/*.*/site-ccache/fibers.go
%{_libdir}/guile/*.*/site-ccache/fibers
%dir %{_libdir}/guile/*.*/site-ccache/web
%dir %{_libdir}/guile/*.*/site-ccache/web/server
%{_libdir}/guile/*.*/site-ccache/web/server/fibers.go
%{_datadir}/guile/site/*.*/fibers.scm
%{_datadir}/guile/site/*.*/fibers
%dir %{_datadir}/guile/site/*.*/web
%dir %{_datadir}/guile/site/*.*/web/server
%{_datadir}/guile/site/*.*/web/server/fibers.scm
%{_infodir}/fibers.info*
