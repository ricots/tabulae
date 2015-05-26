#!/usr/bin/env python3
doc = dict(
	tile_source_type={
		0: 'INTERNET',
		3: 'MAPNA_FILE',
		4: 'TAR',
		5: 'SQLITEDB',
		6: 'BLANK',
		},
	url_builder_type={ # if tile_source_type == 0
		0: 'OSM',
		1: 'GOOGLE',
		2: 'YANDEX',
		3: 'YANDEX.TRAFFIC',
		4: 'GOOGLE.SATTELITE',
		5: 'OPENSPACE',
		6: 'MICROSOFT',
		7: 'DOCELU.PL',
		8: 'VF_CHART',
		9: 'AVCHARTS',
		10: 'SOVIE_MILITAR_MAPS',
		11: 'VFRCB',
		12: 'USE_OW_MA_SOURCE',
		13: 'BLANK',
		},
	projection={
		1: 'MERCATO_SPHEROIDS',
		2: 'O_TH_ELLIPSOID',
		3: 'OSG_3_BRITIS_NATIONA_GRI_REFERENC_SYSTEM',
		},
	)
maps = (
	dict(
		cat="BING",
		name="Satellite",
		id="bingaero",
		descr="http://www.bing.com",
		baseurl="http://ecn.t1.tiles.virtualearth.net/tiles/a",
		image_filenameending=".jpeg?g=1134&amp;n=z",
		zoom_minlevel=1,
		zoom_maxlevel=19,
		maptile_sizepx=256,
		url_builder_type=6,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="BING",
		name="Hybrid",
		id="bingbi",
		descr="http://www.bing.com",
		baseurl="http://ecn.dynamic.t1.tiles.virtualearth.net/comp/ch/",
		image_filenameending="?mkt=en-us&amp;it=A,G,L&amp;shading=hill&amp;n=z&amp;cb=1",
		zoom_minlevel=1,
		zoom_maxlevel=19,
		maptile_sizepx=256,
		url_builder_type=6,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="BING",
		name="Road",
		id="bingmap",
		descr="http://www.bing.com",
		baseurl="http://ecn.dynamic.t3.tiles.virtualearth.net/comp/ch/",
		image_filenameending="?mkt=en-us&amp;it=G,VE,BX,L,LA&amp;shading=hill&amp;n=z&amp;cb=1",
		zoom_minlevel=1,
		zoom_maxlevel=19,
		maptile_sizepx=256,
		url_builder_type=6,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="China",
		name="微软地图",
		id="msmapchina",
		isfake="true",
		descr="",
		baseurl="http://r0.tiles.ditu.live.com/tiles/r",
		image_filenameending=".png?g=1",
		zoom_minlevel=1,
		zoom_maxlevel=18,
		maptile_sizepx=256,
		url_builder_type=6,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="FreeMap",
		name="Slovakia Autoatlas",
		id="freemapsk",
		descr="http://www.freemap.sk/",
		baseurl="http://a.freemap.sk/data/layers/presets/A/",
		image_filenameending=".jpeg",
		zoom_minlevel=0,
		zoom_maxlevel=18,
		maptile_sizepx=256,
		url_builder_type=0,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="FreeMap",
		name="Slovakia Cyclomapa",
		id="freemapskhillshade",
		descr="http://www.freemap.sk/",
		baseurl="http://a.freemap.sk/data/layers/presets/C/",
		image_filenameending=".jpeg",
		zoom_minlevel=0,
		zoom_maxlevel=18,
		maptile_sizepx=256,
		url_builder_type=0,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="FreeMap",
		name="Slovakia Turisticka",
		id="freemapskhiking",
		descr="http://www.freemap.sk/",
		baseurl="http://a.freemap.sk/data/layers/presets/T/",
		image_filenameending=".jpeg",
		zoom_minlevel=0,
		zoom_maxlevel=18,
		maptile_sizepx=256,
		url_builder_type=0,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="Google",
		name="Land",
		id="googleland",
		descr="http://maps.google.com",
		baseurl="http://mt.google.com/vt/lyrs=t@131,r@218000000&amp;",
		image_filenameending=".png",
		zoom_minlevel=0,
		zoom_maxlevel=15,
		maptile_sizepx=256,
		url_builder_type=1,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		googlescale="true",
		),
	dict(
		cat="Google",
		name="Map",
		id="googlemap",
		descr="http://maps.google.com",
		baseurl="http://mts0.google.com/vt/lyrs=m@218000000&amp;",
		image_filenameending=".png",
		zoom_minlevel=0,
		zoom_maxlevel=19,
		maptile_sizepx=256,
		url_builder_type=1,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		googlescale="true",
		),
	dict(
		cat="Google",
		name="Names",
		layer="true",
		id="googlenames",
		descr="http://maps.google.com",
		baseurl="http://mts1.google.com/vt/lyrs=h@195026035&amp;",
		image_filenameending=".png",
		zoom_minlevel=0,
		zoom_maxlevel=19,
		maptile_sizepx=256,
		url_builder_type=1,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="Google",
		name="Satellite",
		id="googlesat",
		descr="http://maps.google.com",
		baseurl="http://khms1.google.com/kh/v=140",
		image_filenameending=".png",
		zoom_minlevel=0,
		zoom_maxlevel=19,
		maptile_sizepx=256,
		url_builder_type=4,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		googlescale="true",
		),
	dict(
		cat="OSM",
		id="mtbmapa",
		name="MTB Mapa Česká republika",
		descr="http://tchor.fi.muni.cz:8080/",
		baseurl="http://tchor.fi.muni.cz:8080/mtbmap_tiles/",
		image_filenameending=".png",
		zoom_minlevel=3,
		zoom_maxlevel=18,
		maptile_sizepx=256,
		url_builder_type=0,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="Ordnance Survey",
		id="openspace",
		name="Map",
		descr="Covering the whole of Great Britain http://www.ordnancesurvey.co.uk",
		baseurl="http://openspace.ordnancesurvey.co.uk/osmapapi/ts?FORMAT=image%2Fpng&amp;KEY=6694613F8B469C97E0405F0AF160360A&amp;URL=http%3A%2F%2Fopenspace.ordnancesurvey.co.uk%2Fopenspace%2Fsupport.html&amp;SERVICE=WMS&amp;VERSION=1.1.1&amp;REQUEST=GetMap&amp;STYLES=&amp;EXCEPTIONS=application%2Fvnd.ogc.se_inimage&amp;",
		image_filenameending="",
		zoom_minlevel=7,
		zoom_maxlevel=17,
		maptile_sizepx=200,
		url_builder_type=5,
		tile_source_type=0,
		projection=3,
		yandex_traffic_on=0,
		),
	dict(
		cat="MapQuest",
		name="Hybrid",
		layer="true",
		id="mqhyb",
		descr="http://www.mapquest.com/",
		baseurl="http://mtile02.mqcdn.com/tiles/1.0.0/vx/hyb/",
		image_filenameending=".png",
		zoom_minlevel=0,
		zoom_maxlevel=18,
		maptile_sizepx=256,
		url_builder_type=0,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="MapQuest",
		name="Map",
		id="mqmap",
		descr="http://www.mapquest.com/",
		baseurl="http://mtile03.mqcdn.com/tiles/1.0.0/vx/map/",
		image_filenameending=".png",
		zoom_minlevel=0,
		zoom_maxlevel=18,
		maptile_sizepx=256,
		url_builder_type=0,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="MapQuest",
		name="Open",
		id="mqopen",
		descr="http://www.openstreetmap.org/",
		baseurl="http://otile2.mqcdn.com/tiles/1.0.0/osm/",
		image_filenameending=".png",
		zoom_minlevel=0,
		zoom_maxlevel=18,
		maptile_sizepx=256,
		url_builder_type=0,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="MapQuest",
		name="Sattelite",
		id="mqsat",
		descr="http://www.mapquest.com/",
		baseurl="http://mtile01.mqcdn.com/tiles/1.0.0/vx/sat/",
		image_filenameending=".png",
		zoom_minlevel=0,
		zoom_maxlevel=18,
		maptile_sizepx=256,
		url_builder_type=0,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="Microsoft",
		name="Hybrid",
		id="msmaphybrid",
		descr="",
		baseurl="http://h0.ortho.tiles.virtualearth.net/tiles/h",
		image_filenameending=".jpg?g=45",
		zoom_minlevel=1,
		zoom_maxlevel=19,
		maptile_sizepx=256,
		url_builder_type=6,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="Microsoft",
		name="Maps China",
		id="msmapchina",
		descr="",
		baseurl="http://r0.tiles.ditu.live.com/tiles/r",
		image_filenameending=".png?g=1",
		zoom_minlevel=1,
		zoom_maxlevel=18,
		maptile_sizepx=256,
		url_builder_type=6,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="Microsoft",
		name="Maps",
		id="msmap",
		descr="",
		baseurl="http://r0.ortho.tiles.virtualearth.net/tiles/r",
		image_filenameending=".png?g=45",
		zoom_minlevel=1,
		zoom_maxlevel=19,
		maptile_sizepx=256,
		url_builder_type=6,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="Microsoft",
		name="Virtual Earth",
		id="msmapearth",
		descr="",
		baseurl="http://a0.ortho.tiles.virtualearth.net/tiles/a",
		image_filenameending=".jpg?g=45",
		zoom_minlevel=1,
		zoom_maxlevel=19,
		maptile_sizepx=256,
		url_builder_type=6,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		enabled=False,
		cat="Cykloatlas ",
		name="Cykloatlas CZ",
		id="cykloatlas",
		descr="http://www.cykloserver.cz/cykloatlas/",
		baseurl="http://services.tmapserver.cz/stiles/gm/shc/",
		image_filenameending=".png?m=s&amp;t=1342300315&amp;k=5we6HahGpebRedkR5NxReQ",
		zoom_minlevel=7,
		zoom_maxlevel=15,
		maptile_sizepx=256,
		url_builder_type=0,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		enabled=False,
		cat="Docelu",
		name="Docelu.pl Poland",
		id="docelupl",
		descr="http://docelu.pl",
		baseurl="http://i.wp.pl/m/tiles013/",
		image_filenameending=".png",
		zoom_minlevel=2,
		zoom_maxlevel=17,
		maptile_sizepx=256,
		url_builder_type=7,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="MapABC",
		name="地图",
		id="mapabc",
		isfake="true",
		descr="",
		baseurl="http://emap0.is.autonavi.com/appmaptile?&amp;",
		image_filenameending=".gif",
		zoom_minlevel=3,
		zoom_maxlevel=17,
		maptile_sizepx=256,
		url_builder_type=1,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		enabled=False,
		cat="MyTopo",
		name="topoG",
		id="mytopo",
		descr="http://www.mytopo.com",
		baseurl="http://maps.mytopo.com/mytopoz63g9R/tilecache.py/1.0.0/topoG/",
		image_filenameending=".jpg",
		zoom_minlevel=9,
		zoom_maxlevel=15,
		maptile_sizepx=256,
		url_builder_type=0,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="Outdooractive",
		name="Map",
		id="outdooractive",
		descr="",
		baseurl="http://s3.outdooractive.com/portal/map/",
		image_filenameending=".png",
		zoom_minlevel=0,
		zoom_maxlevel=18,
		maptile_sizepx=256,
		url_builder_type=0,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="QQ",
		name="地图",
		id="qqmap",
		isfake="true",
		descr="",
		baseurl="http://p1.map.qq.com/maptiles/",
		image_filenameending="png",
		zoom_minlevel=4,
		zoom_maxlevel=17,
		maptile_sizepx=256,
		url_builder_type=7,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="map4freerel",
		name="Relief map",
		id="map4freerel",
		descr="http://maps.peterrobins.co.uk/",
		baseurl="http://maps-for-free.com/layer/relief/z{z}/row{y}/{z}_{x}-{y}.jpg",
		image_filenameending="",
		zoom_minlevel=0,
		zoom_maxlevel=11,
		maptile_sizepx=256,
		url_builder_type=12,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="waw",
		name="UMP-pcPL Poland",
		id="ump_pcpl",
		descr="http://ump.waw.pl",
		baseurl="http://1.tiles.ump.waw.pl/ump_tiles/",
		image_filenameending=".png",
		zoom_minlevel=0,
		zoom_maxlevel=18,
		maptile_sizepx=256,
		url_builder_type=0,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="NLS",
		name="Ordnance Survey Map",
		id="osm",
		descr="National Library of Scotland http://geo.nls.uk",
		baseurl="http://geo.nls.uk/maps/opendata/",
		image_filenameending=".png",
		zoom_minlevel=1,
		zoom_maxlevel=16,
		maptile_sizepx=256,
		url_builder_type=0,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="OSM",
		name="Admin Boundaties",
		layer="true",
		id="osmadmin",
		descr="http://openmapsurfer.uni-hd.de",
		baseurl="http://129.206.74.245:8007/tms_b.ashx?x=",
		image_filenameending="",
		zoom_minlevel=0,
		zoom_maxlevel=18,
		maptile_sizepx=256,
		url_builder_type=2,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="OSM",
		name="ASTER GDEM &amp; SRTM Hillshade",
		layer="true",
		id="osmhill",
		descr="http://openmapsurfer.uni-hd.de",
		baseurl="http://129.206.74.245:8004/tms_hs.ashx?x=",
		image_filenameending="",
		zoom_minlevel=0,
		zoom_maxlevel=18,
		maptile_sizepx=256,
		url_builder_type=2,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="OSM",
		name="ASTER GDEM Contour Lines (14-18)",
		layer="true",
		id="osmcont",
		descr="On zoom 14-18 http://openmapsurfer.uni-hd.de",
		baseurl="http://129.206.74.245:8006/tms_il.ashx?x=",
		image_filenameending="",
		zoom_minlevel=13,
		zoom_maxlevel=16,
		maptile_sizepx=256,
		url_builder_type=2,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		enabled=False,
		cat="OSM",
		name="Cloudmade (Fresh)",
		id="cloudmade997",
		descr="http://cloudmade.com",
		baseurl="http://c.tile.cloudmade.com/BC9A493B41014CAABB98F0471D759707/997@2x/256/",
		image_filenameending=".png",
		zoom_minlevel=0,
		zoom_maxlevel=18,
		maptile_sizepx=256,
		url_builder_type=0,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		enabled=False,
		cat="OSM",
		name="Cloudmade (Midnight Commander)",
		id="cloudmade999",
		descr="http://cloudmade.com",
		baseurl="http://c.tile.cloudmade.com/BC9A493B41014CAABB98F0471D759707/999@2x/256/",
		image_filenameending=".png",
		zoom_minlevel=0,
		zoom_maxlevel=18,
		maptile_sizepx=256,
		url_builder_type=0,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		enabled=False,
		cat="OSM",
		name="Cloudmade (Pale Dawn)",
		id="cloudmade998",
		descr="http://cloudmade.com",
		baseurl="http://c.tile.cloudmade.com/BC9A493B41014CAABB98F0471D759707/998@2x/256/",
		image_filenameending=".png",
		zoom_minlevel=0,
		zoom_maxlevel=18,
		maptile_sizepx=256,
		url_builder_type=0,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		enabled=False,
		cat="OSM",
		name="Cloudmade (Red Alert)",
		id="cloudmade8",
		descr="http://cloudmade.com",
		baseurl="http://c.tile.cloudmade.com/BC9A493B41014CAABB98F0471D759707/8@2x/256/",
		image_filenameending=".png",
		zoom_minlevel=0,
		zoom_maxlevel=18,
		maptile_sizepx=256,
		url_builder_type=0,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		enabled=False,
		cat="OSM",
		name="Cloudmade (Standard tiles)",
		id="cloudmadest",
		descr="http://cloudmade.com",
		baseurl="http://tile.cloudmade.com/BC9A493B41014CAABB98F0471D759707/2@2x/256/",
		image_filenameending=".png",
		zoom_minlevel=0,
		zoom_maxlevel=18,
		maptile_sizepx=256,
		url_builder_type=0,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="OSM",
		name="Cycle",
		id="osmcyc",
		descr="http://www.openstreetmap.org/",
		baseurl="http://a.tile.opencyclemap.org/cycle/",
		image_filenameending=".png",
		zoom_minlevel=0,
		zoom_maxlevel=18,
		maptile_sizepx=256,
		url_builder_type=0,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		enabled=False,
		cat="OSM",
		name="Cycle Map",
		id="cyclemap",
		descr="",
		baseurl="http://b.tile.cloudmade.com/BC9A493B41014CAABB98F0471D759707/1/256/",
		image_filenameending=".png",
		zoom_minlevel=0,
		zoom_maxlevel=17,
		maptile_sizepx=256,
		url_builder_type=0,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="OSM",
		name="Hike &amp; Bike Map",
		id="osmhikin",
		descr="OpenStreetMap Hiking (Germany only) http://hikebikemap.de/",
		baseurl="http://openpistemap.org/tiles/contours/",
		image_filenameending=".png",
		zoom_minlevel=0,
		zoom_maxlevel=18,
		maptile_sizepx=256,
		url_builder_type=0,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="OSM",
		name="Hiking Germany",
		id="osmhikingger",
		descr="OpenStreetMap Hiking (Germany only) http://hikebikemap.de/",
		baseurl="http://toolserver.org/tiles/hikebike/",
		image_filenameending=".png",
		zoom_minlevel=0,
		zoom_maxlevel=18,
		maptile_sizepx=256,
		url_builder_type=0,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="OSM",
		name="Hillshading NASA SRTM3 v2",
		layer="true",
		id="osmdenasa",
		descr="OpenStreetMap Hiking (Germany only) http://hikebikemap.de/",
		baseurl="http://toolserver.org/~cmarqu/hill/",
		image_filenameending=".png",
		zoom_minlevel=0,
		zoom_maxlevel=18,
		maptile_sizepx=256,
		url_builder_type=0,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="OSM",
		name="Lonvia's Hiking Symbols",
		layer="true",
		id="osmdelonv",
		descr="OpenStreetMap Hiking (Germany only) http://hikebikemap.de/",
		baseurl="http://tile.lonvia.de/hiking/",
		image_filenameending=".png",
		zoom_minlevel=0,
		zoom_maxlevel=18,
		maptile_sizepx=256,
		url_builder_type=0,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="OSM",
		name="OpenSeaMap",
		id="seamap",
		descr="http://map.openseamap.org//",
		baseurl="http://osm1.wtnet.de/tiles/base/",
		image_filenameending=".png",
		zoom_minlevel=0,
		zoom_maxlevel=18,
		maptile_sizepx=256,
		url_builder_type=0,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="OSM",
		name="Public Transport",
		id="osmpublictransport",
		descr="OpenStreetMap Hiking (Germany only) http://hikebikemap.de/",
		baseurl="http://tile.xn--pnvkarte-m4a.de/tilegen/",
		image_filenameending=".png",
		zoom_minlevel=0,
		zoom_maxlevel=18,
		maptile_sizepx=256,
		url_builder_type=0,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="OSM",
		name="Roads.Grauscale",
		id="opmrg",
		descr="http://openmapsurfer.uni-hd.de",
		baseurl="http://129.206.74.245:8008/tms_rg.ashx?x=",
		image_filenameending="",
		zoom_minlevel=0,
		zoom_maxlevel=18,
		maptile_sizepx=256,
		url_builder_type=2,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="OSM",
		name="Roads",
		id="opmr",
		descr="http://openmapsurfer.uni-hd.de",
		baseurl="http://129.206.74.245:8001/tms_r.ashx?x=",
		image_filenameending="",
		zoom_minlevel=0,
		zoom_maxlevel=18,
		maptile_sizepx=256,
		url_builder_type=2,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="OSM",
		name="SeaMark",
		layer="true",
		id="seamark",
		descr="http://map.openseamap.org//",
		baseurl="http://t1.openseamap.org/seamark/",
		image_filenameending=".png",
		zoom_minlevel=0,
		zoom_maxlevel=18,
		maptile_sizepx=256,
		url_builder_type=0,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="OSM",
		name="Semitransparent",
		layer="true",
		id="osmsemi",
		descr="http://openmapsurfer.uni-hd.de",
		baseurl="http://129.206.74.245:8003/tms_h.ashx?x=",
		image_filenameending="",
		zoom_minlevel=0,
		zoom_maxlevel=18,
		maptile_sizepx=256,
		url_builder_type=2,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="OSM",
		name="Standard",
		id="mapnik",
		descr="http://www.openstreetmap.org/",
		baseurl="http://tile.openstreetmap.org/",
		image_filenameending=".png",
		zoom_minlevel=0,
		zoom_maxlevel=18,
		maptile_sizepx=256,
		url_builder_type=0,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="OSM",
		name="Transport",
		id="osmtran",
		descr="http://www.openstreetmap.org/",
		baseurl="http://c.tile2.opencyclemap.org/transport/",
		image_filenameending=".png",
		zoom_minlevel=0,
		zoom_maxlevel=18,
		maptile_sizepx=256,
		url_builder_type=0,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="Refuges",
		name="maps",
		id="refuges",
		descr="",
		baseurl="http://maps.refuges.info/tiles/renderer.py/hiking/",
		image_filenameending=".jpeg",
		zoom_minlevel=0,
		zoom_maxlevel=18,
		maptile_sizepx=256,
		url_builder_type=0,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="Soviet Military",
		name="Maps 2",
		id="smm2",
		descr="http://www.marshruty.ru/",
		baseurl="http://maps.marshruty.ru/ml.ashx?al=1&amp;i=1&amp;x=",
		image_filenameending="",
		zoom_minlevel=8,
		zoom_maxlevel=13,
		maptile_sizepx=256,
		url_builder_type=2,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="Soviet Military",
		name="Maps",
		id="smm",
		descr="http://www.topomapper.com/",
		baseurl="http://maps2.atlogis.com/cgi-bin/tilecache-2.11/tilecache.py/1.0.0/topomapper_gmerc/",
		image_filenameending=".jpg",
		zoom_minlevel=0,
		zoom_maxlevel=13,
		maptile_sizepx=256,
		url_builder_type=0,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="Statkart Norway",
		name="Sj&#248;kart (Norway)",
		id="statkartsjo",
		descr="Sea map of Norway",
		baseurl="http://opencache.statkart.no/gatekeeper/gk/gk.open_ve?layers=sjo_hovedkart2&amp;format=image/png&amp;quadkey=",
		image_filenameending="",
		zoom_minlevel=0,
		zoom_maxlevel=19,
		maptile_sizepx=256,
		url_builder_type=6,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="Statkart Norway",
		name="Topo2 (Norway)",
		id="statkarttopo2",
		descr="Topographic map of Norway",
		baseurl="http://opencache.statkart.no/gatekeeper/gk/gk.open_ve?layers=topo2&amp;format=image/png&amp;quadkey=",
		image_filenameending="",
		zoom_minlevel=0,
		zoom_maxlevel=19,
		maptile_sizepx=256,
		url_builder_type=6,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="Topo3",
		name="Wanderreitkarten",
		id="wanderreitkarten",
		descr="http://www.wanderreitkarte.de/",
		baseurl="http://topo3.wanderreitkarte.de/topo/",
		image_filenameending=".png",
		zoom_minlevel=1,
		zoom_maxlevel=19,
		maptile_sizepx=256,
		url_builder_type=0,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="USA ArcGIS",
		name="Imagery",
		id="arcing",
		descr="http://www.arcgis.com/home/webmap/viewer.html",
		baseurl="http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
		image_filenameending="",
		zoom_minlevel=0,
		zoom_maxlevel=15,
		maptile_sizepx=256,
		url_builder_type=12,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="USA ArcGIS",
		name="Light Gray Canvas",
		id="arcgray",
		descr="http://www.arcgis.com/home/webmap/viewer.html",
		baseurl="http://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}",
		image_filenameending="",
		zoom_minlevel=0,
		zoom_maxlevel=15,
		maptile_sizepx=256,
		url_builder_type=12,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="USA ArcGIS",
		name="National Geographic",
		id="arcnat",
		descr="http://www.arcgis.com/home/webmap/viewer.html",
		baseurl="http://server.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer/tile/{z}/{y}/{x}",
		image_filenameending="",
		zoom_minlevel=0,
		zoom_maxlevel=15,
		maptile_sizepx=256,
		url_builder_type=12,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="USA ArcGIS",
		name="Oceans",
		id="arcocn",
		descr="http://www.arcgis.com/home/webmap/viewer.html",
		baseurl="http://server.arcgisonline.com/ArcGIS/rest/services/Ocean_Basemap/MapServer/tile/{z}/{y}/{x}",
		image_filenameending="",
		zoom_minlevel=0,
		zoom_maxlevel=13,
		maptile_sizepx=256,
		url_builder_type=12,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="USA ArcGIS",
		name="Streets",
		id="arcstr",
		descr="http://www.arcgis.com/home/webmap/viewer.html",
		baseurl="http://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}",
		image_filenameending="",
		zoom_minlevel=0,
		zoom_maxlevel=15,
		maptile_sizepx=256,
		url_builder_type=12,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="USA ArcGIS",
		name="Topographic",
		id="arctopo",
		descr="http://www.arcgis.com/home/webmap/viewer.html",
		baseurl="http://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}",
		image_filenameending="",
		zoom_minlevel=0,
		zoom_maxlevel=15,
		maptile_sizepx=256,
		url_builder_type=12,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="USA ArcGIS",
		name="Topo maps",
		id="usatopo",
		descr="http://www.arcgis.com/home/webmap/viewer.html",
		baseurl="http://server.arcgisonline.com/ArcGIS/rest/services/USA_Topo_Maps/MapServer/tile/{z}/{y}/{x}",
		image_filenameending="",
		zoom_minlevel=0,
		zoom_maxlevel=15,
		maptile_sizepx=256,
		url_builder_type=12,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="USGS",
		name="Hydro-NHD",
		id="usggydro",
		descr="http://www.nationalmap.gov",
		baseurl="http://basemap.nationalmap.gov/ArcGIS/rest/services/NHD_Small/MapServer/tile/{z}/{y}/{x}",
		image_filenameending="",
		zoom_minlevel=0,
		zoom_maxlevel=9,
		maptile_sizepx=256,
		url_builder_type=12,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="USGS",
		name="Labels",
		layer="true",
		id="usgslbl",
		descr="http://www.nationalmap.gov",
		baseurl="http://basemap.nationalmap.gov/ArcGIS/rest/services/TNM_Vector_Small/MapServer/tile/{z}/{y}/{x}",
		image_filenameending="",
		zoom_minlevel=0,
		zoom_maxlevel=19,
		maptile_sizepx=256,
		url_builder_type=12,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="USGS",
		name="Topo",
		id="usgstopo",
		descr="http://www.nationalmap.gov",
		baseurl="http://basemap.nationalmap.gov/ArcGIS/rest/services/USGSTopo/MapServer/tile/{z}/{y}/{x}",
		image_filenameending="",
		zoom_minlevel=0,
		zoom_maxlevel=15,
		maptile_sizepx=256,
		url_builder_type=12,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="VFR Charts",
		name="Area Charts",
		id="vfrcbenra",
		descr="http://www.chartbundle.com/",
		baseurl="http://wms.chartbundle.com/tms/1.0.0/enra/",
		image_filenameending=".png",
		zoom_minlevel=0,
		zoom_maxlevel=13,
		maptile_sizepx=256,
		url_builder_type=11,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="VFR Charts",
		name="by avcharts",
		id="vfr_avcharts",
		descr="www.avcharts.com",
		baseurl="http://s3.amazonaws.com/AvCharts/tiles/",
		image_filenameending=".png",
		zoom_minlevel=0,
		zoom_maxlevel=11,
		maptile_sizepx=256,
		url_builder_type=9,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="VFR Charts",
		name="Enroute High Charts",
		id="vfrcbenrh",
		descr="http://www.chartbundle.com/",
		baseurl="http://wms.chartbundle.com/tms/1.0.0/enrh/",
		image_filenameending=".png",
		zoom_minlevel=0,
		zoom_maxlevel=13,
		maptile_sizepx=256,
		url_builder_type=11,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="VFR Charts",
		name="Enroute Low Charts",
		id="vfrcbenrl",
		descr="http://www.chartbundle.com/",
		baseurl="http://wms.chartbundle.com/tms/1.0.0/enrl/",
		image_filenameending=".png",
		zoom_minlevel=0,
		zoom_maxlevel=13,
		maptile_sizepx=256,
		url_builder_type=11,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="VFR Charts",
		name="Sectional Charts",
		id="cbsec",
		descr="http://www.chartbundle.com/",
		baseurl="http://wms.chartbundle.com/tms/1.0.0/sec/",
		image_filenameending=".png",
		zoom_minlevel=0,
		zoom_maxlevel=13,
		maptile_sizepx=256,
		url_builder_type=11,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="VFR Charts",
		name="Sectional Charts with Grid",
		id="vfrcbsecgrids",
		descr="http://www.chartbundle.com/",
		baseurl="http://wms.chartbundle.com/tms/1.0.0/secgrids/",
		image_filenameending=".png",
		zoom_minlevel=0,
		zoom_maxlevel=13,
		maptile_sizepx=256,
		url_builder_type=11,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="VFR Charts",
		name="Terminal Area Charts",
		id="vfrcbtac",
		descr="http://www.chartbundle.com/",
		baseurl="http://wms.chartbundle.com/tms/1.0.0/tac/",
		image_filenameending=".png",
		zoom_minlevel=0,
		zoom_maxlevel=13,
		maptile_sizepx=256,
		url_builder_type=11,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="VFR Charts",
		name="Terminal Area Charts with Grid",
		id="vfrcbtacgrids",
		descr="http://www.chartbundle.com/",
		baseurl="http://wms.chartbundle.com/tms/1.0.0/tacgrids/",
		image_filenameending=".png",
		zoom_minlevel=0,
		zoom_maxlevel=13,
		maptile_sizepx=256,
		url_builder_type=11,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="VFR Charts",
		name="World Aeronautical Charts",
		id="vfrcbwac",
		descr="http://www.chartbundle.com/",
		baseurl="http://wms.chartbundle.com/tms/1.0.0/wac/",
		image_filenameending=".png",
		zoom_minlevel=0,
		zoom_maxlevel=13,
		maptile_sizepx=256,
		url_builder_type=11,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="VFR Charts",
		name="World Aeronautical Charts with Grid",
		id="vfrcbwacgrids",
		descr="http://www.chartbundle.com/",
		baseurl="http://wms.chartbundle.com/tms/1.0.0/wacgrids/",
		image_filenameending=".png",
		zoom_minlevel=0,
		zoom_maxlevel=13,
		maptile_sizepx=256,
		url_builder_type=11,
		tile_source_type=0,
		projection=1,
		yandex_traffic_on=0,
		),
	dict(
		cat="Yandex",
		name="Haritalar.Hybrid",
		layer="true",
		id="yaharhyb",
		descr="http://harita.yandex.com.tr",
		baseurl="http://vec01.maps.yandex.net/tiles?l=skl&amp;v=2.29.0&amp;x=",
		image_filenameending="&amp;lang=tr_TR",
		zoom_minlevel=0,
		zoom_maxlevel=17,
		maptile_sizepx=256,
		url_builder_type=2,
		tile_source_type=0,
		projection=2,
		yandex_traffic_on=0,
		),
	dict(
		cat="Yandex",
		name="Haritalar.Map",
		id="yaharmap",
		descr="http://harita.yandex.com.tr",
		baseurl="http://vec.maps.yandex.net/tiles?l=map&amp;v=2.29.0&amp;x=",
		image_filenameending="&amp;lang=tr_TR",
		zoom_minlevel=0,
		zoom_maxlevel=17,
		maptile_sizepx=256,
		url_builder_type=2,
		tile_source_type=0,
		projection=2,
		yandex_traffic_on=0,
		),
	dict(
		cat="Yandex",
		name="Haritalar.Sattelite",
		id="yaharsat",
		descr="http://harita.yandex.com.tr",
		baseurl="http://sat02.maps.yandex.net/tiles?l=sat&amp;v=1.35.0&amp;x=",
		image_filenameending="&amp;lang=tr_TR",
		zoom_minlevel=0,
		zoom_maxlevel=17,
		maptile_sizepx=256,
		url_builder_type=2,
		tile_source_type=0,
		projection=2,
		yandex_traffic_on=0,
		),
	dict(
		cat="Yandex",
		name="Hybrid",
		layer="true",
		id="yandexhyb",
		descr="http://maps.yandex.ru",
		baseurl="http://vec01.maps.yandex.net/tiles?l=skl&amp;v=2.31.1&amp;x=",
		image_filenameending="",
		zoom_minlevel=0,
		zoom_maxlevel=17,
		maptile_sizepx=256,
		url_builder_type=2,
		tile_source_type=0,
		projection=2,
		yandex_traffic_on=0,
		),
	dict(
		cat="Yandex",
		name="Map",
		id="yandexmap",
		descr="http://maps.yandex.ru",
		baseurl="http://vec.maps.yandex.net/tiles?l=map&amp;v=2.45.0&amp;x=",
		image_filenameending="",
		zoom_minlevel=0,
		zoom_maxlevel=17,
		maptile_sizepx=256,
		url_builder_type=2,
		tile_source_type=0,
		projection=2,
		yandex_traffic_on=0,
		),
	dict(
		cat="Yandex",
		name="People's",
		id="yandexpeople",
		descr="http://maps.yandex.ru",
		baseurl="http://03.pvec.maps.yandex.net/?l=pmap&amp;x=",
		image_filenameending="",
		zoom_minlevel=0,
		zoom_maxlevel=19,
		maptile_sizepx=256,
		url_builder_type=2,
		tile_source_type=0,
		projection=2,
		yandex_traffic_on=0,
		),
	dict(
		cat="Yandex",
		name="Sattelite",
		id="yandexsat",
		descr="http://maps.yandex.ru",
		baseurl="http://sat01.maps.yandex.net/tiles?l=sat&amp;v=3.102.0&amp;x=",
		image_filenameending="",
		zoom_minlevel=0,
		zoom_maxlevel=19,
		maptile_sizepx=256,
		url_builder_type=2,
		tile_source_type=0,
		projection=2,
		yandex_traffic_on=0,
		),
	dict(
		cat="Yandex",
		name="Traffic",
		id="yandexmaptraffic",
		cache="yandexmap",
		descr="http://maps.yandex.ru",
		baseurl="http://vec.maps.yandex.net/tiles?l=map&amp;v=2.45.0&amp;x=",
		image_filenameending="",
		zoom_minlevel=0,
		zoom_maxlevel=17,
		maptile_sizepx=256,
		url_builder_type=2,
		tile_source_type=0,
		projection=2,
		yandex_traffic_on=1,
		),
	dict(
		cat="Yandex",
		name="Traffic",
		timedependent="true",
		layer="true",
		id="yandextraffic",
		descr="",
		baseurl="http://jgo.maps.yandex.net/tiles?l=trf",
		image_filenameending="",
		zoom_minlevel=0,
		zoom_maxlevel=17,
		maptile_sizepx=256,
		url_builder_type=3,
		tile_source_type=0,
		projection=2,
		yandex_traffic_on=0,
		),
	dict(
		cat="Blank",
		name="Empty",
		id="blank",
		descr="",
		baseurl="",
		image_filenameending="",
		zoom_minlevel=0,
		zoom_maxlevel=20,
		maptile_sizepx=256,
		url_builder_type=13,
		tile_source_type=6,
		projection=1,
		yandex_traffic_on=0,
		),
	)

def check(baseurl, url_builder_type, image_filenameending, enabled=True, **argv):
	if enabled:
		if url_builder_type == 12:
			if image_filenameending:
				raise Exception(image_filenameending)
			url = baseurl.format(x=10, y=10, z=10, )
		return True

def xml_out(enabled=True, **argv):
	print('	<map', end=' ')
	for k in (
		'cat',
		'name',
		'timedependent',
		'layer',
		'id',
		'cache',
		'isfake',
		'descr',
		'baseurl',
		'image_filenameending',
		'zoom_minlevel',
		'zoom_maxlevel',
		'maptile_sizepx',
		'url_builder_type',
		'tile_source_type',
		'projection',
		'yandex_traffic_on',
		'googlescale',
	):
		if k in argv:
			print('{}="{}"'.format(k, argv[k]), end=' ')
	print('/>')

def main():
	print('<?xml version="1.0" encoding="UTF-8"?>')
	print('<root>')
	for map_ in maps:
		if check(**map_):
			xml_out(**map_)
	print('</root>')

if __name__ == '__main__':
	from sys import argv
	main(*argv[1:])
# vim:tw=0:nowrap
