%include	/usr/lib/rpm/macros.php
%define         _class          Net
%define         _subclass       Server
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Generic server class
Summary(pl):	%{_pearname} - og�lna klasa serwerowa
Name:		php-pear-%{_pearname}
Version:	0.9
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	46449d01e6af73aa2409bbb648484e4c
URL:		http://pear.php.net/package/Net_Server/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Generic server class based on ext/sockets, used to develop any kind of
server.

This class has in PEAR status: %{_status}.

%description -l pl
Og�lna klasa serwerowa oparta na ext/sockets, s�u��ca do tworzenia
serwer�w dowolnego rodzaju.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
