%define upstream_name    Catalyst-View-Email
%define upstream_version 0.31

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Templated Email View
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Authen::SASL)
BuildRequires:	perl(Catalyst)
BuildRequires:	perl(Catalyst::View::Mason)
BuildRequires:	perl(Catalyst::View::TT)
BuildRequires:	perl(Class::C3)
BuildRequires:	perl(Email::Date::Format)
BuildRequires:	perl(Email::MIME)
BuildRequires:	perl(Email::MIME::Creator)
BuildRequires:	perl(Email::Send)
BuildRequires:	perl(Email::Sender::Simple)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::Requires)
BuildRequires:	perl(parent)

BuildArch:	noarch

%description
Helper for Email Views.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.310.0-2mdv2011.0
+ Revision: 656890
- rebuild for updated spec-helper

* Sun Jan 30 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.310.0-1
+ Revision: 634209
- update to new version 0.31

* Fri Jul 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.300.0-1mdv2011.0
+ Revision: 554266
- update to 0.30

* Wed Mar 24 2010 Jérôme Quelin <jquelin@mandriva.org> 0.270.0-1mdv2010.1
+ Revision: 527092
- update to 0.27

* Mon Feb 01 2010 Jérôme Quelin <jquelin@mandriva.org> 0.230.0-1mdv2010.1
+ Revision: 498975
- update to 0.23

* Fri Jan 29 2010 Jérôme Quelin <jquelin@mandriva.org> 0.220.0-1mdv2010.1
+ Revision: 497905
- update to 0.22

* Wed Jan 27 2010 Jérôme Quelin <jquelin@mandriva.org> 0.200.0-1mdv2010.1
+ Revision: 496999
- update to 0.20

* Tue Jan 19 2010 Jérôme Quelin <jquelin@mandriva.org> 0.190.0-1mdv2010.1
+ Revision: 493483
- update to 0.19

* Mon Jan 18 2010 Jérôme Quelin <jquelin@mandriva.org> 0.180.0-1mdv2010.1
+ Revision: 492949
- update to 0.18

* Fri Jan 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.170.0-1mdv2010.1
+ Revision: 491728
- update to 0.17
- adding missing buildrequires:
- fix setup
- update to 0.16

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.130.0-1mdv2010.1
+ Revision: 471286
- adding missing buildrequires:
- adding missing buildrequires:
- import perl-Catalyst-View-Email


* Sun Nov 29 2009 cpan2dist 0.13-1mdv
- initial mdv release, generated with cpan2dist
