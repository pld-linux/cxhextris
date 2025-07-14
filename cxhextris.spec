Summary:	An X Window System color version of xhextris
Summary(de.UTF-8):	Farbige X11-Version von Hextris
Summary(fr.UTF-8):	Version X11 en couleurs d'hextris
Summary(pl.UTF-8):	Kolorowa wersja gry xhextris pod X Window
Summary(ru.UTF-8):	Цветная версия hextris для X11
Summary(tr.UTF-8):	Düşen blokları yerleştirme oyunu
Summary(uk.UTF-8):	Кольорова версія hextris для X11
Name:		cxhextris
Version:	1.0
Release:	29
License:	distributable
Group:		X11/Applications/Games
Source0:	ftp://sunsite.unc.edu/pub/Linux/games/arcade/tetris/%{name}.tar.z
# Source0-md5:	64fce30ebb859bcce0ff4f91f4ece0a8
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-config.patch
Patch1:		%{name}-axp.patch
Patch2:		%{name}-security.patch
BuildRequires:	xorg-cf-files
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-util-imake
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

%description -l de.UTF-8
cxhextrix ist eine Farbversion des populären hextris, beides nahe
Verwandte des klassischen T*tris Video-Games, bei dem unregelmäßig
geformte Blöcke perfekt aufeinander gestapelt werden müssen.
Voraussetzung ist, daß X-Window korrekt funktioniert.

%description -l fr.UTF-8
cxhextrix est une version en couleurs du célèbre hextris. Tous deux
sont des clones du célèbre jeu vidéo T*tris, où l'on doit essayer
d'empiler parfaitement des blocs avec des formes curieuses. Ce jeu
nécessite X Window pour fonctionner correctement.

%description -l pl.UTF-8
CXHextris jest kolorową wersją popularnej gry xhextris, będącej klonem
Tetrisa używającym sześciobocznych figur zamiast kwadratowych.
CXHextris uruchamia się w środowisku X Window.

Należy zainstalować CXHextris jeśli lubi się gry w rodzaju Tetris. Aby
móc grać w CXHextris należy mieć zainstalowane X Window.

%description -l ru.UTF-8
CXHextris - это цветная версия популярной игры xhextris, которая
является Tetris-подобной игрой, использующей шестиугольники вместо
квадратов. Эта игра требует для своей работы X Window.

%description -l tr.UTF-8
cxhextrix, hextris'in renkli sürümüdür. Her ikisi de, garip şekilli
blokların - arada boşluk bırakılmadan - bir yığın haline getirilmeye
çalışıldığı Tetris oyununa benzer.

%description -l uk.UTF-8
CXHextris - це кольорова версія популярної гри xhextris, яка подібна
до Tetris, але використовує шестикутники замість квадратів. Ця гра
потребує X Window.

%prep
%setup -q -n %{name}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
xmkmf
%{__make} \
	CC="%{__cc}" \
	CDEBUGFLAGS="%{rpmcflags}" \
	FONTDIR=%{_fontsdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/usr/share/fonts/misc,%{_desktopdir},%{_pixmapsdir}}

%{__make} install install.man \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir}/man1 \
	DESTDIR=$RPM_BUILD_ROOT

install hex20.pcf $RPM_BUILD_ROOT%{_fontsdir}/misc

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
%attr(664,root,games) %config(noreplace) %verify(not md5 mtime size) /var/games/xhextris-scores
%{_mandir}/man1/xhextris.1*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
