#
# Conditional build:
%bcond_without	libsmi	# Build without SMI support
#
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
Version:	3.8.1
Release:	1
Epoch:		1
License:	BSD
Group:		Applications/Networking
Source0:	http://www.tcpdump.org/release/%{name}-%{version}.tar.gz
# Source0-md5:	9edcf0d7f526f0f03138286959ccc802
URL:		http://www.tcpdump.org/
BuildRequires:	libpcap-devel >= 2:0.6.1
%{?with_libsmi:BuildRequires:	libsmi-devel}
BuildRequires:	openssl-devel >= 0.9.7c
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
# -c because of "tar: Removing leading `libpcap-0.8.1/./' from member names"
%setup -q -c

%build
# tar < 1.13.9x compat
[ -f configure ] || cd %{name}-%{version}
%configure2_13 \
	--enable-ipv6
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
if [ ! -f configure ]; then
	mv -f %{name}-%{version}/{CHANGES,CREDITS,LICENSE,README,TODO}
	cd %{name}-%{version}
fi

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS LICENSE README TODO
%attr(755,root,root) %{_sbindir}/tcpdump
%{_mandir}/man1/*
