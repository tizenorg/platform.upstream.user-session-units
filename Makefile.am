
systemdsystemunitdir = @SYSTEMDSYSTEMUNITDIR@
systemduserunitdir = @SYSTEMDUSERUNITDIR@

systemdsystemunit_DATA = \
	units/system/user-session@.service

systemduserunit_DATA = \
	units/user/dbus.socket \
	units/user/dbus.service

if HAVE_E
systemduserunit_DATA += \
	units/user/e17.target \
	units/user/enlightenment.service
endif

if HAVE_XBMC
systemduserunit_DATA += \
	units/user/xbmc.target \
	units/user/xbmc.service
endif

if HAVE_XFCE
systemduserunit_DATA += \
	units/user/xfce4-session.service \
	units/user/xfwm4.service \
	units/user/xfce4.target
endif


install-data-hook:
if HAVE_E
	$(mkinstalldirs) $(DESTDIR)$(SYSTEMDUSERUNITDIR)/e17.target.wants
	ln -sf ../enlightenment.service $(DESTDIR)$(SYSTEMDUSERUNITDIR)/e17.target.wants/
endif
if HAVE_XBMC
	$(mkinstalldirs) $(DESTDIR)$(SYSTEMDUSERUNITDIR)/xbmc.target.wants
	ln -sf ../xbmc.service $(DESTDIR)$(SYSTEMDUSERUNITDIR)/xbmc.target.wants/
endif
if HAVE_XFCE
	$(mkinstalldirs) $(DESTDIR)$(SYSTEMDUSERUNITDIR)/xfce4.target.wants
	ln -sf ../xfce4-session.service $(DESTDIR)$(SYSTEMDUSERUNITDIR)/xfce4.target.wants/
	ln -sf ../xfwm4.service $(DESTDIR)$(SYSTEMDUSERUNITDIR)/xfce4.target.wants/
endif
