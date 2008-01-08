#no, i don't want to know
%define _requires_exceptions ld-linux.so.2(GLIBC_PRIVATE)\\|ld-linux-x86-64.so.2(GLIBC_PRIVATE)(64bit)

%define name	mediacheck
%define version	7.3
%define release	%mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Utilities for the insertion/verification of iso embedded MD5 sums
License:	GPL
Group:		File tools
URL:		http://fedora.redhat.com/projects/anaconda-installer/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		mediacheck-7.3-misc.patch
BuildRequires:	newt-devel slang-devel
BuildRoot:	%{_tmppath}/%{name}-root
%description
The mediacheck package contains utilities for the insertion and 
verification of embedded MD5 checksums in iso images. These tools 
form part of the RedHat Anaconda installer, with this from 
version 7.3.

%prep
%setup -q
%patch0 -p1 -b .mdv

%build
%make
%make LIBS="-Wl,-Bstatic -lnewt -lslang -Wl,-Bdynamic" mediacheck

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
install -m 755 mediacheck $RPM_BUILD_ROOT/%{_bindir}

%clean
rm -Rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{_bindir}/checkisomd5
%{_bindir}/implantisomd5
%{_bindir}/mediacheck

