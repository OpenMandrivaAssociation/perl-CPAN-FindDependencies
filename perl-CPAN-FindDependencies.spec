
%define realname   CPAN-FindDependencies
%define version    2.0
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Object representing a module dependency
Source:     http://www.cpan.org/modules/by-module/CPAN/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(LWP::Simple)
BuildRequires: perl(Module::CoreList)
BuildRequires: perl(Parse::CPAN::Packages)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(URI::file)
BuildRequires: perl(YAML)

BuildArch: noarch

%description
no description found

%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc CHANGES README
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/cpandeps
/usr/share/man/man1/cpandeps.1.lzma

