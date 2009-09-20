%define name SpiralSynth
%define version 2.0.0
%define release %mkrel 9

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
URL:		http://www.pawfal.org/Software/SpiralSynth
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

