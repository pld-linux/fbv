Summary:	FrameBuffer Viewer
Summary(pl):	Przegl±darka obrazków dla framebuffera
Name:		fbv
Version:	0.99
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://s-tech.elsat.net.pl/fbv/%{name}-%{version}.tar.gz
# Source0-md5:	fd237cb79ab26d30a7f8bb526a78bd0a
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
Prosty program do ogl±dania obrazków na konsoli z framebufferem.
Obs³uguje pliki PNG, JPEG, GIF i BMP.

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
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
