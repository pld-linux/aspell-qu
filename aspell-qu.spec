Summary:	Quechua dictionary for aspell
Summary(pl.UTF-8):	Słownik keczuański dla aspella
Name:		aspell-qu
Version:	0.02
%define	subv	0
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/qu/aspell6-qu-%{version}-%{subv}.tar.bz2
# Source0-md5:	b1c4a68fd5f46cadb600d925b0764fa5
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quechua dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik keczuański (lista słów) dla aspella.

%prep
%setup -q -n aspell6-qu-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
