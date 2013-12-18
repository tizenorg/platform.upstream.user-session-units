Name:		user-session-units
Version:	8
Release:	1
Summary:	Systemd session units
Group:		System/Base
License:	GPL-2.0
URL:		http://foo-projects.org/~sofar/%{name}
Source0:	http://foo-projects.org/~sofar/%{name}/%{name}-%{version}.tar.gz
Source1001: 	user-session-units.manifest

BuildRequires:	pkgconfig(systemd)
BuildRequires:  xorg-launch-helper
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(libsystemd-login)

%description
Systemd user session units.

%package gnome
Summary:	Gnome user session units
Group:		System/Base
Requires:	user-session-units

%description gnome
Gnome user session units.

%package enlightenment
Summary:	Enlightenment user session units
Group:		System/Base
Requires:	user-session-units

%description enlightenment
Enlightenment user session units.

%prep
%setup -q
cp %{SOURCE1001} .


%build
%autogen
%configure --enable-gnome --enable-enlightenment

make %{?_smp_mflags}


%install
%make_install


%files
%manifest %{name}.manifest
%license COPYING
%{_bindir}/user-session-launch
%{_unitdir}/*
%exclude %{_unitdir_user}/dbus.socket
%exclude %{_unitdir_user}/dbus.service

%files enlightenment
%manifest %{name}.manifest
%{_unitdir_user}/e17.target
%{_unitdir_user}/enlightenment.service
%{_unitdir_user}/e17.target.wants/enlightenment.service

%files gnome
%manifest %{name}.manifest
%{_unitdir_user}/gnome.target
%{_unitdir_user}/gnome-session.service
%{_unitdir_user}/gnome.target.wants/gnome-session.service
