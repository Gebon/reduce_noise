# reduce_noise
## This repository contains Jython script to reduce noise from audio file

Dependencies:
 - JDK >= 1.7
 - Audacity
 - SikuliX 1.1.0
 - ffmpeg

Prerequisites:
 - ffmpeg's bin folder should be in environment's PATH variable
 - real monitor (SikuliX's requirement)
 - free PC, i.e. PC shouldn't be used while script is working

This project uses SikuliX library to manipulate with Audacity. Because Audacity doesn't have command line interface, we have to simulate manual clicking.

Getting started:
 - download and install [JDK](http://java.com/en/download/manual.jsp)
 - download and install [SikuliX](https://launchpad.net/sikuli/sikulix/1.1.0)
 - download and install [Audacity](https://sourceforge.net/projects/audacity)
 - download and install [ffmpeg](https://ffmpeg.org/download.html)
 - add `%path_to_ffmpeg_folder%/bin` to `PATH`
 - set `JAVA_HOME` in environment variables
 - check, that all goes as expected:
  - `java -version`
  - `ffmpeg -version`
 - run in command line `runsikulix.cmd -r reduce_noise.skl`
 - OR run in command line `runsikulix.cmd` and then open `reduce_noise.sikuli` in IDE

`reduce_noise.skl` can be generated inside IDE

Root folder and Audacity executable can be specified from command line or at the runtime.
```
runsikulix.cmd -r %path_to_script% -- "%audacity_path%" "%input_audio_file_path%" "%output_audio_file_path%"
```
`%output_audio_file_path%` shouldn't have an extension. Extension, by default, is WAV

#### [Stable](https://github.com/Gebon/reduce_noise/tree/stable) branch
