#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : Vulkan-Loader
Version  : 1.2.148
Release  : 50
URL      : file:///insilications/build/clearlinux/packages/Vulkan-Loader/Vulkan-Loader-v1.2.148.zip
Source0  : file:///insilications/build/clearlinux/packages/Vulkan-Loader/Vulkan-Loader-v1.2.148.zip
Source1  : file:///insilications/build/clearlinux/packages/Vulkan-Loader/googletest-release-1.10.0.zip
Summary  : Vulkan Loader
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1 MPL-1.1
Requires: Vulkan-Loader-lib = %{version}-%{release}
BuildRequires : Vulkan-Headers-data
BuildRequires : Vulkan-Headers-dev
BuildRequires : buildreq-cmake
BuildRequires : extra-cmake-modules pkgconfig(wayland-client)
BuildRequires : extra-cmake-modules pkgconfig(xcb) xcb-util-cursor-dev xcb-util-image-dev xcb-util-keysyms-dev xcb-util-renderutil-dev xcb-util-wm-dev xcb-util-dev
BuildRequires : findutils
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libICE-dev
BuildRequires : libSM-dev
BuildRequires : libX11-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : libX11-dev32
BuildRequires : libXScrnSaver-dev
BuildRequires : libXau-dev
BuildRequires : libXcomposite-dev
BuildRequires : libXcursor-dev
BuildRequires : libXdamage-dev
BuildRequires : libXdmcp-dev
BuildRequires : libXext-dev
BuildRequires : libXfixes-dev
BuildRequires : libXft-dev
BuildRequires : libXi-dev
BuildRequires : libXinerama-dev
BuildRequires : libXmu-dev
BuildRequires : libXpm-dev
BuildRequires : libXrandr-dev
BuildRequires : libXrender-dev
BuildRequires : libXres-dev
BuildRequires : libXt-dev
BuildRequires : libXtst-dev
BuildRequires : libXv-dev
BuildRequires : libXxf86misc-dev
BuildRequires : libXxf86vm-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(32libudev)
BuildRequires : pkgconfig(32pciaccess)
BuildRequires : pkgconfig(32pthread-stubs)
BuildRequires : pkgconfig(32wayland-client)
BuildRequires : pkgconfig(32wayland-cursor)
BuildRequires : pkgconfig(32wayland-egl)
BuildRequires : pkgconfig(32wayland-server)
BuildRequires : pkgconfig(32x11-xcb)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(pciaccess)
BuildRequires : pkgconfig(pthread-stubs)
BuildRequires : pkgconfig(valgrind)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-cursor)
BuildRequires : pkgconfig(wayland-egl)
BuildRequires : pkgconfig(wayland-server)
BuildRequires : pkgconfig(x11-xcb)
BuildRequires : pkgconfig(xcb)
BuildRequires : python3
BuildRequires : xcb-util-cursor-dev
BuildRequires : xcb-util-dev
BuildRequires : xcb-util-image-dev
BuildRequires : xcb-util-keysyms-dev
BuildRequires : xcb-util-renderutil-dev
BuildRequires : xcb-util-wm-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Vulkan Ecosystem Components
This project provides the Khronos official Vulkan ICD desktop loader for Windows, Linux, and MacOS.

%package dev
Summary: dev components for the Vulkan-Loader package.
Group: Development
Requires: Vulkan-Loader-lib = %{version}-%{release}
Provides: Vulkan-Loader-devel = %{version}-%{release}
Requires: Vulkan-Loader = %{version}-%{release}

%description dev
dev components for the Vulkan-Loader package.


%package dev32
Summary: dev32 components for the Vulkan-Loader package.
Group: Default
Requires: Vulkan-Loader-lib32 = %{version}-%{release}
Requires: Vulkan-Loader-dev = %{version}-%{release}

%description dev32
dev32 components for the Vulkan-Loader package.


%package lib
Summary: lib components for the Vulkan-Loader package.
Group: Libraries

%description lib
lib components for the Vulkan-Loader package.


%package lib32
Summary: lib32 components for the Vulkan-Loader package.
Group: Default

%description lib32
lib32 components for the Vulkan-Loader package.


%prep
%setup -q -n Vulkan-Loader-v1.2.148
cd %{_builddir}
unzip -q %{_sourcedir}/googletest-release-1.10.0.zip
cd %{_builddir}/Vulkan-Loader-v1.2.148
mkdir -p external/googletest
cp -r %{_builddir}/googletest-release-1.10.0/* %{_builddir}/Vulkan-Loader-v1.2.148/external/googletest

%build
unset http_proxy
unset https_proxy
unset no_proxy
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1597329620
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage --coverage -fprofile-partial-training"
export CFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 $PGO_GEN"
export FCFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 $PGO_GEN"
export FFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 $PGO_GEN"
export CXXFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -fvisibility-inlines-hidden -pipe -ffat-lto-objects -flto=16 $PGO_GEN"
export LDFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 $PGO_GEN"
## pgo use
## -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fpic -fvisibility=hidden  -fno-semantic-interposition  -fno-plt
## gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common
export PGO_USE="-fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-correction -fprofile-partial-training"
export CFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects $PGO_USE"
export FCFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects $PGO_USE"
export FFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects $PGO_USE"
export CXXFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects $PGO_USE"
export LDFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects $PGO_USE"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
#export CCACHE_DISABLE=1
## altflags_pgo end
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
%cmake .. -DLIB_INSTALL_DIR=lib64 -DBUILD_TESTS=1 -DBUILD_STATIC_LIBS:BOOL=ON -DBUILD_STATIC_LIBS=1 -DENABLE_SHARED:bool=ON -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS:bool=ON
make  %{?_smp_mflags}

make VERBOSE=1 V=1 %{?_smp_mflags} test || :
find . -type f -not -name '*.gcno' -delete -print
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
%cmake .. -DLIB_INSTALL_DIR=lib64 -DBUILD_TESTS=1 -DBUILD_STATIC_LIBS:BOOL=ON -DBUILD_STATIC_LIBS=1 -DENABLE_SHARED:bool=ON -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS:bool=ON
make  %{?_smp_mflags}
popd
mkdir -p clr-build32
pushd clr-build32
export CFLAGS="-g -O3 -fuse-linker-plugin -pipe"
export CXXFLAGS="-g -O3 -fuse-linker-plugin -fvisibility-inlines-hidden -pipe"
export LDFLAGS="-g -O3 -fuse-linker-plugin -pipe"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%cmake -DLIB_INSTALL_DIR:PATH=/usr/lib32 -DCMAKE_INSTALL_LIBDIR=/usr/lib32 -DLIB_SUFFIX=32 .. -DLIB_INSTALL_DIR=lib64 -DBUILD_TESTS=1 -DBUILD_STATIC_LIBS:BOOL=ON -DBUILD_STATIC_LIBS=1 -DENABLE_SHARED:bool=ON -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS:bool=ON
make  %{?_smp_mflags}
unset PKG_CONFIG_PATH
popd

%check
export LANG=C.UTF-8
unset http_proxy
unset https_proxy
unset no_proxy
cd clr-build; make test || :
cd ../clr-build32;
make test || : || :

%install
export SOURCE_DATE_EPOCH=1597329620
rm -rf %{buildroot}
pushd clr-build32
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/lib64/libvulkan.so
/usr/lib64/pkgconfig/vulkan.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libvulkan.so
/usr/lib32/pkgconfig/32vulkan.pc
/usr/lib32/pkgconfig/vulkan.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libvulkan.so.1
/usr/lib64/libvulkan.so.1.2.150

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libvulkan.so.1
/usr/lib32/libvulkan.so.1.2.150
