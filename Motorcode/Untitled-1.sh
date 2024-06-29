
#!/bin/bash
source env/bin/activate
 i2coutput = $(i2cdetect -y 1)

 if grep -q '70' <<< "$i2coutput"; then
    echo "motor driver is read on i2c bus"
    cd Downloads
    