# Use PHP Apache image
FROM php:7.4-apache

# Set the working directory
WORKDIR /var/www/html

# Copy PHP files
COPY . .

# Overwrite the default Apache configuration to set the document root
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf

# Copy the additional Apache configuration
COPY apache2.conf /etc/apache2/conf-available/hicup.conf
RUN ln -s /etc/apache2/conf-available/hicup.conf /etc/apache2/conf-enabled/hicup.conf

# Enable Apache modules
RUN a2enmod rewrite
RUN a2enmod headers

# Expose port 80
EXPOSE 80
