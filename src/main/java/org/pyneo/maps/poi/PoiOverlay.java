package org.pyneo.maps.poi;

import android.app.Activity;
import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Point;
import android.graphics.Rect;
import android.graphics.drawable.Drawable;
import android.util.DisplayMetrics;
import android.util.SparseArray;
import android.view.LayoutInflater;
import android.view.MotionEvent;
import android.widget.ImageView;
import android.widget.RelativeLayout;
import android.widget.RelativeLayout.LayoutParams;
import android.widget.TextView;

import org.pyneo.maps.R;
import org.pyneo.maps.utils.Ut;
import org.pyneo.maps.map.TileView;
import org.pyneo.maps.map.TileViewOverlay;
import org.pyneo.maps.map.TileView.OpenStreetMapViewProjection;

import org.andnav.osm.util.GeoPoint;

public class PoiOverlay extends TileViewOverlay implements Constants {
	private final Point mMarkerHotSpot;
	private final int mMarkerWidth;
	private final int mMarkerHeight;
	private OnItemTapListener<PoiPoint> mOnItemTapListener;
	private OnItemLongPressListener<PoiPoint> mOnItemLongPressListener;
	private SparseArray<PoiPoint> mItemList = new SparseArray<PoiPoint>();
	private final SparseArray<Drawable> mBtnMap = new SparseArray<Drawable>();
	private Context mCtx;
	private PoiManager mPoiManager;
	private int mTapId;
	private GeoPoint mLastMapCenter;
	private int mLastZoom;
	private final PoiListThread mThread = new PoiListThread();
	private RelativeLayout mT;
	private float mDensity;
	private boolean mNeedUpdateList = false;
	private boolean mCanUpdateList = true;

