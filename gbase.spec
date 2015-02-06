Summary:	Small numeric base converter
Name:		gbase
Version:	0.5
Release:	7
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



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5-6mdv2011.0
+ Revision: 618428
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.5-5mdv2010.0
+ Revision: 429180
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.5-4mdv2009.0
+ Revision: 245700
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.5-2mdv2008.1
+ Revision: 136426
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import gbase


* Thu Aug 10 2006 Lenny Cartier <lenny@mandriva.com> 0.5-2mdv2007.0
- rebuild

* Thu Dec 16 2004 Olivier Blin <blino@mandrake.org> 0.5-1mdk
- initial Mandrakelinux release
