# revision 25990
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-hyphen-indic
Version:	20120611
Release:	1
Summary:	Indic hyphenation patterns
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-indic.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Hyphenation patterns for Assamese, Bengali, Gujarati, Hindi,
Kannada, Malayalam, Marathi, Oriya, Panjabi, Tamil and Telugu
for Unicode engines.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%_texmf_language_dat_d/hyphen-indic
%_texmf_language_def_d/hyphen-indic
%_texmf_language_lua_d/hyphen-indic

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-indic <<EOF
\%% from hyphen-indic:
assamese loadhyph-as.tex
bengali loadhyph-bn.tex
gujarati loadhyph-gu.tex
hindi loadhyph-hi.tex
kannada loadhyph-kn.tex
malayalam loadhyph-ml.tex
marathi loadhyph-mr.tex
oriya loadhyph-or.tex
panjabi loadhyph-pa.tex
tamil loadhyph-ta.tex
telugu loadhyph-te.tex
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/hyphen-indic
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-indic <<EOF
\%% from hyphen-indic:
\addlanguage{assamese}{loadhyph-as.tex}{}{1}{1}
\addlanguage{bengali}{loadhyph-bn.tex}{}{1}{1}
\addlanguage{gujarati}{loadhyph-gu.tex}{}{1}{1}
\addlanguage{hindi}{loadhyph-hi.tex}{}{1}{1}
\addlanguage{kannada}{loadhyph-kn.tex}{}{1}{1}
\addlanguage{malayalam}{loadhyph-ml.tex}{}{1}{1}
\addlanguage{marathi}{loadhyph-mr.tex}{}{1}{1}
\addlanguage{oriya}{loadhyph-or.tex}{}{1}{1}
\addlanguage{panjabi}{loadhyph-pa.tex}{}{1}{1}
\addlanguage{tamil}{loadhyph-ta.tex}{}{1}{1}
\addlanguage{telugu}{loadhyph-te.tex}{}{1}{1}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/hyphen-indic
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-indic <<EOF
-- from hyphen-indic:
	['assamese'] = {
		loader = 'loadhyph-as.tex',
		lefthyphenmin = 1,
		righthyphenmin = 1,
		synonyms = {  },
		patterns = 'hyph-as.pat.txt',
		hyphenation = '',
	},
	['bengali'] = {
		loader = 'loadhyph-bn.tex',
		lefthyphenmin = 1,
		righthyphenmin = 1,
		synonyms = {  },
		patterns = 'hyph-bn.pat.txt',
		hyphenation = '',
	},
	['gujarati'] = {
		loader = 'loadhyph-gu.tex',
		lefthyphenmin = 1,
		righthyphenmin = 1,
		synonyms = {  },
		patterns = 'hyph-gu.pat.txt',
		hyphenation = '',
	},
	['hindi'] = {
		loader = 'loadhyph-hi.tex',
		lefthyphenmin = 1,
		righthyphenmin = 1,
		synonyms = {  },
		patterns = 'hyph-hi.pat.txt',
		hyphenation = '',
	},
	['kannada'] = {
		loader = 'loadhyph-kn.tex',
		lefthyphenmin = 1,
		righthyphenmin = 1,
		synonyms = {  },
		patterns = 'hyph-kn.pat.txt',
		hyphenation = '',
	},
	['malayalam'] = {
		loader = 'loadhyph-ml.tex',
		lefthyphenmin = 1,
		righthyphenmin = 1,
		synonyms = {  },
		patterns = 'hyph-ml.pat.txt',
		hyphenation = '',
	},
	['marathi'] = {
		loader = 'loadhyph-mr.tex',
		lefthyphenmin = 1,
		righthyphenmin = 1,
		synonyms = {  },
		patterns = 'hyph-mr.pat.txt',
		hyphenation = '',
	},
	['oriya'] = {
		loader = 'loadhyph-or.tex',
		lefthyphenmin = 1,
		righthyphenmin = 1,
		synonyms = {  },
		patterns = 'hyph-or.pat.txt',
		hyphenation = '',
	},
	['panjabi'] = {
		loader = 'loadhyph-pa.tex',
		lefthyphenmin = 1,
		righthyphenmin = 1,
		synonyms = {  },
		patterns = 'hyph-pa.pat.txt',
		hyphenation = '',
	},
	['tamil'] = {
		loader = 'loadhyph-ta.tex',
		lefthyphenmin = 1,
		righthyphenmin = 1,
		synonyms = {  },
		patterns = 'hyph-ta.pat.txt',
		hyphenation = '',
	},
	['telugu'] = {
		loader = 'loadhyph-te.tex',
		lefthyphenmin = 1,
		righthyphenmin = 1,
		synonyms = {  },
		patterns = 'hyph-te.pat.txt',
		hyphenation = '',
	},
EOF
