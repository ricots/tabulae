package org.pyneo.maps.mapselector;

import android.app.Activity;
import android.os.Bundle;
import android.widget.ScrollView;

import org.pyneo.maps.R;

public class MapSelectorActivity extends Activity {
	private ScrollView mScrollView;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.mapselector);
		//mScrollView = (ScrollView) findViewById(R.id.GridInt);

	}

}