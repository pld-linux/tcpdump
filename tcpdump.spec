Summary:	dumps packets that are sent or received over a network interface
Summary(de):	deponiert Pakete, die über eine Netzwerkschnittstelle gesandt oder empfangen werden 
Summary(es):	Enseña los paquetes que son enviados o recibidos a través de una interface de red
Summary(fr):	vide les paquets émis ou reçus sur une interface réseau
Summary(pl):	Pokazuje pakiety przechodz±ce przez interfejsy sieciowe
Summary(pt_BR):	Mostra os pacotes que são enviados ou recebidos através de uma interface de rede
Summary(tr):	Bir að arabirimi üzerinden gelen ya da giden paketleri listeler
Name:		tcpdump
Version:	3.7.1
Release:	1
Epoch:		1
License:	BSD
Group:		Applications/Networking
Source0:	http://www.tcpdump.org/release/%{name}-%{version}.tar.gz
URL:		http://www.tcpdump.org/
Patch0:		%{name}-ssl.patch
Patch1:		%{name}-no-libsmi.patch
BuildRequires:	libpcap-devel >= 2:0.6.1
%{!?_without_libsmi:BuildRequires:	libsmi-devel}
BuildRequires:	openssl-devel >= 0.9.6a
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tcpdump prints out the headers of packets on a network interface. It
is very useful for debugging network problems and security operations.

%description -l de
Tcpdump druckt die Headers von Paketen auf einer Netzschnittstelle. Es
ist überaus nützlich zum Debuggen von Netzwerkproblemen und von
Sicherheitsoperationen.

%description -l es
Tcpdump imprime los encabezamientos de los paquetes en una interface
de red. Es muy práctico para solucionar problemas en la red y para
operaciones de seguridad.

%description -l fr
tcpdump affiche les en-têtes des paquets d'une interface réseau. Il
est très utile pour détecter les problèmes de réseau et de sécurité.

%description -l pl
Tcpdump s³u¿y do analizy pakietów przechodz±cych przez interfejsy
sieciowe, jest u¿ytecznym narzêdziem do ¶ledzenia ruchu w sieci.

%description -l pt_BR
Tcpdump imprime os cabeçalhos dos pacotes em uma interface de rede.
Ele é muito prático para resolver problemas na rede e para operações
de segurança.

%description -l tr
Tcpdump, bir að arabirimi üzerinden geçen paketlerin baþlýklarýný
döker. Güvenlik iþlemleri ve að problemlerinin irdelenmesi konularýnda
son derece yararlýdýr.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%{!?_without_libsmi:#}%patch1 -p1

%build
%configure2_13 \
	--enable-ipv6
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man1}

%{__make}  \
	DESTDIR=$RPM_BUILD_ROOT \
	install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/tcpdump
%{_mandir}/man1/*
