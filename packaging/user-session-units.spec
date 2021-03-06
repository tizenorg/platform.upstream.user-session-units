%bcond_with x
Name:           user-session-units
Version:        8
Release:        0
Summary:        Systemd session units
Group:          System/Configuration
License:        GPL-2.0
URL:            http://foo-projects.org/~sofar/%{name}
Source0:        http://foo-projects.org/~sofar/%{name}/%{name}-%{version}.tar.gz
Source1001:     user-session-units.manifest
Source1002:     user-session.pam

BuildRequires:	pkgconfig(systemd)
%if %{with x}
BuildRequires:  xorg-launch-helper
%endif
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(libsystemd-login)

%description
Systemd user session units.

%package gnome
Summary:        Gnome user session units
Group:          System/Configuration
Requires:       user-session-units

%description gnome
Gnome user session units package.

%package enlightenment
Summary:        Enlightenment user session units
Group:          System/Configuration
Requires:       user-session-units

%description enlightenment
Enlightenment user session units package.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%reconfigure --enable-gnome --enable-enlightenment
%__make %{?_smp_mflags}

%install
%make_install
install -m 755 -d %{buildroot}%{_sysconfdir}/pam.d
install -m 644 %{SOURCE1002} %{buildroot}%{_sysconfdir}/pam.d/user-session

%files
%manifest %{name}.manifest
%license COPYING
%{_bindir}/user-session-launch
%{_unitdir}/*
%exclude %{_unitdir_user}/dbus.socket
%exclude %{_unitdir_user}/dbus.service
%config %{_sysconfdir}/pam.d/user-session

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
