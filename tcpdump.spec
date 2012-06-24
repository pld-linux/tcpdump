Summary:	dumps packets that are sent or received over a network interface
Summary(de):	deponiert Pakete, die �ber eine Netzwerkschnittstelle gesandt oder empfangen werden 
Summary(fr):	vide les paquets �mis ou re�us sur une interface r�seau
Summary(pl):	Pokazuje pakiety przechodz�ce przez inerfejsy sieciowe
Summary(tr):	Bir a� arabirimi �zerinden gelen ya da giden paketleri listeler
Name:		tcpdump
Version:	3.6.2
Release:	2
Epoch:		1
License:	BSD
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
Source0:	http://www.tcpdump.org/release/%{name}-%{version}.tar.gz
Patch0:		%{name}-ssl.patch
Patch1:		%{name}-no-libsmi.patch
BuildRequires:	libpcap-devel >= 2:0.6.1
%{!?bcond_off_libsmi:BuildRequires:	libsmi-devel}
BuildRequires:	openssl-devel >= 0.9.6a
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tcpdump prints out the headers of packets on a network interface. It
is very useful for debugging network problems and security operations.

%description -l de
Tcpdump druckt die Headers von Paketen auf einer Netzschnittstelle. Es
ist �beraus n�tzlich zum Debuggen von Netzwerkproblemen und von
Sicherheitsoperationen.

%description -l fr
tcpdump affiche les en-t�tes des paquets d'une interface r�seau. Il
est tr�s utile pour d�tecter les probl�mes de r�seau et de s�curit�.

%description -l pl
Tcpdump s�u�y do analizy pakiet�w przechodz�cych przez interfejscy
sieciowe, jest u�ytecznym narz�dziem do �ledzenia ruchu w sieci.

%description -l tr
Tcpdump, bir a� arabirimi �zerinden ge�en paketlerin ba�l�klar�n�
d�ker. G�venlik i�lemleri ve a� problemlerinin irdelenmesi konular�nda
son derece yararl�d�r.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%{!?bcond_off_libsmi:#}%patch1 -p1

%build
autoconf
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
