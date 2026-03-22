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
%meson
%meson_build

%install
%meson_install
