Name:           nfs4-acl-tools
Version:        0.3.4
Release:        5
Summary:        The nfs4 ACL tools
License:        BSD
URL:            http://www.citi.umich.edu/projects/nfsv4/linux/
Source0:        http://linux-nfs.org/~bfields/nfs4-acl-tools/%{name}-%{version}.tar.gz

BuildRequires: libtool libattr-devel qt-devel git

%description
It contains commandline and GUI NFSv4 ACL tools, which deal directly with NFSv4 ACLs.
It also contains GUI ACL utilities for the Linux NFSv4 client.


%package        gui
Summary:  nfs4 ACL tools qt gui

%description    gui
It contains GUI for the nfs4-acl-tools.

%package        help
Summary:        Including man files for nfs4-acl-tools
Requires:       man

%description    help
This contains man files for the using of nfs4-acl-tools.

%prep
%autosetup -n %{name}-%{version} -p1 -S git


%build
%configure
CFLAGS="`echo $RPM_OPT_FLAGS -fpie`"
export LDFLAGS="-pie"
%make_build

pushd GUI/nfs4-acl-editor
%{qmake_qt4}  nfs4-acl-editor.pro
%make_build
popd

%install
%make_install
install -m 0755 GUI/nfs4-acl-editor/nfs4-acl-editor %{buildroot}/usr/bin/nfs4-acl-editor

%files
%license COPYING
%doc INSTALL README VERSION
%{_bindir}/nfs4_editfacl
%{_bindir}/nfs4_getfacl
%{_bindir}/nfs4_setfacl

%files gui
%{_bindir}/nfs4-acl-editor

%files help
%{_mandir}/man*/*


%changelog
* Sat Jan 11 2020 renxudong <renxudong1@huawei.com> - 0.3.4-5
- Type:enhancemnet
- ID:NA
- SUG:NA
- DESC:Be consistent with the native community

* Wed Sep 11 2019 openEuler Buildteam <buildteam@openeuler.org> - 0.3.4-4
- Type:enhancemnet
- ID:NA
- SUG:NA
- DESC:rollback because of gui package require qt

* Fri Sep 6 2019 openEuler Buildteam <buildteam@openeuler.org> - 0.3.4-3
- Package init
