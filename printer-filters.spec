Name:           printer-filters
Version:        1.1
Release:        4.1%{?dist}
Summary:        Collection of filters for various printer drivers

Group:          System Environment/Libraries
License:        Public Domain
URL:            http://fedoraproject.org/wiki/Printing

BuildArch:      noarch

# Lexmark
Requires:       pbm2l2030 c2050 c2070 lx pbm2l7k
# Canon
Requires:       cjet
# Minolta
Requires:       min12xxw
# Brother
Requires:       ptouch-driver
# Printer independent converters
Requires:       ghostscript psutils pnm2ppa

%files
# No files

%description
This is a meta-package that depends on all available printer filters.
Installing it via tool that resolves dependencies, such as yum or anaconda,
ensures that all printer drivers available from foomatic package that
require external filters will work.

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.1-4.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Adam Jackson <ajax@redhat.com> 1.1-3
- Un-Requires: netpbm-progs, none of the foomatic ppds require it.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jul 27 2007 Lubomir Kundrak <lkundrak@redhat.com> 1.1-1
- Added a dependency on ptouch-driver

* Wed Jul 4 2007 Lubomir Kundrak <lkundrak@redhat.com> 1.0-1
- Changed the name to printer-filters from printer-drivers

* Wed Jul 4 2007 Lubomir Kundrak <lkundrak@redhat.com> 1.0-1
- Initial package
