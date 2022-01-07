package com.example.gamescore2;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.text.TextUtils;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import java.util.List;

import data.models.Login;
import data.models.LoginRequest;
import data.remotes.ApiUtils;
import data.remotes.ApiService;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class SignIn extends AppCompatActivity implements View.OnClickListener{

    private static final String TAG = "";
    private ApiService mApiService;
    static Login apiKey;
    private String key;
    EditText email, password;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button signIn = findViewById(R.id.signInButton);
        signIn.setOnClickListener(this);

        mApiService = ApiUtils.getApiService();
        email = findViewById(R.id.emailSignIn);
        password = findViewById(R.id.passwordSignIn);

    }


    @Override
    public void onClick(View v) {

        email = findViewById(R.id.emailSignIn);
        password = findViewById(R.id.passwordSignIn);

        Log.d("test", "test" + email.getText().toString());
        Log.d("test", password.getText().toString());

        if (email.getText().toString() != null && password.getText().toString() != null) {
            sendLogin(email.getText().toString(), password.getText().toString());

            if (key != null) {
                Intent intent = new Intent(this, Landingpage.class);
                startActivity(intent);
            }

        }
    }

    private void sendLogin(String mEmail, String mPassword) {

        mApiService.sendLogin(new LoginRequest(mEmail, mPassword)).enqueue(new Callback<Login>() {
            @Override
            public void onResponse(Call<Login> call, Response<Login> response) {
                if(response.isSuccessful()) {
                    System.out.println("ja");
                } else {
                    System.out.println("nein");
                }

            }

            @Override
            public void onFailure(Call<Login> call, Throwable t) {
                System.out.println("Exception: " + t);
                Log.e(TAG, "Unable to submit login to API.");
            }

        });

    }
}