<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">Social Media Formatter AWS</h3>

  <p align="center">
    <p></p>
    <br />
    <a href="https://github.com/github_username/repo_name"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/github_username/repo_name">View Demo</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Report Bug</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Request Feature</a>
  
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
Social media auto loader allows you to schedule post for Instagram, Facebook, and Twitter. It can handle posts including
a picture, a gallery of pictures, or a video. 

Drop your jpeg or mp4 file in the input bucket, and it will appear in the output bucket formatted
to comply with the requirements of all three apis.

The video will be properly formatted to play on all three services, oversize photos will be resized,
and pictures that don't meet the aspect ratio requirements will have equal size black bars added to
each side to adjust the ratio.

It does not alter the length of videos, or the size of the videos. So keep that in mind.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Built With

* ## <a href="https://aws.amazon.com/">AWS</a>
* ## <a href="https://johnvansickle.com/ffmpeg/">ffmpeg</a>


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

FFmpeg is a linux based command line video editing tool. In order to use ffmpeg with Lambda you need to create an executable layer. Link above, and 
here are more details on how you do that.

https://blog.devgenius.io/how-to-process-media-in-aws-lambda-ffmpeg-f53491cf8768

An AWS SAM template is included for deployment

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Noel Alderman - [@vintageeurocars](https://twitter.com/twitter_handle) - noele952@gmail.com

Project Link: [https://github.com/noele952/social-media-formatter](https://github.com/noele952/social-media-formatter)

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->


