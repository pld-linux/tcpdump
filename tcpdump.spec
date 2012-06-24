Summary:     dumps packets that are sent or received over a network interface
Summary(de): deponiert Pakete, die �ber eine Netzwerkschnittstelle gesandt oder empfangen werden  
Summary(fr): vide les paquets �mis ou re�us sur une interface r�seau
Summary(pl): Pokazuje pakiety przechodz�ce przez inerfejsy sieciowe
Summary(tr): Bir a� arabirimi �zerinden gelen ya da giden paketleri listeler
Name:        tcpdump
Version:     3.4a6
Release:     1d
Copyright:   BSD
Group:       Applications/Networking
Source0:     ftp://ftp.inner.net/pub/ipv6/%{name}-%{version}+ipv6-1.tar.gz
Source1:     ftp://ftp.inner.net/pub/ipv6/libpcap-0.4a6+ipv6-1.tar.gz
Patch0:      tcpdump.patch
Patch1:      libcap.patch
Patch2:      GNUmakefile.patch
Patch3:      Makefile.patch
Patch4:      pcap.so_attach_filter.patch
Buildroot:   /tmp/%{name}-%{version}-root

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
%setup -q -c -a 1

cd %{name}-%{version}
%patch -p1
%patch2 -p1
cd ..

%build
cd libpcap-0.4a6

patch -p2 < $RPM_SOURCE_DIR/libcap.patch
patch -p1 < $RPM_SOURCE_DIR/Makefile.patch
patch -p1 < $RPM_SOURCE_DIR/pcap.so_attach_filter.patch

CFLAGS=$RPM_OPT_FLAGS ./configure --prefix=/usr
make
cd ..

cd tcpdump-3.4a6
CFLAGS="$RPM_OPT_FLAGS -DIP_MAX_MEMBERSHIPS=20" ./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/{sbin,man/man8}

cd tcpdump-3.4a6
install -s tcpdump $RPM_BUILD_ROOT/usr/sbin
install tcpdump.1 $RPM_BUILD_ROOT%{_mandir}/man8/tcpdump.8

bzip2 -9 $RPM_BUILD_ROOT%{_mandir}/man8/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /usr/sbin/tcpdump
%{_mandir}/man8/*

%changelog
* Tue Jul 2 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [3.4a6-1d]
- build against glibc-2.1,
- added IPv6 support,
- updatet to relase 3.4a6,
- translation modified for pl,
- changed permission of tcpdump to 711,
- moved %changelog at the end of spec.

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sat May  2 1998 Alan Cox <alan@rehat.com>
- Added the SACK printing fix so you can dump Linux 2.1+.

* Tue Oct 21 1997 Erik Troan <ewt@redhat.com>
- updated to release 3.4a5
- uses a buildroot and %attr 

* Thu Jul 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc
