%define upstream_name    CPAN-FindDependencies
%define upstream_version 2.32

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Object representing a module dependency
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/CPAN/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Capture::Tiny)
BuildRequires: perl(Devel::CheckOS)
BuildRequires: perl(LWP::Simple)
BuildRequires: perl(Module::CoreList)
BuildRequires: perl(Parse::CPAN::Packages)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(URI::file)
BuildRequires: perl(YAML)
BuildRequires: perl(YAML::Tiny)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
no description found

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
/usr/share/man/man1/*

