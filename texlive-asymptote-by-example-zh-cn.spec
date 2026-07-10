%global tl_name asymptote-by-example-zh-cn
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Asymptote by example
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/asymptote-by-example-zh-cn
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/asymptote-by-example-zh-cn.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/asymptote-by-example-zh-cn.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a tutorial written in Simplified Chinese.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/doc/support
%dir %{_datadir}/texmf-dist/doc/support/asymptote-by-example-zh-cn
%dir %{_datadir}/texmf-dist/doc/support/asymptote-by-example-zh-cn/src
%dir %{_datadir}/texmf-dist/doc/support/asymptote-by-example-zh-cn/src/figure-src
%doc %{_datadir}/texmf-dist/doc/support/asymptote-by-example-zh-cn/README
%doc %{_datadir}/texmf-dist/doc/support/asymptote-by-example-zh-cn/asymptote-by-example-zh-cn.pdf
%doc %{_datadir}/texmf-dist/doc/support/asymptote-by-example-zh-cn/src/CLEAN.bat
%doc %{_datadir}/texmf-dist/doc/support/asymptote-by-example-zh-cn/src/MAKEPDF.bat
%doc %{_datadir}/texmf-dist/doc/support/asymptote-by-example-zh-cn/src/asy.bib
%doc %{_datadir}/texmf-dist/doc/support/asymptote-by-example-zh-cn/src/asymptote.sty
%doc %{_datadir}/texmf-dist/doc/support/asymptote-by-example-zh-cn/src/asysyntex.sty
%doc %{_datadir}/texmf-dist/doc/support/asymptote-by-example-zh-cn/src/cleantmp
%doc %{_datadir}/texmf-dist/doc/support/asymptote-by-example-zh-cn/src/figure-src/CJKmove.sty
%doc %{_datadir}/texmf-dist/doc/support/asymptote-by-example-zh-cn/src/figure-src/area.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-by-example-zh-cn/src/figure-src/hanoi.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-by-example-zh-cn/src/figure-src/hyper.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-by-example-zh-cn/src/figure-src/movie15.sty
%doc %{_datadir}/texmf-dist/doc/support/asymptote-by-example-zh-cn/src/figure-src/recplot.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-by-example-zh-cn/src/figure-src/stars.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-by-example-zh-cn/src/figure-src/tiling.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-by-example-zh-cn/src/figure-src/xiantu.asy
%doc %{_datadir}/texmf-dist/doc/support/asymptote-by-example-zh-cn/src/gpl-3.0.tex
%doc %{_datadir}/texmf-dist/doc/support/asymptote-by-example-zh-cn/src/main.tex
%doc %{_datadir}/texmf-dist/doc/support/asymptote-by-example-zh-cn/src/makepdf
%doc %{_datadir}/texmf-dist/doc/support/asymptote-by-example-zh-cn/src/myfonts.sty
%doc %{_datadir}/texmf-dist/doc/support/asymptote-by-example-zh-cn/src/tiling.pdf
%doc %{_datadir}/texmf-dist/doc/support/asymptote-by-example-zh-cn/src/tiling.tex
%doc %{_datadir}/texmf-dist/doc/support/asymptote-by-example-zh-cn/src/xiantu-ancient.pdf
%doc %{_datadir}/texmf-dist/doc/support/asymptote-by-example-zh-cn/src/xiantu.pdf
%doc %{_datadir}/texmf-dist/doc/support/asymptote-by-example-zh-cn/src/xiantu.tex
