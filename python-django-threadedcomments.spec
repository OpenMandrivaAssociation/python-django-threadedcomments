%define realname    django-threadedcomments
%define name	    python-%{realname}
%define version 0.9
%define release 2

Name: %{name}
Version: %{version}
Release: %{release}
Summary:        A simple yet flexible threaded commenting system
Group:          Development/Python
License:        BSD
URL:            http://code.google.com/p/django-threadedcomments/
Source:         %{realname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch
BuildRequires:  python-devel python-setuptools
Requires:       python-django

%description
A simple yet flexible threaded commenting system.

%prep
%setup -q -n %{realname}-%{version}
find . -name \*._* -exec rm {} +
find . -name \*.buildinfo* -exec rm {} +

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{py_puresitedir}/*



%changelog
* Tue Nov 02 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.9-1mdv2011.0
+ Revision: 591975
- import python-django-threadedcomments

