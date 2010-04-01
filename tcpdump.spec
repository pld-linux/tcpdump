#
# Conditional build:
%bcond_without	libsmi	# Build without SMI support
#
Summary:	dumps packets that are sent or received over a network interface
Summary(de.UTF-8):	deponiert Pakete, die über eine Netzwerkschnittstelle gesandt oder empfangen werden
Summary(es.UTF-8):	Enseña los paquetes que son enviados o recibidos a través de una interface de red
Summary(fr.UTF-8):	vide les paquets émis ou reçus sur une interface réseau
Summary(pl.UTF-8):	Pokazuje pakiety przechodzące przez interfejsy sieciowe
Summary(pt_BR.UTF-8):	Mostra os pacotes que são enviados ou recebidos através de uma interface de rede
Summary(ru.UTF-8):	Инструмент для мониторинга сетевого траффика
Summary(tr.UTF-8):	Bir ağ arabirimi üzerinden gelen ya da giden paketleri listeler
Summary(uk.UTF-8):	Інструмент для моніторингу мережевого трафіку
Name:		tcpdump
Version:	4.1.0
Release:	1
Epoch:		1
License:	BSD
Group:		Applications/Networking
Source0:	http://www.tcpdump.org/release/%{name}-%{version}.tar.gz
# Source0-md5:	949d4661a7501cfedf7b1eb858302c9c
URL:		http://www.tcpdump.org/
BuildRequires:	automake
BuildRequires:	libpcap-devel >= 2:1.1.0
%{?with_libsmi:BuildRequires:	libsmi-devel}
BuildRequires:	openssl-devel >= 0.9.7d
Requires:	libpcap >= 2:1.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tcpdump prints out the headers of packets on a network interface. It
is very useful for debugging network problems and security operations.

%description -l de.UTF-8
Tcpdump druckt die Headers von Paketen auf einer Netzschnittstelle. Es
ist überaus nützlich zum Debuggen von Netzwerkproblemen und von
Sicherheitsoperationen.

%description -l es.UTF-8
Tcpdump imprime los encabezamientos de los paquetes en una interface
de red. Es muy práctico para solucionar problemas en la red y para
operaciones de seguridad.

%description -l fr.UTF-8
tcpdump affiche les en-têtes des paquets d'une interface réseau. Il
est très utile pour détecter les problèmes de réseau et de sécurité.

%description -l pl.UTF-8
Tcpdump służy do analizy pakietów przechodzących przez interfejsy
sieciowe, jest użytecznym narzędziem do śledzenia ruchu w sieci.

%description -l pt_BR.UTF-8
Tcpdump imprime os cabeçalhos dos pacotes em uma interface de rede.
Ele é muito prático para resolver problemas na rede e para operações
de segurança.

%description -l ru.UTF-8
Tcpdump выводит хедеры пакетов, проходящих через сетевой интерфейс.
Незаменим для диагностики сетевых проблем и нарушений безопасности.

%description -l tr.UTF-8
Tcpdump, bir ağ arabirimi üzerinden geçen paketlerin başlıklarını
döker. Güvenlik işlemleri ve ağ problemlerinin irdelenmesi konularında
son derece yararlıdır.

%description -l uk.UTF-8
Tcpdump виводить хедери пакетів, що проходять через мереживний
інтерфейс. Незамінний для діагностики мереживних проблем та порушень
безпеки.

%prep
%setup -q -n %{name}-4.1

%build
cp -f /usr/share/automake/config.* .
%configure \
	--enable-ipv6
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS LICENSE README
%attr(755,root,root) %{_sbindir}/tcpdump
%{_mandir}/man1/*
