#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ([2.64])
AC_INIT([user-session-units], [8], [auke-jan.h.kok@intel.com])
AM_INIT_AUTOMAKE([])
AC_CONFIG_FILES([Makefile])
AC_PROG_CC

# Systemd is required, obviously
PKG_CHECK_MODULES([SYSTEMD], [systemd])

SYSTEMDSYSTEMUNITDIR="`$PKG_CONFIG --variable=systemdsystemunitdir systemd`"
AC_SUBST(SYSTEMDSYSTEMUNITDIR)
SYSTEMDUSERUNITDIR="`$PKG_CONFIG --variable=systemduserunitdir systemd`"
AC_SUBST(SYSTEMDUSERUNITDIR)
SYSTEMDUTILDIR="`$PKG_CONFIG --variable=systemdutildir systemd`"
AC_SUBST(SYSTEMDUTILDIR)

# test for xorg-launch-helper
AC_MSG_CHECKING(for xorg-launch-helper)
if test -f "$SYSTEMDUSERUNITDIR/xorg.target" ; then
  result=yes
else
  AC_MSG_WARN([xorg-launch-helper is required for most of the units])
  result=no
fi
AC_MSG_RESULT($result)

# Check for dbus daemon path for the session bus
PKG_CHECK_MODULES([DBUS], [dbus-1])
DBUSDAEMONDIR="`$PKG_CONFIG --variable=daemondir dbus-1`"
DBUSPREFIX="`$PKG_CONFIG --variable=prefix dbus-1`"
AC_SUBST(DBUSDAEMONDIR)
AC_SUBST(DBUSPREFIX)

# these are the desktops:
# enlightenment
AC_ARG_ENABLE(enlightenment, [  --enable-enlightenment], enable_enlightenment=yes, )
AC_CHECK_PROG([E_PROG], [enlightenment_start], [`which enlightenment_start`], [/usr/bin/enlightenment_start], [], [])
AC_SUBST(E_PROG)
AM_CONDITIONAL(HAVE_E, test x$enable_enlightenment = xyes)

# xfce
AC_ARG_ENABLE(xfce, [  --enable-xfce],enable_xfce=yes, )
AM_CONDITIONAL(HAVE_XFCE, test x$enable_xfce = xyes)
AC_CHECK_PROG([XFCE_PROG], [xfce4-session], [`which xfce4-session`], [/usr/bin/xfce4-session], [], [])
AC_CHECK_PROG([XFWM_PROG], [xfwm4], [`which xfwm4`], [/usr/bin/xfwm4], [], [])
AC_SUBST(XFCE_PROG)
AC_SUBST(XFWM_PROG)

# xbmc

AC_CHECK_PROG([XBMC_PROG], [xbmc-standalone], [`which xbmc-standalone`], [], [], [])
AC_SUBST(XBMC_PROG)
AM_CONDITIONAL([HAVE_XBMC], [test -n "$XBMC_PROG"])

AC_ARG_ENABLE(gnome, [  --enable-gnome], enable_gnome=yes, )
AM_CONDITIONAL(HAVE_GNOME, test x$enable_gnome = xyes)
AC_CHECK_PROG([GNOME_PROG], [gnome-session], [`which gnome-session`], [/usr/bin/gnome-session], [], [])
AC_SUBST(GNOME_PROG)

AC_CHECK_PROG([KDE_PROG], [startkde], [`which startkde`], [], [], [])
AC_SUBST(KDE_PROG)
AM_CONDITIONAL([HAVE_KDE], [test -n "$KDE_PROG"])

AC_CHECK_PROG([MYTH_PROG], [mythfrontend], [`which mythfrontend`], [], [], [])
AC_SUBST(MYTH_PROG)
AM_CONDITIONAL([HAVE_MYTH], [test -n "$MYTH_PROG"])

AC_CHECK_PROG([OPENBOX_PROG], [openbox], [`which openbox`], [], [], [])
AC_SUBST(OPENBOX_PROG)
AM_CONDITIONAL([HAVE_OPENBOX], [test -n "$OPENBOX_PROG"])

AC_CHECK_PROG([STEAM_PROG], [steam], [`which steam`], [], [], [])
AC_SUBST(STEAM_PROG)
AM_CONDITIONAL([HAVE_STEAM], [test -n "$STEAM_PROG"])

AC_OUTPUT([
units/system/user-session-launch@.service
units/system/user-session@.service
units/system/systemd-stop-user-sessions.service
units/user/dbus.socket
units/user/dbus.service
units/user/e17.target
units/user/enlightenment.service
units/user/xbmc.target
units/user/xbmc.service
units/user/xfce4-session.service
units/user/xfce4.target
units/user/xfwm4.service
units/user/gnome.target
units/user/gnome-session.service
units/user/kde.target
units/user/startkde.service
units/user/mythtv.target
units/user/mythfrontend.service
units/user/openbox.target
units/user/openbox.service
units/user/steam.target
units/user/steam.service
])
