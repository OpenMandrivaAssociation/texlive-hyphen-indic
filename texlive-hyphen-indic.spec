%global tl_name hyphen-indic
%global tl_revision 78069

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Indic hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/pkg/hyphen-indic
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-indic.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Hyphenation patterns for Assamese, Bengali, Gujarati, Hindi, Kannada,
Malayalam, Marathi, Oriya, Panjabi, Tamil and Telugu for Unicode
engines.


%install -a
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-indic:
assamese loadhyph-as.tex
bengali loadhyph-bn.tex
gujarati loadhyph-gu.tex
hindi loadhyph-hi.tex
kannada loadhyph-kn.tex
malayalam loadhyph-ml.tex
marathi loadhyph-mr.tex
oriya loadhyph-or.tex
pali loadhyph-pi.tex
panjabi loadhyph-pa.tex
tamil loadhyph-ta.tex
telugu loadhyph-te.tex
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-indic:
\addlanguage{assamese}{loadhyph-as.tex}{}{1}{1}
\addlanguage{bengali}{loadhyph-bn.tex}{}{1}{1}
\addlanguage{gujarati}{loadhyph-gu.tex}{}{1}{1}
\addlanguage{hindi}{loadhyph-hi.tex}{}{1}{1}
\addlanguage{kannada}{loadhyph-kn.tex}{}{1}{1}
\addlanguage{malayalam}{loadhyph-ml.tex}{}{1}{1}
\addlanguage{marathi}{loadhyph-mr.tex}{}{1}{1}
\addlanguage{oriya}{loadhyph-or.tex}{}{1}{1}
\addlanguage{pali}{loadhyph-pi.tex}{}{1}{2}
\addlanguage{panjabi}{loadhyph-pa.tex}{}{1}{1}
\addlanguage{tamil}{loadhyph-ta.tex}{}{1}{1}
\addlanguage{telugu}{loadhyph-te.tex}{}{1}{1}
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/%{tl_name} <<'TL_HYPHEN_EOF'
-- from hyphen-indic:
['assamese'] = {
	loader = 'loadhyph-as.tex',
	lefthyphenmin = 1,
	righthyphenmin = 1,
	synonyms = {  },
	patterns = 'hyph-as.pat.txt',
},
['bengali'] = {
	loader = 'loadhyph-bn.tex',
	lefthyphenmin = 1,
	righthyphenmin = 1,
	synonyms = {  },
	patterns = 'hyph-bn.pat.txt',
},
['gujarati'] = {
	loader = 'loadhyph-gu.tex',
	lefthyphenmin = 1,
	righthyphenmin = 1,
	synonyms = {  },
	patterns = 'hyph-gu.pat.txt',
},
['hindi'] = {
	loader = 'loadhyph-hi.tex',
	lefthyphenmin = 1,
	righthyphenmin = 1,
	synonyms = {  },
	patterns = 'hyph-hi.pat.txt',
},
['kannada'] = {
	loader = 'loadhyph-kn.tex',
	lefthyphenmin = 1,
	righthyphenmin = 1,
	synonyms = {  },
	patterns = 'hyph-kn.pat.txt',
},
['malayalam'] = {
	loader = 'loadhyph-ml.tex',
	lefthyphenmin = 1,
	righthyphenmin = 1,
	synonyms = {  },
	patterns = 'hyph-ml.pat.txt',
},
['marathi'] = {
	loader = 'loadhyph-mr.tex',
	lefthyphenmin = 1,
	righthyphenmin = 1,
	synonyms = {  },
	patterns = 'hyph-mr.pat.txt',
},
['oriya'] = {
	loader = 'loadhyph-or.tex',
	lefthyphenmin = 1,
	righthyphenmin = 1,
	synonyms = {  },
	patterns = 'hyph-or.pat.txt',
},
['pali'] = {
	loader = 'loadhyph-pi.tex',
	lefthyphenmin = 1,
	righthyphenmin = 2,
	synonyms = {  },
	patterns = 'hyph-pi.pat.txt',
},
['panjabi'] = {
	loader = 'loadhyph-pa.tex',
	lefthyphenmin = 1,
	righthyphenmin = 1,
	synonyms = {  },
	patterns = 'hyph-pa.pat.txt',
},
['tamil'] = {
	loader = 'loadhyph-ta.tex',
	lefthyphenmin = 1,
	righthyphenmin = 1,
	synonyms = {  },
	patterns = 'hyph-ta.pat.txt',
},
['telugu'] = {
	loader = 'loadhyph-te.tex',
	lefthyphenmin = 1,
	righthyphenmin = 1,
	synonyms = {  },
	patterns = 'hyph-te.pat.txt',
},
TL_HYPHEN_EOF
