#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-manipulate
Version  : 1.0.1
Release  : 64
URL      : https://cran.r-project.org/src/contrib/manipulate_1.0.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/manipulate_1.0.1.tar.gz
Summary  : Interactive Plots for RStudio
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : buildreq-R
BuildRequires : util-linux

%description
The manipulate function accepts a plotting expression and a set of
  controls (e.g. slider, picker, checkbox, or button) which are used
  to dynamically change values within the expression. When a value is
  changed using its corresponding control the expression is
  automatically re-executed and the plot is redrawn.

%prep
%setup -q -c -n manipulate

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571859544

%install
export SOURCE_DATE_EPOCH=1571859544
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library manipulate
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library manipulate
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library manipulate
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc manipulate || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/manipulate/DESCRIPTION
/usr/lib64/R/library/manipulate/INDEX
/usr/lib64/R/library/manipulate/Meta/Rd.rds
/usr/lib64/R/library/manipulate/Meta/features.rds
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
