Summary:	FrameBuffer Viewer
Summary(pl):	Przeglądarka obrazków dla framebuffera
Name:		fbv
Version:	0.96
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://s-tech.elsat.net.pl/fbv/%{name}-%{version}.tar.gz
# Source0-md5:	d1c0658681498b8d4ba782d582d4e66b
Patch0:		%{name}-libs.patch
URL:		http://s-tech.elsat.net.pl/
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libungif-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple program to view pictures on a framebuffer console. It
supports PNG, JPEG, GIF and BMP files.

%description -l pl
Prosty program do oglądania obrazków na konsoli z framebufferem.
Obsługuje pliki PNG, JPEG, GIF i BMP.

%prep
%setup -q
%patch -p1

%build
# it's not autoconf script
./configure \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--mandir=%{_mandir}

%{__make} \
	CC="%{__cc} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
