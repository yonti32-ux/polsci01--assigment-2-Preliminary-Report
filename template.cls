\NeedsTeXFormat{LaTeX2e}
% Shared visual system. Keep chapter content in chapters/, not in this class.
% Build with LuaLaTeX, Biber, then LuaLaTeX twice (or use build.ps1).
\ProvidesClass{template}[2026/11/21 v1.0 Burgundy purple and cream Hebrew report]
\LoadClass[12pt,a4paper,oneside,openany]{book}
\RequirePackage{iftex}
\ifLuaTeX\else\ClassError{template}{Use LuaLaTeX to build this report}{}\fi
\RequirePackage[margin=25mm,right=30mm,headheight=18pt]{geometry}
\RequirePackage{fontspec}
\RequirePackage{polyglossia}
\setdefaultlanguage{hebrew}
\setotherlanguage{english}
% Ligatures=TeX turns -- into an en-dash and --- into an em-dash in every font,
% not only the main one (\newfontfamily does not add it by default).
\defaultfontfeatures{Ligatures=TeX}
% OFL fonts are bundled: no system font installation is required.
\setmainfont{NotoSans-Regular.ttf}[Path=fonts/,BoldFont=NotoSans-Bold.ttf,
  ItalicFont=NotoSans-Italic.ttf,BoldItalicFont=NotoSans-BoldItalic.ttf]
\newfontfamily\englishfont{NotoSans-Regular.ttf}[Path=fonts/,BoldFont=NotoSans-Bold.ttf,
  ItalicFont=NotoSans-Italic.ttf,BoldItalicFont=NotoSans-BoldItalic.ttf]
% Hebrew emphasis stays upright; there are no simulated italic outlines.
\newfontfamily\hebrewfont{NotoSansHebrew-Regular.ttf}[Path=fonts/,Script=Hebrew,
  BoldFont=NotoSansHebrew-Bold.ttf,ItalicFont=NotoSansHebrew-Regular.ttf,
  BoldItalicFont=NotoSansHebrew-Bold.ttf]
\newfontfamily\hebrewfontsf{NotoSansHebrew-Regular.ttf}[Path=fonts/,Script=Hebrew,
  BoldFont=NotoSansHebrew-Bold.ttf]
\newfontfamily\hebrewfonttt{NotoSansHebrew-Regular.ttf}[Path=fonts/,Script=Hebrew]
\newfontfamily\headingfont{NotoSansHebrew-CondensedBold.ttf}[Path=fonts/,Script=Hebrew,
  BoldFont=NotoSansHebrew-CondensedBold.ttf]
