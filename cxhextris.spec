Summary:	An X Window System color version of xhextris
Summary(de):	Farbige X11-Version von Hextris
Summary(fr):	Version X11 en couleurs d'hextris
Summary(pl):	Kolorowa wersja gry xhextris pod X Window
Summary(ru):	������� ������ hextris ��� X11
Summary(tr):	D��en bloklar� yerle�tirme oyunu
Summary(uk):	��������� ���Ӧ� hextris ��� X11
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
cxhextrix ist eine Farbversion des popul�ren hextris, beides nahe
Verwandte des klassischen T*tris Video-Games, bei dem unregelm��ig
geformte Bl�cke perfekt aufeinander gestapelt werden m�ssen.
Voraussetzung ist, da� X-Window korrekt funktioniert.

%description -l fr
cxhextrix est une version en couleurs du c�l�bre hextris. Tous deux
sont des clones du c�l�bre jeu vid�o T*tris, o� l'on doit essayer
d'empiler parfaitement des blocs avec des formes curieuses. Ce jeu
n�cessite X Window pour fonctionner correctement.

%description -l pl
CXHextris jest kolorow� wersj� popularnej gry xhextris, b�d�cej klonem
Tetrisa u�ywaj�cym sze�ciobocznych figur zamiast kwadratowych.
CXHextris uruchamia si� w �rodowisku X Window.

Nale�y zainstalowa� CXHextris je�li lubi si� gry w rodzaju Tetris. Aby
m�c gra� w CXHextris nale�y mie� zainstalowane X Window.

%description -l ru
CXHextris - ��� ������� ������ ���������� ���� xhextris, �������
�������� Tetris-�������� �����, ������������ �������������� ������
���������. ��� ���� ������� ��� ����� ������ X Window.

%description -l tr
cxhextrix, hextris'in renkli s�r�m�d�r. Her ikisi de, garip �ekilli
bloklar�n - arada bo�luk b�rak�lmadan - bir y���n haline getirilmeye
�al���ld��� Tetris oyununa benzer.

%description -l uk
CXHextris - �� ��������� ���Ӧ� ��������ϧ ��� xhextris, ��� ��Ħ���
�� Tetris, ��� ����������դ ������������ ��ͦ��� ������Ԧ�. �� ���
������դ X Window.

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
