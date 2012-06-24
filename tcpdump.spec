Summary:	dumps packets that are sent or received over a network interface
Summary(de):	deponiert Pakete, die �ber eine Netzwerkschnittstelle gesandt oder empfangen werden 
Summary(fr):	vide les paquets �mis ou re�us sur une interface r�seau
Summary(pl):	Pokazuje pakiety przechodz�ce przez inerfejsy sieciowe
Summary(tr):	Bir a� arabirimi �zerinden gelen ya da giden paketleri listeler
Name:		tcpdump
Version:	3.4
Release:	17
Copyright:	BSD
Group:		Applications/Networking
Group(pl):	Aplikacje/Sieciowe
Source0:	ftp://ftp.ee.lbl.gov//%{name}-%{version}.tar.Z
Patch0:         ftp://ftp.inr.ac.ru/ip-routing/lbl-tools/tcpdump-3.4-ss990523.dif.gz
Patch1:		tcpdump-glibc2.1.patch
Patch2:		tcpdump-make.patch
Patch3:		tcpdump-giop.patch
Patch4:		tcpdump-iphl.patch
Patch5:		tcpdump-sparc64.patch
BuildRequires:	libpcap-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Tcpdump prints out the headers of packets on a network interface.  It
is very useful for debugging network problems and security operations.

%description -l de
Tcpdump druckt die Headers von Paketen auf einer Netzschnittstelle. 
Es ist �beraus n�tzlich zum Debuggen von Netzwerkproblemen und von
Sicherheitsoperationen.

%description -l fr
tcpdump affiche les en-t�tes des paquets d'une interface r�seau. Il est
tr�s utile pour d�tecter les probl�mes de r�seau et de s�curit�.

%description -l pl
Tcpdump s�u�y do analizy pakiet�w przechodz�cych przez interfejscy
sieciowe, jest u�ytecznym narz�dziem do �ledzenia ruchu w sieci.

%description -l tr
Tcpdump, bir a� arabirimi �zerinden ge�en paketlerin ba�l�klar�n� d�ker.
G�venlik i�lemleri ve a� problemlerinin irdelenmesi konular�nda son derece
yararl�d�r.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
CFLAGS="$RPM_OPT_FLAGS -DIP_MAX_MEMBERSHIPS=20"
LDFLAGS="-s"
export CFLAGS LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man1}

make install install-man DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/tcpdump
%{_mandir}/man1/*
