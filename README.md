# Spotify Playlist
An implementation of Spotify Playlist application using Beautiful Soup, spotipy, requests, and os.

## Requirements
pip install requests  
pip install bs4
pip install spotipy

## What is Spotify Playlist?
Spotify Playlist is an application that serves as a time machine. It goes back in time to find the music that was in the top 100 chart that was being played all over the radio so that the user can relive that period of time once more, through music.

## How does it work?
<ul>
  <li>
    Step 1 - Use Beautiful Soup to scrape top 100 songs form the Billboard Hot 100 on a particular date of the user's choice.   
    Billboard Hot 100™ URL: https://www.billboard.com/charts/hot-100/2005-08-12/
  </li>
  
   <li>
    Step 2 - Authentication with Spotify   
    <ol>
      <li>
        Create an account on Spotify: http://spotify.com/signup/
      </li>
      <li>
        Once the user has signed up/ signed in, go to the developer dashboard and create a new Spotify App: https://developer.spotify.com/dashboard/      
      </li>
      <img width="552" alt="Screenshot 2023-12-25 at 2 28 46 AM" src="https://github.com/CoboAr/Spotify-Playlist/assets/144629565/7715821f-efd4-40cc-b920-842062ba34af"> 
      <li>
        Once the user has created a Spotify app, copy the Client ID and Client Secret into your Python project.
      </li>
      <img width="553" alt="Screenshot 2023-12-25 at 2 31 54 AM" src="https://github.com/CoboAr/Spotify-Playlist/assets/144629565/06da8c17-6b41-40bd-822a-470665c91dcd"> 
      <li>
        Authenticate Python project with Spotify using user's unique Client ID/ Client Secret.  
        Click Edit Settings and add http://example.com on Redirect URIs* field      
      </li>
      <img width="1440" alt="Screenshot 2023-12-25 at 3 05 13 AM" src="https://github.com/CoboAr/Spotify-Playlist/assets/144629565/93e85fa8-b189-4401-a4c0-922774e8af06">
      <li>
        When running the code by using playlist-modify-private scope the user should get this page:  
        <img width="1440" alt="Screenshot 2023-12-25 at 2 56 03 AM" src="https://github.com/CoboAr/Spotify-Playlist/assets/144629565/f0e8f5d5-9948-4c71-a0d5-b24c7c986ce2">
      </li>
      <li>
        Click Agree. Then it will take you to the page below, example.com and you need to copy the entire URL in the address bar:  
        <img width="1440" alt="Screenshot 2023-12-25 at 2 56 43 AM" src="https://github.com/CoboAr/Spotify-Playlist/assets/144629565/5bfe1639-7bbe-482c-98cc-74b6ec2cf8c4">
      </li>
      <li>
      Finally, the user needs to paste the URL into the prompt in PyCharm:  
        <img width="1440" alt="Screenshot 2023-12-25 at 2 58 21 AM" src="https://github.com/CoboAr/Spotify-Playlist/assets/144629565/3e567640-a161-40ee-b839-d4fcf9a866ec">
      </li>
      <li>
        Now if the user closes PyCharm and restart, he should see a new file in this project called token.txt.  
        <img width="474" alt="Screenshot 2023-12-25 at 3 14 59 AM" src="https://github.com/CoboAr/Spotify-Playlist/assets/144629565/b410b9ab-7f15-47cc-81d7-c9dc9daa2212"> 
      </li>
    </ol>
  </li>

  <li>
    Step 3 - Search Spotify for the Songs from Step 1   
    When a song is not available in Spotify, exception handling is used to skip over those songs.
  </li>

  <li>
    Step 4 - Creating and Adding to Spotify Playlist
    <ul>
      <li>
        create a new private playlist with the name "YYYY-MM-DD Billboard 100", where the date is the date the user inputted in step 1.
      </li>
      <li>
        Add each of the songs found in Step 3 to the new playlist.
      </li>
    </ul>
  </li>
</ul>

## Demo  
https://github.com/CoboAr/Spotify-Playlist/assets/144629565/0825965f-5a1a-4b2e-aa63-cfd77f07e4cf  

Enjoy! And please do let me know if you have any comments, constructive criticism, and/or bug reports.
## Author
## Arnold Cobo




