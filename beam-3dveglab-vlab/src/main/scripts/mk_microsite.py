#!/usr/bin/env python
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 3 of the License, or (at your option)
# any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program; if not, see http://www.gnu.org/licenses/
# 
# @(#) $Id: $
#
# small script to generate static content pages for the microsite
#

baseurl = 'http://www.geo.uzh.ch/microsite/3dveglab/index.html'

template = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
<head>
 <meta name="generator" content=
 "HTML Tidy for Linux (vers 25 March 2009), see www.w3.org" />
 <meta http-equiv="Content-Type" content="text/html; charset=us-ascii" />
 <meta http-equiv="Cache-Control" content=
 "no-transform,public,max-age=300,s-maxage=900" />

 <title>3D Vegetation Lab</title>
 <base href="%s" />
 <style type="text/css" media="screen, print, projection">
/*<![CDATA[*/
 html, body   { margin:0; padding:0; color:#000; background:#fff; font-family: Arial,sans-serif }
 #body        { width:960px;  margin:0 auto; background:white; }
 #header      { padding:10px; background:white; }
 #content-1   { float:left;   width:160px; padding:10px; background:white; }
 #content-2   { float:right;  width:780px; }
 #content-2-1 { float:left;   width:660px; padding:10px; background:white; }
 #content-2-2 { float:right;  width:80px; padding:10px; background:white; }
 #footer      { padding:10px; background:white; }
 /* http://positioniseverything.net/easyclearing.html) */
 .cf:after { display:block; clear:both; height:0; visibility:hidden; content:" "; font-size:0; }
 /* use conditional comments for this bit if you want valid CSS */
 .cf {*zoom:1;}
 /*]]>*/
 </style>
</head>

<body>
 <div id="body">
  <div id="header" class="cf">
   <table border="0" width="960">
    <tr>
     <td width="1" rowspan="2"><a href=
     "http://www.geo.uzh.ch/microsite/3dveglab/"><img alt=
     "3d vegetation lab" height="90" src=
     "http://www.geo.uzh.ch/microsite/3dveglab/software/veglablogo.png" /></a></td>
     <td align="right"><img alt="University of Zurich" align="right" width=
     "200" src=
     "http://www.uzh.ch/uzh/authoring/images/uzh_logo_e_pos_web_main.jpg" />
     <img alt="ESA" align="right" width="100" src=
     "http://www.esa.int/esalogo/images/downloads/Digital_logo/Hi_resolution/42_digital_logo_dark_blue_HI.png" />
     </td>
    </tr>
    <tr>
     <td>&nbsp;&nbsp; <a href=
     "http://www.geo.uzh.ch/microsite/3dveglab/index.html">
     [ Project ]</a>&nbsp;&nbsp; <a href="consortium">[ Consortium
     ]</a>&nbsp;&nbsp; <a href="people">[ People ]</a>&nbsp;&nbsp; <a href=
     "documents">[ Documents ]</a>&nbsp;&nbsp; <a href="software">[
     Software ]</a>&nbsp;&nbsp; <a href="site">[
     Site ]</a>&nbsp;&nbsp;</td>
    </tr>
   </table>
   <hr />
  </div>
  <div id="main" class="cf">
   <div id="content-1">
    <b>Sensors</b><br />
    &nbsp;&nbsp;<a href=
    "https://earth.esa.int/web/guest/missions/3rd-party-missions/historical-missions/landsat-tmetm;jsessionid=20181E62B0A37B8CCD6613286FE6539F.eodisp-prod4040">LANDSAT</a><br />
    &nbsp;&nbsp;<a href=
    "https://earth.esa.int/web/guest/missions/esa-operational-eo-missions/envisat/instruments/meris">MERIS</a><br />
    &nbsp;&nbsp;<a href=
    "https://earth.esa.int/web/guest/missions/3rd-party-missions/current-missions/terraaqua-modis">MODIS</a><br />
    &nbsp;&nbsp;<a href=
    "https://earth.esa.int/web/guest/missions/esa-future-missions/sentinel-2">Sentinel
    2</a><br />
    &nbsp;&nbsp;<a href=
    "https://earth.esa.int/web/guest/missions/esa-future-missions/sentinel-3">Sentinel
    3</a><br />
    <br />
    <b>Components</b><br />
    &nbsp;&nbsp;<a href=
    "http://www.brockmann-consult.de/cms/web/beam/">Beam</a><br />
    &nbsp;&nbsp;<a href=
    "http://www.cesbio.ups-tlse.fr/us/dart/dart_contexte.html">DART</a><br />
    &nbsp;&nbsp;<a href=
    "http://www2.geog.ucl.ac.uk/~plewis/librat/">librat</a><br />
    &nbsp;&nbsp;<a href="http://www.libradtran.org">libRADTRAN</a><br />
   </div>
   <div id="content-2">
    <div id="content-2-1">
%s
    </div>
    <div id="content-2-2"></div>
   </div>
  </div>
  <div id="footer" class="cf">
   <hr />
   <p>Copyright &copy;2014</p>
  </div>
 </div>
</body>
</html>
'''

pageindex = '''
    <b>An integrated BEAM-plugin for ground-validated 3D vegetation
     modeling</b><br />  
<figure>
       <img alt="3d Reconstruction" height="300" src=
       "graphics/3D_forest_reconstruction.jpg" />
      <center> <caption> <small> <i>From: Schneider, F.; Leiterer, R.; Morsdorf, F.; Gastellu-Etchegorry, J.-P.; Lauret, N.; Pfeifer, N. & Schaepman, M. E. Simulating imaging spectrometer data: 3D forest modeling based on LiDAR and in situ data Remote Sensing of Environment, 2014, in review.</small></i></caption> </center>
</figure>
  <b>Abstract</b><br />
The up-coming generation of ESA operational missions - the Sentinels -
will enhance the capability to observe the vegetated surfaces of the
Earth.  Nevertheless the quantitative interpretation of the Earth
Observation (EO) signal is a challenging task because vegetation is a
complex and dynamic medium. Effects of horizontal and vertical
heterogeneities and asymmetrical structures of vegetation as well as
their high temporal dynamics are often neglected in the algorithm
development, calibration and validation procedures.  To better
understand the scientific basis as well as the potential of future and
upcoming missions we need detailed knowledge about the observed medium
and the processes governing the radiative transfer. The combination of
a realistic description of the medium in high detail together with a
validated radiative transfer model will create a virtual lab mimicking
reality which is capable to assess the potential of novel observation
systems as well as to develop new algorithms and understand scaling
issues from point measurements to the landscape. The advancement of
ground based LiDAR systems now provides information that helps
describing and reconstructing forest stands in 3D down to the
leaf/shoot level. Such detailed representations of the canopy
structure and the distribution of leaves/branches within a 3D
radiative transfer model will thus allow the simulation of current and
future missions in a controlled but realistic environment. It would
thus offer an opportunity to test and develop dedicated applications
to integrate EO into Earth system modeling.  The 3D-VegtationLab will
develop a concept for land surface reference sites, which will be
demonstrated for two selected pilot super-sites as a scientific
support tool. The tool will include a standardized and comprehensive
multi-temporal and multi-scale benchmark dataset together with a
scientific toolbox based on a radiative transfer model. The
3D-Vegetation Lab will provide the scientific community with a common
benchmarking tool to develop, validate and compare biophysical EO
products from space-borne missions with special attention to prepare
for upcoming Sentinels.  The 3D-VegetationLab is financed by ESA's
STSE funding scheme, and partners are University College of London
(UK), TU Wien (AUT), CESBIO Toulouse (FR) and Netcetera (CH).
'''

pageconsortium = '''
     <table border="0">
      <tr>
       <td colspan="2"><b>Prime Contractor</b></td>
      </tr>
      <tr>
       <td><a href="http://www.geo.uzh.ch/en/units/rsl">University of Zurich - Remote Sensing Labs</a></td>
       <td><img alt="RSL" align="left" height="40" src=
       "http://www.geo.uzh.ch/microsite/sen4sci/img/RSL_logo.jpg" /></td>
      </tr>
      <tr> <td>&nbsp;</td> </tr>
      <tr>
       <td colspan="2"><b>Sub-contractors</b></td>
      </tr>
      <tr>
       <td><a href="http://www.geog.ucl.ac.uk/">University College London</a></td>
       <td><img alt="UCL" align="left" height="40" src=
       "http://sharp.cs.ucl.ac.uk/img/ucl_logo_2.jpg" /></td>
      </tr>
      <tr>
       <td><a href="http://www.cesbio.ups-tlse.fr/index_us.htm">Centre d'Etudes Spatiales de la
       BIOsph&egrave;re</a></td>
       <td><img alt="CESBIO" align="left" height="40" src=
       "http://www.cesbio.ups-tlse.fr/data_all/images/logo_cesbio.png" /></td>
      </tr>
      <tr>
       <td><a href="http://www.ipf.tuwien.ac.at/">Technische Universit&auml;t Wien</a></td>
       <td><img alt="TU Wien" align="left" height="40" src=
       "http://www.tuwien.ac.at/fileadmin/t/tuwien/downloads/cd/CD_NEU_2009/TU_Logos_2009/TU-Signet.png" /></td>
      </tr>
      <tr>
       <td><a href="http://www.netcetera.com">Netcetera AG</a></td>
       <td><img alt="Netcetera" align="left" height="40" src=
       "http://netcetera.com/de/dms/images/logos/nca-logo-home.GIF" /></td>
      </tr>
      <tr> <td>&nbsp;</td> </tr>
      <tr>
       <td colspan="2"><b>Sponsor</b></td>
      </tr>
      <tr>
       <td><a href="http://www.esa.int/Our_Activities/Observing_the_Earth">European Space Agency - Earth Observation</a></td>
       <td><img alt="ESA" align="left" height="38" src=
       "http://www.esa.int/esalogo/images/downloads/Digital_logo/Hi_resolution/42_digital_logo_dark_blue_HI.png" /></td>
      </tr>
     </table>
'''

pagepeople = '''
     <table>
      <tr> <td colspan="2"><b>Team</b></td> </tr>

      <tr> <td>Felix Morsdorf</td> <td>RSL</td> </tr>
      <tr> <td>Reik Leiterer</td> <td>RSL</td> </tr>
      <tr> <td>Fabian Schneider</td> <td>RSL</td> </tr>
      <tr> <td>Michael Schaepman</td> <td>RSL</td> </tr>

      <tr> <td colspan="2">&nbsp;</td> </tr>

      <tr> <td>Mathias Disney</td> <td>UCL</td> </tr>
      <tr> <td>Philip Lewis</td> <td>UCL</td> </tr>

      <tr> <td colspan="2">&nbsp;</td> </tr>

      <tr> <td>Jean-Philippe Gastellu-Etchegorry</td> <td>CESBIO</td> </tr>
      <tr> <td>Nicolas Lauret</td> <td>CESBIO</td> </tr>
      <tr> <td>Tristan Gregoire</td> <td>CESBIO</td> </tr>

      <tr> <td colspan="2">&nbsp;</td> </tr>

      <tr> <td>Norbert Pfeifer</td> <td>TU Wien</td> </tr>
      <tr> <td>Markus Hollaus</td> <td>TU Wien</td> </tr>

      <tr> <td colspan="2">&nbsp;</td> </tr>

      <tr> <td>Jason Brazile</td> <td>Netcetera Zurich</td> </tr>
      <tr> <td>Cyrill Schenkel</td> <td>Netcetera Zurich</td> </tr>

      <tr> <td colspan="2">&nbsp;</td> </tr>

      <tr> <td colspan="2"><b>Consultants</b></td> </tr>

      <tr> <td>Jan Clevers</td> <td>WUR</td> </tr>
      <tr> <td>Hans-Gerd Maas</td> <td>TU Dresden</td> </tr>
      <tr> <td>Jean-Luc Widlowski</td> <td>IES</td> </tr>

      <tr> <td colspan="2">&nbsp;</td> </tr>

      <tr> <td colspan="2"><b>ESA Technical Officer</b></td> </tr>
      <tr> <td>Benjamin Koetz</td> <td>ESA-ERSIN</td> </tr>
     </table>
'''

pagedocuments = '''
     <a href="http://discovery.ucl.ac.uk/1371132/">Novel reference site
     approach to prototyping, calibrating, and validating Earth observation
     data and products</a><br />
     <font size="-2"><i>AGU Proceedings, San Francisco, California, USA
     (2012)</i><br />
     M Schaepman, F Morsdorf, R Leiterer, N Pfeifer, M Hollaus, MI Disney,
     P Lewis, JP Gastellu-Etchegorry, J Brazile, B Koetz</font><br />
     <br />
     <a href="http://discovery.ucl.ac.uk/1371129/">A scientific support
     tool for accuracy assessment and prototyping of EO data and
     products</a><br />
     <font size="-2"><i>ForestSAT Proceeedings, Corvallis, Oregon, USA,
     (2012)</i><br />
     F Morsdorf, R Leiterer, M Schaepman, N Pfeifer, M Hollaus, MI Disney,
     P Lewis, JP Gastellu-Etchegorry, J Brazile, B Koetz</font><br />
     <br />
     <a href=
     "http://www.geo.uzh.ch/microsite/rsl-documents/research/publications/other-sci-communications/Leiterer2012VegetationskartierungWaldstrukturmonitoring-2904624640/Leiterer2012VegetationskartierungWaldstrukturmonitoring.pdf">
     3D Vegetationskartierung: flugzeuggest&uuml;tztes Laserscanning
     f&uuml;r ein operationelles Waldstrukturmonitoring</a><br />
     <font size="-2"><i>Tagung des Arbeitskreises f&uuml;r Fernerkundung,
     Bochum, Deutschland; "Proceedings AK Fernerkundung 2012 Bochum",
     (2012)</i><br />
     R Leiterer, F Morsdorf, ME Schaepman, W M&uuml;cke, N Pfeifer, M
     Hollaus</font><br />
     <br />
     <a href=
     "http://pub-geo.tuwien.ac.at/showentry.php?ID=203992&amp;lang=6&amp;nohtml=1">
     3D-VegetationLab - a concept for land surface reference
     sites</a><br />
     <font size="-2"><i>Poster: Sentinel Potential Science Products for
     Cryosphere, Ocean, Land and Solid Earth Research Assessment &amp;
     Consolidation Workshop, Frascati, Italy, (2011)</i><br />
     F. Morsdorf, J. Brazile, M. Disney, J. Gastellu-Etchegorry, P. Lewis,
     Z. Malenovsky, N. Pfeifer, M. Schaepman, B. Koetz, M. Drusch, K.
     Scipal, D. Fernandez-Prieto</font><br />
'''

pagesoftware = '''
     <h2>BEAM toolkit plugin</h2>
     An <a href="https://github.com/netceteragroup/esa-beam">integrated 
     plugin module</a> is available for version 4.11 of the <a 
     href="http://www.brockmann-consult.de/cms/web/beam/">ESA BEAM Earth 
     Observation Toolbox and Development Platform</a> Please note that the toolbox software is not yet final, but a current development snapshot.

     <h3>Binary Installation</h3>Binary installation of the 3D Vegetation
     Lab plugin is automated by a standalone Java program and involves:

     <ul>
      <li>copying/replacing the plugin (jar) in $HOME/beam-4.11/modules</li>

      <li>first-time run to create/unpack BEAM's
      ${HOME}/.beam/beam-vlab/auxdata/</li>

      <li>fetch/unpack latest versions of dependent 3rd party software into
      BEAM's auxdata directory</li>

      <li>create command line wrappers in the bin directory for batch
      operation</li>
     </ul>

     <h3>Binary Installation (windows)</h3>
     <pre>
rem 1. MANUALLY: Download BEAM  - you have to click to Proceed
rem press Windows-R  to get the "run" prompt
iexplore "http://www.brockmann-consult.de/cms/web/beam/dlsurvey?p_p_id=downloadportlet_WAR_beamdownloadportlet10&amp;what=software/beam/4.11/beam_4.11_win32_installer.exe"
rem 2. run installer
beam_4.11_win32_installer.exe
rem 3. go to the beam bin directory (the directory where you just installed it)
rem press Windows-R to get the "run" prompt
cmd /K "cd /d C:\\Program Files (x86)\\beam-4.11\\bin"
rem 4. download the 3DVegLabInstaller.jar into the bin directory from step 3.
iexplore "http://www.geo.uzh.ch/microsite/3dveglab/software/3DVegLabInstaller.jar"
rem 5. run the 3DVegLabInstaller.jar from inside the bin directory
press Windows-R to get the "run" prompt
cmd /K "cd /d C:\\Program Files (x86)\\beam-4.11\\bin"
java -jar 3DVegLabInstaller.jar
</pre>

     <h3>Binary Installation (linux)</h3>
     <pre>
# 1. MANUALLY: Download BEAM  - you have to click to Proceed
firefox 'http://www.brockmann-consult.de/cms/web/beam/dlsurvey?p_p_id=downloadportlet_WAR_beamdownloadportlet10&amp;what=software/beam/4.11/beam_4.11_linux64_installer.sh'
# 2. run installer
sh beam_4.11_linux64_installer.sh
# NOTE: an early version of BEAM's 4.11 installer had a glitch, ensure the installed directory has the proper version name ${HOME}/beam-4.11
# 3. go to the beam bin directory (the directory where you just installed it)
cd ${HOME}/beam-4.11/bin
# 4. download 3DVegLabInstaller.jar into the bin directory from step 3.
wget http://www.geo.uzh.ch/microsite/3dveglab/software/3DVegLabInstaller.jar
# 5. run the 3DVegLabInstall.jar from inside the bin directory
java -jar 3DVegLabInstaller.jar
# 6. run BEAM
${HOME}/beam-4.11/bin/visat
</pre>
'''

pagesite = '''
     <script src="http://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js">
     </script>
     <script>
         function random() {
             return Math.floor(Math.random() * 9 + 1)
         }
         var a = random();
         var b = random();

         var email_regex = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

         var email = "<tr><td><label for=\\"email\\">E-Mail</label></td><td> \
                      <input type=\\"text\\" id=\\"email\\" value=\\"\\"/> \
                      </td><td id=\\"em_error\\"></td></tr>";
         var anti_spam = "<tr><td><label for=\\"anti_spam\\">The sum of " + a +
                         " and " + b + " is</label></td><td><input \
                         type=\\"text\\" id=\\"anti_spam\\" value=\\"\\"/> \
                         </td><td id=\\"as_error\\"></td></tr>";

         $(document).ready(function () {
             $("#download-form").prepend(email, anti_spam);
             $("#download").click(function () {
                 if (!email_regex.test($("#email").val())) {
                     $("#em_error").text("Invalid.");
                     return false;
                 } else $("#em_error").text("");
                 if ($("#anti_spam").val() != a + b) {
                     $("#as_error").text("Wrong answer. Try again.");
                     return false;
                 } else $("#as_error").text("");
                 $.get("<e-mail_db>",
                       { email: $("#email").val(),
                         anti_spam: $("#anti_spam").val(), a: a, b: b }
                      );
                 return true;});});
     </script>
     <noscript>
       The e-mail address can't be submitted without JavaScript enabled.
     </noscript>
     <form action="<real_download>">
         <table id="download-form" border="0">
             <tr>
                 <td></td>
                 <td><input type="submit" id="download" value="Download"/></td>
                 <td></td>
             </tr>
         </table>
     </form>
'''

pages = (
 ('index.html',            pageindex),
 ('consortium/index.html', pageconsortium),
 ('people/index.html',     pagepeople),
 ('documents/index.html',  pagedocuments),
 ('software/index.html',   pagesoftware),
 ('site/index.html',       pagesite)
)

class UTIL:
  def mkdirs(path):
    import sys
    if sys.platform.startswith('java'):
      from java.io import File
      if not File(path).isDirectory():
        if not File(path).mkdirs():
          raise RuntimeError('failed to mkdir %s' % path)
    else:
      import os
      try: 
        os.stat(path)
      except:
        os.makedirs(path)
  mkdirs = staticmethod(mkdirs)

#
# generate all of the html pages
#
for page in pages:
  (fname, pg) = page
  idx = fname.find('/') 
  if (idx > -1):
    dirs = fname[0:idx]
    UTIL.mkdirs(dirs)
  
  fp = open(fname, 'w')
  fp.write(template[1:] % (baseurl, pg[1:-1]))
  fp.close()
