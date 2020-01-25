#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"

%define		pdir	Crypt
%define		pnam	Simple
Summary:	Crypt::Simple Perl module - encrypt stuff simply
Summary(pl.UTF-8):	Moduł Perla Crypt::Simple - proste szyfrowanie
Name:		perl-Crypt-Simple
Version:	0.06
Release:	5
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	cdea18a98593364855f27afcb8519ec0
URL:		http://search.cpan.org/dist/Crypt-Simple/
BuildRequires:	perl-Crypt-Blowfish >= 2.06
BuildRequires:	perl-Digest-MD5 >= 2.13
BuildRequires:	perl-FreezeThaw >= 0.41
BuildRequires:	perl-IO-Compress >= 1.11
BuildRequires:	perl-MIME-Base64 >= 2.11
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Crypt-Blowfish >= 2.06
Requires:	perl-Digest-MD5 >= 2.13
Requires:	perl-FreezeThaw >= 0.41
Requires:	perl-IO-Compress >= 1.11
Requires:	perl-MIME-Base64 >= 2.11
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This little module will convert all your data into nice base64 text
that you can save in a text file, send in an email, store in a cookie
or web page, or bounce around the Net. The data you encrypt can be as
simple or as complicated as you like.

%description -l pl.UTF-8
Ten mały moduł moduł konwertuje dane na przyjemny tekst base64, który
można zapisać w pliku tekstowym, wysłać pocztą elektroniczną, zapisać
w ciasteczku lub na stronie WWW, albo przesyłać przez sieć.
Zaszyfrowane dane mogą być dowolnie proste lub skomplikowane.

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
%{perl_vendorlib}/Crypt/Simple.pm
%{_mandir}/man3/*
