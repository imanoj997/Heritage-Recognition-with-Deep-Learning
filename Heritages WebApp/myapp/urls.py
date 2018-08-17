from django.conf.urls import patterns, include, url

urlpatterns = patterns('myapp.views',
    url(r'^$', 'index', name='index'),
    url(r'^list/$', 'list', name='list'),
    url(r'^bhandarkhal_tank/$', 'bhandarkhal_tank', name='bhandarkhal_tank'),
    url(r'^bhimsen_temple/$', 'bhimsen_temple', name='bhimsen_temple'),
    url(r'^char_narayan_temple/$', 'char_narayan_temple', name='char_narayan_temple'),
    url(r'^chyasing_dewal/$', 'chyasing_dewal', name='chyasing_dewal'),
    url(r'^degu_taleju_temple/$', 'degu_taleju_temple', name='degu_taleju_temple'),
    url(r'^garuda_pillar/$', 'garuda_pillar', name='garuda_pillar'),
    url(r'^keshav_narayan_temple/$', 'keshav_narayan_temple', name='keshav_narayan_temple'),
    url(r'^kopeshvara_temple/$', 'kopeshvara_temple', name='kopeshvara_temple'),
    url(r'^krishna_mandir/$', 'krishna_mandir', name='krishna_mandir'),
    url(r'^mani_chaitya/$', 'mani_chaitya', name='mani_chaitya'),
    url(r'^mani_dhara/$', 'mani_dhara', name='mani_dhara'),
    url(r'^maniganesh_temple/$', 'maniganesh_temple', name='maniganesh_temple'),
    url(r'^museuem/$', 'museuem', name='museuem'),
    url(r'^narasimha_temple/$', 'narasimha_temple', name='narasimha_temple'),
    url(r'^north_taleju_temple/$', 'north_taleju_temple', name='north_taleju_temple'),
    url(r'^south_taleju_temple/$', 'south_taleju_temple', name='south_taleju_temple'),
    url(r'^taleju_bell/$', 'taleju_bell', name='taleju_bell'),
    url(r'^tushahiti/$', 'tushahiti', name='tushahiti'),
    url(r'^yantaju_shrine/$', 'yantaju_shrine', name='yantaju_shrine'),
    url(r'^yoganarendra_pillar/$', 'yoganarendra_pillar', name='yoganarendra_pillar'),

)

