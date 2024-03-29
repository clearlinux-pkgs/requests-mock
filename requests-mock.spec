#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : requests-mock
Version  : 1.9.3
Release  : 66
URL      : https://files.pythonhosted.org/packages/71/1e/1680394d9ad02bf7fb34f6e161b6eff62c972f2c1e647389ce2d324b3c25/requests-mock-1.9.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/71/1e/1680394d9ad02bf7fb34f6e161b6eff62c972f2c1e647389ce2d324b3c25/requests-mock-1.9.3.tar.gz
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
BuildRequires : pytest
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
Provides: pypi(requests_mock)
Requires: pypi(requests)
Requires: pypi(six)

%description python3
python3 components for the requests-mock package.


%prep
%setup -q -n requests-mock-1.9.3
cd %{_builddir}/requests-mock-1.9.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1633196902
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
pytest --verbose || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/requests-mock
cp %{_builddir}/requests-mock-1.9.3/LICENSE %{buildroot}/usr/share/package-licenses/requests-mock/a018430a439541feea5dbfb78eecb64b4140172e
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/requests-mock/a018430a439541feea5dbfb78eecb64b4140172e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
