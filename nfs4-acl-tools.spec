Name:           nfs4-acl-tools
Version:        0.3.7
Release:        5
Summary:        The nfs4 ACL tools
License:        BSD or GPLv2+ or LGPLv2.1
URL:            http://www.citi.umich.edu/projects/nfsv4/linux/
Source0:        http://linux-nfs.org/~bfields/nfs4-acl-tools/%{name}-%{version}.tar.gz

BuildRequires: libtool libattr-devel

Patch1:        0001-Fix-infinite-loop-when-perl-is-added-in-BEP_FILE_TIM.patch
Patch2:        0002-build-do-not-generate-aclocal.m4.patch

%description
It contains commandline NFSv4 ACL tools, which deal directly with NFSv4 ACLs.

%package        help
Summary:        Including man files for nfs4-acl-tools
Requires:       man

%description    help
This contains man files for the using of nfs4-acl-tools.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%configure
CFLAGS="`echo $RPM_OPT_FLAGS -fpie`"
export LDFLAGS="-pie"
%make_build

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%files
%license COPYING
%doc INSTALL README VERSION
%{_bindir}/nfs4_editfacl
%{_bindir}/nfs4_getfacl
%{_bindir}/nfs4_setfacl

%files help
%{_mandir}/man*/*

%changelog
* Tue Oct 18 2022 zhanchengbin <zhanchengbin1@huawei.com> - 0.3.7-5
- license: fix license error.

* Mon Jan 10 2022 Wenchao Hao <haowenchao@huawei.com> - 0.3.7-4
- DESC: build: do not generate aclocal.m4 to fix compile error

* Wed Dec 1 2021 volcanodragon <linfeilong@huawei.com> - 0.3.7-3
- DESC: Fix infinite loop when perl is added in BEP_FILE_TIME_LIST

* Fri Jul 30 2021 chenyanpanHW <chenyanpan@huawei.com> - 0.3.7-2
- DESC: delete -S git from %autosetup, and delete BuildRequires git

* Thu Jul 16 2020 wuguanghao <wuguanghao3@huawei.com> - 0.3.7-1
- update nfs4-acl-tools version to 0.3.7-1

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
