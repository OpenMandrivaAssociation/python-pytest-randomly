Name:		python-pytest-randomly
Version:	3.16.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-randomly/pytest_randomly-%{version}.tar.gz
Summary:	Pytest plugin to randomly order tests and control random.seed.
URL:		https://pypi.org/project/pytest-randomly/
License:	None
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildRequires:	python-devel
BuildRequires:	python%{pyver}dist(importlib-metadata) >= 3.6
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(setuptools)
BuildArch:	noarch

%description
Pytest plugin to randomly order tests and control random.seed.

%prep
%autosetup -p1 -n pytest_randomly-%{version}

%files
%{py_sitedir}/pytest_randomly
%{py_sitedir}/pytest_randomly-%{version}.dist-info
