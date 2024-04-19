Name: wallpaper-engine-kde-plugin
Version: {{{ git_dir_version }}}
Release: 1%{?dist}
Summary: A kde wallpaper plugin integrating wallpaper engine

Group: Development/System 
License: GPLv2
URL: https://github.com/catsout/wallpaper-engine-kde-plugin

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: extra-cmake-modules mpv-libs-devel vulkan-headers plasma-workspace-devel libplasma-devel lz4-devel qt6-qtbase-private-devel qt6-qtdeclarative-devel git
Requires: plasma-workspace gstreamer1-libav mpv-libs lz4 python3-websockets qt6-qtwebchannel-devel qt6-qtwebsockets-devel

%global _enable_debug_package 0
%global debug_package %{nil}

%description
A wallpaper plugin integrating wallpaper engine into kde wallpaper setting.

%prep
git clone --depth 1 --branch qt6 %{url}.git
cd wallpaper-engine-kde-plugin
git submodule update --init --recursive

%build
cd wallpaper-engine-kde-plugin
mkdir -p build && cd build
cmake .. -DQT_MAJOR_VERSION=6 -DUSE_PLASMAPKG=ON
%make_build

%install
cd wallpaper-engine-kde-plugin
rm -rf $RPM_BUILD_ROOT
cd build
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/*

%changelog 
