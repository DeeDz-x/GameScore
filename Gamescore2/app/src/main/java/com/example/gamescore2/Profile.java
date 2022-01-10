package com.example.gamescore2;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.ArrayMap;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import org.json.JSONArray;
import org.json.JSONObject;

import java.util.Map;

import data.remotes.ApiService;
import data.remotes.ApiUtils;
import okhttp3.RequestBody;

public class Profile extends AppCompatActivity implements View.OnClickListener {

    private static final String TAG = "";
    private ApiService mApiService;
    EditText name, username, age, region, favGames, aboutMe, plattform1, plattform2, plattform3, plattform4;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_profile);
        Button save = findViewById(R.id.saveButtonProfil);
        save.setOnClickListener(this);

        mApiService = ApiUtils.getApiService();
        name = findViewById(R.id.nameProfil);
        username = findViewById(R.id.usernameProfil);
        age = findViewById(R.id.ageProfil);
        region = findViewById(R.id.regionProfil);
        favGames = findViewById(R.id.favoritGamesProfil);
        aboutMe = findViewById(R.id.aboutMeProfil);
        plattform1 = findViewById(R.id.platform1Profil);
        plattform2 = findViewById(R.id.platform2Profil);
        plattform3 = findViewById(R.id.platform3Profil);
        plattform4 = findViewById(R.id.platform4Profil);

    }

    @Override
    public void onClick(View v) {
        Intent intent = new Intent(this, ProfileView.class);
        startActivity(intent);

        name = findViewById(R.id.nameProfil);
        username = findViewById(R.id.usernameProfil);
        age = findViewById(R.id.ageProfil);
        region = findViewById(R.id.regionProfil);
        favGames = findViewById(R.id.favoritGamesProfil);
        aboutMe = findViewById(R.id.aboutMeProfil);
        plattform1 = findViewById(R.id.platform1Profil);
        plattform2 = findViewById(R.id.platform2Profil);
        plattform3 = findViewById(R.id.platform3Profil);
        plattform4 = findViewById(R.id.platform4Profil);

        if (name.getText().toString() != null && username.getText().toString() != null && age.getText().toString() != null
                && region.getText().toString() != null && favGames.getText().toString() != null && aboutMe.getText().toString() != null
                && plattform1.getText().toString() != null && plattform2.getText().toString() != null && plattform3.getText().toString() != null
                && plattform4.getText().toString() != null) {
            sendProfile(name.getText().toString(), name.getText().toString(), name.getText().toString(), name.getText().toString(),
                    name.getText().toString(), name.getText().toString(), name.getText().toString(),
                    name.getText().toString(), name.getText().toString(), name.getText().toString());
        }

    }

    private void sendProfile(String mName, String musername, String mAge, String mRegion, String mfavGames, String mAboutMe
            , String mPlattform1, String mPlattform2, String mPlattform3, String mPlattform4) {

        Map<String, Object> jsonParams = new ArrayMap<>();
        JSONArray jsonArray = new JSONArray();
//put something inside the map, could be null
        jsonParams.put("age", mAge);
        jsonParams.put("country", mRegion);
        jsonParams.put("name", mName);
        jsonParams.put("bio", mAboutMe);
        jsonParams.put("favourite_game_id", mfavGames);
        jsonParams.put("e_mail", "nichts");
        jsonParams.put("picture", "picture");

        RequestBody body = RequestBody.create(okhttp3.MediaType.parse("application/json; charset=utf-8"), (new JSONObject(jsonParams)).toString());


    }
}