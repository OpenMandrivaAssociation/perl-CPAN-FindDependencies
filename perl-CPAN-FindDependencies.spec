%define upstream_name    CPAN-FindDependencies
%define upstream_version 2.42

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Object representing a module dependency
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/CPAN/CPAN-FindDependencies-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Capture::Tiny)
BuildRequires:	perl(Devel::CheckOS)
BuildRequires:	perl(LWP::Simple)
BuildRequires:	perl(Module::CoreList)
BuildRequires:	perl(Parse::CPAN::Packages)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(URI::file)
BuildRequires:	perl(YAML)
BuildRequires:	perl(YAML::Tiny)
BuildArch:	noarch

%description
Object representing a module dependency.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc  README
%perl_vendorlib/*
%{_bindir}/cpandeps
%{_mandir}/man1/*
%{_mandir}/man3/*


%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 2.340.0-2mdv2011.0
+ Revision: 658735
- rebuild for updated spec-helper

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 2.340.0-1mdv2011.0
+ Revision: 552261
- update to 2.34

* Fri Mar 12 2010 Jérôme Quelin <jquelin@mandriva.org> 2.330.0-1mdv2010.1
+ Revision: 518480
- update to 2.33

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 2.320.0-1mdv2010.0
+ Revision: 401698
- rebuild using %%perl_convert_version
- fixed license field

* Mon May 11 2009 Jérôme Quelin <jquelin@mandriva.org> 2.32-1mdv2010.0
+ Revision: 374453
- yet another missing buildrequires
- yet another missing buildrequire
- adding missing buildrequires
- update to 2.32
- import perl-CPAN-FindDependencies


* Mon Dec 08 2008 cpan2dist 2.0-1mdv
- initial mdv release, generated with cpan2dist


