// Generated by view binder compiler. Do not edit!
package com.example.gamescore2.databinding;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.RatingBar;
import android.widget.ScrollView;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.viewbinding.ViewBinding;
import androidx.viewbinding.ViewBindings;
import com.example.gamescore2.R;
import java.lang.NullPointerException;
import java.lang.Override;
import java.lang.String;

public final class ActivityGameProfilBinding implements ViewBinding {
  @NonNull
  private final ScrollView rootView;

  @NonNull
  public final Button addToListButtonGameprofil;

  @NonNull
  public final EditText bestReviewGameprofil;

  @NonNull
  public final EditText bestReviewGameprofil2;

  @NonNull
  public final EditText editTextTextMultiLine;

  @NonNull
  public final TextView friendsWhoPlayGameprofil;

  @NonNull
  public final ImageView gameGameprofil;

  @NonNull
  public final TextView genreGameProfil;

  @NonNull
  public final TextView publisherGameprofil;

  @NonNull
  public final RatingBar ratingBarGameprofil;

  @NonNull
  public final TextView releaseDateGameprofil;

  @NonNull
  public final TextView votesGameprofil;

  private ActivityGameProfilBinding(@NonNull ScrollView rootView,
      @NonNull Button addToListButtonGameprofil, @NonNull EditText bestReviewGameprofil,
      @NonNull EditText bestReviewGameprofil2, @NonNull EditText editTextTextMultiLine,
      @NonNull TextView friendsWhoPlayGameprofil, @NonNull ImageView gameGameprofil,
      @NonNull TextView genreGameProfil, @NonNull TextView publisherGameprofil,
      @NonNull RatingBar ratingBarGameprofil, @NonNull TextView releaseDateGameprofil,
      @NonNull TextView votesGameprofil) {
    this.rootView = rootView;
    this.addToListButtonGameprofil = addToListButtonGameprofil;
    this.bestReviewGameprofil = bestReviewGameprofil;
    this.bestReviewGameprofil2 = bestReviewGameprofil2;
    this.editTextTextMultiLine = editTextTextMultiLine;
    this.friendsWhoPlayGameprofil = friendsWhoPlayGameprofil;
    this.gameGameprofil = gameGameprofil;
    this.genreGameProfil = genreGameProfil;
    this.publisherGameprofil = publisherGameprofil;
    this.ratingBarGameprofil = ratingBarGameprofil;
    this.releaseDateGameprofil = releaseDateGameprofil;
    this.votesGameprofil = votesGameprofil;
  }

  @Override
  @NonNull
  public ScrollView getRoot() {
    return rootView;
  }

  @NonNull
  public static ActivityGameProfilBinding inflate(@NonNull LayoutInflater inflater) {
    return inflate(inflater, null, false);
  }

  @NonNull
  public static ActivityGameProfilBinding inflate(@NonNull LayoutInflater inflater,
      @Nullable ViewGroup parent, boolean attachToParent) {
    View root = inflater.inflate(R.layout.activity_game_profil, parent, false);
    if (attachToParent) {
      parent.addView(root);
    }
    return bind(root);
  }

  @NonNull
  public static ActivityGameProfilBinding bind(@NonNull View rootView) {
    // The body of this method is generated in a way you would not otherwise write.
    // This is done to optimize the compiled bytecode for size and performance.
    int id;
    missingId: {
      id = R.id.addToListButtonGameprofil;
      Button addToListButtonGameprofil = ViewBindings.findChildViewById(rootView, id);
      if (addToListButtonGameprofil == null) {
        break missingId;
      }

      id = R.id.bestReviewGameprofil;
      EditText bestReviewGameprofil = ViewBindings.findChildViewById(rootView, id);
      if (bestReviewGameprofil == null) {
        break missingId;
      }

      id = R.id.bestReviewGameprofil2;
      EditText bestReviewGameprofil2 = ViewBindings.findChildViewById(rootView, id);
      if (bestReviewGameprofil2 == null) {
        break missingId;
      }

      id = R.id.editTextTextMultiLine;
      EditText editTextTextMultiLine = ViewBindings.findChildViewById(rootView, id);
      if (editTextTextMultiLine == null) {
        break missingId;
      }

      id = R.id.friendsWhoPlayGameprofil;
      TextView friendsWhoPlayGameprofil = ViewBindings.findChildViewById(rootView, id);
      if (friendsWhoPlayGameprofil == null) {
        break missingId;
      }

      id = R.id.gameGameprofil;
      ImageView gameGameprofil = ViewBindings.findChildViewById(rootView, id);
      if (gameGameprofil == null) {
        break missingId;
      }

      id = R.id.genreGameProfil;
      TextView genreGameProfil = ViewBindings.findChildViewById(rootView, id);
      if (genreGameProfil == null) {
        break missingId;
      }

      id = R.id.publisherGameprofil;
      TextView publisherGameprofil = ViewBindings.findChildViewById(rootView, id);
      if (publisherGameprofil == null) {
        break missingId;
      }

      id = R.id.ratingBarGameprofil;
      RatingBar ratingBarGameprofil = ViewBindings.findChildViewById(rootView, id);
      if (ratingBarGameprofil == null) {
        break missingId;
      }

      id = R.id.releaseDateGameprofil;
      TextView releaseDateGameprofil = ViewBindings.findChildViewById(rootView, id);
      if (releaseDateGameprofil == null) {
        break missingId;
      }

      id = R.id.votesGameprofil;
      TextView votesGameprofil = ViewBindings.findChildViewById(rootView, id);
      if (votesGameprofil == null) {
        break missingId;
      }

      return new ActivityGameProfilBinding((ScrollView) rootView, addToListButtonGameprofil,
          bestReviewGameprofil, bestReviewGameprofil2, editTextTextMultiLine,
          friendsWhoPlayGameprofil, gameGameprofil, genreGameProfil, publisherGameprofil,
          ratingBarGameprofil, releaseDateGameprofil, votesGameprofil);
    }
    String missingId = rootView.getResources().getResourceName(id);
    throw new NullPointerException("Missing required view with ID: ".concat(missingId));
  }
}