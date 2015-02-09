Name:		shinken-mod-logstore-null
Version:	1.4.1
Release:	2kaji0.2
Summary:	Export logs to /dev/null for the Livestatus module

Group:		Network
License:	AGPLv3+
URL:		https://github.com/kaji-project/shinken-mod-logstore-null
Source0:	%{name}_%{version}.orig.tar.gz

BuildArch:  noarch

Requires:	shinken-mod-livestatus >= 1.0

%description
Export logs to /dev/null for the Livestatus module

%prep
%setup -q


%build


%install
rm -rf %{buildroot}/*

install -d %{buildroot}/usr/share/pyshared/shinken/modules/logstore-null
install -pm07555 module/* %{buildroot}/usr/share/pyshared/shinken/modules/logstore-null

install -d %{buildroot}/usr/share/doc/%{name}
install -pm0755 README.md %{buildroot}/%{_docdir}/%{name}

install -d %{buildroot}/etc/shinken/modules
install -pm0755 etc/modules/* %{buildroot}/etc/shinken/modules


%files
/usr/share/pyshared/shinken/modules/logstore-null
%config(noreplace) %{_sysconfdir}/shinken/modules/

%doc %{_docdir}/%{name}


%changelog
* Mon Feb 09 2015 Thibault Cohen <thibault.cohen@savoirfairelinux.com> 1.4.1-2kaji0.2
- Initial Package
