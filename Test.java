package io.rtms.rtms_examples;

import io.prometheus.client.*;
import io.prometheus.client.exporter.*;
import io.prometheus.client.hotspot.DefaultExports;
import java.util.*;

public class Test 
{
    /** Set Float metrics 
    private static float randFloat(float min, float max) {
        return (float) (min + (Math.random() * (max - min)) );
    } */

    /** Set Double metrics */
    private static double randDouble(double min, double max) {
        return (Math.random()*(max - min + 1) + min);
    }

    /** Set Int metrics */
    private static int randInt(int min, int max){
        return (int)(Math.random()*(max - min + 1) + min);
    }

    /** Set Bool metrics */
    private static int randBool(){
        return (int)(Math.round(Math.random()));
    }

    /** System Metrics */
    static final Gauge system_temp = Gauge.build()
    .name("system_temp_celsius")
    .help("Current temperature of system component")
    .labelNames("component").register();

    static final Gauge system_voltage = Gauge.build()
    .name("system_voltage")
    .help("Current value of voltage pins")
    .labelNames("voltage_pins").register();

    static final Counter power = Counter.build()
    .name("power_supply_joules")
    .help("Current power usage of system").register();

    static final Gauge system_analog = Gauge.build()
    .name("system_analog")
    .help("Current value of analog pins")
    .labelNames("analog_pins").register();

    static final Gauge system_digital = Gauge.build()
    .name("system_digital")
    .help("Current value of digital pins")
    .labelNames("digital_pins").register();

    /** Space Computer Metrics */
    static final Gauge current = Gauge.build()
    .name("SC_current_draw_amperes")
    .help("Current draw of SC").register();

    static final Gauge zynq_Voltage = Gauge.build()
    .name("SC_zynq_voltage")
    .help("Current voltage of zynq").register();

    static final Gauge dieTemp = Gauge.build()
    .name("SC_temperature_celsius")
    .help("Current temperature of dieSC").register();

    /** IMU Metrics */
    static final Gauge euler = Gauge.build().name("system_orientation_eulers").help("Euler Vector Value")
    .labelNames("euler_axis").register();

    static final Gauge quaternion = Gauge.build().name("system_orientation_quaternions").help("Quaternion Vector Value")
    .labelNames("quaternion_axis").register();

    static final Gauge omega = Gauge.build().name("system_acceleration_omegas").help("Acceleration Value")
    .labelNames("omega_axis").register();

    static final Gauge mag = Gauge.build().name("system_orientation_mag").help("Magnetic Value")
    .labelNames("magnetic_value_axis").register();

    static void myFunction() {

        system_temp.labels("temp0").set( randDouble(0, 100) );
        system_temp.labels("temp1").set( randDouble(0, 100) );
        system_temp.labels("power_supply").set( randDouble(0, 100) );
        system_temp.labels("IMU").set( randDouble(-20, 100) );

        system_voltage.labels("v0").set( randInt(0, 6) );
        system_voltage.labels("v1").set( randInt(0, 6) );

        power.inc(1.6);

        system_digital.labels("d0").set( randBool() );
        system_digital.labels("d1").set( randBool() );
        system_digital.labels("d2").set( randBool() );
        system_digital.labels("d3").set( randBool() );

        system_analog.labels("a0").set( randInt(0, 2) );
        system_analog.labels("a1").set( randInt(0, 2) );
        system_analog.labels("a2").set( randInt(0, 2) );
        system_analog.labels("a3").set( randInt(0, 2) );

        current.set( randDouble(0, 2) );
        zynq_Voltage.set( randDouble(0, 4) );
        dieTemp.set( randDouble(0, 45) );

        euler.labels("eulerX").set( randDouble(0, 360) );
        euler.labels("eulerY").set( randDouble(-90, 90) );
        euler.labels("eulerZ").set( randDouble(0, 180) );

        quaternion.labels("quatA").set( randDouble(-1, 1) );
        quaternion.labels("quatB").set( randDouble(-1, 1) );
        quaternion.labels("quatC").set( randDouble(-1, 1) );
        quaternion.labels("quatD").set( randDouble(-1, 1) );

        omega.labels("omegaX").set( randDouble(0, 4) );
        omega.labels("omegaY").set( randDouble(0, 4) );
        omega.labels("omegaZ").set( randDouble(0, 4) );

        mag.labels("magX").set( randDouble(0, 1) );
        mag.labels("magY").set( randDouble(0, 1) );
        mag.labels("magZ").set( randDouble(0, 1) );

    }

    public static void main( String[] args ) throws Exception {

        // Add metrics about CPU, JVM memory etc.
        DefaultExports.initialize();
        HTTPServer server = new HTTPServer(8000);
        while (true) {
            myFunction();
            Thread.sleep(1000);
          }
    }
}
