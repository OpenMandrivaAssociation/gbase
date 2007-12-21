Summary:	Small numeric base converter
Name:		gbase
Version:	0.5
Release:	%mkrel 2
Source0:	%{name}-%{version}.tar.bz2
License:	Artistic
Group:		Sciences/Mathematics
Url:		http://www.hibernaculum.net/gbase/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gtk+1.2-devel

%description
GBase is a GTK program designed to convert between the four common
bases used in programming (decimal, hexadecimal, octal and binary). It
converts numbers on-the-fly as they are typed in. It can also convert
numbers entered on the command line. It can correctly handle both
signed and unsigned 32-bit integers.

%prep
%setup -q

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
install -D -m755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README TODO
%{_bindir}/%{name}

