package com.example.gamescore2;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.ArrayMap;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import com.example.gamescore2.Dialogs.LoginFailedDialog;

import org.json.JSONObject;

import java.io.IOException;
import java.util.Map;

import data.models.Login;
import data.remotes.ApiUtils;
import data.remotes.ApiService;
import okhttp3.RequestBody;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class SignIn extends AppCompatActivity implements View.OnClickListener{

    private static final String TAG = "";
    private ApiService mApiService;
    static Login apiKey;
    private String key;
    EditText email, password;
    static String token;



    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button signIn = findViewById(R.id.signInButton);
        signIn.setOnClickListener(this);


        Button registerB = findViewById(R.id.changeToRegisterButton);
        registerB.setOnClickListener(this);


        mApiService = ApiUtils.getApiService();
        email = findViewById(R.id.emailSignIn);
        password = findViewById(R.id.passwordSignIn);

    }


    @Override
    public void onClick(View v) {

        switch (v.getId()){
            case R.id.signInButton:


        email = findViewById(R.id.emailSignIn);
        password = findViewById(R.id.passwordSignIn);

        Log.d("test", "test" + email.getText().toString());
        Log.d("test", password.getText().toString());

        if (email.getText().toString() != null && password.getText().toString() != null) {
            sendLogin(email.getText().toString(), password.getText().toString());


            if (token != null) {
                Intent intent = new Intent(this, Landingpage.class);
                startActivity(intent);
            }

        }
        break;

            case R.id.changeToRegisterButton:
                Intent intent = new Intent(this, Register.class);
                startActivity(intent);
                break;

    }}

    private void sendLogin(String mEmail, String mPassword) {
        Log.d("test", "klappt");

        Map<String, Object> jsonParams = new ArrayMap<>();
        jsonParams.put("password", mPassword);
        jsonParams.put("e_mail", mEmail);

        RequestBody body = RequestBody.create(okhttp3.MediaType.parse("application/json; charset=utf-8"),(new JSONObject(jsonParams)).toString());

        Call<ResponseBody> response = mApiService.sendLogin(body);

        response.enqueue(new Callback<ResponseBody>() {
            @Override
            public void onResponse(Call<ResponseBody> call, Response<ResponseBody> response) {
                if(response.isSuccessful()) {
                    try {
                        token = "token " + response.body().string();
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                    Log.d("test","Der token ist:" + token);

                    Log.d("test", "logged in");
                } else {
                    Log.d("test", "log in failed");
                    LoginFailedDialog loginFailedDialog = new LoginFailedDialog();
                    loginFailedDialog.show(getSupportFragmentManager(), "Login Failed Try again");


                }

            }

            @Override
            public void onFailure(Call<ResponseBody> call, Throwable t) {
                System.out.println("Exception: " + t);
                Log.e(TAG, "Unable to submit login to API.");
            }

        });

    }}
