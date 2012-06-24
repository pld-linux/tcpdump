#
# Conditional build:
%bcond_without	libsmi	# Build without SMI support
#
Summary:	dumps packets that are sent or received over a network interface
Summary(de):	deponiert Pakete, die �ber eine Netzwerkschnittstelle gesandt oder empfangen werden
Summary(es):	Ense�a los paquetes que son enviados o recibidos a trav�s de una interface de red
Summary(fr):	vide les paquets �mis ou re�us sur une interface r�seau
Summary(pl):	Pokazuje pakiety przechodz�ce przez interfejsy sieciowe
Summary(pt_BR):	Mostra os pacotes que s�o enviados ou recebidos atrav�s de uma interface de rede
Summary(ru):	���������� ��� ����������� �������� ��������
Summary(tr):	Bir a� arabirimi �zerinden gelen ya da giden paketleri listeler
Summary(uk):	���������� ��� ��Φ������� ���������� ���Ʀ��
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
ist �beraus n�tzlich zum Debuggen von Netzwerkproblemen und von
Sicherheitsoperationen.

%description -l es
Tcpdump imprime los encabezamientos de los paquetes en una interface
de red. Es muy pr�ctico para solucionar problemas en la red y para
operaciones de seguridad.

%description -l fr
tcpdump affiche les en-t�tes des paquets d'une interface r�seau. Il
est tr�s utile pour d�tecter les probl�mes de r�seau et de s�curit�.

%description -l pl
Tcpdump s�u�y do analizy pakiet�w przechodz�cych przez interfejsy
sieciowe, jest u�ytecznym narz�dziem do �ledzenia ruchu w sieci.

%description -l pt_BR
Tcpdump imprime os cabe�alhos dos pacotes em uma interface de rede.
Ele � muito pr�tico para resolver problemas na rede e para opera��es
de seguran�a.

%description -l ru
Tcpdump ������� ������ �������, ���������� ����� ������� ���������.
��������� ��� ����������� ������� ������� � ��������� ������������.

%description -l tr
Tcpdump, bir a� arabirimi �zerinden ge�en paketlerin ba�l�klar�n�
d�ker. G�venlik i�lemleri ve a� problemlerinin irdelenmesi konular�nda
son derece yararl�d�r.

%description -l uk
Tcpdump �������� ������ ����Ԧ�, �� ��������� ����� ����������
���������. ����ͦ���� ��� Ħ��������� ���������� ������� �� ��������
�������.

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
