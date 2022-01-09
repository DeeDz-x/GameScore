package com.example.gamescore2;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;

import data.remotes.ApiService;
import data.remotes.ApiUtils;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class GameProfil extends AppCompatActivity implements View.OnClickListener {

    private static final String TAG = "";
    private ApiService mApiService;
    private String gameName;
    private String release;
    private String publisher;
    private String description;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_game_profil);

        Button addToList = findViewById(R.id.addToListButtonGameprofil);
        addToList.setOnClickListener(this);

        mApiService = ApiUtils.getApiService();
        getGame();
    }

    @Override
    public void onClick(View v) {
        Intent intent = new Intent(this, Landingpage.class);
        startActivity(intent);

    }

    private void getGame() {

        Call<ResponseBody> response = mApiService.getPopGames();
        response.enqueue(new Callback<ResponseBody>() {
            @Override
            public void onResponse(Call<ResponseBody> call, Response<ResponseBody> response) {
                if (response.isSuccessful()) {
                    Log.d("test", "Games klappt jetzt");
                    JSONObject json = new JSONObject();
                    try {
                        json = new JSONObject(response.body().string());
                    } catch (JSONException e) {
                        e.printStackTrace();
                    } catch (IOException e) {
                        e.printStackTrace();
                    }


                    try {
                        gameName = json.getString("name");
                        release = json.getString("releaseyear");

                        JSONObject publisherObject = json.getJSONObject("publisher");
                        publisher = publisherObject.getString("name");

                        description = json.getString("description");

                    } catch (JSONException e) {
                        e.printStackTrace();
                    }


                    TextView gameNameView = findViewById(R.id.gameNameGameProfile);
                    gameNameView.setText(gameName);
                    TextView gameReleaseView = findViewById(R.id.releaseDateGameProfile);
                    gameReleaseView.setText(release);
                    TextView gamePublisherView = findViewById(R.id.publisherGameProfile);
                    gamePublisherView.setText(publisher);
                    EditText gameDescriptionView = findViewById(R.id.gameDescriptionGameProfile);
                    gameDescriptionView.setText(description);


                    try {
                        Log.d("test", response.body().string());
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                } else {
                    Log.d("test", "Games klappt nicht");
                }
            }

            @Override
            public void onFailure(Call<ResponseBody> call, Throwable t) {
                System.out.println("Exception: " + t);
                Log.e(TAG, "Unable to submit login to API.");
            }
        });
    }}
