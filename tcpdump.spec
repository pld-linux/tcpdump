Summary:	dumps packets that are sent or received over a network interface
Summary(de):	deponiert Pakete, die über eine Netzwerkschnittstelle gesandt oder empfangen werden 
Summary(fr):	vide les paquets émis ou reçus sur une interface réseau
Summary(pl):	Pokazuje pakiety przechodz±ce przez inerfejsy sieciowe
Summary(tr):	Bir að arabirimi üzerinden gelen ya da giden paketleri listeler
Name:		tcpdump
Version:	cvs20001101
Release:	1
License:	BSD
Epoch:		1
Group:		Applications/Networking
Group(pl):	Aplikacje/Sieciowe
Source0:	cvs://tcpdump@cvs.tcpdump.org/tcpdump/master/%{name}-%{version}.tar.gz
Patch0:		tcpdump-ssl.patch
BuildRequires:	libpcap-devel >= cvs20001101
BuildConflicts:	libsmi-devel
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tcpdump prints out the headers of packets on a network interface. It
is very useful for debugging network problems and security operations.

%description -l de
Tcpdump druckt die Headers von Paketen auf einer Netzschnittstelle. Es
ist überaus nützlich zum Debuggen von Netzwerkproblemen und von
Sicherheitsoperationen.

%description -l fr
tcpdump affiche les en-têtes des paquets d'une interface réseau. Il
est très utile pour détecter les problèmes de réseau et de sécurité.

%description -l pl
Tcpdump s³u¿y do analizy pakietów przechodz±cych przez interfejscy
sieciowe, jest u¿ytecznym narzêdziem do ¶ledzenia ruchu w sieci.

%description -l tr
Tcpdump, bir að arabirimi üzerinden geçen paketlerin baþlýklarýný
döker. Güvenlik iþlemleri ve að problemlerinin irdelenmesi konularýnda
son derece yararlýdýr.

%prep
%setup -q
%patch0 -p1

%build
autoconf
CFLAGS="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O -g}"
%configure \
	--enable-ipv6
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man1}

%{__make}  \
	DESTDIR=$RPM_BUILD_ROOT \
	install

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/tcpdump
%{_mandir}/man1/*
