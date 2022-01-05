package com.example.gamescore2;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class ProfileView extends AppCompatActivity implements View.OnClickListener{

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_profile_view);

        Button change = findViewById(R.id.changeProfileView);
        Button lists = findViewById(R.id.listsProfileView);

        change.setOnClickListener(this);
        lists.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {


        switch (v.getId()){
            case R.id.changeProfileView:
                Intent i = new Intent(this, Profil.class);
                startActivity(i);
                break;
            case R.id.listsProfileView:
                Intent j = new Intent(this, Lists.class);
                startActivity(j);
                break;

        }
    }}
