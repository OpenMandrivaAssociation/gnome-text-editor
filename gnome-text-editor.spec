Name:           gnome-text-editor
Version:        43.1
Release:        1
Group:		Editors
Summary:        GNOME Text Editor
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/GNOME/gnome-text-editor
Source:         https://download.gnome.org/sources/%{name}/41/%{name}-%{version}.tar.xz

BuildRequires:	appstream-util
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(enchant-2)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtksourceview-5)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:	pkgconfig(libpcre2-8)

%description
Text Editor is a simple text editor that focus on session
management. It works hard to keep track of changes and state even
if you quit the application. You can come back to your work even if
you've never saved it to a file.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-Ddevelopment=false
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%files -f %{name}.lang
%license COPYING
%doc NEWS README.md
%doc %{_datadir}/help/*/%{name}/
%{_bindir}/gnome-text-editor
%{_datadir}/metainfo/org.gnome.TextEditor.appdata.xml
%{_datadir}/gnome-text-editor/styles/
%{_datadir}/applications/org.gnome.TextEditor.desktop
%{_datadir}/dbus-1/services/org.gnome.TextEditor.service
%{_datadir}/glib-2.0/schemas/org.gnome.TextEditor.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
