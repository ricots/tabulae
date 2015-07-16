package org.pyneo.maps.poi;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.KeyEvent;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.Toast;

import org.pyneo.maps.utils.Ut;
import org.pyneo.maps.R;

public class PoiCategoryActivity extends Activity implements Constants {
	EditText mTitle;
	CheckBox mHidden;
	ImageView mIcon;
	EditText mMinZoom;
	private PoiCategory mPoiCategory;
	private PoiManager mPoiManager;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		this.setContentView(R.layout.poi_category);
		if (mPoiManager == null)
			mPoiManager = new PoiManager(this);
		mTitle = (EditText)findViewById(R.id.Title);
		mHidden = (CheckBox)findViewById(R.id.Hidden);
		mIcon = (ImageView)findViewById(R.id.ImageIcon);
		mMinZoom = (EditText)findViewById(R.id.MinZoom);
		Bundle extras = getIntent().getExtras();
		if (extras == null) extras = new Bundle();
		int id = extras.getInt(ID, Constants.EMPTY_ID);
		if (id < 0) {
			mPoiCategory = new PoiCategory();
			mTitle.setText(extras.getString(TITLE));
			mHidden.setChecked(false);
			mIcon.setImageResource(PoiActivity.resourceFromPoiIconId(mPoiCategory.mIconId));
			mMinZoom.setText("14");
		} else {
			mPoiCategory = mPoiManager.getPoiCategory(id);
			if (mPoiCategory == null)
				finish();
			mTitle.setText(mPoiCategory.mName);
			mHidden.setChecked(mPoiCategory.mHidden);
			mIcon.setImageResource(PoiActivity.resourceFromPoiIconId(mPoiCategory.mIconId));
			mMinZoom.setText(Integer.toString(mPoiCategory.mMinZoom));
		}
		findViewById(R.id.saveButton)
			.setOnClickListener(new OnClickListener() {
				public void onClick(View v) {
					doSaveAction();
				}
			});
		findViewById(R.id.discardButton)
			.setOnClickListener(new OnClickListener() {
				public void onClick(View v) {
					PoiCategoryActivity.this.finish();
				}
			});
		mIcon.setOnClickListener(new OnClickListener() {
			public void onClick(View v) {
				doSelectIcon();
			}
		});
	}

	@Override
	protected void onDestroy() {
		super.onDestroy();
		mPoiManager.FreeDatabases();
	}

	protected void doSelectIcon() {
		startActivityForResult(new Intent(this, PoiIconSetActivity.class), R.id.ImageIcon);
	}

	@Override
	public boolean onKeyDown(int keyCode, KeyEvent event) {
		switch (keyCode) {
			case KeyEvent.KEYCODE_BACK: {
				doSaveAction();
				return true;
			}
		}
		return super.onKeyDown(keyCode, event);
	}

	private void doSaveAction() {
		mPoiCategory.mName = mTitle.getText().toString();
		mPoiCategory.mHidden = mHidden.isChecked();
		mPoiCategory.mMinZoom = Integer.parseInt(mMinZoom.getText().toString());
		mPoiManager.updatePoiCategory(mPoiCategory);
		finish();
		Toast.makeText(this, R.string.message_saved, Toast.LENGTH_SHORT).show();
	}

	@Override
	protected void onActivityResult(int requestCode, int resultCode, Intent data) {
		if (resultCode == RESULT_OK) {
			mPoiCategory.mIconId = data.getIntExtra(ICONID, 0);
			Ut.d("onActivityResult: IconId=" + mPoiCategory.mIconId);
			mIcon.setImageResource(PoiActivity.resourceFromPoiIconId(mPoiCategory.mIconId));
		}
		super.onActivityResult(requestCode, resultCode, data);
	}
}