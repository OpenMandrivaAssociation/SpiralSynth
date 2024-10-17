%define name SpiralSynth
%define version 2.0.0
%define release 11

Name:    %{name}
Summary: Simple software synthesizer
Version: %{version}
Release: %{release}

Source:		%name-%{version}.tar.bz2
Source1: 	SpiralLogo48.png
Source2: 	SpiralLogo32.png
Source3: 	SpiralLogo16.png
Patch:		%name-2.0.0.patch
Patch1:         SpiralSynth-2.0.0-fix-build.patch
Patch2:		SpiralSynth-2.0.0-gcc43.patch
Patch3:		SpiralSynth-2.0.0-newer-fltk.patch
URL:		https://www.pawfal.org/Software/SpiralSynth
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	fltk-devel mesagl-devel

%description
SSM's little brother has been updated at last, much much faster, better
sounding, a bit prettier and soon to be a SSM polyphonic plugin.
SpiralSynth is a simple polyphonic analogue modelling softsynth that tries
to be as easy to use as possible. 

%prep
%setup -q -n %name-%version
%patch -p1
%patch1 -p1
%patch2 -p0
%patch3 -p0

perl -pi -e 's/usr\/X11R6\/lib/usr\/X11R6\/%{_lib}/g' Makefile.in PluginLink.sh

%build
%configure
%make CXXFLAGS="%{optflags}" LFLAGS="%{?ldflags}"
										
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_bindir
cp %name $RPM_BUILD_ROOT/%_bindir

#menu

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=Synthesized Loops
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=AudioVideo;Audio;Video;X-MandrivaLinux-Multimedia-Video;AudioVideoEditing;
EOF


#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
cat %SOURCE1 > $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
cat %SOURCE2 > $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
cat %SOURCE3 > $RPM_BUILD_ROOT/%_miconsdir/%name.png

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc README CHANGES COPYING
%{_bindir}/%name
%{_datadir}/applications/mandriva-%{name}.desktop
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png



%changelog
* Mon Jan 18 2010 Jérôme Brenier <incubusss@mandriva.org> 2.0.0-10mdv2010.1
+ Revision: 493153
- rebuild for new fltk

* Sun Sep 20 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.0.0-9mdv2010.0
+ Revision: 445205
- rebuild

  + Funda Wang <fwang@mandriva.org>
    - add BR on mesagl

* Sun Dec 14 2008 Funda Wang <fwang@mandriva.org> 2.0.0-8mdv2009.1
+ Revision: 314227
- bunzip2 patch0
- add gcc 4.3 patch and newer fltk patch

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
    - rebuild
    - rebuild
    - fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
    - fix summary-ended-with-dot
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request
    - import SpiralSynth

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Tue Sep 12 2006 Nicolas L�cureuil <neoclust@mandriva.org> 2.0.0-5mdv2007.0
- Rebuild

* Wed Nov 9 2005 Austin Acton <austin@mandriva.org> 2.0.0-4mdk
- lib64 fix

* Thu Jun 17 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 2.0.0-3mdk
- Rebuild

* Fri Apr 2 2004 Austin Acton <austin@mandrake.org> 2.0.0-2mdk
- stale rebuild

* Mon Feb 10 2003 Austin Acton <aacton@yorku.ca> 2.0.0-1mdk
- initial package
- patch from Narfi Stefansson <narfi@cs.wisc.edu>

