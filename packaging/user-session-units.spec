Name:		user-session-units
Version:	6
Release:	1
Summary:	user-session-units
Group:		System/Base
License:	GPLv2
URL:		http://foo-projects.org/~sofar/%{name}
Source0:	http://foo-projects.org/~sofar/%{name}/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(systemd)

%description
user-session-units

%prep
%setup -q


%build
%autogen
%configure
make %{?_smp_mflags}


%install
%make_install


%files
%{_unitdir_user}/*
%{_unitdir}/*