\RequirePackage{amsmath,amssymb,graphicx,booktabs,array}
\RequirePackage[dvipsnames]{xcolor}
\definecolor{accent}{HTML}{820000}
\definecolor{secondary}{HTML}{330F53}
\definecolor{cream}{HTML}{FCFBF4}
\colorlet{accentlight}{cream}
\definecolor{ink}{HTML}{242126}
\colorlet{muted}{ink!65}
\RequirePackage{tikz}
\usetikzlibrary{positioning,arrows.meta,calc}
\RequirePackage{etoolbox,setspace,needspace,longtable}
\RequirePackage[most]{tcolorbox}
\RequirePackage{fancyhdr}
\RequirePackage[backend=biber,style=numeric,sorting=none,maxbibnames=6,language=english]{biblatex}
\DeclareLanguageMapping{hebrew}{english}
\RequirePackage[unicode,colorlinks,linkcolor=secondary,citecolor=accent,urlcolor=secondary]{hyperref}
\RequirePackage{bookmark}
\onehalfspacing
\color{ink}
\raggedbottom
% Keep pages containing only figures/tables aligned with the text area.
\setlength{\@fptop}{0pt}
\renewcommand{\topfraction}{0.85}
\renewcommand{\bottomfraction}{0.6}
\renewcommand{\textfraction}{0.1}
\renewcommand{\floatpagefraction}{0.75}
\setcounter{topnumber}{3}
\setcounter{totalnumber}{4}
\clubpenalty=10000
\widowpenalty=10000
\displaywidowpenalty=10000
\setlength{\parindent}{0pt}
\setlength{\parskip}{5pt plus 1pt}
\setlength{\emergencystretch}{3em}
\setcounter{tocdepth}{2}
\setcounter{secnumdepth}{2}
\renewcommand{\arraystretch}{1.3}
\setlength{\tabcolsep}{4pt}
% Captions follow the chapter counters; chapter sources place table captions
% above tables and figure captions below figures.
\long\def\@makecaption#1#2{%
  \vskip\abovecaptionskip
  {\small\setstretch{1.1}\centering
    {\color{secondary}\bfseries #1}\enspace #2\par}%
  \vskip\belowcaptionskip}
% Isolate inline English as one directional unit. Long terms in narrow table
% cells may wrap inside an English paragraph rather than crossing cell borders.
\newsavebox{\template@englishbox}
\newcommand{\en}[1]{\leavevmode%
  \sbox{\template@englishbox}{\textenglish{#1}}%
  \ifdim\wd\template@englishbox>\linewidth
    \parbox[t]{\linewidth}{\selectlanguage{english}\raggedright #1}%
  \else\usebox{\template@englishbox}\fi}
\pdfstringdefDisableCommands{\def\en#1{#1}\def\LR#1{#1}}
\providecommand{\LR}[1]{\textenglish{#1}}
% Measure tables without shrinking their text. Wide tables must be fixed
% in their chapter source, and build.ps1 treats this warning as an error.
\newsavebox{\template@tablebox}
\BeforeBeginEnvironment{tabular}{\begin{lrbox}{\template@tablebox}}
\AfterEndEnvironment{tabular}{\end{lrbox}%
  \ifdim\wd\template@tablebox>\linewidth
    \ClassWarning{template}{Table wider than available line: \the\wd\template@tablebox\space > \the\linewidth. Fix source column widths}%
  \fi
  \usebox{\template@tablebox}}
\appto\@arrayparboxrestore{\raggedleft\arraybackslash}
\def\@makechapterhead#1{\vspace*{5pt}{\parindent\z@\raggedright\normalfont
  \ifnum\c@secnumdepth>\m@ne\if@mainmatter
  {\large\color{accent}\bfseries\@chapapp\space\thechapter\par}\vskip8pt\fi\fi
  \interlinepenalty\@M\headingfont\huge\bfseries\color{accent} #1\par\nobreak\vskip22pt}}
\def\@makeschapterhead#1{\vspace*{5pt}{\parindent\z@\raggedright\normalfont
  \interlinepenalty\@M\headingfont\huge\bfseries\color{accent} #1\par\nobreak\vskip22pt}}
\renewcommand\section{\@startsection{section}{1}{\z@}%
  {-3.5ex plus -1ex minus -.2ex}{2.3ex plus .2ex}%
  {\normalfont\headingfont\Large\bfseries\color{secondary}}}
\renewcommand\subsection{\@startsection{subsection}{2}{\z@}%
  {-3.25ex plus -1ex minus -.2ex}{1.5ex plus .2ex}%
  {\normalfont\headingfont\large\bfseries\color{accent}}}
\AtBeginEnvironment{tikzpicture}{\selectlanguage{english}}
\tikzset{every node/.append style={execute at begin node=\selectlanguage{hebrew}}}
\newtcolorbox{keybox}[1]{enhanced,colback=cream,colframe=secondary,
  colbacktitle=secondary,coltitle=cream,
  boxrule=0.5pt,arc=1mm,left=3mm,right=3mm,top=2mm,bottom=2mm,
  title={\texthebrew{#1}},fonttitle=\bfseries,
  fontupper=\small\setstretch{1.15},
  before upper={\selectlanguage{hebrew}},before skip=10pt,after skip=10pt}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[R]{\small\color{secondary}\texthebrew{דת ויציבות מדינית}}
\fancyhead[L]{\small\color{muted}\textenglish{Preliminary Report}}
\fancyfoot[C]{\color{accent}\thepage}
\renewcommand{\headrulewidth}{0.4pt}
\fancypagestyle{plain}{\fancyhf{}\fancyfoot[C]{\color{accent}\thepage}\renewcommand{\headrulewidth}{0pt}}
% Book's default front matter uses Roman numerals. The project asks for
% Hebrew letters, with Arabic page numbers restarting at the main matter.
\renewcommand{\frontmatter}{\clearpage\@mainmatterfalse\pagenumbering{alph}}
\renewcommand{\mainmatter}{\clearpage\@mainmattertrue\pagenumbering{arabic}}
\pretocmd{\section}{\Needspace{6\baselineskip}}{}{}
\pretocmd{\subsection}{\Needspace{5\baselineskip}}{}{}
% Run-in paragraph headings (e.g. "שלוש אבני הדרך.") must not be stranded
% at the bottom of a page, away from the text or list that follows them.
\pretocmd{\paragraph}{\Needspace{4\baselineskip}}{}{}
\newcommand{\reporttitle}[2]{\def\rtHeb{#1}\def\rtEng{#2}}
\newcommand{\reportsubtitle}[2]{\def\rsHeb{#1}\def\rsEng{#2}}
\newcommand{\reporttype}[2]{\def\typeHeb{#1}\def\typeEng{#2}}
\newcommand{\institution}[2]{\def\instHeb{#1}\def\instEng{#2}}
\newcommand{\course}[1]{\def\courseText{#1}}
\newcommand{\semester}[1]{\def\semesterText{#1}}
\newcommand{\authors}[1]{\def\authorsText{#1}}
\newcommand{\lecturer}[1]{\def\lecturerText{#1}}
\newcommand{\submissiondate}[1]{\def\dateText{#1}}
\newcommand{\makecoverpage}{%
  \hypersetup{pageanchor=false}% cover has no page label or anchor
  \begin{titlepage}\thispagestyle{empty}
  \begin{tikzpicture}[remember picture,overlay]
    \fill[cream] (current page.north west) rectangle (current page.south east);
    \fill[accent] (current page.north east) rectangle ($(current page.south east)+(-7mm,0)$);
    \fill[secondary] ($(current page.north east)+(-7mm,0)$) rectangle ($(current page.south east)+(-9mm,0)$);
    \draw[secondary!35,line width=0.5pt] ($(current page.north west)+(15mm,-15mm)$) rectangle ($(current page.south east)+(-15mm,15mm)$);
  \end{tikzpicture}
  \centering
  {\large\instHeb\par}\textenglish{\instEng}\par
  \vspace{8mm}{\courseText\par}\semesterText\par
  \vspace{10mm}
  {\setstretch{1.1}\color{accent}\headingfont\Huge\bfseries\rtHeb\par}
  \vspace{5mm}{\large\textenglish{\rtEng}\par}
  \vspace{6mm}{\setstretch{1.15}\large\rsHeb\par}
  \vspace{3mm}{\small\textenglish{\rsEng}\par}
  \vfill
  % Original vector illustration: three arches for the three case studies.
  \begin{tikzpicture}[x=1cm,y=1cm]
    \foreach \x in {-2.1,0,2.1}{%
      \fill[accent!7] (\x-.65,0) -- (\x-.65,.95) arc[start angle=180,end angle=0,radius=.65] -- (\x+.65,0) -- cycle;
      \draw[accent,line width=1.3pt] (\x-.65,0) -- (\x-.65,.95) arc[start angle=180,end angle=0,radius=.65] -- (\x+.65,0);
      \draw[secondary,line width=.8pt] (\x-.85,0)--(\x+.85,0);}
    \draw[secondary!50,line width=.6pt] (-3.1,-.2)--(3.1,-.2);
  \end{tikzpicture}
  \vfill
  {\Large\bfseries\color{secondary}\typeHeb\par}\textenglish{\typeEng}\par
  \vspace{6mm}{\let\and\quad\authorsText\par}
  \lecturerText\par\textenglish{\dateText}\par
  \vspace{5mm}{\footnotesize\textenglish{\copyright\ 2026}\quad כל הזכויות שמורות למחברים\par}
  \end{titlepage}\hypersetup{pageanchor=true}}
\newenvironment{executivesummary}{\chapter*{תקציר מנהלים}\addcontentsline{toc}{chapter}{תקציר מנהלים}}{\par}
\newcommand{\keywords}[1]{\medskip\noindent\textbf{מילות מפתח:} #1\clearpage}
% Related constraints stay compact without reducing the body font size.
\newenvironment{reportconstraints}{\begin{itemize}%
  \setlength{\itemsep}{2pt}\setlength{\parsep}{0pt}\setlength{\parskip}{0pt}}{\end{itemize}}
\newenvironment{abbreviations}{\chapter*{קיצורים ומונחים}\addcontentsline{toc}{chapter}{קיצורים ומונחים}\small\singlespacing
  \begin{longtable}{@{}p{.19\linewidth}p{.75\linewidth}@{}}}{\end{longtable}\clearpage}
% \leavevmode first: a \color at the very start of a p-cell lands in vertical
% mode and adds \parskip above the term, pushing it below its meaning.
\newcommand{\abbr}[2]{\leavevmode{\color{secondary}\bfseries #1} & \leavevmode #2\\[5pt]}
\AtBeginBibliography{\selectlanguage{english}\small\singlespacing}
\defbibheading{bibliography}[מקורות]{\chapter*{\texthebrew{#1}}\addcontentsline{toc}{chapter}{#1}}
\endinput