	public PoiOverlay(Context ctx, PoiManager poiManager, OnItemTapListener<PoiPoint> onItemTapListener, boolean hidepoi) {
		mCtx = ctx;
		mPoiManager = poiManager;
		mCanUpdateList = !hidepoi;
		mTapId = NO_TAP;
		Drawable marker = ctx.getResources().getDrawable(PoiActivity.resourceFromPoiIconId(0));
		mMarkerWidth = marker.getIntrinsicWidth();
		mMarkerHeight = marker.getIntrinsicHeight();
		mMarkerHotSpot = new Point(mMarkerWidth/2, mMarkerHeight);
		mOnItemTapListener = onItemTapListener;
		mLastMapCenter = null;
		mLastZoom = -1;
		mT = (RelativeLayout)LayoutInflater.from(ctx).inflate(R.layout.poi_descr, null);
		mT.setLayoutParams(new RelativeLayout.LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT));
		DisplayMetrics metrics = new DisplayMetrics();
		((Activity)ctx).getWindowManager().getDefaultDisplay().getMetrics(metrics);
		mDensity = metrics.density;
	}

	public int getTapIndex() {
		return mTapId;
	}

	public void setTapIndex(int mTapIndex) {
		mTapId = mTapIndex;
	}

	public void UpdateList() {
		mNeedUpdateList = true;
	}

	public void clearPoiList() {
		mItemList.clear();
	}

	public void setGpsStatusGeoPoint(final int id, final GeoPoint geopoint, final String title, final String descr) {
		mItemList.put(id, new PoiPoint(id, title, descr, geopoint, 0, 0));
		mCanUpdateList = false;
		mTapId = NO_TAP;
	}

	@Override
	public void onDraw(Canvas c, TileView mapView) {
		final OpenStreetMapViewProjection pj = mapView.getProjection();
		final Point curScreenCoords = new Point();
		if (mCanUpdateList) {
			boolean looseCenter = false;
			GeoPoint center = mapView.getMapCenter();
			GeoPoint lefttop = pj.fromPixels(0, 0);
			double deltaX = Math.abs(center.getLongitude() - lefttop.getLongitude());
			double deltaY = Math.abs(center.getLatitude() - lefttop.getLatitude());
			if (mLastMapCenter == null
			|| mLastZoom != mapView.getZoomLevel()) {
				looseCenter = true;
			}
			else if (0.7 * deltaX < Math.abs(center.getLongitude() - mLastMapCenter.getLongitude())
			|| 0.7 * deltaY < Math.abs(center.getLatitude() - mLastMapCenter.getLatitude())) {
				looseCenter = true;
			}
			if (looseCenter || mNeedUpdateList) {
				mLastMapCenter = center;
				mLastZoom = mapView.getZoomLevel();
				mNeedUpdateList = false;
				mThread.setParams(1.5 * deltaX, 1.5 * deltaY);
				mThread.run();
			}
		}
		Ut.d("onDraw mItemList=" + mItemList);
		if (mItemList != null) {
			// Draw in backward cycle, so the items with the least index are on the front:
			for (int i = mItemList.size() - 1; i >= 0; i--) {
				if (i != mTapId) {
					PoiPoint item = mItemList.valueAt(i);
					pj.toPixels(item.mGeoPoint, curScreenCoords);
					c.save();
					c.rotate(mapView.getBearing(), curScreenCoords.x, curScreenCoords.y);
					onDrawItem(c, item.getId(), curScreenCoords);
					c.restore();
				}
			}
			// paint tapped item last:
			if (mTapId != NO_TAP) {
				PoiPoint item = mItemList.get(mTapId);
				if (item != null) {
					pj.toPixels(item.mGeoPoint, curScreenCoords);
					c.save();
					c.rotate(mapView.getBearing(), curScreenCoords.x, curScreenCoords.y);
					onDrawItem(c, mTapId, curScreenCoords);
					c.restore();
				}
			}
		}
	}

	protected void onDrawItem(Canvas c, int id, Point screenCoords) {
		final PoiPoint paintItem = mItemList.get(id);
		if (id == mTapId) { // focussed?
			Ut.d("onDrawItem screenCoords=" + screenCoords);
			final ImageView pic = (ImageView)mT.findViewById(R.id.pic);
			pic.setImageResource(PoiActivity.resourceFromPoiIconId(paintItem.mIconId));
			((TextView)mT.findViewById(R.id.poi_title)).setText(paintItem.mTitle);
			((TextView)mT.findViewById(R.id.descr)).setText(paintItem.mDescr);
			((TextView)mT.findViewById(R.id.coord)).setText(Ut.formatGeoPoint(paintItem.mGeoPoint, mCtx));
			mT.measure(0, 0);
			mT.layout(0, 0, mT.getMeasuredWidth(), mT.getMeasuredHeight());
			c.save();
			c.translate(screenCoords.x - pic.getMeasuredWidth()/2, screenCoords.y - pic.getMeasuredHeight() - pic.getTop());
			mT.draw(c);
			c.restore();
		}
		else {
			final int left = screenCoords.x - mMarkerHotSpot.x;
			final int right = left + mMarkerWidth;
			final int top = screenCoords.y - mMarkerHotSpot.y;
			final int bottom = top + mMarkerHeight;
			Ut.d("onDrawItem left=" + left + ", right=" + right + ", top=" + top + ", bottom=" + bottom);
			Drawable marker = null;
			if (mBtnMap.indexOfKey(PoiActivity.resourceFromPoiIconId(paintItem.mIconId)) < 0) {
				marker = mCtx.getResources().getDrawable(PoiActivity.resourceFromPoiIconId(paintItem.mIconId));
				mBtnMap.put(PoiActivity.resourceFromPoiIconId(paintItem.mIconId), marker);
			}
			else {
				marker = mBtnMap.get(PoiActivity.resourceFromPoiIconId(paintItem.mIconId));
			}
			marker.setBounds(left, top, right, bottom);
			marker.draw(c);
			/*
			final int pxUp = 2;
			final int left2 = (int)(screenCoords.x + mDensity * (5 - pxUp));
			final int right2 = (int)(screenCoords.x + mDensity * (38 + pxUp));
			final int top2 = (int)(screenCoords.y - mMarkerHotSpot.y - mDensity * (pxUp));
			final int bottom2 = (int)(top2 + mDensity * (33 + pxUp));
			Paint p = new Paint();
			c.drawLine(left2, top2, right2, bottom2, p);
			c.drawLine(right2, top2, left2, bottom2, p);
			c.drawLine(screenCoords.x - 5, screenCoords.y - 5, screenCoords.x + 5, screenCoords.y + 5, p);
			c.drawLine(screenCoords.x - 5, screenCoords.y + 5, screenCoords.x + 5, screenCoords.y - 5, p);
			*/
		}
	}

	public PoiPoint getPoiPoint(final int id) {
		return mItemList.get(id);
	}

	public int getMarkerAtPoint(final int eventX, final int eventY, TileView mapView) {
		if (mItemList != null) {
			final OpenStreetMapViewProjection pj = mapView.getProjection();
			final Rect curMarkerBounds = new Rect();
			final Point mCurScreenCoords = new Point();
			for (int i = 0; i < mItemList.size(); i++) {
				final PoiPoint mItem = mItemList.valueAt(i);
				pj.toPixels(mItem.mGeoPoint, mapView.getBearing(), mCurScreenCoords);
				final int pxUp = 2;
				final int left = (int)(mCurScreenCoords.x + mDensity * (5 - pxUp));
				final int right = (int)(mCurScreenCoords.x + mDensity * (38 + pxUp));
				final int top = (int)(mCurScreenCoords.y - mMarkerHotSpot.y - mDensity * (pxUp));
				final int bottom = (int)(top + mDensity * (33 + pxUp));
				curMarkerBounds.set(left, top, right, bottom);
				if (curMarkerBounds.contains(eventX, eventY)) {
					return mItem.getId();
				}
			}
		}
		return NO_TAP;
	}

	@Override
	public boolean onSingleTapUp(MotionEvent event, TileView mapView) {
		final int id = getMarkerAtPoint((int)event.getX(), (int)event.getY(), mapView);
		if (id != NO_TAP)
			if (onTap(id))
				return true;
		return super.onSingleTapUp(event, mapView);
	}

	@Override
	public int onLongPress(MotionEvent event, TileView mapView) {
		final int id = getMarkerAtPoint((int)event.getX(), (int)event.getY(), mapView);
		mapView.mPoiMenuInfo.MarkerIndex = id;
		mapView.mPoiMenuInfo.EventGeoPoint = mapView.getProjection().fromPixels((int)event.getX(), (int)event.getY(), mapView.getBearing());
		if (id != NO_TAP)
			return 1;
		//if (onLongLongPress(id))
		return super.onLongPress(event, mapView);
	}

	private boolean onLongLongPress(int id) {
		return false;
	}

	protected boolean onTap(int id) {
		if (mTapId == id)
			mTapId = NO_TAP;
		else
			mTapId = id;
		if (mOnItemTapListener != null)
			return mOnItemTapListener.onItemTap(id, mItemList.get(id));
		else
			return false;
	}

	@Override
	protected void onDrawFinished(Canvas c, TileView osmv) {
	}

	@SuppressWarnings("hiding")
	public interface OnItemTapListener<PoiPoint> {
		boolean onItemTap(final int aIndex, final PoiPoint aItem);
	}

	@SuppressWarnings("hiding")
	public interface OnItemLongPressListener<PoiPoint> {
		boolean onItemLongPress(final int aIndex, final PoiPoint aItem);
	}

	private class PoiListThread extends Thread {
		private double mdeltaX;
		private double mdeltaY;

		public void setParams(double deltaX, double deltaY) {
			mdeltaX = deltaX;
			mdeltaY = deltaY;
		}

		@Override
		public void run() {
			mItemList = mPoiManager.getPoiListNotHidden(mLastZoom, mLastMapCenter, mdeltaX, mdeltaY);
			super.run();
		}
	}
}
