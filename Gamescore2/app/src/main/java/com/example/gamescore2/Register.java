package com.example.gamescore2;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.ArrayMap;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import org.json.JSONObject;

import java.io.IOException;
import java.util.Map;

import data.remotes.ApiService;
import data.remotes.ApiUtils;
import okhttp3.RequestBody;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class Register extends AppCompatActivity implements View.OnClickListener{

    private static final String TAG = "";
    private ApiService mApiService;
    EditText username, email, confirmEmail, password, confirmPassword;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);

        Button register = findViewById(R.id.registerButton);
        register.setOnClickListener(this);

        mApiService = ApiUtils.getApiService();
        username = findViewById(R.id.usernameRegister);
        email = findViewById(R.id.emailRegister);
        confirmEmail = findViewById(R.id.confirmEmail);
        password = findViewById(R.id.passwordRegister);
        confirmPassword = findViewById(R.id.confirmPassword);

    }

    @Override
    public void onClick(View v) {

        Log.d("test", "testjsdfddfjdjfsdfefsd");

        username = findViewById(R.id.usernameRegister);
        email = findViewById(R.id.emailRegister);
        confirmEmail = findViewById(R.id.confirmEmail);
        password = findViewById(R.id.passwordRegister);
        confirmPassword = findViewById(R.id.confirmPassword);

       // Log.d("test", "username: " + username.getText().toString() + " email: "+ email.getText().toString() + " password: " + password.getText().toString());

        if (email.getText().toString() != null && password.getText().toString() != null
                && username.getText().toString() != null) {
            sendRegister(email.getText().toString(), password.getText().toString(), username.getText().toString());

        Intent intent = new Intent(this,SignIn.class);
        startActivity(intent);
    }
}

    private void sendRegister(String mEmail, String mPassword, String mUsername) {

        Map<String, Object> jsonParams = new ArrayMap<>();
//put something inside the map, could be null
        jsonParams.put("password", mPassword);
        jsonParams.put("e_mail", mEmail);
        jsonParams.put("username", mUsername);

        RequestBody body = RequestBody.create(okhttp3.MediaType.parse("application/json; charset=utf-8"),(new JSONObject(jsonParams)).toString());

        Call<ResponseBody> response = mApiService.sendRegister(body);

        response.enqueue(new Callback<ResponseBody>() {
            @Override
            public void onResponse(Call<ResponseBody> call, Response<ResponseBody> response) {
                if(response.isSuccessful()) {

                    Log.d("test", "klappt jetzt");
                } else {
                    Log.d("test", "klappt nicht");

                }

            }

            @Override
            public void onFailure(Call<ResponseBody> call, Throwable t) {
                System.out.println("Exception: " + t);
                Log.e(TAG, "Unable to submit login to API.");
            }

        });
    }}


