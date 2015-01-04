#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-manipulate
Version  : 1.0.1
Release  : 11
URL      : http://cran.r-project.org/src/contrib/manipulate_1.0.1.tar.gz
Source0  : http://cran.r-project.org/src/contrib/manipulate_1.0.1.tar.gz
Summary  : Interactive Plots for RStudio
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : clr-R-helpers

%description
No detailed description available

%prep
%setup -q -c -n manipulate

%build

%install
rm -rf %{buildroot}
export LANG=C
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library manipulate
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library manipulate


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/manipulate/DESCRIPTION
/usr/lib64/R/library/manipulate/INDEX
/usr/lib64/R/library/manipulate/Meta/Rd.rds
/usr/lib64/R/library/manipulate/Meta/hsearch.rds
/usr/lib64/R/library/manipulate/Meta/links.rds
/usr/lib64/R/library/manipulate/Meta/nsInfo.rds
/usr/lib64/R/library/manipulate/Meta/package.rds
/usr/lib64/R/library/manipulate/NAMESPACE
/usr/lib64/R/library/manipulate/R/manipulate
/usr/lib64/R/library/manipulate/R/manipulate.rdb
/usr/lib64/R/library/manipulate/R/manipulate.rdx
/usr/lib64/R/library/manipulate/help/AnIndex
/usr/lib64/R/library/manipulate/help/aliases.rds
/usr/lib64/R/library/manipulate/help/manipulate.rdb
/usr/lib64/R/library/manipulate/help/manipulate.rdx
/usr/lib64/R/library/manipulate/help/paths.rds
/usr/lib64/R/library/manipulate/html/00Index.html
/usr/lib64/R/library/manipulate/html/R.css
