package org.pyneo.tabulae.geolocation;

import android.content.Context;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Bundle;
import android.util.Log;

import org.pyneo.tabulae.R;
import org.pyneo.tabulae.Tabulae;
import org.pyneo.tabulae.gui.Base;

public class Locus extends Base implements Constants, LocationListener {
	private final static String providers[] = new String[]{LocationManager.PASSIVE_PROVIDER, LocationManager.NETWORK_PROVIDER, LocationManager.GPS_PROVIDER,};
	private LocationManager locationManager;
	private Location last = null;

	public static Location toLocation(Bundle location) {
		Location ret = null;
		if (location != null) {
			ret = new Location(location.getString("provider"));
			if (location.containsKey("accuracy")) {
				ret.setAccuracy((float)location.getDouble("accuracy"));
			}
			if (location.containsKey("altitude")) ret.setAltitude(location.getDouble("altitude"));
			if (location.containsKey("bearing")) {
				ret.setBearing((float)location.getDouble("bearing"));
			}
			ret.setElapsedRealtimeNanos(location.getLong("elapsed"));
			ret.setLatitude(location.getDouble("latitude"));
			ret.setLongitude(location.getDouble("longitude"));
			if (location.containsKey("speed")) ret.setSpeed((float)location.getDouble("speed"));
			ret.setTime(location.getLong("time"));
		}
		return ret;
	}

	public static Bundle toBundle(Location location) {
		Bundle ret = null;
		if (location != null) {
			ret = new Bundle(location.getExtras());
			ret.putString("provider", location.getProvider());
			if (location.hasAccuracy() && location.getAccuracy() != 0) {
				ret.putDouble("accuracy", location.getAccuracy());
			}
			if (location.hasAltitude()) ret.putDouble("altitude", location.getAltitude());
			if (location.hasBearing()) ret.putDouble("bearing", location.getBearing());
			ret.putLong("elapsed", location.getElapsedRealtimeNanos());
			ret.putDouble("latitude", location.getLatitude());
			ret.putDouble("longitude", location.getLongitude());
			if (location.hasSpeed()) ret.putDouble("speed", location.getSpeed());
			ret.putLong("time", location.getTime());
		}
		return ret;
	}

	@Override
	public void onCreate(Bundle bundle) {
		super.onCreate(bundle);
		locationManager = (LocationManager)getActivity().getApplicationContext().getSystemService(Context.LOCATION_SERVICE);
		//locationManager.isProviderEnabled(provider);
		for (String provider : providers) {
			Location pl = locationManager.getLastKnownLocation(provider);
			last = betterLocation(last, pl);
		}
		((Tabulae)getActivity()).inform(R.id.location, toBundle(last));
		for (String provider : providers) {
			locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER, 0, 0, this);
		}
	}

	@Override
	public void onDestroyView() {
		super.onDestroyView();
		for (String provider : providers) {
			locationManager.removeUpdates(this);
		}
	}

	private Location betterLocation(Location l1, Location l2) {
		if (l1 == null) return l2;
		if (l2 == null) return null;
		if (Math.abs(l1.getElapsedRealtimeNanos() - l2.getElapsedRealtimeNanos()) < 3E9 && l1.hasAccuracy() && l2.hasAccuracy()) {
			return l1.getAccuracy() < l2.getAccuracy()? l1: l2;
		}
		if (l1.getElapsedRealtimeNanos() < l2.getElapsedRealtimeNanos()) return l2;
		return l1;
	}

	public void inform(int event, Bundle extra) {
		//if (DEBUG) Log.d(TAG, "Locus.inform event=" + event + ", extra=" + extra);
	}

	@Override
	public void onLocationChanged(Location location) {
		//if (DEBUG) Log.d(TAG, "Locus.onLocationChanged: location=" + location);
		last = betterLocation(last, location);
		// TODO: only send when changed?
		if (getActivity() != null) ((Tabulae)getActivity()).inform(R.id.location, toBundle(last));
	}

	@Override
	public void onProviderDisabled(String provider) {
		if (DEBUG) Log.d(TAG, "Locus.onProviderDisabled: provider=" + provider);
	}

	@Override
	public void onProviderEnabled(String provider) {
		if (DEBUG) Log.d(TAG, "Locus.onProviderEnabled: provider=" + provider);
	}

	@Override
	public void onStatusChanged(String provider, int status, Bundle extras) {
		if (DEBUG) Log.d(TAG, "Locus.onStatusChanged: provider=" + provider);
	}
}