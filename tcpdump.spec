Summary:	dumps packets that are sent or received over a network interface
Summary(de):	deponiert Pakete, die über eine Netzwerkschnittstelle gesandt oder empfangen werden 
Summary(fr):	vide les paquets émis ou reçus sur une interface réseau
Summary(pl):	Pokazuje pakiety przechodz±ce przez inerfejsy sieciowe
Summary(tr):	Bir að arabirimi üzerinden gelen ya da giden paketleri listeler
Name:		tcpdump
Version:	3.4
Release:	1
Copyright:	BSD
Group:		Applications/Networking
Group(pl):	Aplikacje/Sieciowe
Source0:	ftp://ftp.ee.lbl.gov//%{name}-%{version}.tar.Z
Patch0:         ftp://ftp.inr.ac.ru/ip-routing/lbl-tools/tcpdump-3.4-ss990523.dif.gz
Patch1:		tcpdump-glibc2.1.patch
BuildPrereq:	libpcap
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Tcpdump prints out the headers of packets on a network interface.  It
is very useful for debugging network problems and security operations.

%description -l de
Tcpdump druckt die Headers von Paketen auf einer Netzschnittstelle. 
Es ist überaus nützlich zum Debuggen von Netzwerkproblemen und von
Sicherheitsoperationen.

%description -l fr
tcpdump affiche les en-têtes des paquets d'une interface réseau. Il est
très utile pour détecter les problèmes de réseau et de sécurité.

%description -l pl
Tcpdump s³u¿y do analizy pakietów przechodz±cych przez interfejscy
sieciowe, jest u¿ytecznym narzêdziem do ¶ledzenia ruchu w sieci.

%description -l tr
Tcpdump, bir að arabirimi üzerinden geçen paketlerin baþlýklarýný döker.
Güvenlik iþlemleri ve að problemlerinin irdelenmesi konularýnda son derece
yararlýdýr.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure
CFLAGS="$RPM_OPT_FLAGS -DIP_MAX_MEMBERSHIPS=20" \
	./configure --prefix=%{_prefix} \
		    --mandir=%{_mandir}
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install -s tcpdump $RPM_BUILD_ROOT%{_sbindir}
install tcpdump.1 $RPM_BUILD_ROOT%{_mandir}/man8/tcpdump.8

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man8/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/tcpdump
%{_mandir}/man8/*
