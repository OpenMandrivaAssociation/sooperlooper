%define versionExt 2

Name: sooperlooper
Summary: Live Looping Sampler
Version: 1.6.13
Release: %mkrel 1
Source0: %{name}-%{version}-%{versionExt}.tar.gz
URL: http://essej.net/sooperlooper/
Group: Sound
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: LGPLv2

BuildRequires: libjack-devel  >= 0.80
BuildRequires: libwxgtk2.8-devel
BuildRequires: liblo-devel >= 0.18
BuildRequires: libsigc++1.2-devel
BuildRequires: libsndfile-devel
BuildRequires: libsamplerate-devel
BuildRequires: librubberband-devel
BuildRequires: libfftw-devel

%description
SooperLooper is a live looping sampler capable of immediate loop
recording, overdubbing, multiplying, reversing and more.  It allows
for multiple simultaneous multi-channel loops limited only by your
computer's available memory.  The feature-set and operation was
inspired by the impressive Gibson Echoplex Digital Pro (EDP). When used
with a low-latency audio configuration it is capable of truly realtime
live performance looping.
	  
The application is a standalone JACK client with an engine
controllable via OSC and MIDI.  It also includes a GUI which
communicates with the engine via OSC (even over a network) for
user-friendly control on a desktop.  However, this kind of live
performance looping tool is most effectively used via hardware (midi
footpedals, etc) and the engine can be run standalone on a computer
without a monitor.


%prep
%setup -q

%build
%configure  
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_prefix}/bin/slconsole
%{_prefix}/bin/slgui
%{_prefix}/bin/sooperlooper
%{_datadir}/%{name}/presets/bcf2000.slb
%{_datadir}/%{name}/presets/edp4.slb
%{_datadir}/%{name}/presets/midiwizard.slb
%{_datadir}/%{name}/presets/oxy8.slb


