%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/galactic/.*$
%global __requires_exclude_from ^/opt/ros/galactic/.*$

Name:           ros-galactic-turtle-tf2-cpp
Version:        0.3.4
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS turtle_tf2_cpp package

License:        Apache License, Version 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-galactic-geometry-msgs
Requires:       ros-galactic-launch
Requires:       ros-galactic-launch-ros
Requires:       ros-galactic-message-filters
Requires:       ros-galactic-rclcpp
Requires:       ros-galactic-tf2
Requires:       ros-galactic-tf2-geometry-msgs
Requires:       ros-galactic-tf2-ros
Requires:       ros-galactic-turtlesim
Requires:       ros-galactic-ros-workspace
BuildRequires:  ros-galactic-ament-cmake
BuildRequires:  ros-galactic-ament-lint-auto
BuildRequires:  ros-galactic-ament-lint-common
BuildRequires:  ros-galactic-geometry-msgs
BuildRequires:  ros-galactic-launch
BuildRequires:  ros-galactic-launch-ros
BuildRequires:  ros-galactic-message-filters
BuildRequires:  ros-galactic-rclcpp
BuildRequires:  ros-galactic-tf2
BuildRequires:  ros-galactic-tf2-geometry-msgs
BuildRequires:  ros-galactic-tf2-ros
BuildRequires:  ros-galactic-turtlesim
BuildRequires:  ros-galactic-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
turtle_tf2_cpp demonstrates how to write a ROS2 C++ tf2 broadcaster and listener
with the turtlesim. The turtle_tf2_listener commands turtle2 to follow turtle1
around as you drive turtle1 using the keyboard.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/galactic" \
    -DAMENT_PREFIX_PATH="/opt/ros/galactic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/galactic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/galactic

%changelog
* Mon Oct 11 2021 Alejandro Hernández Cordero <alejandro@openrobotics.org> - 0.3.4-1
- Autogenerated by Bloom

* Fri Aug 27 2021 Alejandro Hernández Cordero <alejandro@openrobotics.org> - 0.3.3-1
- Autogenerated by Bloom

* Mon Aug 09 2021 Alejandro Hernández Cordero <alejandro@openrobotics.org> - 0.3.2-1
- Autogenerated by Bloom

