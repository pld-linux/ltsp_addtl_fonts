%define		_arch	i386
%define		_pver	4.1

Summary:	Linux Terminal Server Project - 100dpi fonts for terminals
Summary(pl.UTF-8):	Fonty 100dpi dla terminali z Linux Terminal Server Project
Name:		ltsp_addtl_fonts
Version:	4.0.1
Release:	0.1
License:	GPL
Group:		Applications/Networking
Source0:	http://www.ltsp.org/ltsp-utils-0.11.tgz
# Source0-md5:	b17b350b18b04d769fcadcd12885a573
Source1:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-x-fonts-100dpi-1.5-0-%{_arch}.tgz
# Source1-md5:	47207226af590f3e58eea16a6c7c2a04
URL:		http://www.ltsp.org/
Requires:	ltsp_core
AutoProv:	0
AutoReq:	0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ltspdir	/home/services/ltsp

%description
LTSP is an add-on package for Linux that allows you to connect lots of
low-powered thin client terminals to a Linux server. Applications
typically run on the server and accept input and display their output
on the thin client display. LTSP is available as a set of packages that
can be installed on any Linux system.

This package contains 100dpi fonts for LTSP terminals.

%description -l pl.UTF-8
LTSP to dodatkowy pakiet dla Linuksa pozwalający na podłączenie wielu
cienkich klientów jako terminali do serwera linuksowego. Aplikacje
zwykle działają na serwerze i przyjmują wejście oraz wyświetlają
wyjście na wyświetlaczach cienkich klientów. LTSP jest dostępny jako
zestaw pakietów, które można zainstalować na dowolnym systemie
linuksowym.

Ten pakiet zawiera czcionki 100dpi dla terminali LTSP.

%prep
%setup -q -n ltsp-utils

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_ltspdir}
tar zxf %{SOURCE1}
cd i386
cp -r usr $RPM_BUILD_ROOT%{_ltspdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc README
%dir %{_ltspdir}
%{_ltspdir}/usr/X11R6/lib/X11/fonts/100dpi
