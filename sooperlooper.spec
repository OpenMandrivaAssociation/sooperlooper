%define name    sooperlooper
%define version 1.6.14
%define release %mkrel 1

Name:       %{name}
Summary:    Live audio looper
Version:    %{version}
Release:    %{release}

URL:        http://sonosaurus.com/%{name}
Source:     http://sonosaurus.com/%{name}/%{name}-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
License:    GPLv2
Group:      Sound

BuildRequires:  fftw3-devel libsigc++1.2-devel 
BuildRequires:  sndfile-devel rubberband-devel libsamplerate-devel
BuildRequires:  jackit-devel liblo-devel
BuildRequires:  libxml2-devel ncurses-devel libwxgtk2.8-devel

%description
SooperLooper is a live looping sampler capable of immediate loop recording, 
overdubbing, multiplying, reversing and more. It allows for multiple 
simultaneous multi-channel loops limited only by your computer's 
available memory. 

%prep
%setup -q

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

#menu
mkdir -p %{buildroot}/%{_datadir}/applications
cat > %{buildroot}/%{_datadir}/applications/mandriva-%{name}.desktop << EOF
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
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_bindir}/%name
%{_bindir}/slconsole
%{_bindir}/slgui
%{_bindir}/slregister
%{_datadir}/%name
%{_datadir}/applications/mandriva-%{name}.desktop
