Summary:	An X Window System color version of xhextris
Name:		cxhextris
Version:	1.0
Release:	15
Copyright:	distributable
Group:		X11/Games
Group(pl):	X11/Gry
Source0:	ftp://sunsite.unc.edu/pub/Linux/games/arcade/tetris/%{name}.tar.z
Source1:	cxhextris.wmconfig
Patch0:		cxhextris-config.patch
Patch1:		cxhextris-axp.patch
Patch2:		cxhextris-security.patch
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

%description -l pl
CXHextris jest kolorow± wersj± popularnej gry xhextris, bêd±cej klonem
Tetrisa u¿ywaj±cym sze¶ciobocznych figur zamiast kwadratowych.
CXHextris uruchamia siê w ¶rodowisku X Window.

Nale¿y zainstalowaæ CXHextris je¶li lubi siê gry w rodzaju Tetris. Aby
móc graæ w CXHextris nale¿y mieæ zainstalowane X Window.

%prep
%setup -q -n cxhextris
%patch -p1
%patch1 -p1
%patch2 -p1

%build
xmkmf
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install install.man

install -d $RPM_BUILD_ROOT%{_prefix}/X11R6/lib/X11/fonts/misc
make FONTDIR=$RPM_BUILD_ROOT%{_prefix}/X11R6/lib/X11/fonts install.font

( cd $RPM_BUILD_ROOT
install -d .%{_sysconfdir}/X11/wmconfig
install $RPM_SOURCE_DIR/cxhextris.wmconfig .%{_sysconfdir}/X11/wmconfig/cxhextris
)

%clean
rm -rf $RPM_BUILD_ROOT

%post
(cd /usr/X11R6/lib/X11/fonts/misc; /usr/X11R6/bin/mkfontdir)

%postun
(cd /usr/X11R6/lib/X11/fonts/misc; /usr/X11R6/bin/mkfontdir)

%files
%defattr(644,root,root,755)
%doc README README.Linux
%attr(4755,games,games) %{_bindir}/xhextris
%{_prefix}/X11R6/lib/X11/fonts/misc/hex20.pcf
%attr(-,games,games)	/var/lib/games/xhextris-scores
%{_sysconfdir}/X11/wmconfig/cxhextris
