
Name: xrootd-cmstfc
Version: 1.4
Release: 1
Summary: CMS TFC plugin for xrootd

Group: System Environment/Daemons
License: BSD
URL: svn://t2.unl.edu/brian/XrdCmsTfc
Source0: %{name}-%{version}.tar.gz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: xrootd-devel xerces-c-devel pcre-devel
Requires: xrootd pcre xerces-c

%description
%{summary}

%prep
%setup -q

%build
%configure --with-xrootd-incdir=/usr/include/xrootd
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/libXrdCmsTfc*
%{_includedir}/xrootd/XrdCmsTfc/XrdCmsTfc.hh

%changelog
* Tue Aug 24 2010 Brian Bockelman <bbockelm@cse.unl.edu> 1.4.0-1
- Break xrootd-cmstfc off into its own standalone RPM.
