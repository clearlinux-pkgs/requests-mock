#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : requests-mock
Version  : 1.5.2
Release  : 40
URL      : http://pypi.debian.net/requests-mock/requests-mock-1.5.2.tar.gz
Source0  : http://pypi.debian.net/requests-mock/requests-mock-1.5.2.tar.gz
Summary  : Mock out responses from the requests package
Group    : Development/Tools
License  : Apache-2.0
Requires: requests-mock-license = %{version}-%{release}
Requires: requests-mock-python = %{version}-%{release}
Requires: requests-mock-python3 = %{version}-%{release}
Requires: fixtures
Requires: requests
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : extras
BuildRequires : fixtures
BuildRequires : pbr
BuildRequires : python-mock
BuildRequires : requests
BuildRequires : six
BuildRequires : testtools

%description
requests-mock
        ===============================

%package license
Summary: license components for the requests-mock package.
Group: Default

%description license
license components for the requests-mock package.


%package python
Summary: python components for the requests-mock package.
Group: Default
Requires: requests-mock-python3 = %{version}-%{release}

%description python
python components for the requests-mock package.


%package python3
Summary: python3 components for the requests-mock package.
Group: Default
Requires: python3-core

%description python3
python3 components for the requests-mock package.


%prep
%setup -q -n requests-mock-1.5.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541278478
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 --verbose py2 || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/requests-mock
cp LICENSE %{buildroot}/usr/share/package-licenses/requests-mock/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/requests-mock/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
