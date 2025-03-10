#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Pattern matching and various utilities for file systems paths
Summary(pl.UTF-8):	Dopasowywanie wzorców i różne narzędzia do ścieżek w systemie plików
Name:		python-pathtools
Version:	0.1.2
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pathtools/
Source0:	https://files.pythonhosted.org/packages/source/p/pathtools/pathtools-%{version}.tar.gz
# Source0-md5:	9a1af5c605768ea5804b03b734ff0f82
URL:		https://pypi.org/project/pathtools/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
# uses deprecated "import imp", to be removed in 3.12
BuildRequires:	python3-modules < 1:3.12
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python-flask_sphinx_themes
BuildRequires:	sphinx-pdg-2
%endif
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pattern matching and various utilities for file systems paths.

%description -l pl.UTF-8
Dopasowywanie wzorców i różne narzędzia do ścieżek w systemie plików.

%package -n python3-pathtools
Summary:	Pattern matching and various utilities for file systems paths
Summary(pl.UTF-8):	Dopasowywanie wzorców i różne narzędzia do ścieżek w systemie plików
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-pathtools
Pattern matching and various utilities for file systems paths.

%description -n python3-pathtools -l pl.UTF-8
Dopasowywanie wzorców i różne narzędzia do ścieżek w systemie plików.

%package apidocs
Summary:	API documentation for Python pathtools module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona pathtools
Group:		Documentation

%description apidocs
API documentation for Python pathtools module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona pathtools.

%prep
%setup -q -n pathtools-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%if %{with doc}
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-2
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README
%{py_sitescriptdir}/pathtools
%{py_sitescriptdir}/pathtools-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pathtools
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README
%{py3_sitescriptdir}/pathtools
%{py3_sitescriptdir}/pathtools-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/build/html/{_modules,_static,*.html,*.js}
%endif
