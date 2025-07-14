Summary:	FrameBuffer Viewer
Summary(pl.UTF-8):	Przeglądarka obrazków dla framebuffera
Name:		fbv
Version:	1.0b
Release:	8
License:	GPL v2+
Group:		Applications/Graphics
Source0:	http://s-tech.elsat.net.pl/fbv/%{name}-%{version}.tar.gz
# Source0-md5:	3e466375b930ec22be44f1041e77b55d
Patch0:		%{name}-nocenter.patch
Patch1:		%{name}-libpng15.patch
Patch2:		%{name}-giflib5.patch
URL:		http://s-tech.elsat.net.pl/
BuildRequires:	giflib-devel >= 5
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	util-linux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple program to view pictures on a framebuffer console. It
supports PNG, JPEG, GIF and BMP files.

%description -l pl.UTF-8
Prosty program do oglądania obrazków na konsoli z framebufferem.
Obsługuje pliki PNG, JPEG, GIF i BMP.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
# it's not autoconf script
./configure \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--mandir=%{_mandir}

%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags} -Wall -D_GNU_SOURCE" \
	LDFLAGS="%{rpmldflags} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/fbv
%{_mandir}/man1/fbv.1*
