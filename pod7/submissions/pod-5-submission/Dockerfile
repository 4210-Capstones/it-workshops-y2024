# Author: Mitchell Mennelle
# Pull the latest Ubuntu 22.04 LTS base image
FROM ubuntu:22.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV DEBIAN_FRONTEND=teletype
#ENV LEAPSDK_INSTALL_LOCATION=/usr/share/doc/ultraleap-hand-tracking-service
# Override paths for LeapC headers and libraries
#ENV LEAPC_HEADER_OVERRIDE=/usr/lib/ultraleap-hand-tracking-service/include
#ENV LEAPC_LIB_OVERRIDE=/usr/lib/ultraleap-hand-tracking-service


WORKDIR /usr/local/app/ultraleap-hand-tracking-service

# necessary dependencies
RUN apt update && \
    apt install -y \
    wget \
    curl \
    gpg \
    python3 \
    python3-pip \
    python3.10-venv \
    build-essential \
    libgl1-mesa-glx \
    cmake \
    usbutils\
    git

#EXPOSE 5000

# Add Ultraleap gpg key
RUN wget -qO - https://repo.ultraleap.com/keys/apt/gpg | gpg --dearmor | tee /etc/apt/trusted.gpg.d/ultraleap.gpg

# Add Ultraleap repostory to APT sources
RUN echo 'deb [arch=amd64] https://repo.ultraleap.com/apt stable main' | tee /etc/apt/sources.list.d/ultraleap.list

# Pre-configure acceptance of the EULA for ultraleap-hand-tracking
#RUN echo "ultraleap-hand-tracking ultraleap-hand-tracking/license select true" | debconf-set-selections

# Update APT and install Ultraleap hand tracking packages
RUN apt update && \
    yes | apt install ultraleap-hand-tracking 

# Install Python dependencies
COPY leapc-python-bindings/ /usr/local/app/leap/ultraleap-hand-tracking-service
RUN pip3 install leap
RUN pip3 install -r /usr/local/app/leap/ultraleap-hand-tracking-service/requirements.txt

# Copy leapc-python-bindings directory into the container
COPY leapc-python-bindings /usr/local/leapc-python-bindings

# Install leapc-python-bindings (editable mode)
#WORKDIR /usr/local/leapc-python-bindings
#RUN pip3 install -e .


# Use LEAPC_HEADER_OVERRIDE and LEAPC_LIB_OVERRIDE during the build
RUN python3 -m build /usr/local/app/leap/ultraleap-hand-tracking-service/leapc-cffi
RUN pip3 install /usr/local/app/leap/ultraleap-hand-tracking-service/leapc-cffi/dist/leapc_cffi-0.0.1.tar.gz
RUN pip3 install -e /usr/local/app/leap/ultraleap-hand-tracking-service/leapc-python-api

# Set environment variables for LeapSDK location
#ENV LEAPSDK_INSTALL_LOCATION /usr/lib/ultraleap-hand-tracking-service

# Run a basic hand tracking example (adjust according to your example files)
CMD ["python3", "/usr/local/app/leap/ultraleap-hand-tracking-service/examples/tracking_event_example.py"]