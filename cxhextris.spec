Summary:	An X Window System color version of xhextris
Summary(de):	Farbige X11-Version von Hextris
Summary(fr):	Version X11 en couleurs d'hextris
Summary(pl):	Kolorowa wersja gry xhextris pod X Window
Summary(tr):	Düþen bloklarý yerleþtirme oyunu
Name:		cxhextris
Version:	1.0
Release:	22
Copyright:	distributable
Group:		X11/Games
Group(pl):	X11/Gry
Source0:	ftp://sunsite.unc.edu/pub/Linux/games/arcade/tetris/%{name}.tar.z
Source1:	cxhextris.desktop
Source2:	cxhextris.png
Patch0:		cxhextris-config.patch
Patch1:		cxhextris-axp.patch
Patch2:		cxhextris-security.patch
Icon:		cxhextris.xpm
Prereq:		/usr/X11R6/bin/mkfontdir
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
CXHextris is a color version of the popular xhextris game, which is a
Tetris-like game that uses hexagon shapes instead of square shapes.
CXHextris runs within the X Window System.

Install cxhextris if you enjoy playing Tetris or Tetris-like games and
you'd like to play one on your system. You'll need to have X installed
in order to play CXHextris.

%description -l de
cxhextrix ist eine Farbversion des populären hextris, beides nahe
Verwandte des klassischen T*tris Video-Games, bei dem unregelmäßig
geformte Blöcke perfekt aufeinander gestapelt werden müssen.
Voraussetzung ist, daß X-Windows korrekt funktioniert.

%description -l fr
cxhextrix est une version en couleurs du célèbre hextris. Tous deux
sont des clones du célèbre jeu vidéo T*tris, où l'on doit essayer
d'empiler parfaitement des blocs avec des formes curieuses. Ce jeu
nécessite X Window pour fonctionner correctement.

%description -l pl
CXHextris jest kolorow± wersj± popularnej gry xhextris, bêd±cej klonem
Tetrisa u¿ywaj±cym sze¶ciobocznych figur zamiast kwadratowych.
CXHextris uruchamia siê w ¶rodowisku X Window.

Nale¿y zainstalowaæ CXHextris je¶li lubi siê gry w rodzaju Tetris. Aby
móc graæ w CXHextris nale¿y mieæ zainstalowane X Window.

%description -l tr
cxhextrix, hextris'in renkli sürümüdür. Her ikisi de, garip þekilli
bloklarýn - arada boþluk býrakýlmadan - bir yýðýn haline getirilmeye
çalýþýldýðý Tetris oyununa benzer.

%prep
%setup -q -n cxhextris
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
xmkmf
%{__make} CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/usr/share/fonts/misc,%{_applnkdir}/Games,%{_datadir}/pixmaps}

%{__make} DESTDIR=$RPM_BUILD_ROOT install install.man

%{__make} FONTDIR=$RPM_BUILD_ROOT/usr/share/fonts install.font

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps

gzip -9nf README README.Linux

%clean
rm -rf $RPM_BUILD_ROOT

%post
(cd /usr/share/fonts/misc; /usr/X11R6/bin/mkfontdir)

%postun
(cd /usr/share/fonts/misc; /usr/X11R6/bin/mkfontdir)

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(2755,root,games) %{_bindir}/xhextris
/usr/share/fonts/misc/hex20.pcf
%attr(664,root,games) /var/lib/games/xhextris-scores
%{_applnkdir}/Games/*
%{_datadir}/pixmaps/*
