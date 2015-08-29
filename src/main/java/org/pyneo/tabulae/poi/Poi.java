package org.pyneo.tabulae.poi;

import android.os.Bundle;
import android.util.Log;
import android.widget.Toast;
import org.mapsforge.core.graphics.Bitmap;
import org.mapsforge.core.model.LatLong;
import org.mapsforge.core.model.Point;
import org.mapsforge.map.android.graphics.AndroidGraphicFactory;
import org.mapsforge.map.layer.overlay.Marker;
import org.mapsforge.map.view.MapView;
import org.pyneo.tabulae.Base;
import org.pyneo.tabulae.R;
import org.pyneo.tabulae.Tabulae;
import org.pyneo.tabulae.storage.Storage;
import java.util.ArrayList;
import java.util.List;

public class Poi extends Base implements Constants {
	class PointAd {
		protected PoiItem pointItem;
		protected Marker marker;
		protected Bitmap bitmap;
		PointAd(final PoiItem pointItem) {
			this.pointItem = pointItem;
			MapView mapView = ((Tabulae)getActivity()).getMapView();
			if (marker != null) {
				bitmap.decrementRefCount();
				mapView.getLayerManager().getLayers().remove(marker);
				marker.onDestroy();
				marker = null;
			}
			LatLong latLong = new LatLong(pointItem.getLatitude(), pointItem.getLongitude());
			bitmap = AndroidGraphicFactory.convertToBitmap(getResources().getDrawable(R.drawable.poi_black, null));
			bitmap.incrementRefCount();
			marker = new Marker(latLong, bitmap, 0, -bitmap.getHeight() / 2) {
				@Override public boolean onTap(LatLong geoPoint, Point viewPosition, Point tapPoint) {
					if (contains(viewPosition, tapPoint)) {
						Toast.makeText(getActivity(), String.format("%s: '%s'", pointItem.getName(), pointItem.getDescription()), Toast.LENGTH_SHORT).show();
						return true;
					}
					return false;
				}
			};
			mapView.getLayerManager().getLayers().add(marker);
		}
		void onDestroy() {
			MapView mapView = ((Tabulae)getActivity()).getMapView();
			if (marker != null) {
				bitmap.decrementRefCount();
				mapView.getLayerManager().getLayers().remove(marker);
				marker.onDestroy();
				marker = null;
			}
		}
	}
	protected List<PointAd> pointsAd = new ArrayList<PointAd>();

	@Override public void onCreate(Bundle bundle) {
		if (DEBUG) Log.d(TAG, "Poi.onCreate");
		super.onCreate(bundle);
	}

	@Override public void onResume() {
		super.onResume();
		if (DEBUG) Log.d(TAG, "Poi.onResume");
		MapView mapView = ((Tabulae)getActivity()).getMapView();
		for (PoiItem pointItem: new Storage((Tabulae)getActivity()).getVisiblePoints()) {
			Log.d(TAG, "Poi.onResume pointItem=" + pointItem);
			pointsAd.add(new PointAd(pointItem));
		}
	}

	@Override public void onPause() {
		super.onPause();
		if (DEBUG) Log.d(TAG, "Poi.onPause");
		for (PointAd pointAd: pointsAd) {
			pointAd.onDestroy();
		}
		pointsAd.clear();
	}

	/*
	void center() {
		Bundle extra = new Bundle();
		extra.putBoolean("autofollow", false);
		((Tabulae)getActivity()).inform(R.id.event_autofollow, extra);
		try {
			LatLong location = mapView.getModel().mapViewPosition.getMapPosition().latLong; // TODO: sort
			BoundingBox bb = new BoundingBox(latLong.latitude, latLong.longitude, location.latitude, location.longitude);
			mapView.getModel().mapViewPosition.setMapPosition(new MapPosition(
				bb.getCenterPoint(),
				LatLongUtils.zoomForBounds(mapView.getModel().mapViewDimension.getDimension(), bb,
						mapView.getModel().displayModel.getTileSize())));
		}
		catch (Exception e) {
			mapView.getModel().mapViewPosition.setCenter(latLong);
		}
	}
	*/

	static public long storePointPosition(Tabulae activity, String name, String description, double latitude, double longitude, boolean visible) {
		return new Storage(activity).store(new PoiItem(name, description, latitude, longitude, visible));
	}

	public void inform(int event, Bundle extra) {
		switch (event) {
			case R.id.event_poi_list: {
				if (DEBUG) Log.d(TAG, "Poi.inform event=" + event + ", extra=" + extra);
			}
			break;
		}
	}
}
