#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-activation
Version  : 1.1.1
Release  : 5
URL      : https://repo1.maven.org/maven2/javax/activation/activation/1.1.1/activation-1.1.1.jar
Source0  : https://repo1.maven.org/maven2/javax/activation/activation/1.1.1/activation-1.1.1.jar
Source1  : https://repo1.maven.org/maven2/com/sun/activation/all/1.2.0/all-1.2.0.pom
Source2  : https://repo1.maven.org/maven2/javax/activation/activation/1.1.1/activation-1.1.1.pom
Source3  : https://repo1.maven.org/maven2/javax/activation/javax.activation-api/1.2.0/javax.activation-api-1.2.0.jar
Source4  : https://repo1.maven.org/maven2/javax/activation/javax.activation-api/1.2.0/javax.activation-api-1.2.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : CDDL-1.0
Requires: mvn-activation-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-activation package.
Group: Data

%description data
data components for the mvn-activation package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/javax/activation/activation/1.1.1
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/javax/activation/activation/1.1.1/activation-1.1.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/sun/activation/all/1.2.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/sun/activation/all/1.2.0/all-1.2.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/javax/activation/activation/1.1.1
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/javax/activation/activation/1.1.1/activation-1.1.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/javax/activation/javax.activation-api/1.2.0
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/javax/activation/javax.activation-api/1.2.0/javax.activation-api-1.2.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/javax/activation/javax.activation-api/1.2.0
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/javax/activation/javax.activation-api/1.2.0/javax.activation-api-1.2.0.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/sun/activation/all/1.2.0/all-1.2.0.pom
/usr/share/java/.m2/repository/javax/activation/activation/1.1.1/activation-1.1.1.jar
/usr/share/java/.m2/repository/javax/activation/activation/1.1.1/activation-1.1.1.pom
/usr/share/java/.m2/repository/javax/activation/javax.activation-api/1.2.0/javax.activation-api-1.2.0.jar
/usr/share/java/.m2/repository/javax/activation/javax.activation-api/1.2.0/javax.activation-api-1.2.0.pom
