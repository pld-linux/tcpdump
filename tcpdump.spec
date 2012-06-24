Summary:	dumps packets that are sent or received over a network interface
Summary(de):	deponiert Pakete, die �ber eine Netzwerkschnittstelle gesandt oder empfangen werden 
Summary(fr):	vide les paquets �mis ou re�us sur une interface r�seau
Summary(pl):	Pokazuje pakiety przechodz�ce przez inerfejsy sieciowe
Summary(tr):	Bir a� arabirimi �zerinden gelen ya da giden paketleri listeler
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

%changelog
* Sat Jul 03 1999 PLD Team <pld-list@pld.org.pl>
- new commenting style:

  $Log: tcpdump.spec,v $
  Revision 1.8  1999-07-09 16:22:14  kloczek

  - added line on top spec file with cvs tags ($Revision:$ and $Date:$).

  Revision 1.7  1999/07/03 17:06:12  misiek
  updated to 3.4. IPv6 patches replaced by ANK patches


* Wed Jun 23 1999 Micha� Kuratczyk <kura@pld.org.pl>
  [3.4a6-2]
- gzipping documentation instead bzipping
- added Group(pl)
- more RPM macros
- added using %configure

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
