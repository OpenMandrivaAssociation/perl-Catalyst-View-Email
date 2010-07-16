%define upstream_name    Catalyst-View-Email
%define upstream_version 0.30

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Templated Email View for [% app %]
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Authen::SASL)
BuildRequires: perl(Catalyst)
BuildRequires: perl(Catalyst::View::Mason)
BuildRequires: perl(Catalyst::View::TT)
BuildRequires: perl(Class::C3)
BuildRequires: perl(Email::Date::Format)
BuildRequires: perl(Email::MIME)
BuildRequires: perl(Email::MIME::Creator)
BuildRequires: perl(Email::Send)
BuildRequires: perl(Email::Sender::Simple)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::Requires)
BuildRequires: perl(parent)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Helper for Email Views.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/*
