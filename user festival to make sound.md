
# install festival and essential packages
sudo apt-get install festival festlex-cmu festlex-poslex festlex-oald libestools1.2 unzip

# install the voice
sudo apt-get install festvox-don festvox-rablpc16k festvox-kallpc16k festvox-kdlpc16k


# download all mbrola english voice 
mkdir mbrola_tmp
cd mbrola_tmp/
wget http://tcts.fpms.ac.be/synthesis/mbrola/bin/pclinux/mbrola3.0.1h_i386.deb
wget -c http://tcts.fpms.ac.be/synthesis/mbrola/dba/us1/us1-980512.zip
wget -c http://tcts.fpms.ac.be/synthesis/mbrola/dba/us2/us2-980812.zip
wget -c http://tcts.fpms.ac.be/synthesis/mbrola/dba/us3/us3-990208.zip
wget -c http://www.festvox.org/packed/festival/latest/festvox_us1.tar.gz
wget -c http://www.festvox.org/packed/festival/latest/festvox_us2.tar.gz
wget -c http://www.festvox.org/packed/festival/latest/festvox_us3.tar.gz
wget -c http://tcts.fpms.ac.be/synthesis/mbrola/dba/cn1/cn1.zip

# Installing the binary, unpacking the voices and wrappers
sudo dpkg -i mbrola3.0.1h_i386.deb
unzip -x cn1.zip
unzip -x us2-980812.zip
unzip -x us3-990208.zip
unzip -x us1-980512.zip
tar xvf festvox_us1.tar.gz
tar xvf festvox_us2.tar.gz
tar xvf festvox_us3.tar.gz

# Installing the voices and wrappers
sudo mkdir -p /usr/share/festival/voices/chinese/cn1_mbrola/
sudo mkdir -p /usr/share/festival/voices/english/us1_mbrola/
sudo mkdir -p /usr/share/festival/voices/english/us2_mbrola/
sudo mkdir -p /usr/share/festival/voices/english/us3_mbrola/

sudo mv cn1 /usr/share/festival/voices/chinese/cn1_mbrola/
sudo mv us1 /usr/share/festival/voices/english/us1_mbrola/
sudo mv us2 /usr/share/festival/voices/english/us2_mbrola/
sudo mv us3 /usr/share/festival/voices/english/us3_mbrola/
sudo mv festival/lib/voices/english/us1_mbrola/* /usr/share/festival/voices/english/us1_mbrola/
sudo mv festival/lib/voices/english/us2_mbrola/* /usr/share/festival/voices/english/us2_mbrola/
sudo mv festival/lib/voices/english/us3_mbrola/* /usr/share/festival/voices/english/us3_mbrola/


# tidy up

# cd ../
# rm -rf mbrola_tmp/


## Installing the enhanced CMU Arctic voices
mkdir cmu_tmp
cd cmu_tmp/
wget -c http://www.speech.cs.cmu.edu/cmu_arctic/packed/cmu_us_awb_arctic-0.90-release.tar.bz2
wget -c http://www.speech.cs.cmu.edu/cmu_arctic/packed/cmu_us_bdl_arctic-0.95-release.tar.bz2
wget -c http://www.speech.cs.cmu.edu/cmu_arctic/packed/cmu_us_clb_arctic-0.95-release.tar.bz2
wget -c http://www.speech.cs.cmu.edu/cmu_arctic/packed/cmu_us_jmk_arctic-0.95-release.tar.bz2
wget -c http://www.speech.cs.cmu.edu/cmu_arctic/packed/cmu_us_rms_arctic-0.95-release.tar.bz2
wget -c http://www.speech.cs.cmu.edu/cmu_arctic/packed/cmu_us_slt_arctic-0.95-release.tar.bz2

#unpack 
for t in `ls cmu_*` ; do tar xf $t ; done
rm *.bz2

# install 
sudo mkdir -p /usr/share/festival/voices/english/
sudo mv * /usr/share/festival/voices/english/

# rename dir 
for d in `ls /usr/share/festival/voices/english` ; do
if [[ "$d" =~ "cmu_us_" ]] ; then
sudo mv "/usr/share/festival/voices/english/${d}" "/usr/share/festival/voices/english/${d}_clunits" 
fi ; done

# tidy up 
cd ../
rm -rf cmu_tmp/