Name:		sooperlooper
Version:	1.6.18
Release:	%mkrel 1
Summary:	Live audio looper
URL:		http://sonosaurus.com/%{name}
Source:		http://sonosaurus.com/%{name}/%{name}-%{version}.tar.gz
License:	GPLv2
Group:		Sound
BuildRequires:	fftw3-devel
BuildRequires:	libsigc++1.2-devel
BuildRequires:	sndfile-devel
BuildRequires:	rubberband-devel
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	jackit-devel
BuildRequires:	pkgconfig(liblo)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	ncurses-devel
BuildRequires:	wxgtku-devel

%description
SooperLooper is a live looping sampler capable of immediate loop recording, 
overdubbing, multiplying, reversing and more. It allows for multiple 
simultaneous multi-channel loops limited only by your computer's 
available memory.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

#menu
%__mkdir_p %{buildroot}/%{_datadir}/applications
%__cat > %{buildroot}/%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=SooperLooper
Comment=Live Audio Looper
Exec=%{_bindir}/slgui 
Icon=sound_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-Multimedia-Sound;AudioVideo;Audio;AudioVideoEditing;
EOF

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_bindir}/%{name}
%{_bindir}/slconsole
%{_bindir}/slgui
%{_bindir}/slregister
%{_datadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop


%changelog
* Thu Jan 12 2012 Andrey Bondrov <abondrov@mandriva.org> 1.6.18-1mdv2011.0
+ Revision: 760473
- New version 1.6.18, build against utf8 wxGTK2.8, spec cleanup

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 1.6.14-2mdv2011.0
+ Revision: 614944
- the mass rebuild of 2010.1 packages

* Sun Apr 11 2010 Frank Kober <emuse@mandriva.org> 1.6.14-1mdv2010.1
+ Revision: 533598
- new version 1.6.14, update url, add desktop file
- restablish sooperlooper

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - old directory, without matching package

* Fri Apr 17 2009 Olivier Thauvin <nanardon@mandriva.org> 1.6.13-1mdv2009.1
+ Revision: 367944
- import sooperlooper


* Sat Apr 17 2009 Romain Dep. <rom1dep@gmail.com> 1.6.13-1mdv2009.1
- initial package for Mandriva Linux
