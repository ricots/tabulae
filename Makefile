#!/usr/bin/env make -f
.PHONY: all run clean doc dist dbg art gradle

all: src/main/res/values/strings_news.xml
	./gradlew --quiet --offline assembleRelease

run: src/main/res/values/strings_news.xml
	./gradlew --quiet assembleDebug

dbg: run
	chmod 0644 art/ic_launcher.png build/outputs/apk/*-debug.apk
	#rsync --verbose --archive build/outputs/apk/*-debug.apk littlelun.emdete.de:/var/www/pyneo.org/c/Tabulae-debug.apk
	#rsync --verbose --archive art/ic_launcher.png littlelun.emdete.de:/var/www/pyneo.org/c/Tabulae-logo.png
	adb install -r build/outputs/apk/*-debug.apk
	adb shell am start org.pyneo.tabulae/.Tabulae

clean:
	./gradlew -q clean

src/main/res/values/strings_news.xml: CHANGELOG
	awk -f $<.awk < $< > $@

