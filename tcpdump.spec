Summary:	dumps packets that are sent or received over a network interface
Summary(de):	deponiert Pakete, die Эber eine Netzwerkschnittstelle gesandt oder empfangen werden
Summary(es):	EnseЯa los paquetes que son enviados o recibidos a travИs de una interface de red
Summary(fr):	vide les paquets Иmis ou reГus sur une interface rИseau
Summary(pl):	Pokazuje pakiety przechodz╠ce przez interfejsy sieciowe
Summary(pt_BR):	Mostra os pacotes que sЦo enviados ou recebidos atravИs de uma interface de rede
Summary(ru):	Инструмент для мониторинга сетевого траффика
Summary(tr):	Bir aП arabirimi Эzerinden gelen ya da giden paketleri listeler
Summary(uk):	╤нструмент для мон╕торингу мережевого траф╕ку
Name:		tcpdump
Version:	3.7.1
Release:	2
Epoch:		1
License:	BSD
Group:		Applications/Networking
Source0:	http://www.tcpdump.org/release/%{name}-%{version}.tar.gz
URL:		http://www.tcpdump.org/
Patch0:		%{name}-ssl.patch
Patch1:		%{name}-no-libsmi.patch
Patch2:		%{name}-snaplen.patch
BuildRequires:	libpcap-devel >= 2:0.6.1
%{!?_without_libsmi:BuildRequires:	libsmi-devel}
BuildRequires:	openssl-devel >= 0.9.6a
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tcpdump prints out the headers of packets on a network interface. It
is very useful for debugging network problems and security operations.

%description -l de
Tcpdump druckt die Headers von Paketen auf einer Netzschnittstelle. Es
ist Эberaus nЭtzlich zum Debuggen von Netzwerkproblemen und von
Sicherheitsoperationen.

%description -l es
Tcpdump imprime los encabezamientos de los paquetes en una interface
de red. Es muy prАctico para solucionar problemas en la red y para
operaciones de seguridad.

%description -l fr
tcpdump affiche les en-tЙtes des paquets d'une interface rИseau. Il
est trХs utile pour dИtecter les problХmes de rИseau et de sИcuritИ.

%description -l pl
Tcpdump sЁu©y do analizy pakietСw przechodz╠cych przez interfejsy
sieciowe, jest u©ytecznym narzЙdziem do ╤ledzenia ruchu w sieci.

%description -l pt_BR
Tcpdump imprime os cabeГalhos dos pacotes em uma interface de rede.
Ele И muito prАtico para resolver problemas na rede e para operaГУes
de seguranГa.

%description -l ru
Tcpdump выводит хедеры пакетов, проходящих через сетевой интерфейс.
Незаменим для диагностики сетевых проблем и нарушений безопасности.

%description -l tr
Tcpdump, bir aП arabirimi Эzerinden geГen paketlerin baЧlЩklarЩnЩ
dЖker. GЭvenlik iЧlemleri ve aП problemlerinin irdelenmesi konularЩnda
son derece yararlЩdЩr.

%description -l uk
Tcpdump виводить хедери пакет╕в, що проходять через мереживний
╕нтерфейс. Незам╕нний для д╕агностики мереживних проблем та порушень
безпеки.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%{!?_without_libsmi:#}%patch1 -p1
%patch2 -p1

%build
%configure2_13 \
	--enable-ipv6
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/tcpdump
%{_mandir}/man1/*
