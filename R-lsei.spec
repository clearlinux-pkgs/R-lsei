#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-lsei
Version  : 1.2.0
Release  : 9
URL      : https://cran.r-project.org/src/contrib/lsei_1.2-0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/lsei_1.2-0.tar.gz
Summary  : Solving Least Squares or Quadratic Programming Problems under
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-lsei-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
regression problems under linear equality/inequality
	     constraints. Functions for solving quadratic programming
	     problems are also available, which transform such problems
	     into least squares ones first. It is developed based on the
	     'Fortran' program of Lawson and Hanson (1974, 1995), which is
	     public domain and available at

%package lib
Summary: lib components for the R-lsei package.
Group: Libraries

%description lib
lib components for the R-lsei package.


%prep
%setup -q -c -n lsei

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552927304

%install
export SOURCE_DATE_EPOCH=1552927304
rm -rf %{buildroot}
export LANG=C
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lsei
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lsei
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lsei
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  lsei || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/lsei/DESCRIPTION
/usr/lib64/R/library/lsei/INDEX
/usr/lib64/R/library/lsei/Meta/Rd.rds
/usr/lib64/R/library/lsei/Meta/features.rds
/usr/lib64/R/library/lsei/Meta/hsearch.rds
/usr/lib64/R/library/lsei/Meta/links.rds
/usr/lib64/R/library/lsei/Meta/nsInfo.rds
/usr/lib64/R/library/lsei/Meta/package.rds
/usr/lib64/R/library/lsei/NAMESPACE
/usr/lib64/R/library/lsei/R/lsei
/usr/lib64/R/library/lsei/R/lsei.rdb
/usr/lib64/R/library/lsei/R/lsei.rdx
/usr/lib64/R/library/lsei/help/AnIndex
/usr/lib64/R/library/lsei/help/aliases.rds
/usr/lib64/R/library/lsei/help/lsei.rdb
/usr/lib64/R/library/lsei/help/lsei.rdx
/usr/lib64/R/library/lsei/help/paths.rds
/usr/lib64/R/library/lsei/html/00Index.html
/usr/lib64/R/library/lsei/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/lsei/libs/lsei.so
/usr/lib64/R/library/lsei/libs/lsei.so.avx2
/usr/lib64/R/library/lsei/libs/lsei.so.avx512
