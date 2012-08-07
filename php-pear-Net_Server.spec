%define		status		stable
%define		pearname	Net_Server
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - generic server class
Summary(pl.UTF-8):	%{pearname} - ogólna klasa serwerowa
Name:		php-pear-%{pearname}
Version:	1.0.3
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	46809888cb27e14fdc88ed2f388807cc
URL:		http://pear.php.net/package/Net_Server/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php(sockets)
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
Requires:	php-pear-PEAR-core >= 1:1.4.0-0.b1
Suggests:	php-pcntl
Suggests:	php-pear-PHP_Fork
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	pear(PHP/Fork.*)

%description
Generic server class based on ext/sockets, used to develop any kind of
server.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Ogólna klasa serwerowa oparta na ext/sockets, służąca do tworzenia
serwerów dowolnego rodzaju.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

mv .%{php_pear_dir}/data/Net_Server/README .
mv docs/%{pearname}/examples .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc README
%doc install.log optional-packages.txt
%doc docs/%{pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Net/Server.php
%{php_pear_dir}/Net/Server
%{_examplesdir}/%{name}-%{version}
