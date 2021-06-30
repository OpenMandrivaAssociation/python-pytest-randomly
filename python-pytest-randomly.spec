# Created by pyp2rpm-3.3.5
%global pypi_name pytest-randomly
%global altname pytest_randomly
Name:           python-%{pypi_name}
Version:        3.8.0
Release:        1
Summary:        Pytest plugin to randomly order tests and control random
Group:          Development/Python
License:        MIT
URL:            https://github.com/pytest-dev/pytest-randomly
Source0:        %{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(importlib-metadata) >= 3.6
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)

%description
 pytest-randomly :target:

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/pytest_randomly.py
%{python3_sitelib}/%{altname}.py
%{python3_sitelib}/%{altname}-%{version}-py%{python3_version}.egg-info

