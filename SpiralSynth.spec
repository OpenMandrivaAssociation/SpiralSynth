%define name SpiralSynth
%define version 2.0.0
%define release %mkrel 5

Name:    %{name}
Summary: SpiralSynth is a simple software synthesizer.
Version: %{version}
Release: %{release}

Source:		%name-%{version}.tar.bz2
Source1: 	SpiralLogo48.png
Source2: 	SpiralLogo32.png
Source3: 	SpiralLogo16.png
Patch:		%name-2.0.0.patch.bz2
Patch1:         SpiralSynth-2.0.0-fix-build.patch
URL:		http://www.pawfal.org/Software/SpiralSynth
License:	GPL
Group:		Sound
BuildRequires:	fltk-devel

%description
SSM's little brother has been updated at last, much much faster, better
sounding, a bit prettier and soon to be a SSM polyphonic plugin.
SpiralSynth is a simple polyphonic analogue modelling softsynth that tries
to be as easy to use as possible. 

%prep
%setup -q -n %name-%version
%patch -p1
%patch1 -p1
perl -pi -e 's/usr\/X11R6\/lib/usr\/X11R6\/%{_lib}/g' Makefile.in PluginLink.sh

%build
%configure
%make
										
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_bindir
cp %name $RPM_BUILD_ROOT/%_bindir

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="%{name}.png" needs="x11" title="SpiralSynth" longtitle="Software Synthesizer" section="Multimedia/Sound" xdg="true"
EOF

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

%post
%update_menus
		
%postun
%clean_menus

%files
%defattr(-,root,root)
%doc README CHANGES COPYING
%{_bindir}/%name
%{_menudir}/%name
%{_datadir}/applications/mandriva-%{name}.desktop
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png

