Name:		texlive-cuprum
Version:	49909
Release:	1
Summary:	Cuprum font family support for LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cuprum
License:	ofl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cuprum.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cuprum.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides support for the Cuprum font family (see
http://jovanny.ru).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/cuprum
%{_texmfdistdir}/fonts/truetype/public/cuprum
%{_texmfdistdir}/fonts/tfm/public/cuprum
%{_texmfdistdir}/fonts/map/dvips/cuprum
%doc %{_texmfdistdir}/doc/fonts/cuprum

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
