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
BuildRequires:	libsamplerate-devel
BuildRequires:	jackit-devel
BuildRequires:	liblo-devel
BuildRequires:	libxml2-devel
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
