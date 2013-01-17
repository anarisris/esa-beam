#! /bin/sh

export BEAM4_HOME=${HOME}/beam-4.10.3

if [ -z "$BEAM4_HOME" ]; then
    echo
    echo Error: BEAM4_HOME not found in your environment.
    echo Please set the BEAM4_HOME variable in your environment to match the
    echo location of the BEAM 4.x installation
    echo
    exit 2
fi

. "$BEAM4_HOME/bin/detect_java.sh"

"$app_java_home/bin/java" \
    -Xmx1024M \
    -Dceres.context=beam \
    "-Dbeam.mainClass=org.esa.beam.framework.processor.ProcessorRunner" \
    "-Dbeam.processorClass=com.netcetera.vlab.VLabProcessor" \
    "-Dbeam.home=$BEAM4_HOME" \
    "-Dncsa.hdf.hdflib.HDFLibrary.hdflib=$BEAM4_HOME/modules/lib-hdf-2.7/lib/libjhdf.so" \
    "-Dncsa.hdf.hdf5lib.H5.hdf5lib=$BEAM4_HOME/modules/lib-hdf-2.7/lib/libjhdf5.so" \
    -jar "$BEAM4_HOME/bin/ceres-launcher.jar" "$@"

exit $?
