%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	Server
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - generic server class
Summary(pl):	%{_pearname} - ogólna klasa serwerowa
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	d7e6c9291fc5b60127fa9f3b7667b741
URL:		http://pear.php.net/package/Net_Server/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
Requires:	php-pear-PEAR-core
Requires:	php-sockets
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Generic server class based on ext/sockets, used to develop any kind of
server.

In PEAR status of this package is: %{_status}.

%description -l pl
Ogólna klasa serwerowa oparta na ext/sockets, s³u¿±ca do tworzenia
serwerów dowolnego rodzaju.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/{docs,examples}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
