Summary:	The Intel(R) Active Management Technology (Intel(R) AMT) User Notification Service (UNS)
Name:		uns
Version:	5.0.0.30
Release:	0.1
License:	GPL v2
Group:		Daemons
Source0:	http://dl.sourceforge.net/openamt/%{name}-%{version}.tar.gz
# Source0-md5:	c20cba1e38e86ed7aa56bdd749ecff53
Source1:	%{name}.init
Patch0:		%{name}-build.patch
URL:		http://www.openamt.org/
BuildRequires:	curl-devel
BuildRequires:	gsoap
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel
BuildRequires:	openwsman-devel
BuildRequires:	trousers-devel
BuildRequires:	xerces-c-devel
Requires(post,preun):	/sbin/chkconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Intel(R) Active Management Technology (Intel(R) AMT) User
Notification Service (UNS) runs as a deamon on the host of a platform
that also has Intel AMT enabled. The UNS receives messages from Intel
AMT and write them to the local OS event log for the purpose of
notifying end users of predefined events such as when critical System
Defense policies are applied by the ME FW.

%prep
%setup -q -n UNS-%{version}
%patch0 -p1

%build
%configure \
	CPPFLAGS="%{rpmcppflags} -I/usr/include/openwsman"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/uns

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
