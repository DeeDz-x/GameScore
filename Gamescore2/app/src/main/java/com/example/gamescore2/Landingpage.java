package com.example.gamescore2;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;

public class Landingpage extends AppCompatActivity implements View.OnClickListener {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_landingpage);
        ImageView profil = findViewById(R.id.profilButtonLandingpage);
        ImageView suche = findViewById(R.id.searchButtonLandingpage);
        ImageView plus = findViewById(R.id.plusButtonLandingpage);
        ImageView notification = findViewById(R.id.notiButtonLandingpage);

        profil.setOnClickListener(this);
        suche.setOnClickListener(this);
        plus.setOnClickListener(this);
        notification.setOnClickListener(this);


    }

    @Override
    public void onClick(View v) {
        switch (v.getId()){
            case R.id.profilButtonLandingpage:
                Intent i = new Intent(this, Profil.class);
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
//            case R.id.notiButtonLandingpage:
//                Intent l = new Intent(this, Profil.class);
//                startActivity(l);
//            break;
        }

    }
}