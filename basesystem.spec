Summary: The skeleton package which defines a simple MeeGo system
Name: basesystem
Version: 8.1
Release: 1
License: Public Domain
Group: System/Base
Requires(pre): setup filesystem
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch

%description
Basesystem defines the components of a basic MeeGo system (for
example, the package installation order to use during bootstrapping).
Basesystem should be in every installation of a system, and it
should never be removed.

%prep

%build

%install

%clean

%files
%defattr(-,root,root,-)

