Summary:	An X Window System color version of xhextris
Summary(de):	Farbige X11-Version von Hextris
Summary(fr):	Version X11 en couleurs d'hextris
Summary(pl):	Kolorowa wersja gry xhextris pod X Window
Summary(ru):	Цветная версия hextris для X11
Summary(tr):	DЭЧen bloklarЩ yerleЧtirme oyunu
Summary(uk):	Кольорова верс╕я hextris для X11
Name:		cxhextris
Version:	1.0
Release:	26
License:	distributable
Group:		X11/Applications/Games
Source0:	ftp://sunsite.unc.edu/pub/Linux/games/arcade/tetris/%{name}.tar.z
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-config.patch
Patch1:		%{name}-axp.patch
Patch2:		%{name}-security.patch
Icon:		cxhextris.xpm
BuildRequires:	XFree86-devel
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CXHextris is a color version of the popular xhextris game, which is a
Tetris-like game that uses hexagon shapes instead of square shapes.
CXHextris runs within the X Window System.

Install cxhextris if you enjoy playing Tetris or Tetris-like games and
you'd like to play one on your system. You'll need to have X installed
in order to play CXHextris.

%description -l de
cxhextrix ist eine Farbversion des populДren hextris, beides nahe
Verwandte des klassischen T*tris Video-Games, bei dem unregelmДъig
geformte BlЖcke perfekt aufeinander gestapelt werden mЭssen.
Voraussetzung ist, daъ X-Window korrekt funktioniert.

%description -l fr
cxhextrix est une version en couleurs du cИlХbre hextris. Tous deux
sont des clones du cИlХbre jeu vidИo T*tris, oЫ l'on doit essayer
d'empiler parfaitement des blocs avec des formes curieuses. Ce jeu
nИcessite X Window pour fonctionner correctement.

%description -l pl
CXHextris jest kolorow╠ wersj╠ popularnej gry xhextris, bЙd╠cej klonem
Tetrisa u©ywaj╠cym sze╤ciobocznych figur zamiast kwadratowych.
CXHextris uruchamia siЙ w ╤rodowisku X Window.

Nale©y zainstalowaФ CXHextris je╤li lubi siЙ gry w rodzaju Tetris. Aby
mСc graФ w CXHextris nale©y mieФ zainstalowane X Window.

%description -l ru
CXHextris - это цветная версия популярной игры xhextris, которая
является Tetris-подобной игрой, использующей шестиугольники вместо
квадратов. Эта игра требует для своей работы X Window.

%description -l tr
cxhextrix, hextris'in renkli sЭrЭmЭdЭr. Her ikisi de, garip Чekilli
bloklarЩn - arada boЧluk bЩrakЩlmadan - bir yЩПЩn haline getirilmeye
ГalЩЧЩldЩПЩ Tetris oyununa benzer.

%description -l uk
CXHextris - це кольорова верс╕я популярно╖ гри xhextris, яка под╕бна
до Tetris, але використову╓ шестикутники зам╕сть квадрат╕в. Ця гра
потребу╓ X Window.

%prep
%setup -q -n cxhextris
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
xmkmf
%{__make} \
	CC="%{__cc}" \
	CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/usr/share/fonts/misc,%{_desktopdir},%{_pixmapsdir}}

%{__make} install install.man \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir}/man1 \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} install.font \
	FONTDIR=$RPM_BUILD_ROOT%{_fontsdir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst misc

%postun
fontpostinst misc

%files
%defattr(644,root,root,755)
%doc README README.Linux
%attr(2755,root,games) %{_bindir}/xhextris
%{_fontsdir}/misc/hex20.pcf
%attr(664,root,games) %config(noreplace) %verify(not size mtime md5) /var/games/xhextris-scores
%{_mandir}/man1/xhextris.1*
%{_desktopdir}/*
%{_pixmapsdir}/*
