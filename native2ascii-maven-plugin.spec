%{?_javapackages_macros:%_javapackages_macros}
%global namedreltag -beta-1
%global namedversion %{version}%{?namedreltag}
%global nameddottag  %(echo %{version}%{?namedreltag} | tr \- \. )
Name:          native2ascii-maven-plugin
Version:       1.0
Release:       0.13.beta1%{?dist}
Group:         Development/Java
Summary:       Native2Ascii Maven Plugin
License:       MIT
URL:           http://mojo.codehaus.org/%{name}/
Source0:       http://repo2.maven.org/maven2/org/codehaus/mojo/%{name}/%{namedversion}/%{name}-%{namedversion}-source-release.zip

BuildRequires: mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven:maven-project)

BuildRequires: mvn(junit:junit)

BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-invoker-plugin
BuildRequires: maven-plugin-plugin

# requires by javadoc-plugin
BuildRequires: mvn(org.apache.maven.shared:maven-invoker)
BuildRequires: mvn(org.apache.maven.shared:maven-shared-components:pom:)

BuildArch:     noarch

%description
Converts files with characters in any
supported character encoding to
one with ASCII and/or Unicode escapes.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
# fix version
%pom_xpath_replace "pom:project/pom:version" "<version>%{nameddottag}</version>" .

%pom_remove_plugin org.apache.maven.plugins:maven-invoker-plugin

%mvn_file :%{name} %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.13.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.12.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.11.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 10 2015 gil cattaneo <puntogil@libero.it> 1.0-0.10.beta1
- introduce license macro

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.9.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.0-0.8.beta1
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.7.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 05 2013 gil cattaneo <puntogil@libero.it> 1.0-0.6.beta1
- switch to XMvn
- minor changes to adapt to current guideline

* Tue Feb 19 2013 gil cattaneo <puntogil@libero.it> 1.0-0.5.beta1
- disabled invoker-plugin in f19

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.4.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0-0.3.beta1
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.2.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 04 2012 gil cattaneo <puntogil@libero.it> 1.0-0.1.beta1
- initial rpm

