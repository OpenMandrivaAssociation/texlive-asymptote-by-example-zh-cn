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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a tutorial written in Simplified Chinese.

