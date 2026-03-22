%define major 1

%define libprocessing %mklibname webrtc-processing2
%define devname %mklibname webrtc2 -d

Summary:	Real-Time Communication Library for Web Browsers
Name:		webrtc-audio-processing2
Version:	2.1
Release:	1
License:	BSD-3-Clause
Group:		System/Libraries
Url:		https://www.freedesktop.org/software/pulseaudio/webrtc-audio-processing/
Source0:	https://gitlab.freedesktop.org/pulseaudio/webrtc-audio-processing/-/archive/v%{version}/webrtc-audio-processing-v%{version}.tar.bz2
# Upstream, drop it all with 2.2 release
Patch0:        d0569cfa50c1858ee279d77b3fc8870be6902441.patch
Patch1:        bc838790eeb6066d30f019c2a3516bd2b824a5c8.patch
Patch2:        c8896801dfbfe03b56f85c1533abc077ff74a533.patch
Patch3:        65bea7a0b167509703dbf841a4e2192d6fd659e6.patch
Patch4:        fe8f3672377ccfdbfceecd0bc09d8e5f51187f96.patch
Patch5:        a260b2e8b9ca00119eb6c683121d5c40e040bce6.patch
Patch6:        e9c78dc4712fa6362b0c839ad57b6b46dce1ba83.patch
# OpenSuse
Patch7:        https://build.opensuse.org/projects/openSUSE:Factory/packages/webrtc-audio-processing/files/fix-build.patch

BuildRequires:	meson
BuildRequires:	abseil-cpp-devel

%description
WebRTC is an open source project that enables web browsers with Real-Time
Communications (RTC) capabilities via simple Javascript APIs. The WebRTC
components have been optimized to best serve this purpose.

WebRTC implements the W3C's proposal for video conferencing on the web.

#----------------------------------------------------------------------------

%package -n %{libprocessing}
Summary:	Real-Time Communication Library for Web Browsers
Group:		System/Libraries

%description -n %{libprocessing}
WebRTC is an open source project that enables web browsers with Real-Time
Communications (RTC) capabilities via simple Javascript APIs. The WebRTC
components have been optimized to best serve this purpose.

WebRTC implements the W3C's proposal for video conferencing on the web.

%files -n %{libprocessing}
%{_libdir}/libwebrtc-audio-processing-2.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Real-Time Communication Library for Web Browsers
Group:		Development/C
Requires:	%{libprocessing} = %{EVRD}
Provides:	webrtc-audio-processing2-devel = %{EVRD}
Provides:	webrtc-audio-processing2-devel-static = %{EVRD}

%description -n %{devname}
WebRTC is an open source project that enables web browsers with Real-Time
Communications (RTC) capabilities via simple Javascript APIs. The WebRTC
components have been optimized to best serve this purpose.

WebRTC implements the W3C's proposal for video conferencing on the web.

%files -n %{devname}
%doc AUTHORS COPYING NEWS README
%{_includedir}/webrtc-audio-processing-2/
%{_libdir}/libwebrtc-audio-processing-2.so
%{_libdir}/pkgconfig/webrtc-*.pc

#----------------------------------------------------------------------------

%prep
%autosetup -n webrtc-audio-processing-v%{version} -p1

%build
%meson  \
        -Dcpp_std=c++20 \
%ifnarch aarch64
        -Dneon=disabled
%endif
%meson_build

%install
%meson_install
