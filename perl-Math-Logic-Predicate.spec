#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	Logic-Predicate
Summary:	Math::Logic::Predicate - manage and query a predicate assertion database
Summary(pl):	Math::Logic::Predicate - zarz�dzanie i przeszukiwanie bazy danych twierdze�
Name:		perl-Math-Logic-Predicate
Version:	0.03
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4918c427d82cb3a4d27a080f3f661040
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Logic::Predicate is an implementation which can prove statements
based on first order predicate calculus assertions (think Prolog). At
the moment, it is only a subset of the predicate calculus, but by
version 1.0 at the latest it will support the entire system. It is
written entirely in Perl, and it's really fast, too.

%description -l pl
Math::Logic::Predicate to implementacja potrafi�ca udowadnia�
twierdzenia w oparciu o twierdzenia dotycz�ce rachunku predykat�w
pierwszego rz�du (jak w Prologu). Aktualnie jest to tylko podzbi�r
rachunku predykat�w, ale do wersji 1.0 powinien by� obs�ugiwany ca�y
system. Modu� jest napisany w ca�kowicie w Perlu i jest naprawd�
szybki.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{perl_vendorlib}/Math/Logic
%{perl_vendorlib}/Math/Logic/Predicate.pm
%{_mandir}/man3/*
