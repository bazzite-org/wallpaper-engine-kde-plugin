%global _enable_debug_package 0
%global debug_package %{nil}

Name: wallpaper-engine-kde-plugin
Version: {{{ git_dir_version }}}
Release: 1%{?dist}
Summary: A kde wallpaper plugin integrating wallpaper engine

Group: Development/System 
License: GPLv2
URL: https://github.com/catsout/wallpaper-engine-kde-plugin

Patch1: 001-system-deps.patch
Patch2: 002-fix-gcc-15.patch

BuildRequires: vulkan-loader-devel
BuildRequires: plasma-workspace-devel
BuildRequires: libplasma-devel
BuildRequires: gstreamer1-plugin-libav
BuildRequires: lz4-devel
BuildRequires: mpv-libs-devel
BuildRequires: python3-websockets

BuildRequires: qt6-qtbase-private-devel
BuildRequires: qt6-qtwebsockets-devel
BuildRequires: qt6-qtwebchannel-devel

BuildRequires: git
BuildRequires: cmake
BuildRequires: extra-cmake-modules

BuildRequires: kf6-rpm-macros

Requires:      python3-websockets
Requires:      qt6-qtwebchannel
Requires:      qt6-qtwebsockets-devel 
Requires:      wallpaper-engine-kde-plugin-lib = %{version}-%{release}

%description
A wallpaper plugin integrating wallpaper engine into kde wallpaper setting.

%prep
git clone --depth 1 --branch main %{url}.git %{_builddir}/%{name}-%{version}

cd %{_builddir}/%{name}-%{version}
git submodule update --init --recursive

%autopatch -p1

%build
cd %{_builddir}/%{name}-%{version}
%cmake_kf6 -DQT_MAJOR_VERSION=6 -DBUILD_QML=ON -DUSE_PLASMAPKG=ON
%cmake_build

%install
cd %{_builddir}/%{name}-%{version}
%cmake_install

%files
%{_kf6_qmldir}/com/github/catsout/wallpaperEngineKde/*

%changelog 
%autochangelog
