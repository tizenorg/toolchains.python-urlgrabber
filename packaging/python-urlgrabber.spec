
%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
Name:       python-urlgrabber
Summary:    A high-level cross-protocol url-grabber
Version:    3.9.1
Release:    1
Group:      Development/Libraries
License:    LGPLv2+
BuildArch:  noarch
URL:        http://urlgrabber.baseurl.org/
Source0:    http://urlgrabber.baseurl.org/download/urlgrabber-%{version}.tar.gz
Patch0:     urlgrabber-HEAD.patch
Patch1:     urlgrabber-libproxy-httponly.patch
Requires:   python-pycurl
Requires:   m2crypto
Requires:   libproxy-python
BuildRequires:  python-devel
BuildRequires:  python-pycurl
Provides:   urlgrabber = %{version}-%{release}

BuildRoot:  %{_tmppath}/%{name}-%{version}-build

%description
A high-level cross-protocol url-grabber for python supporting HTTP, FTP 
and file locations.  Features include keepalive, byte ranges, throttling,
authentication, proxies and more.




%prep
%setup -q -n urlgrabber-%{version}
%patch0 -p1
%patch1 -p1

%build

CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot} -O1 --prefix=%{_prefix}

rm -rf $RPM_BUILD_ROOT/%{_docdir}/urlgrabber-%{version}

%clean
rm -rf %{buildroot}






%files
%defattr(-,root,root,-)
%doc ChangeLog LICENSE README TODO
%{python_sitelib}/urlgrabber*
%{_bindir}/urlgrabber

