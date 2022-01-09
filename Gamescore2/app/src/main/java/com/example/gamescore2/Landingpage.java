package com.example.gamescore2;

import static com.example.gamescore2.SignIn.token;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.ArrayMap;
import android.util.Log;
import android.view.View;
import android.widget.ImageView;

import java.util.Map;

import data.remotes.ApiService;
import data.remotes.ApiUtils;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class Landingpage extends AppCompatActivity implements View.OnClickListener {

    private static final String TAG = "";
    private ApiService mApiService;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_landingpage);
        ImageView profile = findViewById(R.id.profileButtonLandingpage);
        ImageView suche = findViewById(R.id.searchButtonLandingpage);
        ImageView plus = findViewById(R.id.plusButtonLandingpage);
        ImageView notification = findViewById(R.id.LogoutButtonLandingpage);

        profile.setOnClickListener(this);
        suche.setOnClickListener(this);
        plus.setOnClickListener(this);
        notification.setOnClickListener(this);

        mApiService = ApiUtils.getApiService();


    }

    @Override
    public void onClick(View v) {
        switch (v.getId()){
            case R.id.profileButtonLandingpage:
                Intent i = new Intent(this, ProfileView.class);
                startActivity(i);
                break;
            case R.id.searchButtonLandingpage:
                Intent j = new Intent(this, Search.class);
                startActivity(j);
                break;
            case R.id.plusButtonLandingpage:
                Intent k = new Intent(this, WriteReview.class);
                startActivity(k);
                break;
            case R.id.LogoutButtonLandingpage:

                sendLogout(token);

                Intent l = new Intent(this, SignIn.class);
                startActivity(l);
            break;
        }

    }

    private void sendLogout(String token){

        Call<Void> response = mApiService.sendLogout(token);
        response.enqueue(new Callback<Void>() {
            @Override
            public void onResponse(Call<Void> call, Response<Void> response) {
                if(response.isSuccessful()) {
                    SignIn.token = null;
                    Log.d("test", SignIn.token);
                    Log.d("test", "klappt jetzt");
                } else {
                    Log.d("test", "klappt nicht");

                }

            }
            @Override
            public void onFailure(Call<Void> call, Throwable t) {
                System.out.println("Exception: " + t);
                Log.e(TAG, "Unable to submit login to API.");
            }
        });
    }
}