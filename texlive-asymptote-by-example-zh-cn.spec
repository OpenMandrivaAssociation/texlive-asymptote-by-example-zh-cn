Name:		texlive-asymptote-by-example-zh-cn
Version:	15878
Release:	1
Summary:	Asymptote by example
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/asymptote-by-example-zh-cn
License:	gpl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/asymptote-by-example-zh-cn.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/asymptote-by-example-zh-cn.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a tutorial written in Simplified Chinese.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/support/asymptote-by-example-zh-cn

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
