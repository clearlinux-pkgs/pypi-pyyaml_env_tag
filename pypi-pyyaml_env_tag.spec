#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pyyaml_env_tag
Version  : 0.1
Release  : 7
URL      : https://files.pythonhosted.org/packages/fb/8e/da1c6c58f751b70f8ceb1eb25bc25d524e8f14fe16edcce3f4e3ba08629c/pyyaml_env_tag-0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/fb/8e/da1c6c58f751b70f8ceb1eb25bc25d524e8f14fe16edcce3f4e3ba08629c/pyyaml_env_tag-0.1.tar.gz
Summary  : A custom YAML tag for referencing environment variables in YAML files.
Group    : Development/Tools
License  : MIT
Requires: pypi-pyyaml_env_tag-license = %{version}-%{release}
Requires: pypi-pyyaml_env_tag-python = %{version}-%{release}
Requires: pypi-pyyaml_env_tag-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(flit_core)

%description
# pyyaml_env_tag
A custom YAML tag for referencing environment variables in YAML files.

%package license
Summary: license components for the pypi-pyyaml_env_tag package.
Group: Default

%description license
license components for the pypi-pyyaml_env_tag package.


%package python
Summary: python components for the pypi-pyyaml_env_tag package.
Group: Default
Requires: pypi-pyyaml_env_tag-python3 = %{version}-%{release}

%description python
python components for the pypi-pyyaml_env_tag package.


%package python3
Summary: python3 components for the pypi-pyyaml_env_tag package.
Group: Default
Requires: python3-core
Provides: pypi(pyyaml_env_tag)
Requires: pypi(pyyaml)

%description python3
python3 components for the pypi-pyyaml_env_tag package.


%prep
%setup -q -n pyyaml_env_tag-0.1
cd %{_builddir}/pyyaml_env_tag-0.1
pushd ..
cp -a pyyaml_env_tag-0.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656403492
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyyaml_env_tag
cp %{_builddir}/pyyaml_env_tag-0.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pyyaml_env_tag/9740bf8b47654938076b40a0f533700e60230032
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pyyaml_env_tag/9740bf8b47654938076b40a0f533700e60230032

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
