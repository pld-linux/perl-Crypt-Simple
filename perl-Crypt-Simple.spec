%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	Simple
Summary:	Crypt::Simple Perl module - encrypt stuff simply
Summary(pl):	Modu³ Perla Crypt::Simple - proste szyfrowanie
Name:		perl-Crypt-Simple
Version:	0.04
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Compress-Zlib >= 1.11
BuildRequires:	perl-Crypt-Blowfish >= 2.06
BuildRequires:	perl-Digest-MD5 >= 2.13
BuildRequires:	perl-FreezeThaw >= 0.41
BuildRequires:	perl-MIME-Base64 >= 2.11
BuildRequires:	rpm-perlprov >= 3.0.3-16
Requires:	perl-Compress-Zlib >= 1.11
Requires:	perl-Crypt-Blowfish >= 2.06
Requires:	perl-Digest-MD5 >= 2.13
Requires:	perl-FreezeThaw >= 0.41
Requires:	perl-MIME-Base64 >= 2.11
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This little module will convert all your data into nice base64 text
that you can save in a text file, send in an email, store in a cookie
or web page, or bounce around the Net. The data you encrypt can be as
simple or as complicated as you like.

%description -l pl
Ten ma³y modu³ modu³ konwertuje dane na przyjemny tekst base64, który
mo¿na zapisaæ w pliku tekstowym, wys³aæ poczt± elektroniczn±, zapisaæ
w ciasteczku lub na stronie WWW, albo przesy³aæ przez sieæ.
Zaszyfrowane dane mog± byæ dowolnie proste lub skomplikowane.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/Crypt/Simple.pm
%{_mandir}/man3/*
