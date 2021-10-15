%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-sbg-driver
Version:        3.1.1
Release:        5%{?dist}%{?release_suffix}
Summary:        ROS sbg_driver package

License:        MIT
URL:            http://wiki.ros.org/sbg_driver
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-geometry-msgs
Requires:       ros-noetic-message-runtime
Requires:       ros-noetic-nav-msgs
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-sensor-msgs
Requires:       ros-noetic-std-msgs
Requires:       ros-noetic-std-srvs
Requires:       ros-noetic-tf2-geometry-msgs
Requires:       ros-noetic-tf2-msgs
Requires:       ros-noetic-tf2-ros
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-geometry-msgs
BuildRequires:  ros-noetic-message-generation
BuildRequires:  ros-noetic-nav-msgs
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-sensor-msgs
BuildRequires:  ros-noetic-std-msgs
BuildRequires:  ros-noetic-std-srvs
BuildRequires:  ros-noetic-tf2-geometry-msgs
BuildRequires:  ros-noetic-tf2-msgs
BuildRequires:  ros-noetic-tf2-ros
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
ROS driver package for communication with the SBG navigation systems.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Fri Oct 15 2021 SBG Systems <support@sbg-systems.com> - 3.1.1-5
- Autogenerated by Bloom

* Thu Oct 14 2021 SBG Systems <support@sbg-systems.com> - 3.1.1-4
- Autogenerated by Bloom

* Wed Oct 13 2021 SBG Systems <support@sbg-systems.com> - 3.1.1-3
- Autogenerated by Bloom

* Wed Oct 13 2021 SBG Systems <support@sbg-systems.com> - 3.1.1-2
- Autogenerated by Bloom

* Wed Oct 13 2021 SBG Systems <support@sbg-systems.com> - 3.1.1-1
- Autogenerated by Bloom

* Thu Oct 07 2021 SBG Systems <support@sbg-systems.com> - 3.1.0-2
- Autogenerated by Bloom

* Thu Oct 07 2021 SBG Systems <support@sbg-systems.com> - 3.1.0-1
- Autogenerated by Bloom

* Wed Sep 01 2021 SBG Systems <support@sbg-systems.com> - 3.0.0-3
- Autogenerated by Bloom

* Wed Sep 01 2021 SBG Systems <support@sbg-systems.com> - 3.0.0-2
- Autogenerated by Bloom

* Tue Aug 31 2021 SBG Systems <support@sbg-systems.com> - 3.0.0-1
- Autogenerated by Bloom

